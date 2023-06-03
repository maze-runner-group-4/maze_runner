from node_letter import Node

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0

    def enqueue(self,value):
        node=Node(value)
        if not self.front:
            self.front=node
            self.rear = node
        else:        
         self.rear.next=node
         self.rear = node
        self.size+=1
        return self.__str__()
    
    def dequeue(self):
        if not self.front:
            raise ValueError("Empty queue")
        elif self.front == self.rear:
            self.rear=None
        self.size-=1
        temp=self.front
        self.front=self.front.next
        temp.next= None
        return temp.value

    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise ValueError("Empty queue")
            
    def isEmpty(self):
        return not self.size
    
    def __str__(self):
        output=""

        if self.front == None:
            output="Empty queue"
        else:
            current=self.front
            while(current):
                output+=f'{current.value} --> '
                current=current.next
            output+=" None"
        return(output)