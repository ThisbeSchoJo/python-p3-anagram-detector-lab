# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word
        self.matches = []
    
    def match(self, word_list):
        self.matches = [] #resets matches each time
        for word in word_list:
            if sorted(letter for letter in word) == sorted(self.word):
                self.matches.append(word)
        return self.matches
      
    # match() takes a list of possible anagrams
    # returns all matches in a list
    # if no matches, it should return an empty list


# Hints:
# will need to iterate over the list of words that the match() method takes as an argument
# will compare each word of the list to the word that the Anagram class is initialized with.
# Determine if they are composed of the same letters...
# you can use a list interpretation on a string to get a list of its individual letters
# [letter for letter in "hello"]
# ["h", "e", "l", "l", "o"]

# You can compare two lists using the ==
# [1, 2, 3] == [1, 2, 3]
# => True
# [1, 3, 2] == [1, 2, 3]
# => False

# Two lists are equal if they contain the same elements, in the same order
# use sorted() on a list to help comparison:
# sorted([1, 3, 2]) == sorted([3, 2, 1])
# => True