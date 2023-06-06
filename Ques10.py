import nltk
#nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def count_pos_tags(text):
    # Tokenize the text into individual words
    words = word_tokenize(text)

    # Tag each word with its part-of-speech (POS)
    tagged_words = pos_tag(words)

    # Count the number of verbs, nouns, pronouns, and adjectives
    counts = {
        'verbs': 0,
        'nouns': 0,
        'pronouns': 0,
        'adjectives': 0
    }

    for word, tag in tagged_words:
        if tag.startswith('V'):  # Verb
            counts['verbs'] += 1
        elif tag.startswith('N'):  # Noun
            counts['nouns'] += 1
        elif tag.startswith('PRP'):  # Pronoun
            counts['pronouns'] += 1
        elif tag.startswith('JJ'):  # Adjective
            counts['adjectives'] += 1

    return counts

# Test case 1: Count POS tags in a phrase
phrase = "The quick brown fox jumps over the lazy dog"
result = count_pos_tags(phrase)
print("POS counts for phrase:", phrase)
print(result)
print()

# Test case 2: Count POS tags in a paragraph
paragraph = "The sun was shining brightly. John went to the park and played with his dog. He felt happy and content."
result = count_pos_tags(paragraph)
print("POS counts for paragraph:")
print(result)
print()

# Additional Test case 3: Count POS tags in a longer paragraph with complex sentence structures
long_paragraph = "The old man stood up, stretched his arms, and looked out of the window. He saw a beautiful rainbow and exclaimed, 'Wow, what a sight!'"
result = count_pos_tags(long_paragraph)
print("POS counts for long paragraph:")
print(result)
