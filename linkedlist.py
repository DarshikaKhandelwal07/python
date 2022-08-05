class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # def __str__(self):
    #     return f"{self.data} --> {self.next}"

    def count(head):
        n = 1
        while (head.link):
            head = head.link
            n += 1
        return f"This Linked List has {n} nodes"
    def reorder(head):
        if not head or not head.next:
            return head
        p1 = head
        p2 = head.next
        if not p1.next or not p2.next:
            return p1
        while(p1.next and p2.next):
            x = p2
            p1 = p2.next
            p1 = p1.next
            p2 = p1.next
            p2 = p2.next
        p1.next = x
        return head



a = Node(1, Node(2, Node(3, Node(4,Node(5,Node(6))))))
p = a.data
print(p.reorder())