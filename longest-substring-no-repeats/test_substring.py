import unittest
from substring import Solution

data = [
         ['hello', 3],
         ['abcabcbb', 3], 
         ['aasskkjsajqw', 5], 
         ['', 0],
         ['lllllll', 1]
]

class Test(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        for string, expected in data:
            s = Solution()
            actual = s.lengthOfLongestSubstring(string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()