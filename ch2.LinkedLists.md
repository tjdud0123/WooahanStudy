# Chapter2. Linked Lists

## 2-1 ) Write code to remove duplicates from an unsorted linked list. How would you solve this problem if a temporary buffer is not allowed?
```python
def removeDuplicates(head):
    cur = head
    while cur:
        srh_pointer = cur
        while srh_pointer.next:
            if srh_pointer.next.data == cur.data:
                srh_pointer.next = srh_pointer.next.next
            else:
                srh_pointer = srh_pointer.next
        cur = cur.next
```
<hr>

## 2-2 )  Implement an algorithm to find the kth to last element of a singly linked list.
```python
def findKthElement(head, k):
    p1, p2 = head, head

    for i in range(k):
        if not p1:
            return null
        p1 = p1.next

    while p1:
        p1, p2 = p1.next, p2.next

    return p2
```
<hr>

## 2-3 ) Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
```python
def deleteMiddleNode(node):
    if node and node.next:
        nxt = node.next
        node.data, node.next = nxt.data, nxt.next
```
<hr>


## 2-5 ) You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

```python
def addTwoLists(l1, l2, carry = 0):
    if not l1 and not l2 and not carry:
        return None

    sum_val = carry
    if l1:
        sum_val += l1.val
    if l2:
        sum_val += l2.val
    node = ListNode(sum_val % 10)
    
    if l1 or l2:
        nxt_l1 = l1.next if l1.next else None
        nxt_l2 = l2.next if l2.next else None 
        carry = sum_val // 10
        nxt_node = addTwoLists(nxt_l1, nxt_l2, carry)
        node.setNext(nxt_node)

    return node
```
<hr>

## 2-6 ) Implement a function to check if a linked list is a palindrome.
```python
def checkIsPalindrome(head):
    slow, fast = head, head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow, fast = slow.next, fast.next.next
 
    if fast:
        slow = slow.next

    while slow:
        if slow.data != stack[-1]:
            return False
        else:
            stack.pop()
            slow = slow.next

    return True
```
<hr>
<hr>
<hr>