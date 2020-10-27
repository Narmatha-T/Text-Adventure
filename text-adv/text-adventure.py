from os import system
from random import randint
from playsound import playsound
from time import time

#title
gametitle = "WELCOME TO INTERACTIVE ADVENTURE GAME"
system("mode 100,40")
system("title "+ gametitle)

#clear screen
def cls():
    system('cls')
    
# Setup
yes_no = ["yes","YES","NO","no"]
game_options = ["left","LEFT","RIGHT", "right","FORWARD","forward","BACKWARD", "backward", "1", "2"]
story_options = ["1", "2"]
maze_directions = ["1", "2"]

#Creating pauses between texts
def enter():
    key = input("Press enter to continue...")
    keyA = [ord(c) for c in key]
    #print(keyA)

    if keyA == []:
        for i in range(5):
            print(".\n")
    else:
        print("Please hit the enter button\n")
        enter()

# Introduction
print("Pleased to see you play this game!!")
name = input("What is your name? ")
print("{} we have got two stories for you to play.".format(name))
print("1. A Super hero fiction story")
print("2. An adventure at the woods\n")
print("What would you like to play??")
print("Note use numbers to choose your options throughout this game")

response = ""
while response not in story_options:             #confining the options to just 1 and 2
    response = input("> ")


    #Story 1

    if response == "1":

        character_name = None
        character_race = None
        character_class = None
        character_strength = None
        character_magic = None
        character_dexterity = None
        character_life = None

        input("Press enter to start the game....")
        cls()
        title = "CASTLE DUNGEONS - AN INTERACTIVE FICTION GAME"
        system("title "+ title)
        print("Welcome to the CASTLE DUNGEONS - AN INTERACTIVE FICTION GAME!!")
        enter()


        def Intro():
            cls()
            print("In this adventure, you are the hero.")
            print("Your choices, skills, and a bit of luck, will influence the outcome of the game.")
            print("")
            print("An evil sorcerer is holding your fellow adventurers prisoners.")
            print("Will you succeed to free your friends from the castle dungeons, or peril trying?")
            print(" ")
            input("Press Enter to start...")


        Intro()

        def create_character():
            cls()
            global character_name
            character_name = name
            global character_race
            while character_race is None:
                race_choice = input("Choose your character race from the list below by entering the relevant number: \n 1 - Elf \n 2 - Dwarf \n > ")
                if race_choice == "1":
                    character_race = "Elf"
                elif race_choice == "2":
                    character_race = "Dwarf"
                else:
                    print("Not a valid choice, try again")
            #enter()
            global character_class
            while character_class is None:
                class_choice = input("Choose your character class from the list below by entering the relevant number:\n 1 - Warrior \n 2 - Wizard \n > ")
                if class_choice == "1":
                    character_class = "Warrior"
                elif class_choice == "2":
                    character_class = "Wizard"
                else:
                    print("Not a valid choice, try again")


        create_character()


        def create_character_skill_sheet():
            cls()
            global character_name, character_class, character_race, character_strength, character_magic, character_dexterity, character_life
            print("""
Now let's determine your character's skills, which you will use throughout the game.
In this game, your character has four skills:

- Strength, which you will use in combat or any strength test
- Dexterity, which you will use in any ability test
- Magic, which you will use whenever you need to cast a spell or use/inspect a magical item or place
- Life, which determines your life energy, points will be lost when hurt, 
and whenever Life reaches 0, your character dies.


Depending on your race and class, you will have a certain point-base already calculated by the game.
You will shortly be able to increase your skills by rolling a 6-face die.

Here is your base Character Skills Sheet: """)
            character_strength = 5
            character_magic = 0
            character_dexterity = 3
            character_life = 10
            if character_race == "Elf":
                character_strength = character_strength + 3
                character_magic = character_magic + 6
                character_dexterity = character_dexterity + 4
                character_life = character_life + 2
            elif character_race == "Dwarf":
                character_strength = character_strength + 5
                character_life = character_life + 4
            if character_class == "Warrior":
                character_strength = character_strength + 3
                character_life = character_life + 3
            elif character_race == "Wizard":
                character_magic = character_magic + 4

            print("""
Name:""" + character_name +
                  """
Race:""" + character_race +
                  """
Class:""" + character_class +
                  """
Strength:""" + str(character_strength) +
                  """
Dexterity:""" + str(character_dexterity) +
                  """
Magic:""" + str(character_magic) +
                  """
Life:""" + str(character_life) + """

            """)
            input("Press Enter to apply your skills modifiers")


        create_character_skill_sheet()

        def modify_skills():
            cls()
            global character_strength, character_magic, character_dexterity, character_life
            print(
                "To modify your skills, roll a six face die for each of your skills, and the game will add your score to the relevant skill")
            input("Press Enter to roll for Strength")
            roll = randint(1, 6)
            print("You rolled: " + str(roll))
            character_strength = character_strength + roll
            enter()
            cls()
            input("Press Enter to roll for Dexterity")
            roll = randint(1, 6)
            print("You rolled: " + str(roll))
            character_dexterity = character_dexterity + roll
            enter()
            cls()
            input("Press Enter to roll for Life")
            roll = randint(1, 6)
            character_life = character_life + roll
            print("You rolled: " + str(roll))
            input("Press Enter to continue...")
            #enter()
            cls()
            print("""
Congratulations! You have completed your character creation!
Your final character sheet is:

Name:""" + character_name +
                  """
Race:""" + character_race +
                  """
Class:""" + character_class +
                  """
      
Strength:""" + str(character_strength) +
                  """
Dexterity:""" + str(character_dexterity) +
                  """
Magic:""" + str(character_magic) +
                  """
Life:""" + str(character_life) + """

            """)
            input("Press Enter to begin your adventure, if you dare...")


        modify_skills()


        def Scene_1():
            cls()
            choice = None
            while choice is None:
                user_input = input("""
You have entered the Castle Dungeons.. 
It is dark, however thankfully your torch is lit and you can see up to 20 feet away from you.
The stone walls are damp, the smell of rats and orcs is strong. 
You walk down a narrow corridor, until you reach a thick stone wall.

The corridor continues on the left, and on the right.

What do you do?

1 - Turn left
2 - Turn right    
> """)
                if user_input == "1" or user_input == "turn left":
                    choice = "1"
                    Scene_2()
                elif user_input == "2" or user_input == "turn right":
                    choice = "2"
                    Scene_3()
                else:
                    print("""
Not a valid choice, type a number or "turn left" / "turn right"
                    """)


        def Scene_2():
            cls()
            choice = None
            while choice is None:
                playsound('Demon-Ghost Sound effect.mp3')
                user_input = input("""
From the darkness behind you.. you hear a strange noise.

What do you do?

1 - Continue walking
2 - Stop to listen

> """)
                if user_input == "1" or user_input == "continue":
                    choice = "1"
                    combat()
                elif user_input == "2" or user_input == "stop":
                    choice = "2"
                    skill_check()
                else:
                    print("""
Not a valid choice, type a number or "continue" / "stop"
                    """)


        def Scene_3():
            cls()
            choice = None
            while choice is None:
                playsound('Demon-Ghost Sound effect.mp3')
                user_input = input("""
From the darkness ahead of you.. you hear a strange noise.

What do you do?

1 - Continue walking
2 - Stop to listen

> """)
                if user_input == "1" or user_input == "continue":
                    choice = "1"
                    print("You walk forward to find a door you give a push annnddd.....")
                    playsound('Big heavy door open and close sound effect.mp3')
                    combat()
                elif user_input == "2" or user_input == "stop":
                    choice = "2"
                    skill_check()
                else:
                    print("""
Not a valid choice, type a number or - "continue" / "stop"
                    """)

        def skill_check():
            cls()
            print(
"A giant rock falls from the ceiling, roll a die to see if you can dodge it.. or you will be crashed by it!")
            roll = randint(1, 6)
            print("You rolled: " + str(roll))
            if roll + character_dexterity > 10:
                playsound('Boulder with sound.mp3')
                print("""
You dodge the stone and survive! Danger is not over though..
The strange noise in the darkness continues, and it feels a lot closer now..""")
                input("Press Enter to continue...")
                combat()
            else:
                playsound('Boulder with sound.mp3')
                playsound('Sad Trombone - Gaming Sound Effect (HD).mp3')
                print("You are smashed by the rock.. You die. The game is over.")
                input("Press Enter to exit the game.")


        def combat():
            cls()
            global character_life
            print("A horrible orc attacks you!")
            input("Press Enter to combat...")
            playsound('Monster Attack Sound Effect.mp3')
            orc = [10,14]                                             #orc[0] -> orc strength and orc[1] -> orc life
            while orc[1] > 0 and character_life > 0:
                char_roll = randint(1, 6)
                print("You rolled: " + str(char_roll))
                monst_roll = randint(1, 6)
                print("The monster rolled: " + str(monst_roll))
                if char_roll + character_strength >= monst_roll + orc[0]:
                    print("You hit the monster!")
                    orc[1] = orc[1] - randint(1,6)
                elif char_roll + character_strength == monst_roll + orc[1]:
                    print("You defended each other")
                else:
                    print("The monster hits you!")
                    character_life = character_life - randint(1,6)
            if character_life > 0:
                playsound('Old victory sound roblox.mp3')
                print("\n\nYou defeated the orc, Wohoooo!! ")
                print("You free your friends!!congratulations!")
                input("Press Enter to exit the game\nThank you for Playing {}. Programmed by Narmatha.T :)".format(name))
            else:
                playsound('Lost Game Sound Effect.mp3')
                print("\n\nYou lost.. your friends will never be freed.. and you're dead.")
                input("Press Enter to exit the game\nThank you for Playing {}. Programmed by Narmatha.T :)".format(name))

        Scene_1()

#Story 2

    elif response == "2":
        title = "FOREST ADVENTURE - AN INTERACTIVE FICTION GAME"
        system("title "+ title)
        cls()
        print("Welcome to the FOREST ADVENTURE - AN INTERACTIVE FICTION GAME!!")
        enter()
        cls()
        print("Greetings, " + name + ". Let us go on a quest!\n")
        print("You have come with a group of adventurers on a trek camp")
        print("An old rickety rackety bus drops you all at the camping site near a forest.")
        print("The smell of the new environment and the thrill in the air made you explore the place putting you in an unknown place away from the trek squad anddd.....")
        print("you find yourself on the edge of a dark forest.")
        print("Can you find your way through?\n")

        # Start of game

        response = ""
        while response not in yes_no:
            response = input("Would you like to step into the forest?\nyes/no\n")
            if response == "yes":
                print("You head into the forest. You hear crows cawing in the distance.\n")
                time.sleep(5)
            elif response == "no":
                print("You are not ready for this quest. Goodbye, " + name + ".")
                playsound('Lost Game Sound Effect.mp3')
                time.sleep(5)
                quit()
            else:
                print("I didn't understand that.\n")


        # Next part of game
        cls()
        response = ""
        while response not in game_options:
            print("To your left, you see a bear.")
            print("To your right, there is more forest.")
            print("There is a rock wall directly in front of you.")
            print("Do you try to find your way back to the camp going backward.\n")
            response = input("What direction do you move?\nleft/right/forward/backward\n")
            if response == "left":
                print("The bear eats you. Farewell, " + name + ".")  
                time.sleep(5)              
                quit()
            elif response == "right":
                print("You head deeper into the forest.\n")
                time.sleep(5)
            elif response == "forward":
                print("There is nothing you can do standing in front of this wall.\n")
                time.sleep(10)
                quit()
            elif response == "backward":
                print("You don't seem to be an adventurer Goodbye, " + name + ".")
                playsound('Lost Game Sound Effect.mp3')
                time.sleep(10)
                quit()
            else:
                print("I didn't understand that.\n")
                continue
        input("Press enter the begin the quest!!")
        cls()
        response = ""
        while response not in game_options:
            print("You walk deep into the forest with all the wildest of vegetation growing without an inch of gap")
            print("You continue walking deeper into the forest of mystery all alone")
            print("At a distance you hear the gush of water ")
            playsound('Stream Water Sound.mp3')
            print("What do you wonder this sound could be?? ")
            print("1 A waterfall ")
            print("2 A river of muddy water")
            response = input("> ")
            if response == "1":
                print("You are wrong {} it was a muddy water river\n".format(name))
                time.sleep(5)
            elif response == "2":
                print("You were absolutely right {}\n ".format(name))
                time.sleep(2)
            else:
                print("I didn't understand that.\n")

        response = ""
        while response not in game_options:
            enter()           
            cls()
            print("Now comes a bigger problem....... You need to cross this river to get onto the other side.")
            print("And the river is filled with with crocodiles!!")
            print("You find the trunk of a tree at a distance.....")
            print("What would you like to do??")
            print("1. Use the trunk as a boat and cross the river ")
            print("2. Swim through the river without minding the obstacles")
            print("3. Head back home")
            response = input("> ")
            if response == "1":
                print("That was a clever use of mind {}.\n".format(name))
                print("You manage to pull the trunk near the edge of the river....")
                print("with a gentle push towards the fast flowing river the trunk has already started moving and you quickly hope in!!")
                print("The current is strong enough to quickly bring you half the distance, but......!!")
                print("\n\nHere comes another danger!!!\n\n")
                input("Press enter the move forward...")
                cls()
                print("A group of crocodiles manage to appear from nowhere and topple your temporary boat")
                print("You are now in the water..... facing the crocodiles")
                print("What do you think of doing {}??".format(name))
                print("1. Swim the other half of the river as soon as you can")
                print("2. Use the trunk to give the crocdiles a light blow and swim quickly to the other side")
                response1 = input("> ")
                if response1 == "1":
                    print("A bad decision {} the adventurer".format(name))
                    print("Crocodiles are really fast swimmers and can catch up with you")
                    print("Farewell {}.".format(name))
                    playsound('Lost Game Sound Effect.mp3')
                    time.sleep(10)
                    quit()
                elif response1 == "2":
                    print("Your decision is gonna save your life {}!!".format(name))
                    print("Crocodiles are fast swimmers trying to distract them then quickly swim away is truly a wise decion")
                    print("Pushing through the waters you reach the land!!\n\n")
                else:
                    print("I didn't understand that.\n")
                    print("You chose option swim the other half of the river, please choose it again followed by the correct options.")
                    response = ""
                    continue

            elif response == "2":
                print("You must be fearless and an amazing swimmer!!")
                print("But crocodiles are much fast in swimming and it is a fact that that crocdiles can not be defeated when in water")
                print("Farewell {}.".format(name))
                    playsound('Lost Game Sound Effect.mp3')
                time.sleep(10)
                quit()
            elif response == "3":
                print("You don't seem to be a real adventurer {} ".format(name))
                playsound('Lost Game Sound Effect.mp3')
                time.sleep(10)
                quit()
            else:
                print("I didn't understand that.\n")
                continue

        print("That was really terrifying!!")
        print("You run deep into the forest searching for some hiding spot so you can take a break.")
        print("A few minutes later you heave a sigh of relief......\n")
        print("But it does not last looong.")

        response = ""
        enter()
        cls()
        while response not in game_options:
            print("The sun almost sets and darkness begins to creep in....")
            playsound('Forest at night.mp3')
            print("You seem to have been stuck in a maze of tall dense trees.")
            print("What would you do??")
            print("1. Walk your way out of this maze by sunset ")
            print("2. Sit at the same place and wait for help")
            response = input("> ")
            if response == "1":
                print("You are right!!")
                time.sleep(5)
                cls()
                print("It is better to find your own way rather than wait for help.")
                print("There is nothing in front of you all you have is trees and a path to the left and right")
                print("How do you go about to come out of this maze??")
                print("Take \n 1.Left \n 2.Right")
                response1 = ""
                while response1 not in maze_directions:
                    response1 = input("> ")
                    if response1 == "1":
                        print("You land in the same place")
                        time.sleep(5)
                        response1 =""
                        continue
                        cls()
                    elif response1 == "2":
                        print("You seem to be going good!!")
                        print("Another Dead end what do you do??\n 1. Take left \n 2. Take right")
                        response2 = ""
                        while response2 not in maze_directions:
                            response2 = input("> ")
                            if response2 == "1":
                                print("You are half way there \n")
                                time.sleep(5)
                                cls()
                                print("You continue walking and there is another choice that you will have to make to be out")
                                print("At this dead end which direction would you like to take??")
                                print("To your left you thick dense trees with barely space for you to breathe")
                                print("To your right is a long straight pathway that seems like the way out")
                                print("What do you take?? \n 1. Left \n 2. Right")
                                response3 = ""
                                while response3 not in maze_directions:
                                    response3 = input("> ")
                                    if response3 == "1":
                                        print("You try breaking through the tough branches of age old trees and continue to make you way ahead.")
                                        print("With a little leap over a small pool you bend over to a branch that blocks your way you seem to have landed in the same place again")
                                        response3 = ""
                                        continue

                                    elif response3 == "2":
                                        print("You seem to be making the right decisions!!")
                                        print("You walk along a long pathway filled with shrubs and colourful flowers and mushrooms")
                                        print("Hurrraaayy!! You have come out of the maze!!")

                                    else:
                                        print("I didn't understand that \n")
                                        continue
                            elif response2 == "2":
                                print("You walk your way around finding the same tree marks and shrubs along your way and in no time you find yourself in the same place again.")
                                response2 = ""
                                continue
                            else:
                                print("I didn't understand that")
                                continue
                    else:
                        print("I didn't understand that.\n")
                        continue
            elif response == "2":
                print("Might not be a very correct desicion {}.".format(name))
                print("You are in a mysterious forest and at night comes a ferocious man-eater.")
                playsound('Tiger Roar Sound Effect.mp3')
                time.sleep(15)
                print("Farewell {}".format(name))
                playsound('Lost Game Sound Effect.mp3')
                time.sleep(10)
                quit()
            else:
                print("I didn't understand that.\n")
                continue

        print("\nYour happiness does not last long.....")
        time.sleep(5)

        response = ""
        enter()
        cls()
        while response not in game_options:
            print("You seem to be trapped in a valley...........\n")
            print(
                "You begin climbing the hill.... the sun is out of your sight and darkness sets in. ")
            print( "With leaps and misses you continue your way up and in no time you are at the hill top ")
            print("You see the sun bid adieu to the horizons and welcome the chill breeze!!")
            print("You were totally not prepared for this..... ")
            print("The temperature keeps dropping... you find  yourself in a bad situations but you don't give up  ")
            print("Your eyes scan the place far and near up and down in the dim lit, to find a tiny cave a little away from you \n  ")
            print("\nWhat would you do now at this situation???\n ")
            print("\n!! YOU ARE IN A DO OR DIE SITUATION !!! \n\n")
            print("  1. Keep hopes and try your best to reach the cave and survive the night ")
            print("  2. Wrap yourself and try to survive the night\n")
            response = input("> ")
            if response == "1":
                print("Brilliant " + name,
                      "these decisions are gonna save your life\n")
                time.sleep(1)
            elif response == "2":
                playsound('Lost Game Sound Effect.mp3')
                print("The night gets colder and colder at the tropical forest and you freeze to death.....Farewell {}\n Great to see you play wise all this way!!".format(name))
                time.sleep(10)
                quit()
            else:
                print("I didn't understand that.\n")
                continue

        response = ""
        enter()
        cls()
        while response not in game_options:
            print("You manage to survive the night and the sun blesses your existence with a welcoming sunny morning")
            playsound('Forest at day.mp3')
            print("You gather some energy to get yourself up and try to search for some food to satisfy your hunger pangs")
            playsound('Tiger Roar Sound Effect.mp3')
            print("\nooooHHH!!!\nYou spot a lion just in time and you have saved yourself from becoming it's morning meal\n")
            print("Sharp enough the lion notices your movement ")
            playsound('Tiger Roar Sound Effect.mp3')
            print("With a majestic roar the lion pounces your way........")
            print('What would you do???')
            print("\nHURRY UP !!! YOU DON'T HAVE MUCH TIME THE LION IS A FEW LEAPS AWAY..... ")
            print(" 1. Quickly climb up a nearby tree.")
            print(" 2. Run as fast as your legs can carry you. ")
            response = input("> ")
            if response == "1":
                print("Great thinking " + name,
                      "you must be aware that lions cannot climb trees..... the lion roars and moans and walks away after a while!!\n")
                print("Pheeewwwww!!! You are SAAAFFEEE!!")


            elif response == "2":
                print("OOOHHH NOOO!!!  " + name, "....Your decision in this panic is gonna help the hungry lion have a feast. ")
                playsound('Tiger Roar Sound Effect.mp3')
                print("Fare eee welll my friend")
                playsound('Lost Game Sound Effect.mp3')
                time.sleep(15)
                quit()
            else:
                print("I didn't understand that.\n")

        response = ""
        enter()
        cls()
        while response not in game_options:
            print("You seems to be more luckier than ever...!!")
            print("You are on a mango tree!!")
            print("Hunger pangs..... mangoes coming innnn!!!")
            print("This seems to be the tastiest ones ever hadd!!")
            print("You sit on the tree watcghing the birds fly and.......\n\n")
            playsound('Elephant Sound Effects.mp3')
            print("WHAT WAS THAT HUGEEEE SOUND..... \n ")
            print("A herd of elephants your way {}".format(name))
            print("Never mess with elephants especially when they are in a herd!!\n")
            print("\nWHATS GOING ON YOUR MIND AT THIS SITUATION.......\n")
            print(" 1. Continue sitting on this tree until the herd passes by. ")
            print(" 2. Get of the tree and run!! ")
            response = input("> ")
            if response == "1":
                print("This might put you in trouble " + name, " elephants have a strong sense of smell... a light push with their mighty muscles and the tree is be down")
                print("You then try to run.... but these huge elephants with long trunks get a hold of you anddd.....")
                playsound('Lost Game Sound Effect.mp3')
                print("Fare eee welll {}.".format(name))
                time.sleep(10)
                quit()

            elif response == "2":
                print('Good presence of mind ' + name,
                      "the elephants are still at a distance and with nimble feet you can escape this threat. ")

            else:
                print("I didn't understand that")
                print("Please enter the right options")

        response = ""
        enter()
        cls()
        while response not in game_options:
            print("Running and running you come to a stop gradually in front of something you did not want..")
            playsound('Wind sound effects.mp3')
            print("A broken bridge dangling between two cliffs... and you peep down to see a vision of infinity.... like as if you are peeping down from the skiess ")
            print(
                "This seems like the only way.")
            print(
                "If you cross the bridge you have chances .. ")

            print("\n YOUR LIFE IS IN YOUR DECISION......\n ")
            print("What would you do now??? ")
            print(" 1. Just go ahead ")
            print(" 2. Try for some other way out ")
            response = input("> ")
            if response == '1':
                print("You walk forward holding the edges of the bridge.... a light breeze and the bridges sways in an endless pendulum....  ")
                playsound('Wind sound effects.mp3')
                print("Grasping and panting and frieked you inch your steps ahead")
                print("With a huff and a puff you are on the other side!!")
                time.sleep(6)

            elif response == "2":
                print("You walk around amidst the tress looking for some other wayy")
                print("\n ROOOOOOOAAAAARRRRRR\n")
                playsound('Tiger Roar Sound Effect.mp3')
                print("Seems like the hungry was keeping an eye on you all this while...")
                print("You quickly grab a stick nearby and fight the lion\n")
                print("You manage to injure it's front paw.....  but the angry lion has already cut open your skin with its fangs")
                print("You slowly lose consciousness and..... farewell " + name)
                playsound('Lost Game Sound Effect.mp3')
                quit()
            else:
                print("I didn't understand that")
                print("Please enter the right options")

        response = ""
        enter()
        cls()
        while response not in game_options:
            print(
                "You give yourself a pat on your back as you walk ahead awaiting the hurdles that are yet to come your way.... ")
            playsound('Wild wolf howling sound effect.mp3')
            print("Suddenly a loud howl captures your attention as a chill shiver runs down your spine...")
            print(
                "And...there it goes again...a howl that echoes throughout the entire forest... that which seems to belong to a hungry wolf...")
            print(
                "You come to a steady halt, your heart pounding...beads of sweat cover your face as your pace becomes faster and faster")
            print("You fail to notice the trap that is hidden beneath a pile of dry leaves... ")
            print(
                "Before you realize you step on the trap which hoists you up by one of your leg that gets caught in a rope...and all of a sudden the world you see is upside down ")
            print("At a distant...the wolf's powerful howl rings through the night sky as you go white with fear")
            print(
                "The rope hoisting you sways...just like the motion of a pendulum")
            print("You see a stone with a curved sharp edge..")
            print("\nWhat do you do now??? \n")
            print(" 1. Find ways to free yourself immediately..")
            print(" 2. Give up and wait till the night ends")

            response = input("> ")
            if response == '1':
                print("Your head throbs as you search frantically for a way to free yourself from the trap")
                print(
                    "You successfully reach out to the stone and manage to cut the rope, crashing down with a small thud...freeing yourself!!")
                print("Even though you are little hurt you heave a sigh of relief as you proceed further...\n")

            elif response == "2":
                playsound('Forest at night.mp3')
                playsound('Wild wolf howling sound effect.mp3')
                print(
                    "The night echoed with the call of the wild as the shrill howl pierces through your eardrums...and continues to linger on...")
                print("The sound seems to approach closer and closer as you feel a familiar ache in your body...")
                print(
                    "The last thing you encounter are a large pair of beady eyes fixed to yours...the wolf is standing right infront of your lips pulled back in a snarl.."
                    )
                print("You slowly start to lose conciousness...and farewell" + name)
                playsound('Lost Game Sound Effect.mp3')
                print("You got eaten up by the wolf!!!")
                time.sleep(10)
                quit()
            else:
                print("I didn't understand that")
                print("Please enter the right options")
        enter()
        cls()
        print("You run and run... faster and faster as you can hear the sound of an old engine and weiry tyres rubbing against the ground.")
        playsound('Bus tyre effect.mp3')
        print("You run towards the direction of the sound and you start to notice a dim light in front of you.....\n")
        playsound('Old victory sound roblox.mp3')
        print("Wohooooo it's the trekking bus that you had missed in the beginning of the story!!!!\n Thank you for Playing {}. Programmed by Narmatha.T :)".format(name))
        time.sleep(10)

        #end of story 2

    else:
        print("I didn't understand that")
        print("Please enter the right options")  #This else is for the wrong option at the story selection