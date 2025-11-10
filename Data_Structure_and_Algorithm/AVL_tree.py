class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=1

class avl:
    def insert(self,root,key):
        if not root:
            return node(key)
        elif key<root.key:
            root.left=self.insert(root.left,key)
        else:
            root.right=self.insert(root.right,key)

        root.height=1+max(self.getheight(root.left),self.getheight(root.right))

        balanced=self.checkbalance(root)

        if balanced>1 and key<root.left.key:
            return self.rightrotate(root)
        
        if balanced<-1 and key>root.right.key:
            return self.leftrotate(root)

        if balanced>1 and key>root.left.key:
            root.left=self.leftrotate(root.left)
            return self.rightrotate(root)
        
        if balanced<-1 and key<root.right.key:
            root.right=self.rightrotate(root.right)
            return self.leftrotate(root)
        
        
        return root
    
    def getheight(self,root):
        if not root:
            return 0
        return root.height
        

    def checkbalance(self,root):
        if not root:
            return 0
        return self.getheight(root.left)-self.getheight(root.right)
    
    def leftrotate(self,r):
        r2=r.right
        r3=r2.left
        r2.left=r
        r.right=r3

        r2.height=1+max(self.getheight(r2.left),self.getheight(r2.right))
        r.height=1+max(self.getheight(r.left),self.getheight(r.right))

        return r2
    

    def rightrotate(self,r):
        r2=r.left
        r3=r2.right
        r2.right=r
        r.left=r3

        r2.height=1+max(self.getheight(r2.left),self.getheight(r2.right))
        r.height=1+max(self.getheight(r.left),self.getheight(r.right))

        return r2

    def inorder(self,root):
        if not root:
            return root
        self.inorder(root.left)
        print(root.key,end=" ")
        self.inorder(root.right)


obj=avl()
root=None

keys = [2, 1, 4, 5, 9, 3, 6, 7]
for i in keys:
    root=obj.insert(root,i)

print("Inorder tree")
obj.inorder(root)
