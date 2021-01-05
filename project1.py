"""
author @ryu
"""
from swampy.TurtleWorld import *
import random
import math


def draw_square():
    for i in range(1, 5):
        fd(drawer, 5)
        lt(drawer, 90)


def draw_blocks():
    for i in range(1, 31, 1):
        pd(drawer)
        draw_square()
        pu(drawer)
        fd(drawer, 30)


def border_line():
    for i in range(0, 2):
        fd(drawer, 900)
        rt(drawer, 90)
        fd(drawer, 150)
        rt(drawer, 90)


def generate_mines(i):
    name_generator = "mine" + str(i)
    return name_generator


def unique(list1):  # listedeki farklı elementleri alır
    unique_list = []
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)

    return unique_list


def random_mines():  # listeye random sayılar verir aynı olabilir
    mine_values = []
    for i in range(1, 6):
        rndm = random.randint(5, 29)

        mine_values.append(rndm)
    return mine_values


mine_values = random_mines()  # ilk listeyi aldık # got the first list
mine_values = unique(
    mine_values)  # farklı sayıları tekrar listeledik örn [16,16,11,6,7] 5 elementli ise [16,11,6,7] 4 elementli olur
# list the unique elements of list

while len(mine_values) != 5:  # listedeki değer sayısı 5 e eşit değilse yani hepsi farklı değilse döngüye girer
    # if lenght of unique elements isn't == 5 then go to random list again

    mine_values = random_mines()
    mine_values = unique(mine_values)
    if mine_values != 5:
        continue


def mine_adress(mine_values):  # mayınların x kordinatı adresleri
    mine_adress = []
    for i in mine_values:
        mine_adress.append(i * 30)

    return mine_adress


def deploy_mines(mine_list):  # mayınları x kordinatındaki adreslerine döşer
    # deploy the mines values on x axis
    n = 0
    for i in mine_list:
        n = n + 1
        mine_name = generate_mines(n)
        mine_name = Turtle()
        pu(mine_name)
        mine_name.y = -28
        mine_name.x = -10
        mine_name.set_color("black")

        fd(mine_name, 30 * i)

        mine_name2 = generate_mines(10 - n)
        mine_name2 = Turtle()
        pu(mine_name2)
        mine_name2.set_color("black")
        mine_name2.y = -116
        mine_name2.x = -10
        fd(mine_name2, 30 * i)


def get_name():  # isim almak için kullanılır
    while True:
        name = input("name of your turtle: ")
        print("name of your turtle is: " + str(name))
        if name == "":
            print("name cannot be emty please type again")
            continue
        else:
            break
    return name


def get_color(name):  # renk seçmek için kullanılır
    while True:
        color = input("chose a color for " + str(name) + " (red,blue or green)")
        if color == "red":
            print("color of " + str(name) + " is red ")
            return "red"
        elif color == "blue":
            print("color of " + str(name) + " is blue")
            return "blue"
        elif color == "green":
            print("color of " + str(name) + " is green")
            return "green"
        else:
            print(color + " is not a valid color! please try again\n")
            continue


def check_name(t1_name, t2_name):  # isimleri kontrol eder
    while True:
        if str(t1_name) == str(t2_name):
            print(t2_name + " is taken please type another name")
            t2_name = get_name()
        else:
            break
    return t2_name


def check_color(t1_color, t2_color, t2_name):  # renkleri kontrol eder
    while True:
        if str(t1_color) == str(t2_color):
            print("this color is already taken! try again")
            t2_color = get_color(t2_name)
        else:
            break
    return t2_color


def coin_toss():  # %50 şans
    rndm = random.randint(1, 2)
    return rndm


def roll_a_dice():  # zar atar
    rndm = random.randint(1, 6)
    print("Dice result : " + str(rndm))
    return rndm


def explosion_check(mine_adress, turtle_distance):  # patlama kontrolü
    for i in mine_adress:  # control the turtles position if it is on a mine
        if i == turtle_distance:
            return True


def press1_to_deploy(mine_list):  # gets an input to deploy the mines
    n = input("Press 1 to deploy mines: ")
    if n == "1":
        deploy_mines(mine_list)
    else:
        print("Quitting the game...")
        quit()


def continue_racing(player, t, turtle_distance, mine_adress, t1name, t2name, score1,
                    score2):  # continue the race if # one of turtles are exploded
    while True:
        if player == "1":  # which is exploded ?

            print("lets roll a dice!\n")
            print("press enter to roll a dice\n")
            input()
            dice = roll_a_dice()
            score2 += dice
            print(t1name + " result: " + str(score1))
            print(t2name + " result: " + str(score2))
            turtle_distance += dice * 30
            fd(t, dice * 30)
            b2 = explosion_check(mine_adress, turtle_distance)
            if (b2):
                print("BOOOOOOOOOOOOOOM!")
                print(t2name + " exploded")
                break
            if turtle_distance >= 900:  # if turtle pass  the border locates at border again
                t2_name.x = 890
                fd(t2_name, 1)
                print(t2name + " won")
                break
        else:
            print("lets roll a dice!\n")
            print("press enter to roll a dice\n")
            input()
            dice = roll_a_dice()
            score1 += dice
            print(t1name + ": result: " + str(score1))
            print(t2name + ": result: " + str(score2))
            turtle_distance += dice * 30
            fd(t, dice * 30)
            b2 = explosion_check(mine_adress, turtle_distance)
            if (b2):
                print("BOOOOOOOOOOOOOOM")
                print(t1name + " exploded")
                break
            elif turtle_distance >= 900:
                t1_name.x = 890
                fd(t1_name, 1)
                print(t1name + " won")
                break


def race(coin_toss, t1, t2, mine_adress, t1name, t2name):  # main function two turtle going to race
    coint = int(coin_toss)  # which turtle start ? depend on coin toss
    if coint % 2 == 0:
        print("Player " + str(t1name) + "  is starting\n")
    else:
        print("Player " + t2name + " is starting\n")
    turtle1_distance = 0
    turtle2_distance = 0
    score1 = 0
    score2 = 0
    while True:
        print("lets roll a dice!")
        print("press enter to roll a dice\n")
        input()
        if coint % 2 == 0:
            dice = roll_a_dice()

            score1 += dice
            if dice == 6:
                print(t1name + " ROLLED 6 " + t1name + " WILL ROLL AGAIN \n")
                coint = coint - 1  # decrease by one to do loop again
            print(t1name + " result: " + str(score1))
            print(t2name + " result: " + str(score2))
            turtle1_distance += dice * 30
            coint = coint + 1
            fd(t1, dice * 30)
            b2 = explosion_check(mine_adress, turtle1_distance)
            if bool(b2):
                print("BOOOOOOOMMM!")
                print(t1name + " exploded")
                continue_racing("1", t2, turtle2_distance, mine_adress, t1name, t2name, score1, score2)

                break
        elif turtle1_distance >= 900:
            t1.x = 890
            fd(t1, 1)
            print(t1name + " WON !!")
            break
        else:
            dice = roll_a_dice()
            score2 += dice
            if dice == 6:
                print(t2name + " ROLLED 6 " + t2name + " ROLL AGAIN\n")
                coint = coint - 1
            print(t1name + " result: " + str(score1))
            print(t2name + " result: " + str(score2))
            turtle2_distance += dice * 30
            coint = coint + 1
            fd(t2, dice * 30)
            b1 = explosion_check(mine_adress, turtle2_distance)

            if bool(b1):
                print("BOOOOOOOOOOOM!")
                print(t2name + " exploded\n")
                continue_racing("2", t1, turtle1_distance, mine_adress, t1name, t2name, score1, score2)

                break
            elif turtle2_distance >= 900:
                t2.x = 890
                fd(t2, 1)
                print(t2name + " WON !!")
                break


world = TurtleWorld()
mine_adress = mine_adress(mine_values)
t1_name = get_name()
t1_color = get_color(t1_name)
t2_name = get_name()
t2_name = check_name(t1_name, t2_name)
t1_name_str = t1_name
t2_name_str = t2_name
t2_color = get_color(t2_name)
t2_color = check_color(t1_color, t2_color, t2_name)
t1_name = Turtle()
t1_name.set_color(str(t1_color))
t2_name = Turtle()
t2_name.set_color(str(t2_color))
t1_name.x = -9  # starting position for turtles
t1_name.y = -28
t2_name.x = -9
t2_name.y = -118
t2_name.delay = 0.1
t1_name.delay = 0.1
coin_toss = coin_toss()

world.geometry("1200x500")

drawer = Turtle()

drawer.delay = 0.00000001

border_line()

drawer.y = -30
drawer.x = 15
draw_blocks()
drawer.y = -120
drawer.x = 15
draw_blocks()
drawer.die()
press1_to_deploy(mine_values)

race(coin_toss, t1_name, t2_name, mine_adress, t1_name_str, t2_name_str)
while True:
    print(
        "Did you like the game ? do you want to play it again ? [Y/n] \n") # asks to user if he wants to continue or not
    # Y=play again n=quit
    play_again = input()
    if play_again == "Y":

        world.clear()

        world.animals.clear()

        drawer = Turtle()

        drawer.delay = 0.00000001

        border_line()

        drawer.y = -30
        drawer.x = 15
        draw_blocks()
        drawer.y = -120
        drawer.x = 15
        draw_blocks()
        drawer.die()

        press1_to_deploy(mine_values)
        t1_name = get_name()
        t1_color = get_color(t1_name)
        t2_name = get_name()
        t2_name = check_name(t1_name, t2_name)
        t1_name_str = t1_name
        t2_name_str = t2_name
        t2_color = get_color(t2_name)
        t2_color = check_color(t1_color, t2_color, t2_name)
        t1_name = Turtle()
        t1_name.set_color(str(t1_color))
        t2_name = Turtle()
        t2_name.set_color(str(t2_color))
        t1_name.x = -9
        t1_name.y = -28
        t2_name.x = -9
        t2_name.y = -118

        race(coin_toss, t1_name, t2_name, mine_adress, t1_name_str, t2_name_str)
    elif play_again == "n":
        quit()
        break
    else:
        continue

wait_for_user()
