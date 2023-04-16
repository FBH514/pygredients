from typing import Any


class Node:

    """Defines a Node object used in data structures."""

    def __init__(self, data: Any, _next: 'Node') -> None:
        """
        Constructor for the Node object.
        :param data: Any
        :param _next: Node
        """
        self.data = data
        self._next = _next

    def __str__(self) -> str:
        """
        Returns a string representation of the Node object to display.
        :return: str
        """
        return "Node has a value of {}\nIts next sibling has a value of {}".format(self.data, self._next.data)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Node object to debug.
        :return: str
        """
        return "Node({})".format(self.data)
