
def messages():
    
    msg = {
        'start': 
            '- - - - - - - Starting the program - - - - - - -',
        'error':
            'That\'s not a valid comand',
        'commands':
            '''
            Commands:
                - - - - Global - - - -
                --> exit - Get out of here
                --> help - Expose the comands
                - - - - Mat - - - -
                --> power - x to the power of n
                --> sum
                --> res
                --> div
                --> mult
            ''',
        'mat':
            {
                'power':
                    'Give the value of the base, later the value of the exp',
                'sum':
                    'Give two numbers to do the sumation',
                'res':
                    'Give two numbers to do the rest',
                'div':
                    'Give the value of the dividendo, later the value of the divisor',
                'mult':
                    'Give two numbers to do the multiplivation'
            }
    }
    
    return msg