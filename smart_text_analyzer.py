
import string
from collections import Counter

class SmartTextAnalyzer:

    def __init__(self):
        self.word_frequency = {}
        self.text = ""

    def enter_text(self):
        self.text = input("\nEnter your text: ")
        self.analyze_text()

    def analyze_text(self):
        cleaned_text = self.text.lower()

        for symbol in string.punctuation:
            cleaned_text = cleaned_text.replace(symbol, " ")

        words = cleaned_text.split()
        self.word_frequency = dict(Counter(words))

        print("\nText analyzed successfully!")

    def display_frequency(self):
        if not self.word_frequency:
            print("\nPlease enter text first!")
            return

        print("\n--- Word Frequency ---")
        for word, count in sorted(
            self.word_frequency.items(),
            key=lambda item: (-item[1], item[0])
        ):
            print(word, ":", count)

    def search_keyword(self):
        if not self.word_frequency:
            print("\nPlease enter text first!")
            return

        keyword = input("Enter keyword to search: ").lower()
        print("Frequency:", self.word_frequency.get(keyword, 0))

    def top_words(self):
        if not self.word_frequency:
            print("\nPlease enter text first!")
            return

        print("\n--- Top 5 Frequent Words ---")
        sorted_words = sorted(
            self.word_frequency.items(),
            key=lambda item: (-item[1], item[0])
        )

        for word, count in sorted_words[:5]:
            print(word, ":", count)

    def display_statistics(self):
        if not self.word_frequency:
            print("\nPlease enter text first!")
            return

        total_words = sum(self.word_frequency.values())
        unique_words = len(self.word_frequency)

        print("\n--- Text Statistics ---")
        print("Total words:", total_words)
        print("Unique words:", unique_words)


def main():
    analyzer = SmartTextAnalyzer()

    while True:
        print("\n===== SMART TEXT ANALYZER =====")
        print("1. Enter Text")
        print("2. Display Word Frequency")
        print("3. Search Keyword")
        print("4. Display Top 5 Words")
        print("5. Display Text Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyzer.enter_text()
        elif choice == "2":
            analyzer.display_frequency()
        elif choice == "3":
            analyzer.search_keyword()
        elif choice == "4":
            analyzer.top_words()
        elif choice == "5":
            analyzer.display_statistics()
        elif choice == "6":
            print("Thank you for using Smart Text Analyzer!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
