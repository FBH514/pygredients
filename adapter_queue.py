from node import Node
from typing import Any
from abc import abstractmethod, ABC

class AdapterQueueInterface(ABC):
    """Defines the interface for the Queue data structure."""

    @abstractmethod
    def __init__(self, limit=None) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def enqueue(self, data: Any) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> Any:
        pass

    @abstractmethod
    def peek(self) -> Any:
        pass

    @abstractmethod
    def contain(self, data: Any) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass


class AdapterQueue(AdapterQueueInterface):
    """Defines a Queue data structure."""

    def __init__(self, limit=None) -> None:
        """
        Constructor for the Queue data structure.
        :param limit: int
        """
        if not limit: self.limit = float("inf")
        else: self.limit = limit
        self._size: int = 0
        self.head = None

    def __str__(self) -> str:
        """
        Returns a string representation of the Queue data structure to display.
        :return: str
        """
        data = []
        current = self.head
        while current is not None:
            data.append(current.data)
            current = current.next
        return "Queue has a size of {} and contains the following items:\n{}".format(self._size, data)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Queue data structure to debug.
        :return: str
        """
        return "Queue({})".format(self._size)

    def enqueue(self, data: Any) -> None:
        """
        Enqueues the data in the Queue data structure.
        :param data: Any
        :return: None
        """
        if data is None:
            raise ValueError("Cannot enqueue {} in the Queue.".format(data))
        if self._size == self.limit:
            raise IndexError("Cannot append {} to the Queue as it is full.".format(data))
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)
        self._size += 1

    def dequeue(self) -> Any:
        """
        Dequeues and returns the first item in the Queue data structure.
        :return: Any
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue an empty Queue.")
        current = self.head
        self.head = current.next
        self._size -= 1
        return current.data

    def peek(self) -> Any:
        """
        Returns the first item in the Queue data structure.
        :return: Any
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty Queue.")
        return self.head.data

    def contain(self, data: Any) -> bool:
        """
        Returns whether the Queue data structure contains the data.
        :param data: Any
        :return: bool
        """
        current = self.head
        while current is not None:
            if data == current.data:
                return True
            current = current.next
        return False

    def size(self) -> int:
        """
        Returns the size of the Queue data structure.
        :return: int
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Returns whether the Queue data structure is empty.
        :return: bool
        """
        return self._size == 0


if __name__ == '__main__':
    queue = AdapterQueue()
    data = [1, 2, 3, 4, 5]
    for _ in data:
        queue.enqueue(_)
    print(queue.head)