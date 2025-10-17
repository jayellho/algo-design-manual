'''
[4] Reverse the words in a sentence - that is, "My name is Chris" becomes "Chris is name My".
Optimize for time and space.
'''
'''
algo:
- split into list by space - O(m) where m is the length of the string.
- do in-line swapping of the elements.
    - n // 2 to get the limits of when to stop.
        - odd case: e.g. 5 // 2 = 2  0 1 2 3 4
        - even case: e.g. 4 // 2 = 2 0 1 2 3
    - do a for loop with 2 pointers up to n // 2 and swap. ==> O(n)
- join the list.
'''

def reverse_sentence(s):

    # define vars.
    list_s = s.split(" ")
    n = len(list_s)
    l, r = 0, n-1

    # edge case: empty
    if not list_s:
        return s

    # iterate.
    for _ in range(n // 2):
        list_s[l], list_s[r] = list_s[r], list_s[l]
        l += 1
        r -= 1
    
    return " ".join(list_s)
    
# Driver code.
if __name__ == "__main__":

    s = "The quick brown fox jumps over the lazy hen"

    print(reverse_sentence(s))

    s = "blue green purple black yellow orange"

    print(reverse_sentence(s))