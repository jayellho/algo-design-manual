'''
[4] You are given a search string and a magazine.
You seek to generate all the characters in the search string by cutting them out from the magazine.
Give an algorithm to efficiently determine whether the magazine contains all the letters in the search string.
'''

'''
algorithm:
- inputs: <search string>, <magazine>
- count frequency of chars/letters in magazine - if know that chars are limited, can consider using a list. else, dictionary.
- iterate through the search string, and minus each char from the dictionary - if don't exist in dictionary OR count falls below 0, return false.
- at the end of the day, return true.
'''
import collections

def find_string(s:str, magazine: str) -> bool:

    # define vars.
    freq_magazine = collections.Counter(magazine)

    # edge case: len of s > len of magazine.
    if len(s) > len(magazine):
        return False

    # iterate.
    for c in s:
        if c not in freq_magazine or freq_magazine[c] - 1 < 0:
            return False
        
        freq_magazine[c] -= 1
    
    return True


# Driver code.
if __name__=="__main__":
    s = "string"
    magazine = "this is a strig"
    print(find_string(s, magazine))


    s = "string"
    magazine = "this is a string"
    print(find_string(s, magazine))

    