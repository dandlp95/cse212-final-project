customers = []

#PROBLEM 1

customers.append('Mike')
customers.append('Joseph')
customers.append('Rachel')
customers.append('Andrew')



#PROBLEM 2
print(customers.pop(0))
print(customers.pop(0))



#PROBLEM 3

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
        if len(self.queue) <= 0:
            print("Queue is empty.")
            return

        value = self.queue[0]
        del self.queue[0]
        return value

