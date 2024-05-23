#!/usr/bin/env python3
"""
Create an abstract class named Animal using the ABC package.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by subclasses
        to produce the sound of the animal.
        """
        pass


class Dog(Animal):
    """
    A class representing a dog.
    """

    def sound(self):
        """
        Return the sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    A class representing a cat.
    """
    def sound(self):
        """
        Return the sound of a cat.
        """
        return "Meow"
