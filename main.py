import random, side, discord

#Variables
token = open('note_token_test', 'r').read()
client = discord.Client()
results = [('Water','Aether'),('Water','Fire'),('Air','Water'),('Air','Earth'),('Fire','Air'),
        ('Fire','Aether'),('Earth','Fire'),('Earth','Water'),('Aether','Earth'),('Aether','Air'),]
moves = [result[1] for result in results]


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user.mentioned_in(message):
      await message.channel.send('Greetings gladiator! My prefix is B \n Stands for "Battle!" easy to remember!')
    
    if message.content == 'Bhelp':
        await message.channel.send('balblabla')

    if message.content.startswith('Bcreature'):
        creature_id = message.content[9:12]
        for data in side.get_data():
            
                
    
    
    
    
    # if message.content == 'Bsolo':
    #     bot_life = 10
    #     player_life = 10
    #     player = random.choice(get_data())
    #     bot = random.choice(get_data())
    #     if player == bot:
    #         while player == bot:
    #             player = random.choice(get_data())
    #             bot = random.choice(get_data())
        
    #     while bot_life > 0 and player_life > 0:
    #         bot_move = random.choice(moves)
    #         player_move = 






    if message.content == 'Bchallenge':
        pass
    
    if message.content == 'Bbo3':
        pass
    
    if message.content == 'Btournament':
        pass

    # if message.content == prefix+'sologame':
    #     while True:
    #     #como player escolhe
    #     bot = random.choice(moves)

    #     if choice == bot:
    #         print(f"bot choose {bot}, It's a tie!")
    #     elif (choice, bot) in results:
    #         print(f'bot chooses {bot} You win!')
    #     elif (bot, choice) in results:
    #         print(f"bot chooses {bot}, you loses")
        





client.run(token)