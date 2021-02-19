
def do_power(values):
    result = float(values[0]) ** float(values[1])
    msg_result(values, result, '**')


def do_mult(values):
    result = float(values[0]) * float(values[1])
    msg_result(values, result, '*')
    

def do_div(values):
    result = float(values[0]) / float(values[1])
    msg_result(values, result, '/')
    

def do_sum(values):
    result = float(values[0]) + float(values[1])
    msg_result(values, result, '+')
    

def do_rest(values):
    result = float(values[0]) - float(values[1])
    msg_result(values, result, '-')


def msg_result(values, result, operation):
    print(f'The result of {values[0]} {operation} {values[1]} is {result}')