import sys


def get_mail() -> str:
    args = sys.argv
    if len(args) == 2:  # Если аргументов комадной строки не 2, то поднимается исключение
        return args[1].lower()

    raise Exception("Incorrect input parameters!")


def get_name(mail: str) -> str:
    path = 'employees.tsv'

    # В списке строк, полученном из содержимого файла, разбитого по '\n', элементы разбиваются на списки по '\t'.
    # Из каждого списка берется 0 элемент, если 2 элемент - нужный mail. Если итоговый список не пустой - выводится
    # нулевой элемент.

    with (open(path) as file):
        table = file.read()
        mail_list = [el.split('\t')[0] for el in table.split('\n') if el.split('\t')[2] == mail]
        if len(mail_list):
            return mail_list[0]


def create_letter_text() -> str:
    name = get_name(get_mail())

    if name:
        return (f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you.\n'
                f'That’s a precondition for the professionals that our company hires.')

    return 'Unknown mail'


if __name__ == "__main__":
    print(create_letter_text())
