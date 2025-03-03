def data_types() -> None:
    a = 1
    b = '1'
    c = 1.0
    d = True
    e = [1]
    f = {1: 1}
    g = (1,)
    h = {1}

    names_lst = [type(el).__name__ for el in (a, b, c, d, e, f, g, h)]
    names_string = ', '.join(names_lst)

    print(f'[{names_string}]')


if __name__ == '__main__':
    data_types()
