import json

# def employees_rewrite(sort_type):
#     with open("employees.json", "r") as write_file:
#         a=json.load(write_file)
#         b=sorted(a['employees'], key=lambda x: x[sort_type])
#         print(b)
# employees_rewrite('lastName')
# import json

def employees_rewrite(sort_type):
    if sort_type not in ['firstName', 'lastName', 'department', 'salary']:
        raise ValueError('Bad key for sorting')

    with open('employees.json', 'r') as file:
        data = json.load(file)
        if sort_type == 'salary':
            sorted_data = sorted(data['employees'], key=lambda x: x[sort_type], reverse=True)
        else:
            sorted_data = sorted(data['employees'], key=lambda x: x[sort_type])

    with open(f'employees_{sort_type}_sorted.json', 'w') as file:
        json.dump({'employees': sorted_data}, file, indent=2)

# Пример вызова функции для сортировки по ключу 'lastName'
employees_rewrite('firstName')