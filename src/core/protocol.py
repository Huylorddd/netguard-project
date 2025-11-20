from abc import ABC, abstractmethod

class Protocol(ABC):
    def __init__(self, port):
        self.port = port

    @abstractmethod
    def __str__(self):
        pass


class TCP(Protocol):
    def __init__(self, port):
        super().__init__(port)
    
    def __str__(self):
        return "TCP"

class UDP(Protocol):
    def __init__(self, port):
        super().__init__(port)

    def __str__(self):
        return "UDP"