def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Jerson', 'lastname':'Rodas'}
    
    super_list = [
        {'firstname': 'Jerson', 'lastname':'Rodas'},
        {'firstname': 'Marilyn', 'lastname':'Coronel'},
        {'firstname': 'Juan', 'lastname':'Castro'},
        {'firstname': 'Alison', 'lastname':'Retamozo'},
        {'firstname': 'Isabel', 'lastname':'Alarcon'}
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 5.34]
    }
    
    for key, value in super_dict.items():
        print(key, ' - ', value)
    
    for value in super_list:
        print(f'{value["firstname"]} {value["lastname"]}') 
    
if __name__ == '__main__':
    run()
    