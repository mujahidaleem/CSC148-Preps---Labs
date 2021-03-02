"""Prep 5 Synthesize

=== CSC148 Winter 2019 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the code for a linked list implementation with two classes,
LinkedList and _Node.
"""
from __future__ import annotations
from typing import Any, Optional


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    def __init__(self) -> None:
        """Initialize an empty linked list.
        """
        self._first = None

    def print_items(self) -> None:
        """Print out each item in this linked list."""
        curr = self._first
        while curr is not None:
            print(curr.item)
            curr = curr.next

    # ------------------------------------------------------------------------
    # Prep 5 exercises
    # ------------------------------------------------------------------------
    # For each of the following linked list methods, read its docstring
    # and the complete its implementation.
    # You should use as your starting point our *linked list traversal*
    # code template, but of course you should modify it as necessary!
    #
    # NOTE: the first two methods are new special methods (you can tell by the
    # double underscores), and enable some special Python behaviour that we've
    # illustrated in the doctests.
    #
    # At the bottom of this file, we've included some helpers
    # to create some basic linked lists for our doctests.
    def __len__(self) -> int:
        """Return the number of elements in this list.

        >>> lst = LinkedList()
        >>> len(lst)              # Equivalent to lst.__len__()
        0
        >>> lst = LinkedList()
        >>> node1 = _Node(1)
        >>> node2 = _Node(2)
        >>> node3 = _Node(3)
        >>> node1.next = node2
        >>> node2.next = node3
        >>> lst._first = node1
        >>> len(lst)
        3
        """
        # TODO: implement this method
        # curr = self._first
        # while curr is not None:
        #     ... curr.item ...
        #     curr = curr.next

        current = self._first
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this list.

        Use == to compare items.

        >>> lst = LinkedList()
        >>> node1 = _Node(1)
        >>> node2 = _Node(2)
        >>> node3 = _Node(3)
        >>> node1.next = node2
        >>> node2.next = node3
        >>> lst._first = node1
        >>> 2 in lst                     # Equivalent to lst.__contains__(2)
        True
        >>> 4 in lst
        False
        """
        # TODO: implement this method
        current = self._first
        while current is not None:
            if current.item == item:
                return True
            else:
                current = current.next
        return False

    # HINTS: for this one, you'll be adding a new item to a linked list.
    #   1. Create a new _Node object first.
    #   2. Consider the cases where the list is empty and non-empty separately.
    #   3. For the non-empty case, you'll first need to iterate to the
    #      *last node* in the linked list. (Review this prep's Quercus quiz!)
    def append(self, item: Any) -> None:
        """Append <item> to the end of this list.

        >>> lst = LinkedList()
        >>> lst.append(1)
        >>> lst._first.item
        1
        >>> lst.append(2)
        >>> lst._first.next.item
        2
        """
        # TODO: implement this method
        current = self._first
        new_node = _Node(item)
        if current is None:
            self._first = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

    def switch(self, index):
        if index == 0:
            pass
        else:
            temp = self._first
            while curr is not None:
                curr = curr.next

    def insert(self, index: int, item: Any) -> None:
        # Create a new node
        new_node = _Node(item)

        # Need to do something special if we insert into the first position.
        # In this case, self._first *must* be updated.
        if index == 0:
            new_node.next = self._first
            self._first = new_node
        else:
            # Get the node at position (index - 1)
            curr_index = 0
            curr = self._first
            while curr is not None and curr_index < index - 1:
                print(curr.item)
                curr = curr.next
                curr_index = curr_index + 1

            if curr is None:
                raise IndexError
            else:
                # At this point, curr refers to the node at position (index - 1)
                curr.next, new_node.next = new_node, curr.next

if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.insert(1,5)
    current = l._first
    while current is not None:
        print(current.item)
        current = current.next

    print(l.next.item)

