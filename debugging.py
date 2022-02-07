from ast import Num
from site import venv


def divisor(num):
    divisors = [i for i in range(1, num+1) if num % i == 0 ]
    return divisors
            

def run():
    try:        
        num = int(input('ingrese un número: '))
        if num < 0:
            raise Exception
        
        print(divisor(num))
        print('El programa terminó')
    
    except ValueError:
        print('Debes ingreso un número :) ')
    
    except Exception:
        print('Debes ingresar un valor positivo :/')

if __name__ == '__main__':
    run()