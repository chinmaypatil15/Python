from collections import Counter

def is_valid_string(s):
    # Count the frequency of each character
    char_freq = Counter(s)

    # Count the frequency of frequencies
    freq_freq = Counter(char_freq.values())

    # If there is only one frequency, the string is valid
    if len(freq_freq) == 1:
        return "YES"

    # If there are more than two frequencies, the string is not valid
    if len(freq_freq) > 2:
        return "NO"

    # If there are two frequencies, check if removing one character makes the string valid
    freq1, count1 = freq_freq.most_common(1)[0]
    freq2, count2 = freq_freq.most_common(2)[-1]

    if (count1 == 1 and freq1 == 1) or (count2 == 1 and freq2 == 1):
        return "YES"

    return "NO"


# Test case 1
s1 = "abc"
result1 = is_valid_string(s1)
print(result1)
# Output: YES
# Explanation: All characters appear the same number of times (1), so the string is valid.

# Test case 2
s2 = "abcc"
result2 = is_valid_string(s2)
print(result2)
# Output: NO
# Explanation: If we remove one occurrence of "c", the remaining characters will have frequencies { "a": 1, "b": 1, "c": 2 },
# which is not a valid string.

# Test case 3
s3 = "aabbc"
result3 = is_valid_string(s3)
print(result3)
# Output: YES
# Explanation: All characters appear the same number of times (2), so the string is valid.

# Test case 4
s4 = "aabbcc"
result4 = is_valid_string(s4)
print(result4)
# Output: YES
# Explanation: All characters appear the same number of times (2), so the string is valid.
