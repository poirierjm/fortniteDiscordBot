# Fortnite ranking system discord bot

## How it work?

With this script, discord users can rank themself with commands.  
Your rank depend of your overall fortnite Kill/Death ratio.
Here are the ranks you can have, you need to create all of these ranks in your discord in order to the bot work.
```
@Wood,        0.00 → 0.99  K/D  
@Carton,      1.00 → 1.49  K/D  
@Bronze,      1.50 → 1.99  K/D  
@Silver,      2.00 → 2.49  K/D  
@Gold,        2.50 → 2.99  K/D  
@Platinium,   3.00 → 3.49  K/D  
@Diamond,     3.50 → 3.99  K/D  
@Ruby,        4.00 → 4.99  K/D  
@Royality,    5.00 → 5.99  K/D  
@Illuminati,  6.00 → 7.99  K/D  
@Hackeur,     8.00 → +  K/D  
```

Once the ranks are created you can create rooms with permissions based on the rank / K/D of the user.  
An example of a discord using the bot.  
![alt text](discordEx.png "Discord example")


## Author

Jean-Michel Poirier (poirier.jmp@gmail.com)   

## How to run?

To setup the bot, open the file ```bot.py ``` and modify the constant ```DISCORD_TOKEN ```with your own discord token. 
Then, modify the constant ```FORTNITE_API_KEY ```with your fornitetracker api key. You can get one at https://fortnitetracker.com  

You are all setup to run the script, execute the command ```./script.sh ```  

## License

The project is under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).  

## Bugs
- ... 