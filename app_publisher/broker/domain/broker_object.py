from abc import ABC, abstractmethod

class BrokerObject:
    @abstractmethod
    def create(self):
        ...
        