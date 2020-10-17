from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Optional

from structures.own_types import T

class List(ABC, Generic[T]):
    @abstractmethod
    def length(self) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        pass

    @abstractmethod
    def __setitem__(self, index: int, element: T) -> None:
        pass

    @abstractmethod
    def append(self, element: T) -> None:
        pass

    @abstractmethod
    def __iter__(self) -> None:
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass

    def __len__(self): # tu nie trzeba abstract method bo jest posrednie z length
        return self.length() # bo dziedziczymy po abstrakcyjnej to jest przeniesione na klase List

class LinkedList(List[T]):
    @dataclass
    class Node(Generic[T]):
        value: T
        next: Optional[LinkedList.Node] = None

    def __init__(self, *args: T) -> None:
        self.head = None
        self._append_init_elements(args)

    def _append_init_elements(self, args):
        if args:
            for element in args:
                self.append(element)

    def length(self) -> int:
        result = 0
        pointer = self.head
        while pointer is not None:
            result += 1
            pointer = pointer.next
        return result

    def __str__(self) -> str:
        pointer = self.head
        result = ""
        while pointer is not None:
            result += f"{pointer.value}"
            pointer = pointer.next
            if pointer is not None:
                result += ", "
        return f"[{result}]"

    def append(self, element) -> None:
        node = LinkedList.Node[int](element)
        if self.head is None:
            self.head = node
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = node

    def __getitem__(self, index: int) -> T:
        pointer = self.head
        pointer_index = 0
        while pointer is not None and pointer_index < index:
            pointer_index += 1
            pointer = pointer.next
        if pointer is not None:
            return pointer.value
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index: int, element: T) -> T:
        pointer = self.head
        pointer_index = 0
        while pointer_index != index:
            pointer_index += 1
            # print("##")
            # print(pointer.next)
            # print(pointer.value)
            # print("##")
            pointer = pointer.next

        if pointer is None:
            raise IndexError("list index out of range")

        pointer.value = element

        # pointer = self.head
        # pointer_index = 0
        # while pointer is not None:
        #     print("##")
        #     print(pointer.next)
        #     print(pointer.value)
        #     print("##")
        #     pointer = pointer.next

        print("#########")

    def __iter__(self) -> None:
        pointer = self.head
        while pointer is not None:
            yield pointer.value
            pointer = pointer.next

    def __eq__(self, other) -> None:
        # First condition
        if not isinstance(other, LinkedList):
            return False
        # Second condition
        if len(self) != len(other):
            return False
        # Third condition
        pointer_1 = self.head
        pointer_2 = other.head
        pointer_index = 0
        while pointer_1 is not None:
            if pointer_1.value != pointer_2.value:
                return False
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next
        return True