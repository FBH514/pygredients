from node import Node
from typing import Any
from abc import abstractmethod, ABC

class AdapterLinkedListInterface(ABC):
    """Defines the interface for the Linked List data structure."""

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
    def append(self, data: Any) -> None:
        pass

    @abstractmethod
    def remove(self, data: Any) -> Any:
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


class AdapterLinkedList(AdapterLinkedListInterface):
    """
    Defines a Linked List data structure.
    Contracted by the Linked List interface.
    """

    def __init__(self, limit=None) -> None:
        """
        Constructor for the Linked List data structure.
        :param limit: int
        """
        if not limit: self._limit = float("inf")
        else: self._limit = limit
        self._size: int = 0
        self.head = None

    def __str__(self) -> str:
        """
        Returns a string representation of the Linked List data structure to display.
        :return: str
        """
        data = []
        current = self.head
        while current is not None:
            data.append(current.data)
            current = current.next
        return "Linked List has a size of {} and contains the following items:\n{}".format(self._size, data)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Linked List data structure to debug.
        :return: str
        """
        return "LinkedList({})".format(self._size)

    @property
    def limit(self) -> int:
        """
        Returns the limit of the Linked List data structure.
        :return: int
        """
        return self._limit

    @limit.setter
    def limit(self, value: int) -> None:
        """
        Sets the limit of the Linked List data structure.
        :param value: int
        :return: None
        """
        if not value > 0:
            raise ValueError("Cannot set the limit to {} as it is not a valid value.".format(value))
        elif value < self._size:
            raise ValueError("Cannot set the limit to {} as it is smaller than the current size of the Linked List.".format(value))
        self._limit = value

    def append(self, data: Any) -> None:
        """
        Appends the data to the Linked List data structure.
        :param data: Any
        :return: None
        """
        if data is None:
            raise ValueError("Cannot append {} to the Linked List.".format(data))
        if self._size == self._limit:
            raise IndexError("Cannot append {} to Linked List as it is full.".format(data))
        self.head = Node(data, self.head)
        self._size += 1

    def remove(self, data: Any) -> Any:
        """
        Removes and returns the data from the Linked List data structure.
        :param data: Any
        :return: Any
        """
        if self.is_empty():
            raise IndexError("Cannot remove {} from an empty Linked List.".format(data))
        if data is None:
            raise ValueError("Cannot remove {} from the Linked List.".format(data))
        current = self.head
        previous = None
        while current is not None:
            if data == current.data:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                self._size -= 1
                return current.data
            previous = current
            current = current.next
        raise ValueError("Cannot remove {} from Linked List as it does not exist.".format(data))

    def peek(self) -> Any:
        """
        Returns the first item in the Linked List data structure.
        :return: Any
        """
        if self.is_empty():
            raise ValueError("Cannot peek an empty Linked List.")
        return self.head.data

    def contain(self, data: Any) -> bool:
        """
        Returns whether the Linked List data structure contains the data.
        :param data: Any
        :return: bool
        """
        if self.is_empty():
            raise IndexError("Cannot search an empty Linked List.")
        if data is None:
            raise ValueError("Cannot search for {} in the Linked List.".format(data))
        current = self.head
        while current is not None:
            if data == current.data:
                return True
            current = current.next
        return False

    def size(self) -> int:
        """
        Returns the size of the Linked List data structure.
        :return: int
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Returns whether the Linked List data structure is empty.
        :return: bool
        """
        return self._size == 0
