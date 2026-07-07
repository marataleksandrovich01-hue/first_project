from random import randint
number = randint(1, 100)
print('Угадай число от 1 до 100')
while True:
    guess = int(input('Введите число: '))
    if guess > number:
        print('Ваше число больше загаданного')
    if guess < number:
        print('Ваше число меньше загаданного')
    if guess == number:
        break
print('Вы угадали число! Хорошая интуиция!')