from unittest import TestCase
from adapter_queue import AdapterQueue as Queue

class TestAdapterQueue(TestCase):
    """Tests the Queue data structure."""

    def setUp(self) -> None:
        """
        Sets up the test suite.
        :return: None
        """
        data = [1, 2, 3, 4, 5]
        self.queue = Queue()
        for item in data:
            self.queue.enqueue(item)

    def test_init(self) -> None:
        """
        Tests the initialization of the Queue data structure.
        :return: None
        """
        self.assertTrue(self.queue.head is not None)
        self.assertTrue(self.queue._size == 5)

    def test_enqueue(self) -> None:
        """
        Tests the enqueue method of the Queue data structure.
        :return: None
        """
        self.queue.enqueue(6)
        self.assertTrue(self.queue._size == 6)
        self.assertTrue(self.queue.head.data == 1)

    def test_dequeue(self) -> None:
        """
        Tests the dequeue method of the Queue data structure.
        :return: None
        """
        self.queue.dequeue()
        self.assertTrue(self.queue._size == 4)
        self.assertTrue(self.queue.head.data == 2)

    def test_peek(self) -> None:
        """
        Tests the peek method of the Queue data structure.
        :return: None
        """
        self.assertTrue(self.queue.peek() == 1)
        self.assertTrue(self.queue._size == 5)

    def test_contain(self) -> None:
        """
        Tests the contain method of the Queue data structure.
        :return: None
        """
        self.assertTrue(self.queue.contain(1))
        self.assertTrue(self.queue.contain(2))
        self.assertTrue(self.queue.contain(3))
        self.assertTrue(self.queue.contain(4))
        self.assertTrue(self.queue.contain(5))
        self.assertFalse(self.queue.contain(6))

    def test_size(self) -> None:
        """
        Tests the size method of the Queue data structure.
        :return: None
        """
        self.assertTrue(self.queue.size() == 5)
        self.queue.enqueue(6)
        self.assertTrue(self.queue.size() == 6)

    def test_is_empty(self) -> None:
        """
        Tests the is_empty method of the Queue data structure.
        :return: None
        """
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())
