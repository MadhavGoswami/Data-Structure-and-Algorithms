class Cqueue:
    def __init__(self,k):
     self.k=k
     self.queue=[None]*k
     self.head=-1
     self.tail=-1

    def enqueue(self,data):
       if self.head==-1:
            self.head=0
            self.tail=0
            self.queue[self.tail]=data
       elif self.head==((self.tail+1)%self.k):
            print("queue is full")
       else:
           self.tail=(self.tail+1)%self.k
           self.queue[self.tail]=data        

    def dequeue(self):
        if self.head==-1:
            print("queue is empty")

        elif self.head==self.tail:
            temp=self.queue[self.head]
            self.head=-1
            self.tail=-1
            return temp
        else:
            temp=self.queue[self.head]
            self.head=(self.head+1)%self.k
            return temp
                
    def displayqueue(self):
        if self.head==-1:
            print("Queue is empty")
        elif self.tail>=self.head:
             for i in range(self.head,self.tail+1):
                 print(self.queue[i])        
        else:
            for i in range(self.head,self.k):
                 print(self.queue[i])
            for j in range(0,self.tail+1):
                 print(self.queue[i])

                   
obj = Cqueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.displayqueue()

obj.dequeue()
print("After removing an element from the queue")
obj.displayqueue()                   

