class node:
    def __init__(self,key):
        self.data=key
        self.next=None
        
class add_two:
    def add(self,l1,l2):
        dummy = node(0)
        current = dummy
        carry = 0

        while l1 or l2:
            x = l1.data if l1 else 0
            y = l2.data if l2 else 0
            total = x + y + carry
            
            carry = total // 10
            current.next = node(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry > 0:
            current.next = node(carry)

        return dummy.next
    
        
    def create_list(self,arr):
        head = node(arr[0])
        temp = head
        for i in arr[1:]:
            temp.next = node(i)
            temp = temp.next
        return head
    




obj = add_two()
l1 = obj.create_list([2, 4, 3])
l2 = obj.create_list([5, 6, 4])
result = obj.add(l1, l2)
