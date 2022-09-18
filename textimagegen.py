from PIL import Image, ImageDraw,ImageFont
from discord.ext import commands
import discord
import random
import io


bot = commands.Bot(command_prefix=['?'],intents=discord.Intents.all())

BotToken='Put your bot token here'


@bot.command()
#trigger it by ' ?image [text] '
async def image(ctx,*,text):
	
	#loads custom font
	font=ImageFont.truetype('roboto.ttf',20)
	
	#randomizes colors value but ''a" is set to 255
	rgb=random.randint(0,255),random.randint(0,255),random.randint(0,255),255
	
	#makes new image to draw
	temp= Image.new('RGBA',(150,100),rgb)
	
	#creates a drawing context
	tempd=ImageDraw.Draw(temp)
	
	#randomizes the colors for text's
	rgb=random.randint(0,255),random.randint(0,255),random.randint(0,255),255
	
	#applying the text and its font
	tempd.text((5,5),text,font=font,fill=rgb)
	
	#saves it to a buffer 
	buffer=io.BytesIO()
	temp.save(buffer,"PNG")	
	
	#sends it to the chat
	await ctx.send(file=discord.File(buffer,filename='image.png'))

bot.run(BotToken)

