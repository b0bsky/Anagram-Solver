# Program to output all possible anagrams that can be created from an inputted string of characters

from itertools import permutations

# Variables for input and output
users_letters = input("Input letters: ")
anagrams = []
combinations = []
for i in range(0, len(users_letters) + 1):
    for j in permutations(users_letters, i):
        combinations.append("".join(j))

combinations = list(set(combinations))
# print("combo: ", combinations)
# Function to check each letter in users input and compares it with word from dictionary, if it is in the given dictionary then add it to anagrams array
def check_for_anagram(check_word):
    for i in combinations:
        if i == check_word:
            if not any(i in s for s in anagrams):
                if len(i) > 1:
                    anagrams.append(i)

# Main function
def main():

    dictionary = open("dictionary", "r")

    for word in dictionary:
        word = word.strip()
        check_for_anagram(word)
    if not anagrams:
        print("No matches found!")
    else:
        print("Anagrams: ", anagrams)
    dictionary.close()
if __name__ == "__main__":
    main()