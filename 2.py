from collections import Counter
import string

def menu():
    print("\nАнализатор текста")
    print("1. Подсчёт слов и символов")
    print("2. Частота букв")
    print("3. Самое длинное слово")
    print("4. Средняя длина слова")

def count_words_and_chars(text):
    words = text.split()
    num_words = len(words)
    chars_with_spaces = len(text)
    chars_without_spaces = len(text.replace(" ", ""))
    return num_words, chars_with_spaces, chars_without_spaces

def letter_frequency(text):
    letters = [ch.lower() for ch in text if ch.isalpha()]
    return Counter(letters)

def longest_word(text):
    words = text.split()
    if not words:
        return None
    return max(words, key=len)

def average_word_length_clean(text):
    translator = str.maketrans('', '', string.punctuation)
    cleaned = text.translate(translator)
    words = cleaned.split()
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)

def main():
    while True:
        text = input("Введите текст: ")
        menu()
        choice = input("Выберите опцию: ")
        if choice == "1":
            w, cws, cwos = count_words_and_chars(text)
            print(f"Слов: {w}")
            print(f"Символов (с побелами): {cws}")
            print(f"Символов (без пробелов): {cwos}")

        elif choice == "2":
            freq = letter_frequency(text)
            if not freq:
                print("Нет букв в тексте")
            else:
                for ch, cnt in freq.most_common():
                    print(f"{ch}: {cnt}")

        elif choice == "3":
            lw = longest_word(text)
            if lw:
                print(f"Самое длинное слово: '{lw}' (длина {len(lw)})")
            else:
                print("Текст пуст")
        elif choice == "4":
            print(f"Средняя длина слова: {average_word_length_clean(text)}")
        else:
            break

if __name__ == "__main__":
    main()