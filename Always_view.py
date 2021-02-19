
from msgs import messages
from Operations import do_power, do_mult, do_div, do_sum, do_rest


def rq_input():
    return input('>>> ')


def rq_num(operation):
    print(messages()['mat'][operation])
    num1 = rq_input()
    num2 = rq_input()
    return num1, num2


def detect_command(command):
    if command == 'exit':
        return False
    elif command == 'help':
        print(messages()['commands'])
        return True
    elif command == 'power':
        do_power(rq_num('power'))
        return True
    elif command == 'sum':
        do_sum(rq_num('sum'))
        return True
    elif command == 'res':
        do_rest(rq_num('res'))
        return True
    elif command == 'div':
        do_div(rq_num('div'))
        return True
    elif command == 'mult':
        do_mult(rq_num('mult'))
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