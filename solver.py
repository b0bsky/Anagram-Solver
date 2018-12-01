# Program to output all possible anagrams that can be created from an inputted string of characters

# Variables for input and output
users_letters = input("Input letters: ")
anagrams = []

# Function to check each letter in users input and compares it with word from dictionary, if it is in the given dictionary then add it to anagrams array
def check_for_anagram( letters, check_word):
    for letter in letters:
        if letter in check_word:
            if not any(letter in s for s in anagrams):
                anagrams.append(letter)

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