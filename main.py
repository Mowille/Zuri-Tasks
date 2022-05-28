# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code
    if (sorted(word)) == (sorted(anagram)):
        result = True
    else:
        result = False
    print(result)


first_str = input("Enter your first word: ")
second_str = input("Enter your second word: ")
find_anagram(first_str, second_str)
