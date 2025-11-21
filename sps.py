'''
sessior paper stone game let's play
'''
import random
end = True
player_point = 0
computer_point = 0
while end :
    print("AI =", computer_point,"YOU =", player_point)
    answer = input("sessior,paper or stone?choose on of them and type: \n")
    
    if answer == "sessior" :
        end = True
    elif answer == "paper" :
        end = True
    elif answer == "stone" :
        end == True
    else :
        print("you did't choose invalid answer")
        continue

    ai = random.randint(1,3)
    if ai == 1 :
        computer_answer = "paper"
    elif ai == 2 :
        computer_answer = "sessior"
    else :
        computer_answer = "stone"

    if computer_answer == answer :
        print("unlucky !!!!!!!it's DRAW!!!!!!!")
        print("computer answer= ",computer_answer)
    elif computer_answer == "paper" and answer == "stone" :
        print("!!!!!!!you LOSE!!!!!!!")
        computer_point += 1
        print("computer answer= ",computer_answer)
    elif computer_answer == "paper" and answer == "sessior" :
        print("!!!!!!!you WON!!!!!!!")
        player_point += 1
        print("computer answer= ",computer_answer)
    elif computer_answer == "sessior" and answer == "paper" :
        print("!!!!!!!you LOSE!!!!!!!")
        computer_point += 1
        print("computer answer= ",computer_answer)
    elif computer_answer == "sessior" and answer == "stone" :
        print("!!!!!!!you WON!!!!!!!")
        player_point += 1
        print("computer answer= ",computer_answer)
    elif computer_answer == "stone" and answer == "sessior" :
        print("!!!!!!!you LOSE!!!!!!!")
        computer_point += 1
        print("computer answer= ",computer_answer)
    elif computer_answer == "stone" and answer == "paper" :
        print("!!!!!!!you WIN!!!!!!!")
        player_point += 1
        print("computer answer= ",computer_answer)
    if computer_point == 3 :
        print("!!!!!!the computer is the finalist WINNER!!!!!!!")
        end = False
    elif player_point == 3 :
        print("!!!!!!!you are the finalist WINNER!!!!!!!")
        end = False
print("!!!!!!! AI =", computer_point,"YOU =", player_point, "!!!!!!!")