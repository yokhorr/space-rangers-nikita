import os
from random import choice

know_snail: bool = False


def sep():
    # print()
    if os.name == 'nt':  # for Windows
        os.system('cls')
    elif os.name == 'posix':  # for Unix-based systems like Linux or macOS
        os.system('clear')
    print()


def strong(text):
    print()
    print('\033[91m' + text + '\033[0m')


def main():
    # change dir to texts
    os.chdir("texts")
    start()


def start(fail=True):
    if fail:
        global know_snail
        know_snail = False

    sep()
    print(open("start.txt", encoding="utf-8").read())

    choice = input("Ваш выбор (введите номер): ")

    if choice == "1":
        terminal()
    elif choice == "2":
        corridor()
    elif choice == "3":
        steward()
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        start(False)


def mission_info():
    sep()
    print(open("mission_info.txt", encoding="utf-8").read())

    # press any button to continue
    strong("Нажмите Enter для продолжения...")
    input()
    terminal()


def snail_info():
    global know_snail
    know_snail = True
    sep()
    print(open("snail_info.txt", encoding="utf-8").read())

    # press any button to continue
    strong("Нажмите Enter для продолжения...")
    input()
    terminal()


def terminal():
    sep()

    print(open("terminal.txt", encoding="utf-8").read())

    choice = input("Ваш выбор (введите номер): ")

    if choice == "1":
        print("1. Попытаться найти информацию о своей миссии")
        mission_info()
    elif choice == "2":
        print("2. Прочитать про гигантских улиток (интересно же!)")
        snail_info()
    elif choice == "3":
        print("3. Отойти от терминала")
        start(False)


def no_pass():
    sep()
    print(open("no_pass.txt", encoding="utf-8").read())

    # press any button to continue
    strong("Нажмите Enter для продолжения...")
    input()
    corridor()


def ventil_1():
    sep()
    print(open("ventil_1.txt", encoding="utf-8").read())

    strong("Квест провален.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def ventil_2():
    sep()
    print(open("ventil_2.txt", encoding="utf-8").read())

    strong("Квест провален.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def ventil_3():
    sep()
    print(open("ventil_3.txt", encoding="utf-8").read())

    choice = input("Ваш выбор (введите номер): ")

    if choice == "1":
        officer()
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        ventil_3()


def ventil_4():
    sep()
    print(open("ventil_4.txt", encoding="utf-8").read())

    strong("Нажмите Enter для продолжения...")
    input()
    corridor()


def steal_pass():
    sep()
    print(open("steal_pass.txt", encoding="utf-8").read())

    strong("Квест провален.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def run_officer():
    sep()
    print(open("run_officer.txt", encoding="utf-8").read())

    strong("Квест провален.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def talk_officer():
    sep()
    print(open("talk_officer.txt", encoding="utf-8").read())

    strong("Нажмите Enter для продолжения...")
    input()
    snail()


def snail():
    sep()
    print(open("snail.txt", encoding="utf-8").read())

    if not know_snail:
        print()
        print("Вы судорожно вспоминаете все, что знаете о таких созданиях, но, увы, "
              "никаких полезных сведений в голове нет. "
              "Без четкого плана действий, вы решаете просто рискнуть и побежать напролом.")
        print()
        print("Улитка реагирует мгновенно. Щупальца с лазерными резаками опасно сверкают, "
              "и вам едва не удается избежать попадания. Зато ваша семья получит страховку в 10000 cr...")
        strong("Жизнь великого рейнджера закончилась.")
        strong("Нажмите Enter, чтобы начать сначала...")
        input()
        start()
    else:
        print()
        print("1. Попробовать обойти улитку")
        print("2. Попытаться подкупить улитку")
        print("3. Использовать что-нибудь из инвентаря, чтобы отвлечь улитку")
        choice = input("Ваш выбор (введите номер): ")

        if choice == "1":
            pass_snail()
        elif choice == "2":
            buy_snail()
        elif choice == "3":
            gum_snail()
        else:
            strong("Некорректный выбор. Попробуйте снова.")
            input()
            snail()


def building():
    sep()
    print(open("building.txt", encoding="utf-8").read())

    choice = input("Ваш выбор (введите номер): ")

    if choice == "1":
        pass_buildind()
    elif choice == "2":
        talk_building()
    elif choice == "3":
        ventil_building()
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        building()


def pass_buildind():
    sep()
    print(open("pass_buildind.txt", encoding="utf-8").read())

    strong("Квест провален.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def talk_building():
    sep()
    print(open("talk_building.txt", encoding="utf-8").read())

    strong("Квест провален.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def ventil_building():
    sep()
    print(open("ventil_building.txt", encoding="utf-8").read())

    choice = input("Ваш выбор (введите номер): ")

    if choice == "1":
        ventil_1()
    elif choice == "2":
        ventil_2()
    elif choice == "3":
        ventil_3()
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        ventil_building()


def pass_snail():
    sep()
    print(open("pass_snail.txt", encoding="utf-8").read())

    strong("Жизнь великого рейнджера закончилась.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def buy_snail():
    sep()
    print(open("buy_snail.txt", encoding="utf-8").read())

    strong("Нажмите Enter для продолжения...")
    input()
    building()


def gum_snail():
    sep()
    print(open("gum_snail.txt", encoding="utf-8").read())

    strong("Нажмите Enter для продолжения...")
    input()
    building()



def officer():
    sep()
    print(open("officer.txt", encoding="utf-8").read())

    choice = input("Ваш выбор (введите номер): ")

    if choice == "1":
        steal_pass()
    elif choice == "2":
        talk_officer()
    elif choice == "3":
        run_officer()
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        officer()


def ventil():
    sep()
    print(open("ventil.txt", encoding="utf-8").read())

    choice = input("Ваш выбор (введите номер): ")

    if choice == "1":
        ventil_1()
    elif choice == "2":
        ventil_2()
    elif choice == "3":
        ventil_3()
    elif choice == "4":
        ventil_4()
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        ventil()


def corridor():
    sep()
    print(open("corridor.txt", encoding="utf-8").read())

    choice = input("Ваш выбор (введите номер): ")

    if choice == "1":
        no_pass()
    elif choice == "2":
        ventil()
    elif choice == "3":
        terminal()
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        corridor()


def steward():
    sep()
    print("Вы подошли к роботу-стюарду, который выглядел не слишком дружелюбно, но, по крайней мере, был запрограммирован отвечать на вопросы.")
    print()
    print("— Извините, а что здесь происходит? — спросили вы, надеясь получить какую-то полезную информацию.")
    print()
    print("Робот, дёрнувшись, словно от внутреннего раздражения, ответил:")
    print()
    print("— Ведется подготовка к важному мероприятию, которое состоится через несколько минут. К сожалению, вы не уполномочены находиться здесь.")
    print()
    print("1. Узнать больше информации о мероприятии")
    print("2. Оставить стюарда")

    choice = input("Ваш выбор (введите номер): ")

    if choice == "1":
        sep()
        print("— Какого рода мероприятие? Кто организатор? Есть ли еще кто-то, кто мог бы мне помочь? — начали вы задавать вопросы, не догадываясь, что каждый ваш вопрос вызывает всё большее недовольство у робота.")
        print()
        print("На ваше недоумение, его металлическое лицо искривилось в нечто похожее на злую гримасу:")
        print()
        print("— Прекратите задавать вопросы, или я буду вынужден удалить вас из этой зоны! — прорычал он. И, не дождавшись вашего ответа, вытолкнул вас за пределы здания, отправляя вас в коридор, который вы только что покинули.")
        strong("Нажмите Enter для продолжения...")
        input()
        start(False)
    elif choice == "2":
        sep()
        print()
        print("Вы решили не беспокоить робота лишними вопросами. Мало ли, ещё тревогу поднимет.")
        strong("Нажмите Enter для продолжения...")
        input()
        start(False)
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        steward()



if __name__ == "__main__":
    main()
