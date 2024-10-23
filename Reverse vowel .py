class Solution:
    def reverseVowels(self, s: str) -> str:
        char = list(s)
        Vowels = 'aeiouAEIOU'
        i = 0
        j = len(s) - 1
        
        while i < j:
            while i < j and char[i] not in Vowels:
                i += 1
            while i < j and char[j] not in Vowels:
                j -= 1
            
            char[i], char[j] = char[j], char[i]
            i += 1 
            j -= 1
        
        return ''.join(char)