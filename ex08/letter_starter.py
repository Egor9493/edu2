import sys


def get_mail() -> str:
    args = sys.argv
    if len(args) == 2:
        return args[1]

    raise Exception("Incorrect input parameters!")


def get_name(mail: str) -> str:
    path = 'employees.tsv'

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
    create_letter_text()
