import random

if __name__ == '__main__':
    # Ввод пользователем слова
    input_word = input('Введите слово: ')

    # Задаем путь к файлу
    file_path = 'synonym.txt'

    # Читаем файл и записываем данные словарь
    synonyms_dict = dict()
    try:
        with open(file_path, 'r', encoding='UTF-8') as f:
            synonyms = f.read().split('\n')
        for line in synonyms:  # Проходим по считанным строчкам файла
            if line:  # Если строка не пустая, то добавляем в словарь ключ(слово) и значение(его синоним)
                word = line.split('-')[0].strip().lower()
                synonyms = [x.strip() for x in line.split('-')[1].strip().split(';')]
                if word not in synonyms_dict:
                    synonyms_dict[word] = synonyms
                else:
                    synonyms_dict[word].extend(synonyms)
                for synonym in synonyms:
                    if synonym not in synonyms_dict:
                        synonyms_dict[synonym] = [word] + [x for x in synonyms if x != synonym]
                    else:
                        synonyms_dict[synonym].extend([word] + [x for x in synonyms if x != synonym])

        if input_word.lower() in synonyms_dict:  # Если слово пользователя есть в словаре
            while True:
                return_synonym = random.choice(synonyms_dict[input_word.lower()])
                if return_synonym:
                    print(return_synonym)
                    break
            while True:
                # Спршиваем пользователе о том, устраивает ли его выданный синоним
                synonym_correctness = input('Синоним устраивает?\n'
                                            '1. Да\n'
                                            '2. Нет\n')
                if synonym_correctness == '1':  # Если устраивает, то завершаем работу программы
                    break
                elif synonym_correctness == '2':  # Если не устраивает, то добавляем слово в словарь
                    new_synonym = input('Введите новый синоним: ')
                    if new_synonym not in synonyms_dict[input_word.lower()]:
                        synonyms_dict[input_word.lower()].append(new_synonym)
                        # Запишем данные словаря в файл
                        string_to_write = ''
                        for key in synonyms_dict:
                            synonyms_dict[key] = list(filter(None, synonyms_dict[key]))
                        for word, synonym in synonyms_dict.items():
                            string_to_write += f'{word} - {"; ".join(synonym)}\n'
                        with open(file_path, 'w', encoding='UTF-8') as f:
                            f.write(string_to_write)
                    else:
                        print('\033[31mСлово уже имеется в списке синонимов.\033[0m')
                    break
                else:  # Если ввели не 1 или 2
                    print('\033[31mМожно ввести только 1 или 2.\033[0m')
        else:  # Если слово отсутствует
            print('\033[31mСлово отсутствует в файле.\033[0m')
    except FileNotFoundError:  # В случае если файл не существует
        print(f'\033[31mФайл {file_path} не найден.\033[0m')
