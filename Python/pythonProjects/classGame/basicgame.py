from random import randint, choices

# The character class that defines all entities ie Player and enemy
class character:
    def __init__(self, name, weapons, health):
         self.name = name
         self.weapons = weapons
         self.health = health

# Weapon class that makes all weapons
class weapon:
    def __init__(self, damage, speed):
        self.damage = damage
        self.speed = speed

# The fight between a player and enemy
def fight(damage, speed, health):
    dagger = weapon(3,3)
    blade = weapon(4, 5)
    randEnemy = randint(1,2)
    goblin = character("goblin", dagger, 15)
    skeleton = character("skeleton", blade, 20)
    if randEnemy == 1:
        enemy = goblin
    else:
        enemy = skeleton
    turns = 1
    while True:
        if death(enemy.health):
            print("You Have defeated the enemy!!!")
            break
        if death(health):
            print("You have died :sob:")
            break
        print("-----------------------------------------------------------------------")
        print(f"Turn {turns}\n")
        print("Hit Points:")
        print(f"   HP: {health}")
        print(f"   Enemy HP: {enemy.health}\n")
        enemyTurn = 0
        playerTurn = 0
        enemyAction = randomAction()[0]
        print("\nWould you like to Attack, Heavy, or Block: ", end="")
        playerAction = input()
        playerAction.lower()
        print(f"\nThe enemy will {enemyAction}")
        if enemy.weapons.speed < speed:
            if playerAction == "block" and enemyAction == "heavy":
                print("You blocked the heavy attack!!!")
                playerTurn = 1
            elif playerAction != "block" and enemyAction == "heavy":
                print(f"The enemy uses a heavy attack and does {enemy.weapons.damage*2}")
                health = heavy(enemy.weapons.damage, health)
            elif playerAction == "block" and enemyAction == "block":
                playerTurn = 1
                enemyTurn = 1
            elif enemyAction == "block":
                enemyTurn = 1
            else:
                print(f"The enemy will do {enemy.weapons.damage} damage")
                health = attack(enemy.weapons.damage, health)
            if death(health):
                print("You have died :sob:")
                break
            while playerTurn == 0:
                if playerAction == "attack":
                    print(f"You did {damage} damage")
                    enemy.health = attack(damage, enemy.health)
                    playerTurn = 1
                elif playerAction == "heavy" and enemyAction != 'block':
                    print(f"You did {damage*1.25} damage")
                    enemy.health = heavy(damage, enemy.health)
                    playerTurn = 1
                elif playerAction == "heavy" and enemyAction == 'block':
                    print("The enemy has blocked your heavy attack!")
                    playerTurn = 1
                elif playerAction == "block" and enemyAction == "attack":
                    print("You can't block attacks")
                    playerTurn = 1
                elif playerAction == "block":
                    print("You will block")
                    playerTurn = 1
                else:
                    print("Enter correct action")
                    playerAction = input()
                    playerAction.lower()
            enemyTurn = 1
        else:
            while playerTurn == 0:
                if playerAction == "attack":
                    print(f"You did {damage} damage")
                    enemy.health = attack(damage, enemy.health)
                    playerTurn = 1
                elif playerAction == "heavy" and enemyAction != 'block':
                    print(f"You did {damage*1.25} damage")
                    enemy.health = heavy(damage, enemy.health)
                    playerTurn = 1
                elif playerAction == "heavy" and enemyAction == 'block':
                    print("The enemy has blocked your heavy attack!")
                    playerTurn = 1
                elif playerAction == "block":
                    playerTurn = 1
                elif playerAction == "block" and enemyAction == "attack":
                    print("You can't block attacks")
                    playerTurn = 1
                else:
                    print("Enter correct action")
                    playerAction = input()
                    playerAction.lower()
            if enemyTurn != 1:
                if enemyAction == "attack":
                    print(f"The enemy will do {enemy.weapons.damage} damage")
                    health = attack(enemy.weapons.damage, health)
                elif enemyAction == 'heavy' and playerAction != 'block':
                    health = heavy(enemy.weapons.damage, health)
        turns+=1
        
# Performs a standard attack
def attack(damageTaken, hp):
    return hp - damageTaken

# Performs a heavy attack
def heavy(damage, hp):
    return hp - (damage*1.25)

# Checks to see the player or enemy died
def death(hp):
    if hp <= 0:
        return True
    else:
        return False

# Shows the percent chance of the enemy's action and chooses an action based on those percentages
"""
Only cool thing going on.
"""
def randomAction():
    allActions = ['block', 'heavy', 'attack']
    overAllChance = 100
    blockChance = randint(0, overAllChance-50)
    overAllChance-=blockChance
    heavyChance = randint(0, overAllChance - 12)
    overAllChance-=heavyChance
    attackChance = overAllChance
    chances = [blockChance, heavyChance, attackChance]
    print("Enemy Action Chances: ")
    print("   Block: ",blockChance)
    print("   Heavy: ",heavyChance)
    print("   Attack: ",attackChance)
    return choices(allActions, weights=chances, k=1)

# Gets information about the player and starts a fight with a random enemy
def main():
    print("What is your name: ", end="")
    name = input()
    sword = weapon(4, 10)
    spellBook = weapon(6, 1)
    print("Would you like a sword or spell book?: ", end="")
    weaponChoice = input()
    if weaponChoice == "sword":
        player = character(name, sword, 12)
    else:
        player = character(name, spellBook, 7)   
    print(f"You, {player.name}, have {player.health} hp")
    fight(player.weapons.damage, player.weapons.speed, player.health)

if __name__ == "__main__":
        main()