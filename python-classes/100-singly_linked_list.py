#!/usr/bin/python3
"""
Define a Node class that represents a node in a singly-linked list
"""


class Node:
    """
    A class representing a node in a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the SinglyLinkedListNode class.

        Args:
            data: The data to be stored in the node.
            next_node: The next node in the linked list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for accessing the data attribute.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the 'data' attribute of the class.

        Args:
            value (int): The value to set as the data attribute.

        Raises:
            TypeError: If the value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node attribute.

        Returns:
            The value of the next_node attribute.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.

        Args:
            value (Node): The next_node value to be set.

        Raises:
            TypeError: If the value is not a Node object.

        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        __head (Node): The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        string = ""
        current = self.__head
        while current is not None:
            string += str(current.data) + "\n"
            current = current.next_node
        return string

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value,
        into the linked list in sorted order.

        Args:
            value: The value to be inserted into the linked list.

        Returns:
            None
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        if value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new
