def make_dict() -> dict:
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

    return dict(list_of_tuples)


def sort_list(src_dct: dict) -> None:
    dct_reversed = {}
    sorted_lst = []

    for name, number in src_dct.items():  # Заполняем словарь dct_reversed - {число: список стран}
        dct_reversed[int(number)] = dct_reversed.get(int(number), []) + [name]

    for key in sorted(dct_reversed.keys(), reverse=True):  # По отсортированным ключам получаем списки стран, сортируем
        sorted_lst.extend(sorted(dct_reversed[key]))       # и добавляем в итоговый список

    [print(el) for el in sorted_lst]


def main():
    dct = make_dict()
    sort_list(dct)


if __name__ == "__main__":
    main()

