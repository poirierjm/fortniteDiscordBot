
import discord
import requests
import math

client = discord.Client()

# Constant
DISCORD_TOKEN = "NDA4MTU2OTE2NDA2Mjg4Mzg1.DVL9Ww.e9ku6WBNQwmvz0rzY_i6wrogwXY"

FORTNITE_API_KEY = 'ea5ffa46-76a0-426c-a2e8-8b9c6084ee96'

LISTE = ['Wood', 'Carton', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Ruby', 'Royality', 'Illuminati', 'Hackeur']
WOOD_B = 0.00
WOOD_E = 0.99
CARTON_B = 1.00
CARTON_E = 1.49
BRONZE_B = 1.50
BRONZE_E = 1.99
SILVER_B = 2.00
SILVER_E = 2.49
GOLD_B = 2.50
GOLD_E = 2.99
PLATINUM_B = 3.00
PLATINUM_E = 3.49
DIAMOND_B = 3.50
DIAMOND_E = 3.99
RUBY_B = 4.00
RUBY_E = 4.99
ROYALITY_B = 5.00
ROYALITY_E = 5.99
ILLUMINATI_B = 6.00
ILLUMINATI_E = 7.99
HACKEUR_B = 8.00
HACKEUR_E = 100

# Return the overall K/D of the fortnite player pass in parameter
def get_ratio(username):
    print(username)
    link = 'https://api.fortnitetracker.com/v1/profile/pc/' + username
    response = requests.get(link, headers={'TRN-Api-Key': FORTNITE_API_KEY})
    if response.status_code == 200:
        collection = response.json()
        if 'error' in collection:
            return "-1"
        else:
            for data_item in collection['lifeTimeStats']:
                if data_item['key'] == 'K/d':
                    ratio = data_item['value']
                    return ratio
        print("Invalid username")
        return "-1"
    else:
        print("Error recovering fortnite data")
        return "-2"

def print_nextLvl(begin, end, ratio):
    rang = end - begin 
    if ratio >= rang * 0.00 + begin and ratio <= rang * 0.059999 + begin:
        return '[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.06 + begin and ratio <= rang * 0.109999 + begin:
        return '[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.11 + begin and ratio <= rang * 0.159999 + begin:
        return '[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.16 + begin and ratio <= rang * 0.209999 + begin:
        return '[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.21 + begin and ratio <= rang * 0.259999 + begin:
        return '[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.26 + begin and ratio <= rang * 0.309999 + begin:
        return '[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.31 + begin and ratio <= rang * 0.359999 + begin:
        return '[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.36 + begin and ratio <= rang * 0.409999 + begin:
        return '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.41 + begin and ratio <= rang * 0.459999 + begin:
        return '[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.46 + begin and ratio <= rang * 0.509999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.51 + begin and ratio <= rang * 0.559999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.56 + begin and ratio <= rang * 0.609999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.61 + begin and ratio <= rang * 0.659999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.66 + begin and ratio <= rang * 0.709999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.71 + begin and ratio <= rang * 0.759999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]'
    elif ratio >= rang * 0.76 + begin and ratio <= rang * 0.809999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]'
    elif ratio >= rang * 0.81 + begin and ratio <= rang * 0.859999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]'
    elif ratio >= rang * 0.86 + begin and ratio <= rang * 0.909999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□]'
    elif ratio >= rang * 0.91 + begin and ratio <= rang * 0.959999 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]'
    elif ratio >= rang * 0.96 + begin and ratio <= rang * 1.00 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]'

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # The command /patch return a link withvthe lastest patch note
    if message.content.startswith('/patch'):
        await client.send_message(message.channel, 'Last patchnotes: https://www.epicgames.com/fortnite/en/news')
    # The command /rank return attribute a rank according to the K/D of the user
    if message.content.startswith("/rank"):
        for list in LISTE:
            roles = discord.utils.get(message.server.roles, name=list)
            await client.remove_roles(message.author, roles)
        username = '{0.author.display_name}'.format(message)
        ratio = float(get_ratio(username))
        print(ratio)
        if ratio >= WOOD_B and ratio <= WOOD_E:
            role = discord.utils.get(message.server.roles, name=LISTE[0])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(CARTON_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(WOOD_B, WOOD_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= CARTON_B and ratio <= CARTON_E:
            role = discord.utils.get(message.server.roles, name=LISTE[1])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(BRONZE_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(CARTON_B, CARTON_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= BRONZE_B and ratio <= BRONZE_E:
            role = discord.utils.get(message.server.roles, name=LISTE[2])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(SILVER_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(BRONZE_B, BRONZE_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= SILVER_B and ratio <= SILVER_E:
            role = discord.utils.get(message.server.roles, name=LISTE[3])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(GOLD_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(SILVER_B, SILVER_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= GOLD_B and ratio <= GOLD_E:
            role = discord.utils.get(message.server.roles, name=LISTE[4])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(PLATINUM_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(GOLD_B, GOLD_E, ratio))
            await client.add_roles(message.author, role)  
        elif ratio >= PLATINUM_B and ratio <= PLATINUM_E:
            role = discord.utils.get(message.server.roles, name=LISTE[5])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(DIAMOND_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(PLATINUM_B, PLATINUM_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= DIAMOND_B and ratio <= DIAMOND_E:
            role = discord.utils.get(message.server.roles, name=LISTE[6])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(RUBY_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(DIAMOND_B, DIAMOND_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= RUBY_B and ratio <= RUBY_E:
            role = discord.utils.get(message.server.roles, name=LISTE[7])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(ROYALITY_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(RUBY_B, RUBY_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= ROYALITY_B and ratio <= ROYALITY_E:
            role = discord.utils.get(message.server.roles, name=LISTE[8])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(ILLUMINATI_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(ROYALITY_B, ROYALITY_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= ILLUMINATI_B and ratio <= ILLUMINATI_E:
            role = discord.utils.get(message.server.roles, name=LISTE[9])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(HACKEUR_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(ILLUMINATI_B, ILLUMINATI_E, ratio))
            await client.add_roles(message.author, role) 
        elif ratio >= HACKEUR_B:
            role = discord.utils.get(message.server.roles, name=LISTE[10])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Your ratio: " + str(ratio) + " K/D \n Max level! ¯\_(ツ)_/¯ "
            await client.send_message(message.channel, msgRatio)
            await client.add_roles(message.author, role) 
        elif ratio == -1:
            msg = "Your discord name is not a fortnite username! Use the command ```/nick YOUR_FORTNITE_USERNAME``` first!".format(message)
            await client.send_message(message.channel, msg)
        elif ratio == -2:
            msg = "The fortnite servers are offline. Try again later!".format(message)
            await client.send_message(message.channel, msg)
 

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(DISCORD_TOKEN)


