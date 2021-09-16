import unittest
from answer import Solution

data = [ 
        [ [1,4,6,86,2,0], 8, [2,4] ],
        [ [2,2,3], 4, [0,1] ],
        [ [12,23,34,56,67,87,98,75,45,24,31,21,3,5,6,8,235,123,545,786,3332], 590, [8,18]]
        ]
class TestingAnswer(unittest.TestCase):
    def test_twoSum(self):
        for nums, target, expected in data:
            actual = Solution.twoSum(nums, target)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()