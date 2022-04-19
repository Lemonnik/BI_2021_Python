import unittest
from LinkedList import LinkedList, LinkedListItem


class BasicTest(unittest.TestCase):
    """Tests for basic functions"""

    def test_add_and_get(self):
        """Add and get elements"""
        items = LinkedList()
        items.add(10)
        items.add(11)
        items.add(12)
        items.add(13)
        items.add(20)
        self.assertEqual(items[3], 13)

    def test_get_first_1(self):
        """Get first element if one"""
        items = LinkedList()
        items.add(10)
        self.assertEqual(items.first(), 10)
    
    def test_get_first_2(self):
        """Get first element if many"""
        items = LinkedList()
        items.add(10)
        items.add(20)
        items.add(30)
        self.assertEqual(items.first(), 10)

    def test_get_last_1(self):
       """Get last element if one"""
       items = LinkedList()
       items.add(10)
       self.assertEqual(items.last(), 10)
       
    def test_get_last_2(self):
       """Get last element if many"""
       items = LinkedList()
       items.add(10)
       items.add(20)
       items.add(30)
       self.assertEqual(items.last(), 30)

    def test_first_and_last(self):
       """First equals last"""
       items = LinkedList()
       items.add(10)
       self.assertEqual(items.last(), items.first())
 
    def test_len_one(self):
        """Length"""
        items = LinkedList()
        items.add(1000)
        self.assertEqual(len(items), 1)
        
    def test_len_many(self):
        """Length"""
        items = LinkedList()
        for _ in range(1000):
            items.add(1000)
        self.assertEqual(len(items), 1000)
        

class AddTests(unittest.TestCase):
    """Tests for ADD method"""

    def test_add_by_index_1(self):
        """Add to 0 position"""
        items = LinkedList()
        items.add(10)
        items.add(11)
        items.add(12)
        items.add(13)
        items.add(20)

        items.add(255, 0)
        self.assertEqual(items[0], 255)


    def test_add_by_index_2(self):
        """Add to END position"""
        items = LinkedList()
        items.add(10)
        items.add(11)
        items.add(12)
        items.add(13)
        items.add(20)

        items.add(255, len(items))
        self.assertEqual(items[len(items)-1], 255)


    def test_add_by_index_3(self):
        """Add to INTERMEDIATE position"""
        items = LinkedList()
        items.add(10)
        items.add(11)
        items.add(12)
        items.add(13)
        items.add(20)

        items.add(255, 3)
        self.assertEqual(items[3], 255)


    def test_add_by_index_4(self):
        """Add by index to empty List"""
        items = LinkedList()

        items.add(255, 0)
        items.add(10)
        items.add(20)

        self.assertEqual(items[0], 255)


class ExtendTests(unittest.TestCase):
    """Tests for EXTEND method"""

    def test_extend_1(self):
        """Extend to 0 position"""
        items = LinkedList()
        items.add(10)
        items.add(11)

        items.extend([1,2,3,4,5], 0)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 2)
        self.assertEqual(items[2], 3)
        self.assertEqual(items[3], 4)
        self.assertEqual(items[4], 5)

    def test_extend_2(self):
        """Extend to 0 position at empty List"""
        items = LinkedList()

        items.extend([1,2,3,4,5], 0)
        self.assertEqual(items[0], 1)
        self.assertEqual(items[1], 2)
        self.assertEqual(items[2], 3)
        self.assertEqual(items[3], 4)
        self.assertEqual(items[4], 5)


    def test_extend_3(self):
        """Extend to 0 position at empty List but only one element added"""
        items = LinkedList()

        items.extend([5], 0)
        self.assertEqual(items[0], 5)

    
    def test_extend_4(self):
        """Extend to END position """
        items = LinkedList()
        items.add(10)
        items.add(10)

        items.extend([42, 1337], len(items))
        self.assertEqual(items[2], 42)
        self.assertEqual(items[3], 1337)
    
    def test_extend_5(self):
        """Extend to MIDDLE position """
        items = LinkedList()
        items.add(10)
        items.add(20)
        items.add(30)

        items.extend([42, 1337], 1)
        self.assertEqual(items[0], 10)
        self.assertEqual(items[1], 42)    
        self.assertEqual(items[2], 1337)
        self.assertEqual(items[3], 20)
        self.assertEqual(items[4], 30)


class INTests(unittest.TestCase):
    """Tests for IN magic method"""

    def test_in_1(self):
        """True IN"""
        items = LinkedList()
        items.add(10)
        items.add(11)

        self.assertTrue(10 in items)

    def test_in_2(self):
        """False IN"""
        items = LinkedList()
        items.add(10)
        items.add(11)

        self.assertFalse(20 in items)



class PopTests(unittest.TestCase):
    """Tests for POP method"""

    def test_pop_1(self):
        """Add and then pop until empty"""
        items = LinkedList()
        items.add(10)
        items.pop()
        
        self.assertEqual((items._LinkedList__head, items._LinkedList__tail), (None, None))

    def test_pop_2(self):
        """Add and then pop last one"""
        items = LinkedList()
        items.extend([1,2,4,5])
        items.pop()

        self.assertEqual(items.last(), 4)

    def test_pop_3(self):
        """Pop by index (LAST)"""
        items = LinkedList()
        items.extend([1,2,4,5])
        items.pop(3)

        self.assertEqual(items.last(), 4)

    
    def test_pop_4(self):
        """Pop by index (FIRST)"""
        items = LinkedList()
        items.extend([1,2,4,5])
        items.pop(0)

        self.assertEqual(items.first(), 2)

    
    def test_pop_5(self):
        """Pop by index (MIDDLE)"""
        items = LinkedList()
        items.extend([1,2,4,5])
        items.pop(1)

        self.assertEqual(items[1], 4)


class RemoveLastOccuranceTests(unittest.TestCase):
    """Tests for RemoveLastOccurance method"""

    def test_RLO_1(self):
        """Add and then remove"""
        items = LinkedList()
        items.add(10)
        items.remove_last_occurence(10)
        
        self.assertEqual((items._LinkedList__head, items._LinkedList__tail), (None, None))

    def test_RLO_2(self):
        """Add many and then remove"""
        items = LinkedList()
        items.add(10)
        items.add(20)
        items.add(10)
        items.remove_last_occurence(10)

        self.assertEqual(items.last(), 20)




if __name__ == '__main__':
    unittest.main()