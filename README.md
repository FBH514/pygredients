# Pygredients

Version 0.1.2

##### Pygredients is an open-source Python library for data structures and algorithms available on PyPi. 🍎🍊🍋🫐

## Installation
```pip install pygredients```

```pip3 install pygredients``` for OSX users

## Usage
```python
from pygredients import *
```

## Data Structures
### Linked List
```python
# Create a linked list
ll = LinkedList()

# Add a node to the linked list
ll.append(1)
ll.append(2)
ll.append(3)

# Remove a node from the linked list
ll.remove(2) # 2

# Check if a value is in the linked list
ll.contains(1) # True

# Get the head of the linked list
ll.peek() # 3

# Get the length of the linked list
ll.size() # 2

# Check if the linked list is empty
ll.is_empty() # False

# Print the linked list
print(ll) # [1, 3]

# Limit the length of the linked list
ll.limit = 2
ll.append(4) # ValueError: Cannot append 4 to Linked List as it is full.
```

### Stack
```python
# Create a stack
stack = Stack()

# Push a value to the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Pop a value from the stack
stack.pop() # 3

# Peek the top of the stack
stack.peek() # 2

# Check if a value is in the stack
stack.contains(1) # True

# Get the length of the stack
stack.size() # 2

# Check if the stack is empty
stack.is_empty() # False

# Print the stack
print(stack) # [1, 2]

# Limit the length of the stack
stack.limit = 2
stack.push(4) # ValueError: Cannot push 4 to Stack as it is full.
```

### Queue
```python
# Create a queue
queue = Queue()

# Enqueue a value to the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue a value from the queue
queue.dequeue() # 1

# Peek the front of the queue
queue.peek() # 2

# Check if a value is in the queue
queue.contains(1) # True

# Get the length of the queue
queue.size() # 2

# Check if the queue is empty
queue.is_empty() # False

# Print the queue
print(queue) # [2, 3]

# Limit the length of the queue
queue.limit = 2 
queue.enqueue(4) # ValueError: Cannot enqueue 4 to Queue as it is full.
```