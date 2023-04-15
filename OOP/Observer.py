class YouTubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify_subscribers(self, event):
        for subscriber in self.subscribers:
            subscriber.update(event)


from abc import ABC, abstractmethod


# abstractmethod is a decorator that marks a method as abstract
# abstract methods are methods that must be implemented in the
# subclasses of the class that contains the abstract method
# if a class contains an abstract method, it must be marked as
# abstract as well (using the ABC decorator) and it cannot be
# instantiated (you cannot create an object of that class)
class Subscriber(ABC):
    @abstractmethod
    def update(self, event):
        pass


class User(Subscriber):
    def __init__(self, name):
        self.name = name

    def update(self, event):
        print(f'{self.name} received notification about {event}')


if __name__ == '__main__':
    channel = YouTubeChannel('Python Tricks')

    channel.subscribe(User('John'))
    channel.subscribe(User('Mary'))
    channel.subscribe(User('Alice'))

    channel.notify_subscribers('new video')

# the Observer pattern is a behavioral pattern that allows us to
# define a subscription mechanism to notify multiple objects about
# any events that happen to the object they are observing
# this pattern is the cornerstone of event driven programming
# in this example, we have a YouTube channel that notifies its
# subscribers when a new video is uploaded
# the subscribers are notified by calling the update method
# the subscribers are objects that implement the Subscriber interface
# the YouTubeChannel class is the subject and the subscribers are
# the observers
# the subject maintains a list of observers and notifies them
# whenever a change occurs
# the subject does not know anything about the observers, it only
# knows that they implement the Subscriber interface
# the observers are objects that implement the Subscriber interface
# the observers register themselves with the subject to receive
# notifications
# the observers implement the update method that is called by the
# subject whenever a change occurs
# the update method receives the event that occurred as an argument
# the observers can use this event to update their state
# the Observer pattern is also known as the Publish/Subscribe pattern
