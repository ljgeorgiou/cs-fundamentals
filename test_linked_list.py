from ch06_linked_lists import LinkedList

def test_append_keeps_order():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    assert ll.to_list() == [3, 4]

def test_prepend_puts_at_front():
    ll = LinkedList()
    ll.prepend(1)
    ll.prepend(0)
    assert ll.to_list() == [0, 1]

def test_find_missing_is_false():
    ll = LinkedList()
    assert ll.find(99) is False

def test_delete_from_empty_list():
    ll = LinkedList()
    assert ll.delete(5) is False
    ll.append(5)
    assert ll.delete(3) is False
    assert ll.delete(5) is True
    assert ll.head is None