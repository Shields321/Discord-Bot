import asyncio
import os
import discord
import random
from math import *


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    #this part is only if you wanna be notified when the bot is availible
    """channel = client.get_channel(1163652451082174467)
    await channel.send('Melusine is ready for battle')"""
          
@client.event
async def on_message(message):
    if message.author == client.user:
        return 0
    
    if message.content.startswith('$Commands'):
        await message.channel.send('The Commands are:\n$Melusine Daily - Promps user to create a daily post \n $Integrate - needs to have an accuracy amount a lower bound and upper bound to be able to do the integration of a integral\n$image - to display a image \n $stop - to Stop ALL Commads(restarts the discord bot)')
    
    if message.content.startswith('$Integrate'):
        bounds = [None]*4
        
        bounds = message.content.split(" ")

        N = int(bounds[1]) #number of repatitions (more = more accurate value)
        a = int(bounds[2]) #Lower bound
        b = int(bounds[3]) #Upper bound
        e = "(sin(sqrt(x)+9))/sqrt(x)" 
        print(N,a,b)

        def Integrate(N,a,b): #this can't do integrations with equation boundaries (i.e can only be a value in the boundary like 2 or 2.5 not an equation)
            def f(x): #try to figure out a way for the user to input the integral
                return (sin(sqrt(x)+9))/sqrt(x) # Enter the integral equation here  
            value = 0
            value2 = 0
            for n in range(1,N+1):
                value += f(a+((n-(1/2))*((b-a)/N)))
            value2 = ((b-a)/N)*value
            return value2
        STR = 'Integral of ',e, ' with Lower bound ',a,' and Upper bound ',b,' is: ' , Integrate(N,a,b)
        await message.channel.send(STR)
    
    
    if message.content.startswith('$Melusine Daily'):
        id = '<@'+str(message.author.id)+'>'
        while(1):
            await message.channel.send(id +' Create a Melusine Daily Post')
            for i in range(3600*24):# sleep for 1 hour = 3600
                await asyncio.sleep(1)
      
    if message.content.startswith('$image'): # make the program go through pixiv instead of a folder
        folder_dir = os.path.dirname(__file__)+"\\Melusine"
        #these are used to get the amount of elements in the folder and store them into an array of that length
        i=0
        j=0
        
        for images in os.listdir(folder_dir):# check how many images are in the folder
            j=j+1
        # array for the image path
        path = [None] *j
        
        for images in os.listdir(folder_dir):# store the path for each image
        
            # most of the images come from twitter account https://twitter.com/MelusineDaily Go check them out
            if (images.endswith(".png")) or (images.endswith(".PNG")) or (images.endswith(".gif")) or (images.endswith(".jpg")):
                txt = folder_dir + "\\" + images

                x = txt.replace("\\", "\\")

                path[i] = x
                i = i+1

        number = random.randint(0,len(path))

        if(number<=i):
            with open(path[number], 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)
        else:
            await message.channel.send("The image cannot be sent try again")
            
    #need to work on making music play
    if message.content.startswith('$play'):
        
        args = message.content.split("*")
        print(args[1])
        if(args[0] == '$play'):
            if args[1] == None:
               await message.channel.send("must include URL") 
    
    if message.content.startswith('$stop'):
        await message.channel.send("ending All commands")
        await client.close()
                 
client.run('Token')  
