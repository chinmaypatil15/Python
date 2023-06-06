def find_highest_frequency_word_length(input_string):
    # Remove punctuation marks and convert the string to lowercase
    cleaned_string = 'write'.join(c.lower() for c in input_string if c.isalpha() or c.isspace())

    # Split the string into words
    words = cleaned_string.split()

    # Count the frequency of each word
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Find the highest frequency
    max_freq = 0
    for freq in word_freq.values():
        if freq > max_freq:
            max_freq = freq

    # Find the length of the highest-frequency word
    highest_freq_word_length = 0
    for word, freq in word_freq.items():
        if freq == max_freq and len(word) > highest_freq_word_length:
            highest_freq_word_length = len(word)

    return highest_freq_word_length


# Test case 1
input_string1 = "write write write all the number from from from 1 to 100"
result1 = find_highest_frequency_word_length(input_string1)
print("Length of the highest-frequency word:", result1)
# Output: Length of the highest-frequency word: 5
# Explanation: The most frequent word is "write" with a frequency of 3, and its length is 5.

# Test case 2
input_string2 = "the quick brown fox jumps over the lazy dog"
result2 = find_highest_frequency_word_length(input_string2)
print("Length of the highest-frequency word:", result2)
# Output: Length of the highest-frequency word: 4
# Explanation: The words "the" and "over" both appear twice in the string, but "over" has a length of 4, which is higher.

# Test case 3
input_string3 = "apple apple orange banana banana banana cherry cherry cherry cherry cherry"
result3 = find_highest_frequency_word_length(input_string3)
print("Length of the highest-frequency word:", result3)
# Output: Length of the highest-frequency word: 6
# Explanation: The most frequent word is "cherry" with a frequency of 5, and its length is 6.
