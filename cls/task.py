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
    """

    def __init__(self):
        """
        Parameters
        ----------
        _task_id : uuid.UUID
            A private instance variable that points to TID


        Examples
        --------
        >>> isinstance(Task().TID, uuid.UUID)
        True
        """

        self._task_id = uuid.uuid1()

    @property
    def TID(self) -> uuid.UUID:
        return self._task_id
