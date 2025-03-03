import sys


def get_arg() -> str:
    args = sys.argv

    if 1 < len(args) < 3:
        return args[1].capitalize()


def show_price() -> None:

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
        stock = COMPANIES.get(arg)

        if stock:
            print(STOCKS.get(stock))
        else:
            print('Unknown company')


if __name__ == "__main__":
    show_price()
