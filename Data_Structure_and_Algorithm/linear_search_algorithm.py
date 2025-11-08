class linearsearch:
    def __init__(self,array,target):
        self.array=array
        self.target=target
    def display(self):
        for i in self.array:
            if i==self.target:
                return self.array.index(i)
        return -1
#declaring list   
array=[5,6,4,7,4,23,66,34,32]

#getting list element and targer from user
"""
#getting size of list or array
size=int(input("Enter the length of the array or list :"))

#getting list from user
for i in range(size):
    element=int(input(f"Enter the element {i+1} :"))
    array.append(element)


#getting target element from user
target=int(input("Enter the Element to find :"))
"""

#declaring target
target=66

#calling class and function          
obj=linearsearch(array,target)
ans=obj.display()


#print output
if ans>=0:
    print(f"The Element {target} is found in the index {ans}")
else:
    print("The element not found.")
    