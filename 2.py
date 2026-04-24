def menu():
print("\n=== Анализатор текста ===")
print("1. Подсчёт слов и символов")
print("2. Частота букв")
print("3. Самое длинное слово")
print("4. Удалить стоп-слова")
print("0. Выход")

def main():
while True:
menu()
choice = input("Выберите опцию: ")
if choice == "0":
break
text = input("Введите текст: ")
if choice == "1":
print("[Заглушка] Функция 1")
elif choice == "2":
print("[Заглушка] Функция 2")
elif choice == "3":
print("[Заглушка] Функция 3")
elif choice == "4":
print("[Заглушка] Функция 4")
else:
print("Неверный ввод")

if __name__ == "__main__":
main()