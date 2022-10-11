from random import randint
candies = int(input('Введите количество конфет для игры: '))
name1 = input('Введите имя первого игрока: ')
name2 = input('Введите имя второго игрока. Для игры с ботом введите "Бот": ')
if randint(0, 2):
    user1_name, user2_name = name1, name2
    print(f'Первым ходит игрок {name1}')
else:
    user1_name, user2_name = name2, name1
    print(f'Первым ходит игрок {name2}')
user1_candies = 0
user2_candies = 0
max_candies = 28
print(f'Всего осталось: {candies} конфет')
while candies > 0:
    number_of_candies = 0
    if candies < 28:
        max_candies = candies
    if user1_name == 'Бот':
        if candies < 29:
            print(f'Бот забрал {candies} конфет')
            user1_candies += candies
            candies -= candies
        elif candies == 29:
            print(f'Бот забрал {candies%28} конфет')
            user1_candies += candies % 28
            candies -= candies % 28
        elif candies//28 == 1:
            print(f'Бот забрал {candies%28-1} конфет')
            user1_candies += candies % 28-1
            candies -= candies % 28-1
        else:
            print(f'Бот забрал {candies%28+1} конфет')
            user1_candies += candies % 28+1
            candies -= candies % 28+1
    else:
        while number_of_candies not in range(1, max_candies+1):
            number_of_candies = int(input(f'{user1_name}, введите количество конфет (от 1 до {max_candies}): '))
        candies -= number_of_candies
        user1_candies += number_of_candies
    if candies <= 0:
        print(f'Победил игрок {user1_name}!')
        break
    print(f'У игрока {user1_name}: {user1_candies} конфет')
    print(f'Всего осталось: {candies} конфет')
    number_of_candies = 0
    if candies < 28:
        max_candies = candies
    if user2_name == 'Бот':
        if candies < 29:
            print(f'Бот забрал {candies} конфет')
            user2_candies += candies
            candies -= candies
        elif candies == 29:
            print(f'Бот забрал {candies % 28} конфет')
            user2_candies += candies % 28
            candies -= candies % 28
        elif candies//28 == 1:
            print(f'Бот забрал {candies%28-1} конфет')
            user2_candies += candies % 28-1
            candies -= candies % 28-1
        else:
            print(f'Бот забрал {candies % 28+1} конфет')
            user2_candies += candies % 28+1
            candies -= candies % 28+1
    else:
        while number_of_candies not in range(1, max_candies+1):
            number_of_candies = int(input(f'{user2_name}, введите количество конфет (от 1 до {max_candies}): '))
        candies -= number_of_candies
        user2_candies += number_of_candies
    if candies <= 0:
        print(f'Победил игрок {user2_name}!')
        break
    print(f'У игрока {user2_name}: {user2_candies} конфет')
    print(f'Всего осталось: {candies} конфет')