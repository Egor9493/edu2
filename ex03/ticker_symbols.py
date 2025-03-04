import sys


def get_arg() -> str:
    args = sys.argv

    if len(args) == 2:  # Если аргументов комадной строки 2
        return args[1].upper()


def show_info(arg) -> None:
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    if arg:  # Если аргументы командной строки корректны
        names = {v: k for k, v in COMPANIES.items()}  # создаем вспомогательный словарь {ticker: name}

        name = names.get(arg)
        price = STOCKS.get(arg)

        if name and price:  # если тикер найден в словарях STOCKS и names
            print(f'{name} {price}')
        else:
            print('Unknown ticker')


def main():
    arg = get_arg()
    show_info(arg)


if __name__ == "__main__":
    main()
