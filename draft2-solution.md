**Create a function to insert at the head for the class above:**

```

    def insert_head(self, value):

        new_node = LinkedList.Node(value)  
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node      


```

**Create a function to insert at the tail for the class above:**

```

    def insert_tail(self, value):

        new_node = LinkedList.Node(value)

        if self.tail is not None:
           
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        # If the tail does not have a node, it means it's empty, so we will just assign the tail to the new node. 
        # Since the list is empty, we'll do the same with the head.
        elif self.tail is None:
            self.tail = new_node
            self.head = new_node
            

```

**Create a function to remove at the tail for the class above:**

```

    def remove_tail(self):

        if self.tail != self.head:

            self.tail.prev.next = None
            self.tail = self.tail.prev

        else:

            self.head = None
            self.tail = None


```


