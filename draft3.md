# TREES DATA STRUCTURES

In our previous lessons, we talked about how regular linked lists are very efficient with 
operations performed in both ends of the list. However, in order to find a specific node in
the list, every single node has to be iterated. This makes our lists have an O(n) efficiency
for those types of operations.

## WHAT ARE THEY

An improvement we can make for those types of operations are tree data structures. Trees are
technically still linked lists. You still have objects (nodes) pointing at other objects. In trees,
though, each node can be pointing at multiple objects and are typically organized in a hierarchical
manner. 

The most common type of tree data structures are binary trees.

## WHY ARE THEY USEFUL

With regular linked lists, there is typically not hierarchical order. This is not a big deal when 
all we do is grabbing or adding nodes at the beggining or end of the list. However, when retrieving
specific data from anywhere in the list is required, the efficiency cost is not great. Trees allow
us to organize data hierarchically, and if they are well organized, it exponentially increases the
efficiency of retrieving specific data. 

For example, think of a book with 100 pages. Imagine this book's page number are not organized from the
lowest to the highest number. Instead, the numbers are randomly assigned in each page. So, you could open 
the book and the first page will have the number 34, then you flip to the next page and page is numbered
83, and so on. There is no organization whatsoever. Imagine that for some reason, you are trying to find
the page 25 in the book. Because each page number is randomly assigned, your only option to find that page
is iterating each single page until you find the right one. If finding this specific page takes you
10 minutes, imagine if you had a similar book but with 1000 pages instead. It will take you approximately
10 times more. 

Fortunately, basically every book has its pages numbered in order to avoid a situation like this. Now, imagine
you have a regular book with ordered page numbers. If you wanted to find the 25th page, would you still
have to iterate through each single page? Not at all. If the book has 100 pages, you will attempt to open
the book within the first quarter. If you find get the page 30, then you will look through the pages to the left
because 25 is lower than 30. This search will take you like 5 seconds. If you had a  similar book with 1000
pages, it would not take you 10 times longer to find a specific page neither. Because they are ordered, you
will repeat a similar process and would take you just slightly longer.

## BINARY TREES

Binary trees is the most common type of tree. In a binary tree, each node only connects to no more than 2 nodes. These are the elements of a binary tree:

1. Root node: You can think of this node as the head of the tree. When you perform a search, this is where
you will start. It is the element on top of the tree. 
2. Parent node: A parent node is a node that points towards a node lower in the hierarchy.
3. Child node: A the node that is being pointed by the parent node.
4. Leaf nodes: These are nodes that do not point towards any nodes lower in the hierarchy.
5. Subtrees: When you grab a node in the tree, you can think of it as the upmost node in relation of all the
nodes that are beneath it. In this sense, that node along with the nodes beneath it form a subtree.  


## BINARY SEARCH TREES

When properly implemented, binary tree strutures can be very efficient. One of the most common types of trees are 
**binary search trees.** Binary search trees are trees that implement sorting rules to insert data in the tree.
When data is going to be inserted in the tree, the data is compared with the data in the root node. If the data in
the new node is greater than the data in the root node, the new data is sent to the right subtree. If it's smaller,
it is sent to the left subtree. Then, the data is compared the same way with the data of the root node of that subtree
and so on, until an empty place in the tree is found. If duplicate data is inserted into the tree, it can be inserted
either at the right or the left side of the dupliate data.

## EFFICIENCY

Binary search trees are highly efficient, because with each iteration, you're ideally splitting the tree in halves.
This goes back to go the book example from earlier. It doesn't matter if the book is 100 pages or 1000 pages. The 
time it will take us to find an specific page will be similar as long as the page numbers are properly sorted. So,
while the efficiency of iterating a regular list is linear or O(n), the efficiency of finding a specific value in a 
balanced search tree is O(log n).


## BALANCED BINARY SEARCH TREES

Unfortunately, binary search trees aren't necessarily efficient by default. Worst case scenarios happen. Let's say that
you had 10 values added to your search tree, and each value was smaller than the previous one. Eventually, your tree would look something like this:

[ IMAGE OF UNBALANCED BINARY SEARCH TREE HERE ]


As you can see, it now does not look much different than a regular linked list. This means that all the benefits that
we talked about the efficiency of search trees will not apply to this case, as we will end up checking each value,
one-by-one, instead of splitting  the tree in half with each comparison. 

To avoid this worst case scenario, we need to make sure our tree is balanced. A balanced tree, refers to a tree that is 
symmetrical. In other words, it should have the same amount of subtrees on each side, and each subtree should also have
approximately the same amount of subtrees on each side. This is what a balanced binary search tree would look like:

[IMAGE OF BALANCED SEARCH TREE HERE]


## EFFICIENCY OF BINARY SEARCH TREES



