class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class bst:
    def __init__(self):
        self.root=None

    def insert(self,key):
        if self.root is None:
            self.root=node(key)
        else:
            self._insert(self.root,key)

    def _insert(self,root,key):
        if key<root.key:
            if root.left is None:
                root.left=node(key)
            else:
                self._insert(root.left,key)
        else:
            if root.right is None:
                root.right = node(key)
            else:
                self._insert(root.right,key)

    def min_value(self,root):
        current=root
        while current.left:
            current=current.left
        return current


    def delete(self,key):
        self.root=self._delete(self.root,key)

    def _delete(self,root,key):
        if root is None:
            return None
        if key<root.key:
            root.left=self._delete(root.left,key)
        elif key>root.key:
            root.right=self._delete(root.right,key)

        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp=self.min_value(root.right)
            root.key=temp.key
            root.right=self._delete(root.right,temp.key)
        return root


    def preorder(self,root):
        if root:
            print(root.key,end=" ",flush=True)
            self.preorder(root.left)
            self.preorder(root.right)


    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key,end=" ",flush=True)
            
    
b=bst()
listt=[10,20,35,17,180,11,21]
for i in listt:
    b.insert(i)
b.insert(6)

b.delete(11)
b.delete(20)

print("preorder traversal")
b.preorder(b.root)
print()

print("postorder traversal")
b.postorder(b.root)

print()
        