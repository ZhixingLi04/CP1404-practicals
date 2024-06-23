"""
Word Occurrences
Estimate: 45 minutes
Actual:   50 minutes
"""


def main():
    text = input("Enter a string: ")
    words = text.split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    max_word_length = max(len(word) for word in word_counts)

    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_length}} : {count}")


main()
