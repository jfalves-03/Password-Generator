from turtle import color
from colorama.ansi import AnsiFore

def lines(num: int) -> None: 
    print('-'*num) 

def colors(c: str) -> int: 
    color = {'GREEN': AnsiFore.GREEN, 'RED': AnsiFore.RED, 'BLACK': AnsiFore.BLACK, 
             'BLUE': AnsiFore.BLUE, 'YELLOW': AnsiFore.YELLOW, 'WHITE': AnsiFore.WHITE, 
             'RESET': AnsiFore.RESET} 
    
    for k in color.keys(): 
        if k == c.upper(): 
            return f'\033[{color[k]}m'  
    
def title() -> None: 
    lines(50) 
    t = f'{colors("GREEN")}PASSWORD GENERATOR{colors("RESET")}'
    print(t.center(57)) 
    lines(50) 

def password_strong(password: str, sit: bool) -> None: 
    print(f'{password} -> ', end='') 
    if sit: 
        print(f'{colors("BLUE")}SENHA FORTE{colors("RESET")}') 
    else: 
        print('FRACA!')

