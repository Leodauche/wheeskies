#Enju
import discord
import random
import time
import os
import asyncio
import pickle
from discord.ext import commands
from discord.ext.commands import Bot


bot = commands.Bot(command_prefix='!')
emojis = bot.get_all_emojis()
bot.remove_command('help')

@bot.event
async def on_ready():
	print ("Enju prete !")
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='!aide'))

	
@bot.command(pass_context=True)
async def aide():
	embed = discord.Embed(title="Commandes d'Enju", color=0x800000)
	embed.add_field(name="enju", value="Envoie une image d'Enju", inline=False)
	embed.add_field(name="avatar", value="Affiche l'avatar d'un utilisateur", inline=False)
	embed.add_field(name="emoji", value="Affiche un emoji en plus gros", inline=False)
	msg = await bot.say(embed=embed)
	await autodestruct(msg,ctx.message,ctx.message.author)


@bot.command(pass_context=True)
async def wait(ctx,nombre):
	await bot.say("début")
	time.sleep(int(nombre))
	await bot.say("fin")



@bot.command(pass_context=True)
async def test(ctx, Texte):
	pathfile = img_txt(Texte)
	await bot.send_file(ctx.message.channel,pathfile)
	os.remove(pathfile)


@bot.command(pass_context=True)
async def delete(ctx, nombre):
	weeb = discord.utils.get(ctx.message.server.roles, id='413821933478739970')
	if (ctx.message.author.top_role == weeb) :
		await bot.purge_from(ctx.message.channel, limit=int(nombre))
	else :
		msg = await bot.say("Seul mon Kinji peut utiliser cette commande !")
		await autodestruct(msg,ctx.message,ctx.message.author)



		
	
@bot.command(pass_context=True)
async def enju(ctx):
	fp = "Donnes/Img/Enju/{}".format(random.choice(os.listdir("Donnes/Img/Enju")))
	await bot.send_file(ctx.message.channel, fp )

@bot.command(pass_context=True)
async def dit(ctx,*,message):
	weeb = discord.utils.get(ctx.message.server.roles, id='413821933478739970')
	if (ctx.message.author.top_role == weeb) :
		await bot.say(str(message))
	else :
		msg = await bot.say("Seul mon Kinji peut utiliser cette commande !")
		await autodestruct(msg,ctx.message,ctx.message.author)

@bot.command(pass_context=True)
async def sayd(ctx,*,message):
	await bot.say(str(message))
	await bot.delete_message(ctx.message)




"""
@bot.command(pass_context=True)
async def couleur(ctx, arg1, arg2=None):
	Arg1=str(arg1)
	if(Arg1.lower()=="reset"):
		roles = ctx.message.author.roles
		print(roles)
		print(len(roles))
		for i in range(0,len(roles)):
			nomRoles = roles[i].name
			print("nom role = ", nomRoles)
			if (nomRoles in Couleurs):
				nomRolesId = discord.utils.get(ctx.message.server.roles, name=nomRoles)
				await bot.remove_roles(ctx.message.author, nomRolesId)
				print(nomRoles,"enlevé")
			i += 1
			print(i)
			time.sleep(0.5)
		msg = await bot.say("Votre couleur a bien été enlevée, si ce n'est pas le cas contacter un adminitrateur pour qu'il vous le fasse manuellement")
		await autodestruct(msg,ctx.message,ctx.message.author)
	elif(Arg1.lower()=="help"):
		CoulEmb = discord.Embed(title="La commande !couleur vous permet de changer la couleur de votre pseudo sur le serveur", color=0x0a00ff)
		CoulEmb.set_author(name="Guide de la commande !couleur")
		CoulEmb.add_field(name="Pour ajouter une couleur faites :", value="```!couleur + nomDeLaCouleur```", inline=False)
		CoulEmb.add_field(name="Pour enlever une couleur faites :", value="```!couleur - nomDeLaCouleur```", inline=False)
		CoulEmb.add_field(name="Pour réinisialliser vos couleurs faites :", value="```!couleur reset```", inline=False)
		CoulEmb.add_field(name="Voici les couleurs disponibles :", value=Couleurs, inline=False )
		msg = await bot.say(embed=CoulEmb)
		await autodestruct(msg,ctx.message,ctx.message.author)
	elif(Arg1=="+"):
		Couleur=str(arg2)
		if(Couleur in Couleur):
			role = discord.utils.get(ctx.message.server.roles, name=Couleur.lower())
			await bot.add_roles(ctx.message.author, role)
		else:
			msg = await bot.say("La couleur que vous voulez n'éxiste pas, pour voir les couleurs disponibles faites ```!couleur help```")
			await autodestruct(msg,ctx.message,ctx.message.author)
	elif(Arg1=="-"):
		Couleur=str(arg2)
		if(Couleur in Couleur):
			role = discord.utils.get(ctx.message.server.roles, name=Couleur.lower())
			await bot.remove_roles(ctx.message.author, role)
		else:
			msg = await bot.say("La couleur que vous voulez n'éxiste pas, pour voir les couleurs disponibles faites ```!couleur help```")
			await autodestruct(msg,ctx.message,ctx.message.author)
	else:
		msg = await bot.say("Vous vous etes trompé dans la commande, pour voir comment s'en servir faites : ```!couleur help```")
		await autodestruct(msg,ctx.message,ctx.message.author)
"""		


@bot.command(pass_context=True)
async def emoji(ctx, emoji: discord.Emoji):
	#embed = discord.Embed(title = ":{}:".format(emoji.name),color=0x4286f4)
	embed = discord.Embed(color=0x4286f4)
	embed.set_image(url=emoji.url)
	await bot.say(embed=embed)

"""
@bot.command(pass_context=True)
async def RemoveRole(ctx,role):
	role = discord.utils.get(ctx.message.server.roles, name=role)
	await bot.remove_roles(ctx.message.author, role)
	
"""
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(title="Avatar de {}".format(user.name), color=0xff0000)
	embed.set_image(url=user.avatar_url)
	await bot.say(embed=embed)


@bot.command(pass_context=True)
async def Say3(ctx,Texte):
	Chnl = bot.get_channel("447763181314768896")
	await bot.send_message(Chnl,str(Texte))


"""
@bot.command(pass_context=True)
async def test2(ctx,nomRole,couleur):
	await bot.create_role(server = ctx.message.server, name=nomRole,colour=discord.Colour(int(couleur, 16)))
	msg = await bot.say("le role {} a bien été créé".format(nomRole))
	await autodestruct(msg,ctx.message,ctx.message.author)
"""

async def autodestruct(msgBot,msgUser,user):
	await bot.add_reaction(msgBot,":enju:463080771465510912")
	await bot.wait_for_reaction(":enju:463080771465510912", message=msgBot, user=user ,timeout=40)
	await bot.delete_message(msgBot)
	await bot.delete_message(msgUser)

bot.run(os.getenv("TOKEN"))

