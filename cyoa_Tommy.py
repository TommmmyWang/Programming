import time
import random

hp = 1
atk = 1
gld = 0
phd = 0
atkUp = 0


def restart():
    restart = input("enter 'E' to start again?")
    if restart == "E" or restart == "e":
        story()


def waitBeforeEnding():
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)


def combat(enemy, enemyAtk, enemyHp, enemyLv):
    print(f"*Began combat with {enemy}!")
    global hp
    global atk
    global gld
    global phd
    global atkUp
    while enemyHp > 0 and hp > 0:
        if random.randint(1, 2) == 1 and phd != 0:
            hp = hp - (enemyAtk + random.randint(-2, 1))
            print("The Enemy`s attack hit you!")
            print(f"you only have {hp} HP left!")
            if atkUp != 0:
                print("You lost your ATK up!")
                atkUp = 0
        elif phd == 0:
            print("The Enemy`s attack was blocked!")
        else:
            print("The Enemy`s attack missed!")
        print('enter "a" to attack, "b" to defend')
        combatChoose = input("What would you do?")
        if combatChoose == "a" or combatChoose == "A":
            if random.randint(enemyLv, 10) != 10:
                enemyHp = enemyHp - atk
                print("The Attack was success!")
                print(f"The Enemy lost {round(atk * (1 + atkUp * 0.5))} HP!")
                phd = 0
            else:
                print("The Enemy dodged the Attack!")
        elif combatChoose == "b" or combatChoose == "B":
            phd = round(enemyAtk / 2) + random.randint(-round(enemyLv / 2), 2)
            if phd <= 1:
                print("You Blocked the Enemy`s Attack!")
                if atkUp < 5:
                    atkUp = atkUp + 1
                    print("Your ATK raised for the next Attack!")
                else:
                    print("You can't continue to raise your Attack!")
                phd = 0
            elif phd > 1:
                print("Your Block failed!")
                phd = 1

    if hp <= 0:
        print("You Lost!")
        waitBeforeEnding()
        print("== Ending 2 ==")
        print("  Maybe next time...")
        print("  No, there is no next time.")
        restart()
    elif enemyHp <= 0:
        print("You won!")
        print(f"Gained {2 * enemyLv + 3} gold!")
        global battleResult
        battleResult = "Win"


hp = 100
atk = 10
gld = 50
combat("Bandit Leader", 4, 20, 2)


def story():
    name = input("Enter here the name you want to be refered to as.")
    print("Very well.")
    time.sleep(1)

    # 2. Ask the player to begin the game
    print(f"{name}, shall we began tonight`s story?")
    enter = input("Let's see… enter 'E' to continue.")
    if enter == "E" or enter == "e":
        print("Good! Good, good.")
        print("Then let us begin, tonight`s story.")
    else:
        print("...")
        print("Alright, come back when you are ready.")
        waitBeforeEnding()
        print("== Ending ? ==")
        print("  What's the fastest way to end a story?")
        print("  --Not starting one at the first place.")
        restart()

    # 3. Story-Inroduction

    print("")
    print(f"{name}.")
    time.sleep(2)
    print("That name is all you remember about yourself.")
    time.sleep(2)
    print(
        "The first thing that meets your consiousness is the rumbling stones and falling trees."
    )
    time.sleep(2)
    print("Your instincts roar with all of it`s might to wake your legs.")
    time.sleep(2)
    print(
        "But it`s not responding, it`s jammed in the ground. You were unable to move."
    )
    time.sleep(2)
    print("If it wasn`t for that old Gary……")
    time.sleep(2)
    print("You`d be buried.")
    time.sleep(2)
    print(
        'So, you lived in this small, poor village called "Ledin" for a while. Long enough for you to learn---'
    )
    time.sleep(2)
    print("---or possibly relearn all life skills you need.")
    time.sleep(2)
    print(
        "However, with every passing day, a thirst grows in your heart---to venture out and find out about yourself, your past, and your memories."
    )
    time.sleep(2)
    print("Looking again at this small village, do you want to step out?")
    time.sleep(1)
    print("1: I must step out.")
    Cventure = input("2: I`d just stay here.")
    if Cventure == "2":
        print("Nah, you`d possibly die on day 2 if you went out.")
        time.sleep(2)
        print("You stayed in little Ledin for the rest of your life.")
        time.sleep(2)
        print(
            "Alas, years later, when you are lying in your deathbed, surrounded by all the villages you helped…"
        )
        time.sleep(2)
        print(f"{name}, do you regret?")
        time.sleep(2)
        print("Do you regret this barely useful life?")
        waitBeforeEnding()
        print("== Ending 1 ==")
        print("  Actually, if you think about it---")
        print("  ---peacefully dying isn`t entirely bad.")
        restart()
    elif Cventure == "1":
        story2()


def story2():
    print("You decided that this small village is too small for you.")
    time.sleep(2)
    print(
        "After saying goodbye to the villagers, you packed some items and left the small Ledin."
    )
    time.sleep(2)
    print("*Initializing Stats...")
    hp = 100
    atk = 10
    gld = 50
    time.sleep(2)
    print("*Gained 100 HP.")
    time.sleep(2)
    print("*Gained 10 ATK.")
    time.sleep(2)
    print("*Gained 50 Gold.")
    time.sleep(2)
    print("Now is day……somewhere around 5, good news: You didn`t die.")
    time.sleep(2)
    print("Bad news: You found yourself completely directionless.")
    time.sleep(2)
    print(
        "You roamed from settlement to settlement for quite a while, until your legs start to stress out."
    )
    time.sleep(2)
    print("You sit down on the grass and tries your best to squeeze out a valid map.")
    time.sleep(2)
    print(
        'According to the people you`ve met, there is a city in this region named "Karnos."'
    )
    time.sleep(2)
    print("Do you want to go to Karnos?")
    time.sleep(2)
    print("1: Go to Karnos.")
    print("2: Find another settlement or village.")
    Cgoto = input("3: Continue roaming.")
    if Cgoto == "1":
        storyKnight1()
    elif Cgoto == "2":
        storyResist1()
    elif Cgoto == "3":
        storyRoam1()


def storyKnight1():
    print(
        "You decided that going to a large city would yield the best odds of finding stuff."
    )
    time.sleep(2)
    print(
        "You walked for quite a while, but anyways, despite the challenge, you finally reach Kar..."
    )
    time.sleep(2)
    print("...Are those, some 4 people, bandits?")
    time.sleep(2)
    print("No, you don`t get to choose here, the bandit leader noticed you and ran up.")
    time.sleep(2)
    print("They Want to kidnap you.")
    combat("Bandit Leader", 4, 20, 2)
    time.sleep(2)
    print("You did it! the rest of the henchmans are too afraid to come up!")
    time.sleep(2)
    print(
        "Definitly not because you threw their head to the ground like a wet cloth, yeah."
    )
    time.sleep(2)
    print(
        "Just as those bandits were deciding on whether to come up, Another figure wearing heavy armor suddenly jumped in!"
    )
    time.sleep(2)
    print("You raised your weapon and prepeared for battle, and the figure...")
    time.sleep(2)
    print("...He`s starting to throw another bandit to the ground.")
    time.sleep(2)
    print("Yeah, that`s not a bandit.")
    time.sleep(2)
    print("Now the rest of the bandits are fleeing, the man turned towards you.")
    time.sleep(2)


def storyResist1():
    print("WIP")


def storyRoam1():
    print("WIP")


story()
