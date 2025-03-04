def make_dict():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('США', '610'),
        ('Великобритания', '95'),
        ('Китай', '83'),
        ('Иран', '76'),
        ('Турция', '65'),
        ('Бельгия', '34'),
        ('Канада', '28'),
        ('Швейцария', '26'),
        ('Бразилия', '25'),
        ('Австрия', '14'),
        ('Израиль', '12')
    ]

    dct = {}

    for name, number in list_of_tuples:
        dct[number] = dct.get(number, []) + [name]

    return dct


def print_dict(dct: dict):
    for key in dct:
        for el in dct[key]:
            print(f"'{key}':'{el}'")


def main():
    countries = make_dict()
    print_dict(countries)


if __name__ == "__main__":
    main()
