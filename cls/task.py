"""
File: cls/task.py
Author: Joshua Rose
Email: joshuarose@gmx.com
Github: https://github.com/yourname
Description: container file for Task class
"""

import uuid


class Task:
    """A mutable Task with multiple allowable instances

    Class Properties
    ----------------
    TID : uuid.UUID
        A unique Task ID that is randomly generated
    name : str
        A short task name that is less than 15 characters

    Usage
    -----

    The Task class can be instanced as follows:
    >>> my_task = Task("Clean my room")
    >>> isinstance(my_task, Task)
    True
    """

    def __init__(self, name):
        """
        Parameters
        ----------
        _task_id : uuid.UUID
            A private instance variable that points to TID
        """

        self._task_id = uuid.uuid1()
        self.name = name

    @property
    def TID(self) -> uuid.UUID:
        """
        The TID (task id) is public instance variable that
        is accessed privately throuugh self._task_id

        TID Datatype
        ------------

        >>> isinstance(Task(name='walk the dog').TID, uuid.UUID)
        True
        """

        return self._task_id

    @property
    def name(self) -> str:
        """
        The name of a task, which can be accessed simply as self.task


        Constraints
        -----------

        1. Cannot exceed 25 characters:
        >>> Task(name="A really really long task name...")
        Traceback (most recent call last):
            ...
        Exception: The length of a task name cannot exceed 25 characters.

        2. Cannot be empty:
        >>> Task(name="")
        Traceback (most recent call last):
            ...
        Exception: A task name cannot be empty.


        Type assurance
        --------------
        >>> task = Task(name="Change the world")
        >>> task.name == "Change the world"
        True
        """

        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) > 25:
            raise Exception("The length of a task name cannot exceed 15 characters.")
        if not len(value):
            raise Exception("A task name cannot be empty.")

        self._name = value
