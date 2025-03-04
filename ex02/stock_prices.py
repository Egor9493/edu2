import sys


def get_arg() -> str:
    args = sys.argv

    if len(args) == 2:
        return args[1].capitalize()


def show_price(arg: str) -> None:
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

    if arg:
        stock = COMPANIES.get(arg)

        if stock:
            print(STOCKS.get(stock))
        else:
            print('Unknown company')


def main():
    arg = get_arg()
    show_price(arg)


if __name__ == "__main__":
    main()
