# Chapter3. Stacks and Queues

## 3-2 ) Stack Min : How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.

```python
class Stack:

    def __init__(self):
        self.arr = []
        self.min_arr = []

    def getMin(self):
        return self.min_arr[-1] if self.min_arr else None

    def push(self, value):
        self.arr.append(value)
        min_val = min(self.min_arr[-1], value) if self.min_arr else value
        self.min_arr.append(min_val)

    def pop(self):
        if not self.arr:
            return None
        self.arr.pop()
        self.min_arr.pop()

```
<hr>

## 3-3 ) Stack of Plates : Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).

```python
# 2중 stack 형태로 가능..? [[], [], [] ...]
# python arr로 구현
class SetOfStacks():
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, value):
        if not self.stacks or len(self.stacks[-1]) == capacity:
            self.stacks.append([value])
        else:
            top_stack.append(value)

    def pop(self, value):
        if not self.stacks:
            return None
        top_stack = self.stacks[-1]
        top_stack.pop()
        if not top_stack:
            self.stacks.pop()
```
<hr>

## 3-4 ) Queue via Stacks : Implement a MyQueue class which implements a queue using two stacks

```python
class MyQueue:

    def __init__(self):
        self.new = []
        self.old = []

    def enQue(self, value):
        self.new.append(value)
 
    def deQue(self):
        if self.old:
            return self.old.pop()
        # 붓기
        while self.new:
            item = self.new.pop()
            self.old.append(item)
        return self.old.pop() if self.old else None

```
<hr>

## 3-5 ) Sort Stack : Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

```python
# 다시 뒤집어 주기 때문에 큰 수가 위로 오도록
def sortStack(stack):
    temp = new Stack()
    while not stack.isEmpty():
        item = stack.pop()
        while not temp.isEmpty() and temp.peek() > item:
            stack.push(temp.pop())
        temp.push(item)
    while not temp.isEmpty():
        stack.push(temp.pop())
    return stack
```
<hr>
<hr>
<hr>