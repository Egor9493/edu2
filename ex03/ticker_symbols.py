import sys


def get_arg() -> str:
    args = sys.argv

    if 1 < len(args) < 3:
        return args[1].upper()


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

    arg = get_arg()

    if arg:
        names = {v: k for k, v in COMPANIES.items()}

        name = names.get(arg)
        price = STOCKS.get(arg)

        if name and price:
            print(f'{name} {price}')
        else:
            print('Unknown ticker')


if __name__ == "__main__":
    show_info()
