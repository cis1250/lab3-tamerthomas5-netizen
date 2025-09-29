#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

# word_frequency.py

def is_sentence(text):
    """Check if text is a valid sentence."""
    if not text:
        return False
    return (
        text[0].isupper()
        and text[-1] in ".?!"
        and len(text.split()) > 0
    )

def main():
    # Prompt user until a valid sentence is entered
    while True:
        sentence = input("Enter a sentence: ")
        if is_sentence(sentence):
            break
        else:
            print("Please enter a valid sentence (start with capital, end with . ? or !).")

    # Split sentence into words
    words = sentence.split()

    # Initialize lists
    unique_words = []
    frequencies = []

    # Count word frequencies
    for word in words:
        # Normalize word by removing punctuation at end
        word = word.strip(".,!?").lower()
        if word in unique_words:
            index = unique_words.index(word)
            frequencies[index] += 1
        else:
            unique_words.append(word)
            frequencies.append(1)

    # Print results
    print("\nWord Frequencies:")
    for i in range(len(unique_words)):
        print(f"{unique_words[i]}: {frequencies[i]}")

if __name__ == "__main__":
    main()

    
