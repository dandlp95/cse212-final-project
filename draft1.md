# QUEUES DATA STRUCTURES

Understanding this data structure is very intuitive because it's all around us. Virtually every
business or organizations that deals with customers, uses this data structure. Think about it, 
whenever you go to a service that is too busy to assist everone at the same time, you have to be
put on some sort of queue. Most of the time, those that got on the queue first, will be the ones
that are assisted first as well and vice versa.

Due to the uses of queues in the real world, it is important to become familiar of how this data 
structure works and how it can be implemented. 

## DEFINITIONS
Before we start, let's become familiar with some definitions we will use throughout this guide:

**Enqueue** Refers to adding a new item to the queue data structure. Remember that in a queue, 
items will always be first added to the back of the queue.

**Dequeue** Removing an item from the queue data structure. We always remove the item that has
been in the queue first.

## FORMS OF IMPLEMENTATION

Data strctures can often be represented in more than one way. In Python, Queues are often represented
with lists or the dequeue library which is very easy to import. In this tutorial, we will review both.

# QUEUES USING LISTS

We start the queue by setting up a list:

```
queue = []
```
## ENQUEING

Now, let's add some items to our queue. We always want to add items to the back of the queue. So, recall
that Python already has the append built-in method to add items at the end of lists. Let's add 3 items:

```
queue.append("item1")
queue.append("item2")
queue.append("item3")
```
As you can see, we will type the name of our queue, use the Python append method and pass the value we
want to enqueue between the parenthesis.


Our queue now should look something like this:
```
print("Initial Queue")
print(queue)

Initial Queue
[item1, item2, item3]
```
Notice the order of each item. The item we added first, item1, is at the beginning of the queue. While the item3, the
item we added last, is at the end of the queue.

## DEQUEING

### FIRST DEQUEING METHOD

Since our queue is not empty anymore, let's go ahead and dequeue some items. Queues are "first in, first out" data structures.
This means that whenever we want to remove an item, we always remove the item that has been in the queue the longest. 
Python also offers a built in method to remove the first item off a list: pop().

Let's see an example:
```
# Remember our queue currently look like this: [item1, item2, item3]

queue.pop(0)

print(Queue after removing 1 item)
print(queue)

Queue after removing 1 item
[item2, item3]
```
The pop() method is used to remove values from a list, based on the value's index. For example, if pass it a parameter of 1,
it will remove the list value with an index of 1 (aka, the second value in the list.) With queue data structures, always  make sure
to pass the index of the first item in the array, 0. If you simply call the pop method without passing any parameters, it will 
remove the last item in the queue.

When dealing with data structures, we may also want to store or display the data that was deleted. Well, the pop method does not just
remove the data, it also returns the value that was removed. So, if we did something like this, it would remove the first item in the
list, return the item and print it.:

```
print(queue.pop(0))
```


### SECOND DEQUEING METHOD

Another way to remove things from the queue, is the del statement. To
use it, simply add the del statement following by the array element you want to remove:

```
# Our current array loos like this: [item2, item3]

del queue[0]

print("This is the queue after the del statement: ")
print(queue)

This is the queue after the del statement
[item3]
```

## CHECK IF THE ARRAY IS EMPTY

As we are adding and removing items from the queue, you want to keep
an eye on whether the array is empty or not to catch any errors. For example, if you have a queue with 3 items and you dequeue 4 times, you will get an 
Index Error.  

Adding an "If" statement does the trick: 

```
if len(queue) <= 0:
    raise Index Error()

# The rest of your code here...
```

# QUEUES USING THE DEQUE LIBRARY

Python lists are not the most efficient way to implement queues. For example, when dealing with pop and append operations on the 
left side of an array, every element to the right will need to be moved to the left if an item was removed or to the right to make
room for the new item added. In terms of efficiency, it would be O(n). Operations done to the left side of the array are much more 
efficienct (O(1)). However, when dealing with a bigger amount of data, then Python needs to reallocate memory to grow the underlying
list and allow for new data to be added.

Python created a class to deal these limitations: Deque(), which is accessible through the collections library. Adding and removing
data on either side of an array is very efficient using the Deque class, since it works as a double linked list. We will cover the 
subject of linked lists in a different tutorial.

Here is an example on how to use them:

```
# We need to import the class from the collections library.
from collections import deque

# Initiazes an instance of the deque class
queue = deque()

# To add items to the array, you would do it with the append method, just
# like with a regular list.
queue.append(item1)
queue.append(item2)

# The queue right now will look like this: [item1, item2]

# The remove method will be slightly different. Instead of pop, we will use popleft()
# Very self explanatory. It will remove an item from the left side of the array.
# Popleft will also return the item that was removed.
queue.popleft()

# Now the queue will look like this: [item2]
```

# EFFICIENCY

Using lists, enqueing is extremely efficient and has an efficiency of O(1) while dequeing has an efficiency of O(n)
because when the first item in the array is removed, everything has to be pushed forward. 

Dequeing or Enqueing is always O(1) using the deque class.

# PROBLEM:

```
customers = []

# Imagine you run a fast food business. We will keep track of our waiting customers in the 
# queue in the list above.


# PROBLEM 1
# 4 customers named Joseph, Mike, Andrew and Rachel just ordered food. Mike ordered first, 
# Joseph ordered second, Rachel ordered third and Andrew ordered last. Add them all to the 
# customers waiting list using the list above. Write your code below



# PROBLEM 2
# Since its a queue, the restaurant will prepare the meals starting at the beggining of the list.
# After a few minutes, the first 2 orders are ready. Go ahead and remove the first 2 customers
# from the queue. You also want to display the name of the customers whose order is ready in the 
# restaurant's screen so the customers can see if their order is ready. 

```

```
# PROBLEM 3
# Below is a class to manage a queue through a list in Python. Notice
# how if you were to dequeue from an empty list or more dequeue more
# times than there are items, it would create an error.

# Modify the dequeue method to handle this error.

class Queue:

    def __init__(self):
        """
        Initialize queue.  
        """
        self.queue = []

    def enqueue(self, value):
        """
        Enqueue the new value
        """
        self.queue.append(value)

    def dequeue(self):
        """
        Dequeue from the queue.
        """
        value = self.queue[0]
        del self.queue[0]
        return value

```