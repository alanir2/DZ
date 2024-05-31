import csv


def write_holiday_cities(first_letter):
    # РЕАЛИЗАЦИЯ
    with open('travel-notes.csv', 'r', newline='') as csv_file:
        csv_data = csv.reader(csv_file)  # <_csv.reader object at 0x01CCFD30>
        data = list(csv_data)
        visited_cities = set()
        desired_cities = set()
        never_visited_cities = []
        city_next = []
        for student_data in data:
            student_name, visited, desired = student_data
            if student_name.startswith(first_letter):
                visited_cities.update(visited.split(';'))  # Добавление посещенных городов студента
                desired_cities.update(desired.split(';'))

        all_cities = (visited_cities | desired_cities)
        # print(sorted(all_cities))
        for city in all_cities:
            # print(city)
            if city not in visited_cities:
                never_visited_cities.append(city)  # Добавление никогда не посещенных городов
                # print(never_visited_cities[0])

        visited_cities = (sorted(visited_cities))
        # print(visited_cities)
        desired_cities = (sorted(desired_cities))
        never_visited_cities = (sorted(never_visited_cities))
        city_next.append(never_visited_cities[0])
    with open('holiday.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Посетили:"] + visited_cities)
        writer.writerow(['Хотят посетить:'] + desired_cities)
        writer.writerow(['Никогда не были в:'] + never_visited_cities)
        writer.writerow(['Следующим городом будет:'] + city_next)



# import csv
file_1 = "['Lisa', 'Moscow;Saint Petersburg;Luxembourg', 'Cairo;Levan;Minsk']", "['Artemy', 'Saint Petersburg;Nizhny Novgorod', 'Pinsk;Rostov;Odintsovo;Minsk']", "['Egor', 'Moscow;Lyubertsy;Dubai', 'Krasnodar;Naberezhnye Chelny;Kazan']", "['Vlad', 'Rostov;Nizhny Novgorod', 'Tokyo;Beijing']", "['Nastya', 'Stavropol;Saratov;Paris', 'Kazan']", "['Lera', 'Kiev;Minsk;Moscow', 'Almaty']", "['Lyuba', 'Beijing;Dushanbe;Tbilisi;Aktau', 'Cairo;Minsk']", "['Larisa', 'New York;Irkutsk;Vladikavkaz', 'Nizhny Tagil;Kursk;Orel']", "['Lyubov', 'Beijing;Kiev', 'Tokyo']", "['Anna', 'Minsk', 'Moscow']", "['Ruslan', 'Lyubertsy;Odintsovo;Nizhny Tagil', 'Kiev;Perm']"
inventory_of_stash = []

# with open('travel-notes.csv', 'r', newline='') as csv_file:
#     csv_data = csv.reader(csv_file)  # <_csv.reader object at 0x01CCFD30>
#     # data = list(csv_data)
#     for row in csv_data:
#         a = row[1]
#         # print(a)
#         inventory_of_stash.append(row)
# with open('holiday.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(inventory_of_stash)

# print(data)


file_1 = [['Lisa', 'Moscow;Saint Petersburg;Luxembourg', 'Cairo;Levan;Minsk'],
          ['Artemy', 'Saint Petersburg;Nizhny Novgorod', 'Pinsk;Rostov;Odintsovo;Minsk'],
          ['Egor', 'Moscow;Lyubertsy;Dubai', 'Krasnodar;Naberezhnye Chelny;Kazan'],
          ['Vlad', 'Rostov;Nizhny Novgorod', 'Tokyo;Beijing'],
          ['Nastya', 'Stavropol;Saratov;Paris', 'Kazan'],
          ['Lera', 'Kiev;Minsk;Moscow', 'Almaty'],
          ['Lyuba', 'Beijing;Dushanbe;Tbilisi;Aktau', 'Cairo;Minsk'],
          ['Larisa', 'New York;Irkutsk;Vladikavkaz', 'Nizhny Tagil;Kursk;Orel'],
          ['Lyubov', 'Beijing;Kiev', 'Tokyo'],
          ['Anna', 'Minsk', 'Moscow'],
          ['Ruslan', 'Lyubertsy;Odintsovo;Nizhny Tagil', 'Kiev;Perm']]

# visited_cities = set()
# desired_cities = set()
# never_visited_cities = []
# for student_data in file_1:
#     student_name, visited, desired = student_data
#     if student_name.startswith('L'):
#         visited_cities.update(visited.split(';'))  # Добавление посещенных городов студента
#         desired_cities.update(desired.split(';'))
#
# all_cities = (visited_cities | desired_cities)
# # print(sorted(all_cities))
# for city in all_cities:
#     # print(city)
#     if city not in visited_cities:
#         never_visited_cities.append(city)  # Добавление никогда не посещенных городов
#         # print(never_visited_cities)
#
# visited_cities = (sorted(visited_cities))
# # print(visited_cities)
# desired_cities = (sorted(desired_cities))
# never_visited_cities = (sorted(never_visited_cities))
# with open('holiday.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(visited_cities)
#     writer.writerow(desired_cities)
#     writer.writerow(never_visited_cities)


# def write_holiday_cities(first_letter):
#     with open('holiday.csv', 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#
#         visited_cities = []
#         desired_cities = []
#         never_visited_cities = []
#
#         for student_data in file_1:
#             student_name, visited, desired = student_data  # Разделение строки на имя студента и списки городов
#
#             if student_name.startswith(first_letter):
#                 visited_cities.extend(visited.split(';'))  # Добавление посещенных городов студента
#                 desired_cities.extend(desired.split(';'))  # Добавление желаемых городов студента
#
#         all_cities = set(visited_cities + desired_cities)  # Множество всех городов
#
#         for city in all_cities:
#             if city not in visited_cities and city not in desired_cities:
#                 never_visited_cities.append(city)  # Добавление никогда не посещенных городов
#
#         visited_cities = sorted(set(visited_cities))  # Сортировка посещенных городов
#         print(visited_cities)
#         desired_cities = sorted(set(desired_cities))  # Сортировка желаемых городов
#         never_visited_cities = sorted(set(never_visited_cities))  # Сортировка никогда не посещенных городов
#
#         next_city = min(all_cities)  # Первый город в алфавитном порядке
#
#         writer.writerow(["Посетили:"] + visited_cities)
#         writer.writerow(["Хотят посетить:"] + desired_cities)
#         writer.writerow(["Никогда не были в:"] + never_visited_cities)
#         writer.writerow(["Следующим городом будет:", next_city])
#
#
# # Проверка для буквы 'L'
print(write_holiday_cities('L'))
#
# # Проверка для буквы 'R'
# write_holiday_cities('R')
