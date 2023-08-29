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

player_health = 1000
monster_health = 1200

attack_value = int(input("Enter an attack value: "))
new_monster_health = int(monster_health) - int(attack_value)
while int(new_monster_health) > 0:
    print("The beast still lives! ")
    
else: 
    int(new_monster_health) < 0
    print("The beast is no more!!!")