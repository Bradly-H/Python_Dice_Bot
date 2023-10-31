import dice
import discord
from dotenv import load_dotenv
import os

def roll_die():
    while(True):
        word = input("thing to parse: ")
        if word == "break":
            break
        dice.func(word)





def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to discord!')
        print("ready!")

    @client.event
    async def on_message(message):
        print("current message: ", message)
        if message.author == client.user:
            return
        elif message.content.startswith('/roll'): #have keyword
            try:
                command = message.content.split(" ")
                rolls = []
                val = dice.func(command[1])
                while (True):
                    try:
                        rolls.append(next(val))
                    except:
                        break
                if rolls[0] == -1:
                    raise Exception
                else:
                    list = str(rolls[:-2])
                    plus_val = str(rolls[-2])
                    tot = str(rolls[-1])
                    if rolls[-2] == 0:
                        response = f'{message.author} request: `{command[1]}` \nRolls: `{list}` \nTotal: `{tot}`'
                        if len(response) > 1500:
                            await message.channel.send(f'{message.author} request: `{command[1]}` \nTotal: `{tot}`')
                        else:
                            await message.channel.send(response)
                    else:
                        response = f'{message.author} request: `{command[1]}` \nRolls: `{list}` \nModifier: `{plus_val}` \nTotal: `{tot}`'
                        if len(response) > 1500:
                            await message.channel.send(f'{message.author} request: `{command[1]}` \nTotal: `{tot}`')
                        else:
                            await message.channel.send(response)

            except Exception as n:
                print(n)
                await message.channel.send("invalid input")
    client.run(TOKEN)

if __name__ == '__main__':
    main()

