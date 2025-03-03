import sys


def get_arg() -> list:
    args = sys.argv

    if 1 < len(args) < 3:
        string = args[1]
        lst = [el.strip() for el in string.split(',')]
        if all(lst):
            return lst


def show_info() -> None:
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

    arg_list = get_arg()

    if arg_list:
        names = {v: k for k, v in COMPANIES.items()}

        for arg in arg_list:
            name_by_stock = names.get(arg.upper())
            stock_by_name = COMPANIES.get(arg.capitalize())

            if stock_by_name:
                price_by_name = STOCKS[stock_by_name]
                if price_by_name:
                    print(f'{arg.capitalize()} stock price is {price_by_name}')

            elif name_by_stock:
                print(f'{arg.upper()} is a ticker symbol for {name_by_stock}')

            else:
                print(f'{arg} is an unknown company or an unknown ticker symbol')


if __name__ == '__main__':
    show_info()
