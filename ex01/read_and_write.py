def read_csv(path: str = './ds.csv') -> str:
    with open(path) as file:
        txt = file.read()
        lst = []

        for row in txt.split('\n'):  # Для каждой строки файла
            if row:  # Если строка не пуста создаем временные разделители
                row = row.replace('","', '***')
                row = row.replace('",', '***')
                row = row.replace(',"', '***')
                lst.append(row.strip('"').split('***'))  # Разбиваем на списки и добавляем в список lst

        result_lst = []

        for row in lst:
            result_row = []
            for col_n, col in enumerate(row):  # Дополнительно разбиваем 4 колонку
                if col_n == 3:
                    result_row.extend(col.split(','))
                else:
                    result_row.append(col)

            result_lst.append(result_row)  # Помещаем результат в список result_lst

    result_txt = '\n'.join(['\t'.join(row) for row in result_lst])  # Формируем таблицу

    return result_txt


def write_tsv(text: str, path: str = './ds.tsv') -> None:
    with open(path, 'w') as file:
        file.write(text)


def main():
    res = read_csv()
    write_tsv(res)


if __name__ == "__main__":
    main()
