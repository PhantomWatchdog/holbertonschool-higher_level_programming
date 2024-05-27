#!/usr/bin/env python3
"""
This module contains a class that demonstrates
serialization and deserialization using the pickle module.
"""

import pickle


class CustomObject:
    """
    A class representing a custom object.

    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): Indicates whether the object is a student or not.
    """

    class MyClass:
        def __init__(self, name, age, is_student):
            """
            Initializes a new instance of the MyClass class.

            Args:
                name (str): The name of the object.
                age (int): The age of the object.
                is_student (bool): Indicates whether the object is
                a student or not.
            """
            self.name = name
            self.age = age
            self.is_student = is_student

    def display(self):
        """
        Display the object's information.

        This method prints the name, age, and student status of the object.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        Args:
            filename (str): The name of the file to save
            the serialized object to.

        Returns:
            None: If the serialization fails.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): The name of the file
            to deserialize the object from.

        Returns:
            CustomObject: The deserialized object.
            None: If the deserialization fails.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
