"""
插入排序
中等
时间复杂度：O(n^2)
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def insertionSortList(head):
    if not head: #判断链表是否为空
        return
    
    dummyHead=ListNode(0)
    dummyHead.next=head
    lastSorted=head
    cur=head.next

    while cur:
        if cur.val>=lastSorted.val:  #直接插入在当前有序列表之后
            lastSorted=cur
        else:
            ins=dummyHead
            while ins:   #寻找插入位置
                if cur.val<ins.next.val:
                    lastSorted.next=cur.next
                    cur.next=ins.next
                    ins.next=cur
                    break
                else:
                    ins=ins.next
        cur=lastSorted.next
    return dummyHead.next

print(insertionSortList([4,2,1,3]))

# def insertionSortList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
        
#         dummyHead = ListNode(0)
#         dummyHead.next = head
#         lastSorted = head
#         curr = head.next

#         while curr:
#             if lastSorted.val <= curr.val:
#                 lastSorted = lastSorted.next
#             else:
#                 prev = dummyHead
#                 while prev.next.val <= curr.val:
#                     prev = prev.next
#                 lastSorted.next = curr.next
#                 curr.next = prev.next
#                 prev.next = curr
#             curr = lastSorted.next
        
#         return dummyHead.next