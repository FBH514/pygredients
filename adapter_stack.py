from node import Node
from typing import Any
from abc import abstractmethod, ABC

class AdapterStackInterface(ABC):
    """Defines the interface for the Stack data structure."""

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
    def push(self, data: Any) -> None:
        pass

    @abstractmethod
    def pop(self) -> Any:
        pass

    @abstractmethod
    def peek(self) -> Any:
        pass

    @abstractmethod
    def contains(self, data: Any) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass


class AdapterStack(AdapterStackInterface):
    """
    Defines a Stack data structure.
    Contracted by the Stack interface.
    """

    def __init__(self, limit=None) -> None:
        """
        Constructor for the Stack data structure.
        :param limit: int
        """
        if not limit: self._limit = float("inf")
        else: self._limit = limit
        self._size: int = 0
        self.head = None

    def __str__(self) -> str:
        """
        Defines a string representation of the Stack data structure to display.
        :return: str
        """
        data = []
        current = self.head
        while current is not None:
            data.append(current.data)
            current = current.next
        return "Stack has a size of {} and contains the following items:\n{}.".format(self._size, data)

    def __repr__(self) -> str:
        """
        Defines a string representation of the Stack data structure to debug.
        :return: str
        """
        return "Stack({})".format(self._size)

    @property
    def limit(self) -> int:
        """
        Returns the limit of the Stack data structure.
        :return: int
        """
        return self._limit

    @limit.setter
    def limit(self, value: int) -> None:
        """
        Sets the limit of the Stack data structure.
        :param value: int
        :return: None
        """
        if not value > 0:
            raise ValueError("Cannot set the limit to {} as it is not a valid value.".format(value))
        elif value < self._size:
            raise ValueError(
                "Cannot set the limit to {} as it is smaller than the current size of the Stack.".format(value))
        self._limit = value

    def push(self, data: Any) -> None:
        """
        Pushes the data to the Stack data structure.
        :param data: Any
        :return: None
        """
        if data is None:
            raise ValueError("Cannot push {} to the Stack.".format(data))
        if self._size == self._limit:
            raise IndexError("Cannot push {} to Stack as it is full.".format(data))
        self.head = Node(data, self.head)
        self._size += 1

    def pop(self) -> Any:
        """
        Pops and returns the first item in the Stack data structure.
        :return: Any
        """
        if self.is_empty():
            raise IndexError("Cannot pop {} from an empty Stack.")
        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return data

    def peek(self) -> Any:
        """
        Returns the first item in the Stack data structure.
        :return: Any
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty Stack.")
        return self.head.data

    def contains(self, data: Any) -> bool:
        """
        Returns whether the Stack data structure contains the data.
        :param data: Any
        :return: bool
        """
        if self.is_empty():
            raise IndexError("Cannot search an empty Stack.")
        if data is None:
            raise ValueError("Cannot search for {} in the Stack.".format(data))
        current = self.head
        while current is not None:
            if data == current.data:
                return True
            current = current.next
        return False

    def size(self) -> int:
        """
        Returns the size of the Stack data structure.
        :return: int
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Returns whether the Stack data structure is empty.
        :return: bool
        """
        return self._size == 0
