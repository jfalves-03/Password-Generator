from password import *

def lines(txt='100') -> None: 
    if txt.isnumeric(): 
        print('-'*txt) 
    else: 
        print('-'*len(txt))  

new_pass = ''

if __name__ == '__main__': 
    # input password 
    generate = str(input('Input your password: ')) 
    code = Password(generate) 
    # ==================================================================

    # check if there´s special characters, if not it´s added in password
    c_special = code.check_special_characs()
    if c_special is not True: 
        add_special = code.add_special_characs()
        code.transform(add_special) 
    else:
        end = code.global_check(True) 
    # ==================================================================
 
    # check if there´s upper case, if not it´s added in password 
    c_upper = code.check_upper_case()
    if c_upper[0] is not True:
        add_upper = code.add_upper_case(c_upper[1])
        code.transform(add_upper)
    else: 
        end = code.global_check(True)
    # ================================================================== 

    # check if there-s lower case, if not it´s added in password 
    c_lower = code.check_lower_case() 
    if c_lower[0] is not True: 
        add_lower = code.add_lower_case(c_lower[1]) 
        code.transform(add_lower)
        print(code.password)
    else: 
        end = code.global_check(True) 
    # ================================================================== 

    #check if there´s some sumber, if not it´s added in password 
    c_number = code.check_numbers() 
    if c_number[0] is not True: 
        add_number = code.add_numbers(c_number[1])
        code.transform(add_number) 
        print(code.password)
    
    

