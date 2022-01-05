import unittest
from addtwo import Solution

#change from list to linked list
data = [
    [ [2,4,3], [5,6,4], [7,0,8] ]
    [ [0], [0], [0] ]
    [ [9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1] ]
    [ [], [], [] ]
    [ [], [], [] ]
]

class Test(unittest.TestCase):
    def addTwoNumbers_test(self):
        for list1, list2, expected in data:
            anwser = Solution()
            actual = anwser.addTwoNumbers(list1, list2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()