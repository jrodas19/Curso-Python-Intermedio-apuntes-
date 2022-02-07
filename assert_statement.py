def divisor(num):
    divisors = [i for i in range(1, num+1) if num % i == 0 ]
    return divisors
            

def run():
    num = input('ingrese un número: ')
    
    assert num.isnumeric() and int(num)>0, 'Debe ingresar un número'
    
    num = int(num)
    # assert num > 0, 'Debe ingresar un número positivo'
    
    print(divisor(num))
    print('El programa terminó')

if __name__ == '__main__':
    run()