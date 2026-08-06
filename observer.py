class Observer:
    def update(self,msg):
        print("Notification:",msg)

class Subject:
    def __init__(self):
        self.observers=[]

    def add_observer(self,observer):
        self.observers.append(observer)

    def notify(self,msg):
        for observer in self.observers:
            observer.update(msg)

user1= Observer()
user2= Observer()

stock = Subject()
stock.add_observer(user1)

stock.notify("Stock price is increased")