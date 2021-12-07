from PIL import Image, ImageDraw,ImageFont
from discord.ext import commands
import discord
import random


bot = commands.Bot(command_prefix=['?'])

BotToken='Put your bot token here'


@bot.command()
#trigger it by ' ?image [text] '
async def image(ctx,*,text):
	
	#loads custom font
	font=ImageFont.truetype('roboto.ttf',20)
	
	#randomizes colors value but ''a" is set to 255
	r,g,b,a=random.randint(0,255),random.randint(0,255),random.randint(0,255),255
	
	#makes new image to draw
	temp= Image.new('RGBA',(150,100),(r,g,b,a))
	
	#creates a drawing context
	tempd=ImageDraw.Draw(temp)
	
	#randomizes the colors for text's
	r,g,b,a=random.randint(0,255),random.randint(0,255),random.randint(0,255),255
	
	#applying the text and its font
	tempd.text((5,5),text,font=font,fill=(r,g,b,a))
	
	#saves it
	temp.save('image.png')
	
	#sends it to the chat
	await ctx.send(file=discord.File('image.png'))

bot.run(BotToken)

