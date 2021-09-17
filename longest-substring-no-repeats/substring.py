class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        stack = []
        count = 0
        highest_count = 0
        s_list = list(s)
        
        for _ in range(len(s_list)):
            for letter in s_list:
                if letter in stack:
                    stack = []
                    del s_list[0]
                    break
                else:
                    stack.append(letter)
                    count = len(stack)
                    if count > highest_count:
                        highest_count = count
        
        return highest_count