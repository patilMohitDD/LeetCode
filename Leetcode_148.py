# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        dd=[]
        
        ## looping through the LInklist and appending the list named as dd
        while(temp):
            dd.append(temp.val)
            temp=temp.next
            
        ## Sorting the List in ascedning order
        dd.sort()
        temp=head
        
        ### now overwriting linklist values with the values of the list named DD
        for i in dd:  
            temp.val=i
            temp=temp.next
            
        return head
        
    
