from unittest import TestCase
from adapter_linkedlist import AdapterLinkedList as LinkedList


class TestAdapterLinkedList(TestCase):
    """Tests the Linked List data structure."""

    def setUp(self) -> None:
        """
        Sets up the test suite.
        :return: None
        """
        data = [1, 2, 3, 4, 5]
        self.linked_list = LinkedList()
        for item in data:
            self.linked_list.append(item)

    def test_init(self) -> None:
        """
        Tests the initialization of the Linked List data structure.
        :return: None
        """
        self.assertTrue(self.linked_list.head is not None)
        self.assertTrue(self.linked_list._size == 5)

    def test_append(self):
        """
        Tests the append method of the Linked List data structure.
        :return: None
        """
        self.linked_list.append(6)
        self.assertTrue(self.linked_list._size == 6)
        self.assertTrue(self.linked_list.head.data == 6)

    def test_remove(self) -> None:
        """
        Tests the remove method of the Linked List data structure.
        :return: None
        """
        self.linked_list.remove(5)
        self.assertTrue(self.linked_list._size == 4)
        self.assertTrue(self.linked_list.head.data == 4)
        self.linked_list.remove(1)
        self.assertTrue(self.linked_list._size == 3)
        self.assertTrue(self.linked_list.head.data == 4)
        self.linked_list.remove(4)
        self.assertTrue(self.linked_list._size == 2)
        self.assertTrue(self.linked_list.head.data == 3)

    def test_peek(self) -> None:
        """
        Tests the peek method of the Linked List data structure.
        :return: None
        """
        self.assertTrue(self.linked_list.peek() == 5)
        self.assertTrue(self.linked_list._size == 5)

    def test_contain(self) -> None:
        """
        Tests the contain method of the Linked List data structure.
        :return: None
        """
        self.assertTrue(self.linked_list.contain(5))
        self.assertTrue(self.linked_list.contain(1))
        self.assertTrue(self.linked_list.contain(3))
        self.assertFalse(self.linked_list.contain(6))
        self.assertFalse(self.linked_list.contain(0))

    def test_size(self) -> None:
        """
        Tests the size method of the Linked List data structure.
        :return: None
        """
        self.assertTrue(self.linked_list.size() == 5)
        self.linked_list.append(6)
        self.assertTrue(self.linked_list.size() == 6)
        self.linked_list.remove(6)
        self.assertTrue(self.linked_list.size() == 5)

    def test_is_empty(self) -> None:
        """
        Tests the is_empty method of the Linked List data structure.
        :return: None
        """
        self.assertFalse(self.linked_list.is_empty())
        self.linked_list.remove(5)
        self.linked_list.remove(4)
        self.linked_list.remove(3)
        self.linked_list.remove(2)
        self.linked_list.remove(1)
        self.assertTrue(self.linked_list.is_empty())
