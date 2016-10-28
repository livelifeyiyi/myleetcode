class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == NULL) return l2;
        if(l2 == NULL) return l1;
        ListNode* head;
        if(l1->val <= l2->val){
            head = l1;
            l1 = l1->next;
        }
        else{
            head = l2;
            l2 = l2->next;
        }
        ListNode* point = head;
        while(l1 && l2){
            if(l1->val <= l2->val){
                point->next = l1;
                l1 = l1->next;
            }
            else{
                point->next = l2;
                l2 = l2->next;
            }
            point = point->next;
        }
        if(l1){
            point->next = l1;
        }
        else{
            point->next = l2;
        }
        return head;
    }
};