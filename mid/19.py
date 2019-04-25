class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        listNode1 = head
        for i in range(n): # listNode1向前走 n 步
            listNode1 = listNode1.next

        if listNode1 == None: # listNode1走到了NULL，要删除的是第一个结点
            toDelete = head
            head = head.next
            del toDelete
            return head
        
        listNode2 = head
        while listNode1.next != None: # listNode2->toDelete->node
            listNode1 = listNode1.next
            listNode2 = listNode2.next
        
        toDelete = listNode2.next
        listNode2.next = listNode2.next.next
        del toDelete
        return head