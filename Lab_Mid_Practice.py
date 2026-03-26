# Get sentence input and split into list of words
sentence = input("Enter a sentence: ")
words = sentence.lower().split()  # .lower() so 'The' and 'the' count as same word

# Empty dictionary to store word counts
word_count = {}

for word in words:
    # If word already exists in dict, add 1 to its count
    if word in word_count:
        word_count[word] += 1
    else:
        # First time seeing this word — set count to 1
        word_count[word] = 1

print("\nWord frequencies:")
for word, count in word_count.items():
    print(f"  '{word}': {count}")

# max() with key= finds the key (word) with the highest value (count)
most_common = max(word_count, key=word_count.get)
print(f"\nMost frequent word: '{most_common}' ({word_count[most_common]} times)")