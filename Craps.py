from __future__ import division

import random



print("*********Welcome to Craps*********")
br = "\n"
global money, bet, games, moneybet, lost, won,total, percent

list = []

def standarddeviation():
    global list
    liststandard = []
    mean = 0
    whole = 0
    sigma = 0
    for i in list:
        mean = mean + i
    mean = mean/len(list)
    for j in list:
        liststandard.append(pow((j - mean),2))
    for k in liststandard:
        whole = whole + k
    sigma = float(whole * 1/len(list))
    sigma = sigma ** .5
    return sigma


def simulationpt1(bet):
    global moneybet, games, lost, won, list
    totmoney= bet
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice2+dice1
    list.append(total)


    if(total == 12 or total == 2 or total == 3):
        print"You won! "
        moneybet += totmoney
        won = won + 1

    elif (total == 11 or total == 7):
        print"You lost! "
        moneybet -= totmoney
        lost = lost +1

    else:
        return simulationpt2(total, totmoney)

def simulationpt2(total, bet):
    global moneybet, games, lost, won,list
    dice1h = random.randint(1, 6)
    dice2h = random.randint(1, 6)
    point = total
    totalh = dice1h + dice2h
    list.append(totalh)
    moneyh = bet *2


    if(totalh == point):
        print ("You won!")
        moneybet += moneyh
        won = won + 1
    elif(totalh == 7):
        print ("You lost!")
        moneybet -= moneyh
        lost = lost + 1
    else:
        return simulationpt2(point, bet)

def Phase1(bet):
    global money
    totmoney= bet
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice2+dice1

    print("You rolled a " + str(dice1) +" and a "+ str(dice2))
    if(total == 12 or total == 2 or total == 3):
        print("You won! $" +str(totmoney))
        money += totmoney

    elif (total == 11 or total == 7):
        print("You Lost! $" + str(totmoney))
        money -= totmoney
    else:
        return Phase2(total, totmoney)

def Phase2(total, bet):
    global money
    print("You have to match " + str(total) + " to win. if you roll 7 you lose")
    dice1h = random.randint(1, 6)
    dice2h = random.randint(1, 6)
    point = total
    totalh = dice1h + dice2h
    moneyh = bet *2
    print("You rolled a " + str(dice1h) + " and a " + str(dice2h)+br)

    if(totalh == point):
        print ("You won! $" + str(moneyh))
        money += moneyh
    elif(totalh == 7):
        print ("You lost! $" + str(moneyh))
        money -= moneyh
    else:
        return Phase2(point, bet)

def starting ():
    global num2, money,moneybet, percent, won, lost,games
    while(1):
        num2 = raw_input("Press 1 to play Craps" + br + "Press 2 to simulate up to 1000 games of Craps" + br + "press 3 to quit " + br)

        if num2 == "1" or num2 == "2" or num2 == "3":
            break
    if num2 == "3":
        print("You have a total of $" + str(money) + " to take home")
        quit()
    elif num2 == "1":

        print("You have a total of $" +str(money)+" with you")
        bet2 = input("How much would you like to bet: ")
        if (bet2 > money):
            if(bet2 > money and money > 0):
                print ("you do not have enough money")
                starting()
            else:
                print("you can not bet you actually owe the bank $" + str(abs(money)) + " pay or you will have to liquidate your assets to pay")

                starting()

        else:
            Phase1(bet2)
            starting()
    else:
        x = 0
        won = 0
        lost = 0
        percent = 0
        moneybet = 10000
        print("the starting bet is always $200"+br)
        games = input("How many games would you like to simulate up to 1000 games.  You get 10000 dollars worth of chips when you start " + br)

        if (games > 1000):
            print("You can not simulate more than 1000 games")
        else:
            while (x < games):
                simulationpt1(200)
                x = x + 1
            if (moneybet < 0):
                percent = (won/games)*100
                print("At the end of " + str(games) + " games you owe $" + str(abs(moneybet)) + " to pay to the casino" + br)
                print("Out of " + str(games) + " games you won " + str(won) + " and lost " + str(lost) + " games" + br)
                print("You won " + str(round(percent, 2)) + "% of games" + br)
                print("The standard deviation on your rolls with 2 dice was " + str(round(standarddeviation(), 2)) + br)
                starting()
            else:
                percent = (won/total)*100
                print("At the end of " + str(games) + " games you have $" + str(abs(moneybet)) + " left")
                print("Out of " + str(games) + " games you won " + str(won) + " and lost " + str(lost) + " games" + br)
                print("You won " + str(round(percent, 2)) + "% of games" + br)
                print("The standard deviation on your rolls with 2 dice was " + str(round(standarddeviation(), 2)) + br)
                starting()

access = False

while 1:

    num = raw_input("Press 1 to play Craps" + br+"Press 2 to simulate up to 1000 games of Craps" + br+"press 3 to quit "+br)

    if num == "1" or num == "2" or num == "3":
        break


if num == "3":
    print("You have a total of $" + str(money) + " to take home")
    quit()
elif num == "1":
    money = 2000
    print ("you are given $2000 dollars as starting chips to play. when you lose all of it then you will be given $2000 more")
    bet = input("How much would you like to bet: ")
    if(bet > money):
        print("You do not have enough money")
    else:
        Phase1(bet)
        starting()
else:

    x = 0
    percent =0

    moneybet = 10000
    games = input("How many games would you like to simulate up to 1000 games.  You get 10000 dollars worth of chips when you start "+ br)
    print("the starting bet is always $200")
    if(games > 1000):
        print("You can not simulate more than 1000 games")
    else:
        won = 0
        lost = 0
        while(x < games):
            simulationpt1(200)
            x = x +1
        if(moneybet < 0):
            total = lost + won
            percent = (won/total)*100
            print("At the end of "+ str(games)+ " games you owe $"+ str(abs(moneybet))+ " to pay to the casino"+ br)
            print("Out of "+str(total)+" games you won "+ str(won)+" and lost "+str(lost)+" games" + br)
            print("You won " + str(round(percent, 2)) + "% of games" + br)
            print("The standard deviation on your rolls with 2 dice was " + str(round(standarddeviation(), 2)) + br)
            starting()
        else:
            total = lost + won
            percent = (won/total)*100
            print("At the end of " + str(games) + " games you have $" + str(abs(moneybet)) + " left")
            print("Out of " + str(total) + " games you won " + str(won) + " and lost " + str(lost) + " games" + br)
            print("You won " + str(round(percent, 2)) + "% of games" + br)
            print("The standard deviation on your rolls with 2 dice was " + str(round(standarddeviation(), 2)) + br)
            starting()

