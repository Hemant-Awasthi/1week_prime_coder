class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        char = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not char[i].isalpha():
                i += 1
            while i < j and not char[j].isalpha():
                j -= 1
            if i < j:
                char[i], char[j] = char[j], char[i]
                i += 1
                j -= 1

        return ''.join(char)