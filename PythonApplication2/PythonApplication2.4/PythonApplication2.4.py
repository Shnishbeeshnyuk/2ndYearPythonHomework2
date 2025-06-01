def count_words():
    # Получаем строку от пользователя
    text = input("Enter string: ")
    
    # Разбиваем строку на слова (регистронезависимо)
    words = text.lower().split()
    
    # Создаем словарь для подсчета
    word_count = {}
    
    # Подсчитываем слова
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Выводим результат
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Запускаем программу
count_words()
