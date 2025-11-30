'''
let's play russian roulette who will alive?
'''
import random


def random_shot(shot):
    gun_shot = random.randint(1,shot)
    gun_trigger = random.randint(1,shot)
    if gun_shot == gun_trigger:
        return True
    else:
        return False
    
shot = 7
while True:
    print("_"* 10, "russian roulette", "_"* 10)
    print(f"remianing cartridge: {shot}\n")
    
    try:
        user_answer = input("It's ypur turn!Enter 's' to shot or 'x' to run away!")
        action = user_answer.lower()
    
        if action[0] not in ['s', 'x']:
            print("invalid answer!scard?")
            continue
    except (ValueError, IndexError):
        print("invalid answer!just say 's' or 'x'!")
        continue
    
    if action == 'x':
        print("hey man no way to escape,comeback to table!")
        continue
    elif action == 's':
        die = random_shot(shot)
        shot -= 1
        if die:
            print( "ᡕᠵデᡁ᠊╾━ ✷ your brain")
            print("war cartridge!you died!")
            break
        else:
            print("🔫 blank cartridge,do you want some water?\n")
            
    
    computer_die = random_shot(shot)
    shot -= 1
    if computer_die:
        print( "ᡕᠵデᡁ᠊╾━ ✷ cpu")
        print("war cartridge!computer's cpu Exploded!")
        break
    else:
        print("🔫 blank cartridge,computer alived\n")
        
         