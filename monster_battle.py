import random
"""
Set initial health values for yourself (the player) and the monster.
Use a while loop to run the game until either you or the monster has no health left.
Inside the loop:                                                        initial health values
Prompt the player to enter an attack value.                         input atttack value
Subtract the attack value from the monster’s health.
Check if the monster’s health is 0 or less. If so, exit the loop.
Generate a random attack value for the monster.
Subtract the monster’s attack value from the player’s health.
Check if the player’s health is 0 or less. If so, exit the loop.
After the loop ends, print the result of the battle (e.g., victory or defeat).

"""
player_health = 2000
monster_health = 1200


def monster_attack_power():
    return random.choice(list(range(3, 353)) + list(range(793, 912)))

attack_value = int(input("Enter an attack value: "))
new_monster_health = monster_health - attack_value

while new_monster_health > 0 and player_health > 0:
    print("The beast still lives! there are " + str((new_monster_health)) + " hit points left")
    monster_attack = monster_attack_power()
    player_health -= monster_attack
    print("The Mighty beast swings! You lose " + str(monster_attack) + " hit points left")
   
    if player_health <= 0: 
        print("You have been slain by the beast! fear not, your body will not go to waste.")
        break
    else:
        print("You are the hero!!")
        print("you have" + str(player_health) + "remaining!")   
    attack_value = int(input("Attack again!: please enter your attack value!: "))
    new_monster_health = monster_health - attack_value
if new_monster_health <= 0:
    print("The beast is no more!!!")



       
