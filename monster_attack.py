"""
Here is where I will do the monster attack - then combine them.

I will use a function to generate random number for monster attack.  max? min? crit%?
"""
import random

new_player_healthplayer_health = 2000

def monster_attack_power(rand):
    return random.choice((range(3, 353)) + range((793, 912))) 

while new_player_health > 0: 
    new_player_health= (new_player_health) - (monster_attack_power(rand))
    new_player_health -= monster_attack_power
    print(monster_attack_power)
    if new_player_health <= 0: 
        print("You have been slain by the beast! fear not, your body will not go to waste.")
        break
    else:
        print("You are the hero!!")
        print("you have" + new_player_health + "remaining!")          

    