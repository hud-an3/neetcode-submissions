class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def mergeTwoLists(self, head1,head2):
        dummy=ListNode()
        tail=dummy
        while head1 and head2:
            if head1.val<=head2.val:
                tail.next=head1
                head1=head1.next
                tail=tail.next
            else:
                tail.next=head2
                head2=head2.next
                tail=tail.next
        if head1:
            tail.next=head1
        else:
            tail.next=head2
        return dummy.next