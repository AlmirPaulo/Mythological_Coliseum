#Libraries
import random

#Variables
results = [('Water','Aether'),('Water','Fire'),('Air','Water'),('Air','Earth'),('Fire','Air'),
        ('Fire','Aether'),('Earth','Fire'),('Earth','Water'),('Aether','Earth'),('Aether','Air'),]
moves = [result[1] for result in results]

while True:
    choice = input(f"Water, Earth, Aether, Fire, Earth >")
    bot = random.choice(moves)

    if choice == bot:
        print(f"bot choose {bot}, It's a tie!")
    elif (choice, bot) in results:
        print(f'bot chooses {bot} You win!')
    elif (bot, choice) in results:
        print(f"bot chooses {bot}, you loses")
    else:
        print('something is wrong')



#Jo, Ken, Po System
#def jokenpo()
