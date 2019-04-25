class Solution {
public:
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        ListNode *first = head, *second = head;
        for(int i = 0; i < n; i++) { // first向前走n步
            first = first->next;
        }
        if(first == NULL) { // first走到了NULL，要删除的是第一个结点
            ListNode *toDelete = second;
            second = second->next;
            delete toDelete;
            toDelete = NULL;
            return second;

        }
        while(first->next != NULL) { // first还没走到NULL
            first = first->next;
            second = second->next;
        }
        ListNode *toDelete = second->next; // second->toDelete->node
        second->next = second->next->next;
        delete toDelete;
        toDelete = NULL;

        return head;
    }
};