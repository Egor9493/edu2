import sys


def main() -> str:
    args = sys.argv

    try:
        if len(args) != 4:  # Проверка количества аргументов командной строки
            raise ValueError("Incorrect number of arguments")

        for symbol in args[2]:  # Проверка на допустимые симолы исходной строки
            if ord(symbol) not in list(range(32, 127)):
                raise ValueError("Incorrect symbols in input string")

        if args[1] not in ['encode', 'decode']:  # Проверка на допустимые команды
            raise ValueError("Incorrect command")

        shift = int(args[3])  # Проверка/преобразование значения сдвига

        return encode_decode(args[1], args[2], shift)

    except Exception as err:
        return str(err)


def encode_decode(command: str, text: str, shift: int):
    res_text = ''
    for symbol in text:
        code_0 = ord(symbol) - 32  # Номер символа в таблице кодов ASCII разрешенных символов

        if command == 'encode':  # В зависимости от полученной команды вычисление результирующего символа
            shifted_code = (code_0 + shift) % 94 + 32
        else:
            shifted_code = (94 + code_0 - shift) % 94 + 32

        res_text += chr(shifted_code)

    return res_text


if __name__ == "__main__":
    print(main())
