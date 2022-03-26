# LINKED LISTS

## WHAT'S WRONG WITH REGULAR LISTS 

Previously when we talked about queues, you learned how lists are fairly efficient,
but no as efficient as the deque class that we imported from the collections library.
This is because the deque class works as a linked list. 

Let's talk about it for a second. Lists store items right next to each other in memory.  
This allows for easier access when looking for a value, since by knowing the address of 
the first elemenet in the list, we know the second element will be next to it in memory, 
and the third one will be next to the second one, and so on. Because of the importance of
elements being next to each other, doing operations in the beggining or the middle of lists 
is not very efficient. For example, if you wanted to add an element at the beggining of a list 
with 10 thousand elements, this would mean moving each one of those 10 thousand elements back
in order to make room for the new one. This means the efficiency for this operation is linear
or O(n) which is not terrible, but we can do better.

## WHAT ARE LINKED LISTS.

Linked lists are essentially objects pointing at each other. That's the basic concept of it. Each
object is called a node. Each node will typically have 2 things:

* The data
* The pointer

The pointer is the node's attribute that will point in the direction in memory of the next node in
the linked list. Because of this, they do not have to be constrained by having to be next to each other, 
rather, they can be in completely random places in memory and we can still find any element
by following the pointers. 

## WHY LINKED LISTS ARE MORE EFFICIENT.

Since nodes in a linked list do not have to be next to each other, this means we can add a node in the
beggining of the list, and we do not have to push everything back. Instead, we just need to adjust the
pointers and that's it!

Think about it. We do not have to deal with reassigning a new address to potentially hundreds of thousands of
elements in an array. Instead, it's as easy to change to where a node is pointing to. So, while efficiency in
operations done at the beggining of a list are O(n), the efficiency is O(1) in a linked list.

However, in order to find a specific node or value in a linked list, we do need to iterate through each node
until the value is found. Therefore, operations done in the middle of a linked list are O(n), the same as lists.

## DOUBLE LINKED LISTS.

Double linked lists is when nodes do not just point to the next node in the list, they also point to the previous 
node in the array. Basically they have 2 pointers and allows for more functionality, such as iterating each
node in reverse. 

## IMPLEMENTING LINKED LISTS IN PYTHON.

### CUSTOME LINKED LIST. 

One way to implement linked lists in Python is through the deque class imported from the collections library as we 
talked about earlier. However, for demonstration purposes, we'll use a different class, so we can see how each
method work and how everything functions under the radar. 

Here is an example of how a linked list that we created looks like:

```

class LinkedList:

    class Node:

        def __init__(self, value):

            self.value = value
            self.next = None
            self.prev = None
    
    def __init__(self):

        self.head = None
        self.tail = None
    
    # More code below...


```

So, what is happening is that we have a parent class called "LinkedList." This is the actual "list." The children class refers to the nodes that will be inside the linked list.  If you 
see the attributes of the Node, you will see 3 things:

* The value attribute refers to the data that the node contains.
* Self.next refers to the Next pointer. In other words, the object the node is pointing forward 
in the list.
* Self.prev is the Previous pointer. In other words, the object the node is pointing behind in the list.

Also notice how the linked list keeps track of the head (the first node in the list) and the tail
(the last node in the list.) This is important because it will help us know where the list starts
and where it ends. Having the head and tail readily accessible also makes it highly efficient to 
do operations at the begining and end of the list, making it ideal for data strcutters like stacks
or queues. 

Ideally, you should not have to manually input the next and previous pointers. Rather, there will be functions that will take care of that for us. That way, we can simply call that function
and everything will be done behind the curtains.

Now, let's talk about those functions, and how they would work:

**Inserting a new node:**

* If you are inserting at the beginning of the list:

1. Create a new node.
2. The new node's next pointer should point towards the former head.
3. The former head's (now the second node in the list) previous pointer, needs to point towards the new node (which will now be the new head.)
4. Make sure the head attribute of the LinkedList instance object you are working with equals to the new node you just added. 

* If you are inserting at the end of the list (This is basically the exact same process, except
for a few details):

1. Create a new node.
2. The new node's previous pointer should point towards the former tail.
3. The former's tail (now the second-to-last node in the list) next pointere, needs to point towards the new node (which will now be the tail.)
4. Make sure the tail attribute of the LinkedList instance object you are working with equals to the new node you just added.

* If you are inserting somewhere in the middle of the list:

Remember inserting in the middle of the list is not as efficient. You will typically need to perform a for loop until you find a matching node where you want to insert on. For example, if you want to insert a new node after the first node that holds a value of 5, then the insert function will iterate through the list until that node is found (We will call this node, current_node for the purposes of this example.) This means the efficiency is linear or O(n)

After the current_node is found, this are the steps:

1. Create new node.
2. Access the previous pointer of node that the current node next pointer is pointing to (read that again if you have to.) That pointer is currently pointing at the current_node. Change it so that it points to the new node instead.
3. Change the current node's next pointer so that it points to the new node.
4. The new node's previous pointer needs to point to the current pointer.
5. The new node's next pointer needs to point to the node that was formerly after the current node.

This last process can be confusing, so here is an example. Carefully read the comments:

```
    def insert_after(self, value, new_value):

        # This while loop will iterate through each node until the node we are looking is found.
        current_node = self.head
        while current_node is not None:

            # If the value attribute equals the value we were looking for, the node we want to
            # insert to has been found.
            if current_node.value == value:

                if current_node == self.tail:

                    # Code here on what to do if the current_node is the tail...

                else:
                    
                    # Creates new node.
                    new_node = LinkedList.Node(new_value)

                    # The previous pointer will point to the current node.
                    new_node.prev = current_node 

                    # The next pointer of the new node will point to the node that was formerly after
                    # the current_node.
                    new_node.next = current_node.next  

                    # The current_node.next will give us the node that comes after the current_node (not the new node yet.)
                    # By adding the previous pointer after that, we access the previous pointer of that node, so we need to 
                    # change it to the new node.
                    current_node.next.prev = new_node  

                    # The next pointer of the  current_node needs to point towards the new node now.
                    current_node.next = new_node       
                return 
            
            current_node = current_node.next 

```

**Removing a node**

* Removing the head:

1. Access the head's next node's previous pointer (self.head.next.prev) and set it to None.
2. Access the head attribute of the link list and set it to the second node in the list (which will become the new head.)

* Removing the tail:

1. Access the tail's previous node's next pointer (self.tail.prev.next) and set it to None.
2. Access the tail attribute of the link list and set it to the second to last node in the list (which will become the new tail.)

* Removing from the middle:

1. Change the next pointer of the node before the node you are trying to remove, so that it points to the node after the node you are trying to remove.
2.  Change the previous pointer of the node after the node you are trying to remove, so that it points to the node before the node you are trying to remove.

So, as you can see, removing nodes from a linked list is as simple as altering the pointers of the objects.