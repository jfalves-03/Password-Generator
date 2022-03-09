from random import * 
class Password: 
    
    __requirements = ['@', '#', '&', '%', '$', '!']
    __alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                    'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                    'o', 'p', 'q', 'r', 's', 't', 'u', 
                    'v', 'w', 'x', 'y', 'z']
    __number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self, password): 
        self.__password = password 

    @property 
    def password(self): 
        return self.__password 
        
    def check_special_characs(self): 
        cont = 0
        for item in self.__password: 
            for symbol in self.__requirements: 
                if item == symbol: 
                    cont += 1 
        if len(self.__password) <= 5 and cont == 1: 
            return True, cont
        elif 5 < len(self.__password) <= 10 and cont == 2: 
            return True, cont 
        elif 10 < len(self.__password) <= 15 and cont == 4: 
            return True, cont 
        elif len(self.__password) > 15 and cont == 5: 
            return True, cont 
        return False, cont

    def add_special_characs(self) -> str:  
        cont = 0
        list_letters = [] 
        for letter in self.__password: 
            list_letters.append(letter) 
        
        tam = len(self.__password)
        
        if len(self.__password) > 0: 
            if tam <= 5: 
                times = 1 
            elif 5 < tam <= 10: 
                times = 2 
            elif 10 < tam <= 15: 
                times = 4
            else: 
                times = 5 

            while cont < times: 
                add_index = randint(0, len(list_letters)-1)
                c =  choice(self.__requirements)
                if list_letters[add_index] == c:
                    cont += 1
                else: 
                    list_letters[add_index] = c
                    cont += 1
        
        return ''.join(list_letters)
                 
    def check_upper_case(self): 
        cont = 0 
        for item in self.__password: 
            for alpha in self.__alpha: 
                if item == alpha.upper(): 
                    cont += 1 
        if len(self.__password) <= 5 and cont >= 1: 
            return True, cont  
        elif 5 < len(self.__password) <= 10 and cont >= 2: 
            return True, cont 
        elif 10 < len(self.__password) <= 15 and cont >= 4: 
            return True, cont 
        elif len(self.__password) > 15 and cont >= 5: 
            return True, cont 
        return False, cont

    def add_upper_case(self, cont) -> str: 
        list_letters = [] 
        
        for letter in self.__password: 
            list_letters.append(letter)  
        
        tam = len(self.__password)
        
        if len(self.__password) > 0: 
            if tam <= 5: 
                times = 1 
            elif 5 < tam <= 10: 
                times = 2 
            elif 10 < tam <= 15: 
                times = 4
            else: 
                times = 5 

            while cont < times:  
                add_index = randint(0, len(list_letters)-1) 
                for l in self.__alpha: 
                    if list_letters[add_index] == l.upper(): 
                        continue
                    if list_letters[add_index] == l: 
                        list_letters[add_index] = l.upper()
                        cont += 1 
                    
        return ''.join(list_letters)

    def check_lower_case(self): 
        cont = 0 
        for item in self.__password: 
            for alpha in self.__alpha: 
                if item == alpha: 
                    cont += 1 
        if len(self.__password) <= 5 and cont >= 1: 
            return True, cont 
        elif 5 < len(self.__password) <= 10 and cont >= 2: 
            return True, cont  
        elif 10 < len(self.__password) <= 15 and cont >= 4: 
            return True, cont
        elif len(self.__password) > 15 and cont >= 5: 
            return True, cont 
        return False, cont 

    def add_lower_case(self, cont): 
        list_letters = [] 

        for letter in self.__password: 
            list_letters.append(letter) 

        tam = len(self.__password)
        
        if len(self.__password) > 0: 
            if tam <= 5: 
                times = 1 
            elif 5 < tam <= 10: 
                times = 2 
            elif 10 < tam <= 15: 
                times = 4
            else: 
                times = 5 

            while cont < times:  
                add_index = randint(0, len(list_letters)-1) 
                for l in self.__alpha: 
                    if list_letters[add_index] == l: 
                        continue
                    if list_letters[add_index] == l.upper(): 
                        list_letters[add_index] = l
                        cont += 1 
        
        return ''.join(list_letters)

    def check_numbers(self): 
        cont = 0 
        for letter in self.__password: 
            for number in self.__number: 
                if letter == number: 
                    cont += 1 
        if len(self.__password) <= 5 and cont >= 1: 
            return True, cont 
        elif 5 < len(self.__password) <= 10 and cont >= 2: 
            return True, cont  
        elif 10 < len(self.__password) <= 15 and cont >= 4: 
            return True, cont
        elif len(self.__password) > 15 and cont >= 5: 
            return True, cont 
        return False, cont  
        
    def add_numbers(self, cont): 
        list_letters = [] 

        for letter in self.__password: 
            list_letters.append(letter) 

        tam = len(self.__password)
        
        if len(self.__password) > 0: 
            if tam <= 5: 
                times = 1 
            elif 5 < tam <= 10: 
                times = 2 
            elif 10 < tam <= 15: 
                times = 4
            else: 
                times = 5 
          
            while cont < times:  
                add_index = randint(0, len(list_letters) - 1) 
                if list_letters[add_index] in self.__number: 
                    continue 
                else: 
                    list_letters.insert(add_index, choice(self.__number)) 
                    cont += 1
            
            return ''.join(list_letters)
                            
    def transform(self, new): 
        self.__password = new
        return self.__password

    def global_check(self, final): 
        if final: 
            return True 
        else: 
            return False




    