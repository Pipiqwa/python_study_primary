# 定义链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 定义反转链表的函数
def reverseList(head: ListNode) -> ListNode:
    prev = None  # 用于保存前一个节点
    current = head  # 用于遍历链表

    while current:
        next_node = current.next  # 保存下一个节点
        current.next = prev  # 反转当前节点的指针
        prev = current  # 移动prev节点
        current = next_node  # 移动到下一个节点

    return prev  # 返回新的头节点

# 创建链表 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# 调用反转链表函数
new_head = reverseList(head)

# 遍历并打印反转后的链表
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")  # 输出应该是 5 -> 4 -> 3 -> 2 -> 1 -> None