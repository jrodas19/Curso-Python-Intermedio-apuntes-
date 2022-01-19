def run():
    
    # lista = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         lista.append(i**2)
        
    lista = [i**2 for i in range(1,100000) if i % 36 ==0]
    print(lista[0:10])

if __name__ == '__main__':
    run()

