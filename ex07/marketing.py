import sys


def data_dict() -> dict:
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    return dict(clients=set(clients), participants=set(participants), recipients=set(recipients))


def main() -> list:
    args = sys.argv
    if len(args) == 2:
        if args[1] == 'call_center':
            return create_call_center_list()
        elif args[1] == 'potential_clients':
            return create_potential_clients_list()
        elif args[1] == 'loyalty_program':
            return create_loyalty_program_list()

    raise Exception("Incorrect input parameters!")


def create_call_center_list() -> list:
    dct = data_dict()
    return list(dct['clients'] - dct['recipients'])


def create_potential_clients_list() -> list:
    dct = data_dict()
    return list(dct['participants'] - dct['clients'])


def create_loyalty_program_list() -> list:
    dct = data_dict()
    return list(dct['clients'] - dct['participants'])


if __name__ == "__main__":
    print(main())
