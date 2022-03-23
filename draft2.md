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


