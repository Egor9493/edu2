import sys


def get_path() -> str:
    args = sys.argv
    if len(args) == 2:  # Если аргументов комадной строки не 2, то поднимается исключение
        return args[1]

    raise AttributeError("Incorrect input parameters!")


def get_names(path: str) -> str:
    try:
        with open(path) as file:
            mails_lst = [el for el in file.read().split('\n') if el]  # Создается список из непустых строк файла
            names = []

            for mail in mails_lst:  # Для каждой строки выделяются имя и фамилия
                name = mail.split('.')[0].capitalize()
                surname = mail.split('.')[1].split('@')[0].capitalize()

                names.append('\t'.join([name, surname, mail]))  # Имя, Фамилия, почта в виде строки, разделенной \t
                # добавляются в список names

            return '\n'.join(names)  # Список name объединяется в строку по \n и возвращается

    except FileNotFoundError:  # Обрабатывется исключение, возникающее при отсутствии исходного файла
        print(f'File {path} not found!')


def write_to_file(table: str) -> None:
    path = 'employees.tsv'
    if table:
        with open(path, 'w') as file:
            file.write(table)
        print(f'File {path} created successfully.')


def main():
    try:
        path_to_input_file = get_path()
        tbl = get_names(path_to_input_file)
        write_to_file(tbl)
    except IndexError:  # Обрабатываются возможные исключения при несоответствии формата записи mail в файле
        print('Incorrect file format!')


if __name__ == "__main__":
    main()
