# Program to output all possible anagrams that can be created from an inputted string of characters

from itertools import permutations

# Variables for input and output
users_letters = input("Input letters: ")
anagrams = []

# Function to check each letter in users input and compares it with word from dictionary, if it is in the given dictionary then add it to anagrams array
def check_for_anagram( letters, check_word):
    letter_anagrams = []
    for j in permutations(users_letters):
        letter_anagrams.append("".join(j))
    for i in range(0, len(letter_anagrams)):
        if letter_anagrams[i] == check_word:
            if not any(letter_anagrams[i] in s for s in anagrams):
                anagrams.append(letter_anagrams[i])

# Main function
def main():

    dictionary = open("dictionary", "r")

    for word in dictionary:
        word = word.strip()
        check_for_anagram(users_letters, word)

    print(anagrams)
    dictionary.close()
if __name__ == "__main__":
    main()