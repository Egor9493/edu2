import sys


class Data:
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
                   'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
                   'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                        'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                        'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']


def main() -> list:
    args = sys.argv
    if len(args) == 2:    # Если аргументов комадной строки не 2, то поднимается исключение
        if args[1] == 'call_center':
            return create_call_center_list()
        elif args[1] == 'potential_clients':
            return create_potential_clients_list()
        elif args[1] == 'loyalty_program':
            return create_loyalty_program_list()

    raise Exception("Incorrect input parameters!")


def create_call_center_list() -> list:
    return list(set(Data.clients) - set(Data.recipients))  # Клиенты не вошедшие в рассылку


def create_potential_clients_list() -> list:
    return list(set(Data.participants) - set(Data.clients))  # Участники мероприятия, не являющиеся клиентами


def create_loyalty_program_list() -> list:
    return list(set(Data.clients) - set(Data.participants))  # Клиенты, не учавствовавшие в мероприятии


if __name__ == "__main__":
    print(main())
