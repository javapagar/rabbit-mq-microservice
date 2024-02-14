from abc import ABC, abstractmethod

class Connection:  
    @abstractmethod
    def connect(self):
        ...
    
    @abstractmethod
    def close(self):
        ...