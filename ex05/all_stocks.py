import sys


def get_arg() -> list:
    args = sys.argv

    if len(args) == 2:  # Если аргументов комадной строки 2, то генерируем список элементов строки, разделенных ','
        lst = [el.strip() for el in args[1].split(',')]
        if all(lst):  # Если все элементы списка не пусты (в исходной строке отсутствуют двойные запятые и пробелы)
            return lst


def show_info(arg_list: list) -> None:
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

    if arg_list:  # Если аргументы командной строки корректны
        names = {v: k for k, v in COMPANIES.items()}  # создаем вспомогательный словарь {ticker: name}

        for arg in arg_list:
            name_by_ticker = names.get(arg.upper())  # Ищем значение среди тикеров
            ticker_by_name = COMPANIES.get(arg.capitalize())  # Ищем значение среди наименований

            if ticker_by_name:  # Если элемент нашелся среди имен компаний ищем стоимость.
                price_by_name = STOCKS.get(ticker_by_name)
                if price_by_name:
                    print(f'{arg.capitalize()} stock price is {price_by_name}')

            elif name_by_ticker:  # Если элемент нашелся среди тикеров в словаре names
                print(f'{arg.upper()} is a ticker symbol for {name_by_ticker}')

            else:  # Если элемент не нашелся
                print(f'{arg} is an unknown company or an unknown ticker symbol')


def main():
    args = get_arg()
    show_info(args)


if __name__ == '__main__':
    main()
