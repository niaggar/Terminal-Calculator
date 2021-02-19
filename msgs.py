
def messages():
    
    msg = {
        'start': 
            '- - - - - - - Starting the program - - - - - - -',
        'error':
            'That\'s not a valid comand',
        'commands':
            '''
            Commands:
                - - Global - -
                --> exit - Get out of here
                --> help - Expose the comands
                
                - - Mat - -
                --> power - x to the power of n
            ''',
        'mat':
            {
                'power':
                    'Give the value of the base, later the value of the exp'
            }
    }
    
    return msg