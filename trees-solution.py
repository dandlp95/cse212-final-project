class Binary_Trees:

    class Node:

        def __init__(self, value):

            self.value = value
            self.left = None # Remember we put the node with lower value in the left side
            self.right = None # Nodes with a higher value go to the right
    
    def __init__(self):

        self.root = None # Not having a root node would mean the tree is empty. Think of it as the head of linked lists.
    
    def insert(self, value):
        if self.root is None:
            self.root = Binary_Trees.Node(value)
        else:
            self._insert(value, self.root)  
    
    def _insert(self, value, node):

        if value < node.value:
            
            if node.left is None:
               
                node.left =  Binary_Trees.Node(value)
            else:
             
                self._insert(value, node.left)
       
        elif value > node.value:
           
            if node.right is None:
                
                node.right = Binary_Trees.Node(value)
            else:
            
                self._insert(value, node.right)

        else:
            return