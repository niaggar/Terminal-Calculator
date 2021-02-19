
from msgs import messages


def rq_input():
    return input('>>> ')


def rq_num(operation):
    print(messages()['mat'][operation])
    num1 = rq_input()
    num2 = rq_input()
    return num1, num2


def do_power(values):
    result = float(values[0]) ** float(values[1])
    print(f'The result of {values[0]} ** {values[1]} is {result}')


def detect_command(command):
    if command == 'exit':
        return False
    elif command == 'help':
        print(messages()['commands'])
        return True
    elif command == 'power':
        do_power(rq_num('power'))
        return True
    else:
        print(messages()['error'])
        return True


if __name__ == '__main__':
    
    print(messages()['start'])
    
    state = True
    while state:
        command = rq_input()
        state = detect_command(command.lower())