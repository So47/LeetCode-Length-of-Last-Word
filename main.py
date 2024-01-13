class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_list = s.split()
        last_word = str_list[len(str_list)-1]
        return len(last_word)
        
