# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Egor Solyanik
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

know_snail: bool = False
shutted_cameras: bool = False
got_database: bool = False
hidden_guard: bool = False


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
        global know_snail, shutted_cameras, got_database, hidden_guard
        know_snail = False
        shutted_cameras = False
        got_database = False
        hidden_guard = False

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
        pass_building()
    elif choice == "2":
        ventil_building()
    elif choice == "3":
        talk_building()
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        building()


def pass_building():
    sep()
    print(open("pass_building.txt", encoding="utf-8").read())

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
        sneak_bot()
    elif choice == "2":
        talk_bot()
    elif choice == "3":
        poweroff_bot()
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        ventil_building()


def sneak_bot():
    sep()
    print(open("sneak_bot.txt", encoding="utf-8").read())

    strong("Квест провален.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def talk_bot():
    sep()
    print(open("talk_bot.txt", encoding="utf-8").read())

    choice = input("Ваш выбор (введите номер): ")

    if choice == "1":
        help_bot()
    elif choice == "2":
        lie_bot()
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        talk_bot()


def help_bot():
    global got_database
    global shutted_cameras
    sep()
    print(open("help_bot.txt", encoding="utf-8").read())

    choice = input("Ваш выбор (введите номер): ")

    if choice == "1":
        if shutted_cameras:
            sep()
            print("Хотя вы только что выключили камеры, вы почему-то решили сделать это снова. Это было роковой тратой времени - вас заметили и подняли тревогу...")
            strong("Квест провален.")
            strong("Нажмите Enter, чтобы начать сначала...")
            input()
            start()
        else:
            shutted_cameras = True
            shut_cameras()
            help_bot()
    elif choice == "2":
        if got_database:
            sep()
            print(
                "Хотя вы только что взломали базы данных, вы почему-то решили сделать это снова. Это было роковой тратой времени - вас заметили и подняли тревогу...")
            strong("Квест провален.")
            strong("Нажмите Enter, чтобы начать сначала...")
            input()
            start()
        else:
            got_database = True
            database()
            help_bot()
    elif choice == "3":
        codes()
    elif choice == "4":
        if not got_database:
            sep()
            print("Вы решаете пробраться к главному залу, не зная точно, что там происходит. Прячьтесь за углами, стараясь избегать камер, и пытаетесь наугад найти нужный путь. Всё выглядит одинаково: бесконечные коридоры, закрытые двери, странные знаки на стенах.")
            print()
            print("Наконец, вам удаётся добраться до большого помещения, которое кажется важным. Но вместо зала для собраний вы обнаруживаете склад с канистрами технических жидкостей и ящиками с запчастями для роботов. И тут раздаётся тревожный сигнал: вы зашли не туда.")
            print()
            print("— Незарегистрированный доступ! Посторонний в зоне хранения! — снова звучит голос системы безопасности.")
            print()
            print("Через мгновение дверь захлопывается за вашей спиной, блокируя выход. Снаружи слышны шаги охраны, приближающиеся с явной решимостью вас поймать.")
            print()
            print("Вы не смогли найти правильный путь и оказались в ловушке. Дело плохо.")
            print()

            strong("Квест провален.")
            strong("Нажмите Enter, чтобы начать сначала...")
            input()
            start()
        elif not shutted_cameras:
            sep()
            print("Вы, стараясь держаться в тени, осторожно продвигаетесь по коридору в сторону главного зала. Путь кажется свободным, но вы замечаете несколько камер, следящих за каждым движением.")
            print()
            print("Игнорируя их, вы продолжаете идти, надеясь, что никто не обратит внимания на непрошеного гостя. Но не тут-то было. Вдруг из динамиков раздается металлический голос системы безопасности:")
            print()
            print("— Обнаружен посторонний. Идентификация не пройдена. Служба безопасности, реагировать немедленно.")
            print()
            print("Через секунду из-за угла выскакивают несколько охранников с парализующими пистолетами. Вас окружают и, не успев сделать и шага, вы оказываетесь пойманным.")

            strong("Квест провален.")
            strong("Нажмите Enter, чтобы начать сначала...")
            input()
            start()
        else:
            main_hall()
    elif choice == "52":
        sep()
        print("Семь бед - один ответ: костыль и велосипед!")
        input()
        help_bot()
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        help_bot()


def main_hall():
    global hidden_guard
    sep()
    print(open("main_hall.txt", encoding="utf-8").read())

    choice = input("Ваш выбор (введите номер): ")

    if choice == "1":
        if not hidden_guard:
            pass_guard_fail()
        else:
            pass_guard_success()
    elif choice == "2":
        ventil_guard()
    elif choice == "3":
        if not hidden_guard:
            hidden_guard = True
            hidden_success()
            main_hall()
        else:
            hidden_fail()
    else:
        strong("Некорректный выбор. Попробуйте снова.")
        input()
        main_hall()


def hidden_success():
    sep()
    print(open("hidden_success.txt", encoding="utf-8").read())

    strong("Нажмите Enter, чтобы начать продолжить...")
    input()


def hidden_fail():
    sep()
    print(open("hidden_fail.txt", encoding="utf-8").read())

    strong("Квест провален.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def pass_guard_success():
    sep()
    print(open("pass_guard_success.txt", encoding="utf-8").read())

    strong("Нажмите Enter, чтобы начать продолжить...")
    input()
    end()


def end():
    sep()
    print(open("end.txt", encoding="utf-8").read())

    strong("Задание выполнено, пора лететь на планету Земля за вознаграждением...")
    input()


def pass_guard_fail():
    sep()
    print(open("pass_guard_fail.txt", encoding="utf-8").read())

    strong("Квест провален.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def ventil_guard():
    sep()
    print(open("ventil_guard.txt", encoding="utf-8").read())

    strong("Жизнь великого рейнджера закончилась.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def codes():
    sep()
    print(open("codes.txt", encoding="utf-8").read())

    strong("Квест провален.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def database():
    sep()
    print(open("database.txt", encoding="utf-8").read())

    strong("Нажмите Enter для продолжения...")
    input()


def shut_cameras():
    sep()
    print(open("shut_cameras.txt", encoding="utf-8").read())

    strong("Нажмите Enter для продолжения...")
    input()


def lie_bot():
    sep()
    print(open("lie_bot.txt", encoding="utf-8").read())

    strong("Квест провален.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


def poweroff_bot():
    sep()
    print(open("poweroff_bot.txt", encoding="utf-8").read())

    strong("Квест провален.")
    strong("Нажмите Enter, чтобы начать сначала...")
    input()
    start()


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
