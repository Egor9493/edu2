import sys


def main() -> str:
    args = sys.argv

    try:
        if len(args) != 4:
            raise ValueError("Incorrect number of arguments")

        for symbol in args[2]:
            if ord(symbol) not in range(32, 127):
                raise ValueError("Incorrect symbols in input string")

        if args[1] not in ['encode', 'decode']:
            raise ValueError("Incorrect command")

        shift = int(args[3])

        return encode_decode(args[1], args[2], shift)

    except Exception as err:
        return str(err)


def encode_decode(command: str, text: str, shift: int):
    res_text = ''

    for symbol in text:
        index = ord(symbol) - 32
        print(index)

        if command == 'encode':
            code = index + shift
        else:
            code = index - shift

        res_text += chr(code)

    return res_text


if __name__ == "__main__":
    print(main())
