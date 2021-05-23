import random
from os import system

clear = lambda: system('clear')

def finding(letter):
    global word_star, the_word
    num = the_word.count(letter)
    word_star = list(word_star)
    the_word = list(the_word)
    for i in range(num + 1):
        try:
            l_ind = the_word.index(letter)
        except:
            pass
        word_star[l_ind] = letter
        the_word[l_ind] = '_'
    word_star = ''.join(word_star)
    return word_star

def pr_hangman(num):
    if num == 0:
        for i in range(10):
            print(hangman[i].strip('\n'))
    if num == 1:
        for i in range(10, 20):
            print(hangman[i].strip('\n'))
    if num == 2:
        for i in range(20, 30):
            print(hangman[i].strip('\n'))
    if num == 3:
        for i in range(30, 40):
            print(hangman[i].strip('\n'))
    if num == 4:
        for i in range(40, 50):
            print(hangman[i].strip('\n'))
    if num == 5:
        for i in range(50, 60):
            print(hangman[i].strip('\n'))
    if num == 6:
        for i in range(60, 70):
            print(hangman[i].strip('\n'))
    if num > 6:
        print("ВЫ ПРОИГРАЛИ")
        
words = open('words.txt', 'r')
spisok = words.readlines()
hang = open('hangman.txt', 'r')
hangman = hang.readlines()
rand_num = random.randint(0, len(spisok) - 1)
the_word = spisok[rand_num].strip('\n')
final_word = the_word
w_len = len(the_word)
word_star = ''.join(['*' for letters in range(w_len)])
print('Сейчас мы с вами сыграем в игру виселица.\n\
     \rваша задача угадать слово по буквам. У вас есть право на 6 ошибок\n\
     \rПриступим!')
pr_hangman(0)
print(f'Угадайте слово состоящее из {w_len} букв: {word_star}')
tries = 6
hanging = 0
entered_letters = []
while tries > 0:
    letter = input('Введите букву: ').lower()
    if letter.isalpha and len(letter) == 1:
        if letter in the_word:
            clear
            pr_hangman(hanging)
            print(f'Буква "{letter}" есть в этом слове!')
            print(finding(letter))
            print(f'у вас осталось {tries} попыток!')
            entered_letters.append(letter)
        elif letter in entered_letters:
            print(f'Вы уже вводили букву {letter}. Это ошибка.')
            hanging += 1
            pr_hangman(hanging)
            tries -= 1
            print(word_star)
            print(f'у вас осталось {tries} попыток!')
        else:
            clear
            hanging += 1
            pr_hangman(hanging)
            tries -= 1
            print(f'Буквы "{letter}" нет в этом слове!')
            print(word_star)
            print(f'у вас осталось {tries} попыток!')
            entered_letters.append(letter)
        if word_star == final_word:
            clear
            print(f'***Поздравляю! Вы угадали слово {word_star}!***')
            break
    else:
        print('Неправильный ввод')
        hanging += 1
        pr_hangman(hanging)
        tries -= 1
        print(word_star)
        print(f'у вас осталось {tries} попыток!')
if tries == 0:
    print(f'Вы не угадали слово {final_word}!')
print('Спасибо за игру')
