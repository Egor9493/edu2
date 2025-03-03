import sys


def get_path() -> str:
    args = sys.argv
    if len(args) == 2:
        return args[1]

    raise Exception("Incorrect input parameters!")


def get_names() -> str:
    path = get_path()

    with open(path) as file:
        mails_lst = [el for el in file.read().split('\n') if el]
        names = []

        for mail in mails_lst:
            name = mail.split('.')[0].capitalize()
            surname = mail.split('.')[1].split('@')[0].capitalize()

            names.append('\t'.join([name, surname, mail]))

        return '\n'.join(names)


def write_to_file(table: str) -> None:
    path = 'employees.tsv'
    with open(path, 'w') as file:
        file.write(table)


if __name__ == "__main__":
    try:
        tbl = get_names()
        write_to_file(tbl)
    except IndexError:
        print('Incorrect file!')

