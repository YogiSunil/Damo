class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:
    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.

        Time complexity: O(n) 
        Explanation: We need to look at each node to count them all.
        """
        count = 0 
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
  
        Time complexity: O(1) 
        Explanation: We can directly add to the tail without going through the list.
        """
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
    
        Time complexity: O(1) 
        Explanation: We can insert the new node at the head directly.
        """
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, matcher):
        """Return an item from this linked list if it is present.
    
        Best case time: O(1) 
        Explanation: The item is the first node.
        
        Worst case time: O(n) 
        Explanation: We may need to check every node.
        """
        node = self.head
        while node is not None:
            if matcher(node.data):
                return node.data
            node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.

        Best case time: O(1) 
        Explanation: The item to delete is the first node.
        
        Worst case time: O(n) 
        Explanation: We may need to go through the entire list to find it.
        """
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))
        
        if self.head.data == item:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        
        node = self.head
        while node.next is not None:
            if node.next.data == item:
                node.next = node.next.next
                if node.next is None:
                    self.tail = node
                return
            node = node.next
        
        raise ValueError('Item not found: {}'.format(item))

    def replace(self, old_item, new_item):
        """Replace the first occurrence of old_item with new_item."""
        node = self.head
        while node is not None:
            if node.data == old_item:
                node.data = new_item  # Replace the data of the node
                return  # Exit once the item is replaced
            node = node.next
        raise ValueError(f'Item not found: {old_item}')


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Testing replace
    print('\nTesting replace:')
    ll.replace('B', 'Z')
    print('list after replace: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['Z', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
