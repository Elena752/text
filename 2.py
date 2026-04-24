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
            print("Функция 2")
        elif choice == "3":
            print("Функция 3")
        elif choice == "4":
            print("Функция 4")
        else:
            break

if __name__ == "__main__":
    main()