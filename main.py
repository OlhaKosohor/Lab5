import string


def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            first_sentence = text.split(".")[0]  # Зчитуємо перше речення
            print("Перше речення:", first_sentence)

            translator = str.maketrans("", "", string.punctuation)
            words = text.translate(translator).split()

            uk_words = [
                word
                for word in words
                if all("а" <= char <= "я" or "А" <= char <= "Я" for char in word)
            ]
            en_words = [
                word
                for word in words
                if all("a" <= char <= "z" or "A" <= char <= "Z" for char in word)
            ]

            uk_words_sorted = sorted(uk_words, key=lambda w: w.lower())
            en_words_sorted = sorted(en_words, key=lambda w: w.lower())

            print("\nУкраїнські слова (відсортовані):", uk_words_sorted)
            print("\nАнглійські слова (відсортовані):", en_words_sorted)
            print(f"\nЗагальна кількість слів: {len(words)}")

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    read_file("file.txt")
