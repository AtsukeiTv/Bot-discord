from random import*
import discord
from discord.ext import commands
from discord.ext.commands.converter import ColorConverter
import youtube_dl
import asyncio
from typing import Optional, Set
#from discord_slash import ButtonStyle, SlashCommand
#from discord_slash.utils.manage_components import*
bot = commands.Bot(command_prefix = "", description = "Bot de Ladybug host by Neo")
#slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("Ready !")

#commandes aide bot

@bot.command()
async def reglement(ctx):
    embed = discord.Embed(title = "Voici le règlement du serveur Watch and rewatch", color=0xd51919, description = "Salons textuels \n \n I/ Pseudonyme :\n\n Votre pseudonyme et votre avatar sur Discord \n - Ne doit pas avoir de caractère pornographique. \n - Ne doit pas pouvoir être confondu/ressemblant avec/à celui d'un membre du staff.\n - Ne doit pas contenir de propos racistes, homophobes, sexistes ou faire référence à la drogue.\n \n II/ Conduite à adopter : \n\n - Ne pas recourir aux insultes.\n - Soyez respectueux, courtois, poli envers les utilisateurs et le staff. ""Bonjour""," "Merci""," "Au revoir" "n'ont jamais tué personne, vous pouvez être plus familier également, on est pas dans une entreprise non plus . \n - Pas de pub pour serveur sans demander à @Ladybug  MEME EN MP \n - Respect des sujets des channels." )
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/854301482086170644/913887798111637555/20211116_033606.png")
    await ctx.send(embed = embed)


#### Create the initial embed object ####
@bot.command()
async def reglement2(ctx):
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0x109319)

# Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")

    embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")

    embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=False) 
    embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
    embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)

    embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")


#### Useful ctx variables ####
## User's display name in the server
    ctx.author.display_name

## User's avatar URL
    ctx.author.avatar_url
    await ctx.send(embed=embed)



#- Respect des sujets des channels.
#- Pas de spam d'émotes ou de messages.

#III/ Besoin d'un Admin:
#-Si vous rencontrez le besoin d'UN admin, merci de prendre un ticket dans 📥-ticket et ainsi ping le rôle @|▬▬▬▬ Admin ▬▬▬▬|et le rôle @@|▬▬▬ Modérateurs ▬▬▬|
#- L'usurpation d'identité d'un membre du staff, avec ou sans intention de nuire, se verra immédiatement et sans préavis sanctionnée d'un ban de 7 jours du Discord.
#- En cas de récidive, le staff se réserve le droit d'alourdir les sanctions.

#Salons vocaux
#- Aucun saut de canal de chat vocal.
#- Aucun bruit gênant, fort ou aigu.
#- Réduisez la quantité de bruit de fond, si possible.
#- Aucune soundboard
#- Les modérateurs se réservent le droit de vous déconnecter d'un canal vocal si votre qualité sonore est mauvaise.
#- Les modérateurs se réservent le droit de déconnecter, de mettre en sourdine, d'assourdir ou de déplacer des membres vers et depuis les canaux vocaux.

#Surtout n'oubliez pas:  @Ladybug a toujours raison.

#Pour accepter le règlement du serveur veuillez interagir avec la réaction  ! 
#")
@bot.command()
async def reglement_staff(ctx):
    embed = discord.Embed(title = "Voici le règlement staff du serveur Watch and rewatch", color=0xa8072, description ="|-------------------| \n -Ne pas ban sans ma permission a part urgence. \n Respecter Ladybug ansi que les autres membres du staff.\n - Etre actif sinon vous ne serez plus staff. \n -Inactivite de plus de 2 mois \n|-------------------| ")
    await ctx.send(embed = embed)
#commandes slash



#commandes embed

#@bot.command()
#    discord.Embed()
 #   await ctx.send(embed = embed)
    
#commandes de discussion

@bot.command()
async def Bonjour(ctx):
    await ctx.send("Bonjour! 👀")

@bot.command()
async def trop_con(ctx):
    await ctx.send("moi? non")

@bot.command()
async def cv(ctx):
    await ctx.send("ça va et toi!")

@bot.command()
async def coucou(ctx):
    await ctx.send("coucou toi!")

@bot.command()
async def non(ctx):
    await ctx.send("meh sii 😂")

@bot.command()
async def oui(ctx):
    await ctx.send("je ne crois pas")

@bot.command()
async def ftg(ctx):
    await ctx.send("alors non")

@bot.command()
async def mdr(ctx):
    await ctx.send("mdrr")

@bot.command()
async def hihihi(ctx):
    await ctx.send("Upupu")
@bot.command()
async def Mdrr(ctx):
    await ctx.send("mdrr")

@bot.command()
async def Mdr(ctx):
    await ctx.send("mdrr")

@bot.command()
async def XD(ctx):
    await ctx.send("Tu mens, tu ne ris pas je le vois")

@bot.command()
async def a(ctx):
    await ctx.send("e")

@bot.command()
async def i(ctx):
    await ctx.send("o")

@bot.command()
async def u(ctx):
    await ctx.send("euh... c'est quoi le reste?")

@bot.command()
async def jpp(ctx):
    await ctx.send("t'en peux plus de quoi?")

@bot.command()
async def rien(ctx):
    await ctx.send("Tu ne fais pas rien, la preuve tu me parles et je te réponds^^")

@bot.command()
async def tfk(ctx):
    await ctx.send("Je mange des pop corn en regardant netflou le fou")

@bot.command()
async def pk(ctx):
    await ctx.send("parce que")

@bot.command()
async def si(ctx):
    await ctx.send("non")

@bot.command()
async def jsp(ctx):
    await ctx.send("mon taux d'inteliigence est trop élevé pour savoir 😂")

@bot.command()
async def ok(ctx):
    await ctx.send("https://tenor.com/view/ok-okay-gif-7309546")

@bot.command()
async def ferme(ctx):
    await ctx.send("Je ferme la fenêtre, la porte, ou les deux?")

@bot.command()
async def InfoServeur(ctx):
    serveur = ctx.guild
    nombreDeChainesTexte = len(serveur.text_channels)
    nombreDeChainesVocale = len(serveur.voice_channels)
    Description_du_serveur = serveur.description
    Nombre_de_personnes = serveur.member_count
    Nom_du_serveur = serveur.name
    message = f"Le serveur **{Nom_du_serveur}** contient *{Nombre_de_personnes}* personnes ! \n La description du serveur est {Description_du_serveur}. \nCe serveur possède {nombreDeChainesTexte} salons écrit et {nombreDeChainesVocale} salon vocaux."
    await ctx.send(message)

#commande musique 

musics = {}
ytdl = youtube_dl.YoutubeDL()

class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

@bot.command()
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []

@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()


@bot.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()


@bot.command()
async def skip(ctx):
    client = ctx.guild.voice_client
    client.stop()


def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
        , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

    client.play(source, after=next)


@bot.command()
async def play(ctx, url):
    print("play")
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"Je lance : {video.url}")
        play_song(client, musics[ctx.guild], video)

#commande modération

@bot.command()
async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole

@bot.command()
async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    
    return await createMutedRole(ctx)

@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été mute !")

@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été unmute !")

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} à été unban.")
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")

@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, user, *reason):
    embed = discord.Embed(title = "**warn**", description = "Un staff a frappé !", color=0xfa8072)
    embed.set_thumbnail(url ="https://tse1.mm.bing.net/th?id=OIP.n4FC3sAZ-8QcUCx3ErjtnQAAAA&pid=Api&P=0&w=300&h=300")
    embed.set_author(name = ctx.author.name, icon_url= ctx.author.avatar_url)
    embed.add_field(name = "Membre warn", value = user.name , inline = True)
    embed.add_field(name = "Raison", value = reason, inline = True)
    embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
    reason = " ".join(reason)
    await ctx.send(embed = embed)
    


@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, user : discord.User, *reason):
    embed = discord.Embed(title = "**kick**", description = "Un staff a frappé !", color=0xfa8072)
    embed.set_thumbnail(url ="https://media.discordapp.net/attachments/898561761479905280/911038131078303764/20211119_003815.png")
    embed.set_author(name = ctx.author.name, icon_url= ctx.author.avatar_url)
    embed.add_field(name = "Membre expulsé", value = user.name , inline = True)
    embed.add_field(name = "Raison", value = reason, inline = True)
    embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, nombre : int):
	messages = await ctx.channel.history(limit = nombre + 1).flatten()
	for message in messages:
		await message.delete()

@bot.command()
async def clearchannel(ctx):
    guild = ctx.guild
    for channel in guild.channels:
        await channel.delete()
    
@bot.command()
async def delete_channels(ctx):
    [await channel.delete() for channel in ctx.guild.text_channels]

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user : discord.User, *, reason = "aucune raison n'a été donnée"):
    embed = discord.Embed(title = "**Bannissement**", description = "Un staff a frappé !")
    embed.set_thumbnail(url ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNjsV2pVE63TdGjV82bn66vveLD7kMc5xKV9v4Z34WQ5qIqsWa6_3OlX345rK_XmTSovs&usqp=CAU", color=0xfa8072 )
    embed.set_author(name = ctx.author.name, icon_url= ctx.author.avatar_url)
    embed.add_field(name = "Membre banni", value = user.name , inline = True)
    embed.add_field(name = "Raison", value = reason, inline = True)
    embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(embed = embed)

#Commandes films

@bot.command()
async def Le_Grinch(ctx):
     embed = discord.Embed(title = "Voici le Grinch", color=0xfa8072, url ="https://wiflix.land/film-ancien/13934-le-grinch-dr-seuss-the-grinch.html", description = "Résumé du Grinch: La vie est belle et joyeuse à Chouville, une bourgade située au cœur d'un flocon de neige. Ses habitants, les Choux, aiment célébrer des fêtes, dont celle de Noël. Seul le Grinch leur fait peur. C'est une créature verte et poilue qui ne s'est jamais remise de la méchanceté dont ont fait preuve ses camarades de classe envers lui. Exilé dans la montagne avec son chien, le Grinch rumine sa vengeance." )
     embed.set_thumbnail(url ="https://s3.eu-west-3.amazonaws.com/nova-ici-production/product/images_4/146423.jpg")
     embed.set_image(url = "https://img.20mn.fr/0g08aIzyTpGp1ooK0LtR_w/830x532_grinch-scott-mosier-yarrow-cheney.jpg")
     await ctx.send(embed = embed)

@bot.command()
async def Pole_express(ctx):
    embed = discord.Embed(title = "Voici le Pôle express", color=0xfa8072, url ="https://wiflix.land/film-ancien/11704-le-pole.html", description = "Un jeune garçon qui se met à douter de l'existence du père Noël monte dans un train mystérieux en partance pour le pôle Nord. A mesure que le Pôle Express s'enfonce dans des contrées enchantées, l'aventure est au rendez-vous et les jeunes passagers prennent conscience de l'étendue de leurs dons.")
    embed.set_thumbnail(url ="https://tse3.mm.bing.net/th?id=OIP.6Vw5QCxICNvYBA1y94ZhYwHaJ4&pid=Api&P=0&w=300&h=300")
    embed.set_image(url = "https://tse1.mm.bing.net/th?id=OIP.fCc9VjR9Xd7-lBk5kpy7UwHaEK&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def La_reine_des_neiges(ctx):
    embed = discord.Embed(title = "Voici la reine des neiges", color=0xfa8072, url ="https://wiflix.land/film-ancien/3656-la-reine-des-neiges-frozen.html", description = "Résumé de la Reine des neiges: Anna, une jeune fille aussi audacieuse qu’optimiste, se lance dans un incroyable voyage en compagnie de Kristoff, un montagnard expérimenté, et de son fidèle renne, Sven. Elle est à la recherche de sa sœur, Elsa, la Reine des Neiges, qui a plongé le royaume d’Arendelle dans un hiver éternel… En chemin, ils vont rencontrer de mystérieux trolls et un drôle de bonhomme de neige nommé Olaf, braver les conditions extrêmes des sommets escarpés et glacés, et affronter la magie qui les guette à chaque pas.")
    embed.set_thumbnail(url ="https://cdn.franceloisirs.com/26917-3368508-thickbox/la-reine-des-neiges.jpg")
    embed.set_image(url = "https://www.ludilabel.fr/media/wysiwyg/licences/disney/frozen/reine-des-neiges-disney-etiquettes-personnalisees_2.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def La_reine_des_neiges_2(ctx):
    embed = discord.Embed(title = "Voici la reine des neiges 2", color=0xfa8072, url ="https://wiflix.tel/film-ancien/16213-la-reine-des-neiges-2.html", description = "Pourquoi Elsa est-elle née avec des pouvoirs magiques ? La jeune fille rêve de l’apprendre, mais la réponse met son royaume en danger. Avec l’aide d’Anna, Kristoff, Olaf et Sven, Elsa entreprend un voyage aussi périlleux qu’extraordinaire. Dans La Reine des neiges, Elsa craignait que ses pouvoirs ne menacent le monde. Dans La Reine des neiges 2, elle espère qu’ils seront assez puissants pour le sauver…")
    embed.set_thumbnail(url ="https://wiflix.tel/checkimg.php?urli=0db8-a3c8-48dd-4709.jpg")
    embed.set_image(url = "https://tse3.mm.bing.net/th?id=OIP.OzDyk_v15aPyIQduSr_gBQHaDF&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def Avatar(ctx):
    embed = discord.Embed(title = "Voici Avatar", color=0xfa8072, url ="https://wiflix.land/film-ancien/4961-avatar.html", description = "Résumé de Avatar: Malgré sa paralysie, Jake Sully, un ancien marine immobilisé dans un fauteuil roulant, est resté un combattant au plus profond de son être. Il est recruté pour se rendre à des années-lumière de la Terre, sur Pandora, où de puissants groupes industriels exploitent un minerai rarissime destiné à résoudre la crise énergétique sur Terre. Parce que l'atmosphère de Pandora est toxique pour les humains, ceux-ci ont créé le Programme Avatar, qui permet à des ""pilotes"" humains de lier leur esprit à un avatar, un corps biologique commandé à distance, capable de survivre dans cette atmosphère létale. Ces avatars sont des hybrides créés génétiquement en croisant l'ADN humain avec celui des Na'vi, les autochtones de Pandora.")
    embed.set_thumbnail(url ="https://tse1.mm.bing.net/th?id=OIP.lsyx5H7-NVMaVV81D1pYdQHaLH&pid=Api&P=0&w=300&h=300")
    embed.set_image(url = "https://www.10wallpaper.com/wallpaper/1366x768/2003/2021_Avatar_2_Films_HD_Poster_1366x768.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def Valerian(ctx):
    embed = discord.Embed(title = "Voici Valerian", color =0xfa8072, url ="https://wiflix.land/film-ancien/13241-valerian-et-la-cite-des-mille-planetes-valerian-and-the-city-of-a-thousand-planets.html", description = "Au 28ème siècle, Valérian et Laureline forment une équipe d'agents spatio-temporels chargés de maintenir l'ordre dans les territoires humains. Mandaté par le Ministre de la Défense, le duo part en mission sur l’extraordinaire cité intergalactique Alpha - une métropole en constante expansion où des espèces venues de l'univers tout entier ont convergé au fil des siècles pour partager leurs connaissances, leur savoir-faire et leur culture. Un mystère se cache au cœur d'Alpha, une force obscure qui menace l'existence paisible de la Cité des Mille Planètes. Valérian et Laureline vont devoir engager une course contre la montre pour identifier la terrible menace et sauvegarder non seulement Alpha, mais l'avenir de l'univers.")
    embed.set_thumbnail(url = "https://tse1.mm.bing.net/th?id=OIP.ELyu1fE9oeuxLO7Zs2q0oQHaLH&pid=Api&P=0&w=300&h=300")
    embed.set_image(url = "https://tse3.explicit.bing.net/th?id=OIP.jSCP_VWJy3n4GNlrYOqhFAHaDt&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def Labyrinthe(ctx):
    embed = discord.Embed(title = "Voici le Labyrinthe", color=0xfa8072, url ="https://wiflix.land/film-ancien/450-le-labyrinthe-the-maze-runner.html", description = "Quand Thomas reprend connaissance, il est pris au piège avec un groupe d'autres garçons dans un labyrinthe géant dont le plan est modifié chaque nuit. Il n'a plus aucun souvenir du monde extérieur, à part d'étranges rêves à propos d'une mystérieuse organisation appelée W.C.K.D. En reliant certains fragments de son passé, avec des indices qu'il découvre au sein du labyrinthe, Thomas espère trouver un moyen de s'en échapper.")
    embed.set_thumbnail(url ="https://wiflix.tel/checkimg.php?urli=1d8e-4f7f-52a1-4d19.jpg")
    embed.set_image(url = "https://tse2.mm.bing.net/th?id=OIP.XNpVRB-LpEicfW3L9Vv2VgHaEK&pid=Api&P=0&w=306&h=172")
    await ctx.send(embed = embed)

@bot.command()
async def Labyrinthe_la_terre_brulee(ctx):
    embed = discord.Embed(title = "Voici le labyrinthe: La terre brûlée", color=0xfa8072, url = "https://wiflix.land/film-ancien/12175-le-labyrinthe-la-terre-brulee-maze-runner-the-scorch-trials.html", description = "Dans ce second volet de la saga épique LE LABYRINTHE, Thomas et les autres Blocards vont devoir faire face à leur plus grand défi, rechercher des indices à propos de la mystérieuse et puissante organisation connue sous le nom de WICKED. Or le monde qu’ils découvrent à l’extérieur du Labyrinthe a été ravagé par l’Apocalypse. Leur périple les amène à la Terre Brûlée, un paysage de désolation rempli d'obstacles inimaginables. Plus de gouvernement, plus d'ordre… et des hordes de gens en proie à une folie meurtrière qui errent dans les villes en ruine. Les Blocards vont devoir unir leurs forces avec d'autres combattants pour pouvoir affronter WICKED et tenter de défier son immense pouvoir.")
    embed.set_thumbnail(url = "https://wiflix.tel/checkimg.php?urli=d5ed-7ff0-6af2-4aed.jpg")
    embed.set_image(url = "https://tse2.mm.bing.net/th?id=OIP.TYoRyFXv_X5cL_X28hzTUgHaE8&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def Labyrinthe_le_remede_mortel(ctx):
    embed = discord.Embed(title = "Voici le Labyrinthe: le remède mortel", color=0xfa8072, url = "https://wiflix.land/film-ancien/13038-le-labyrinthe-le-remede-mortel-maze-runner-the-death-cure.html", description = "Dans ce dernier volet de l'épopée LE LABYRINTHE, Thomas et les Blocards s'engagent dans une ultime mission, plus dangereuse que jamais. Afin de sauver leurs amis, ils devront pénétrer dans la légendaire et sinueuse Dernière Ville contrôlée par la terrible organisation WICKED. Une cité qui pourrait s'avérer être le plus redoutable des labyrinthes. Seuls les Blocards qui parviendront à en sortir vivants auront une chance d'obtenir les réponses tant recherchées depuis leur réveil au coeur du Labyrinthe.")
    embed.set_thumbnail(url = "https://wiflix.tel/checkimg.php?urli=ac24-4cc6-2ef7-4c21.jpg")
    embed.set_image(url = "https://tse4.mm.bing.net/th?id=OIP.ZKsC5PG3fkhdK5D7SEOoDwHaEH&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def Le_seigneur_des_anneaux_la_communaute(ctx):
    embed = discord.Embed(title = "Voici le seigneur des anneaux: la connumauté de l'anneau", color=0xfa8072, url ="https://wiflix.land/film-ancien/10360-le-seigneur-des-anneaux-la-communaute-de-lanneau-the-lord-of-the-rings-the-fellowship-of-the-ring.html", description="Dans ce chapitre de la trilogie, le jeune et timide Hobbit, Frodon Sacquet, hérite d'un anneau. Bien loin d'être une simple babiole, il s'agit de l'Anneau Unique, un instrument de pouvoir absolu qui permettrait à Sauron, le Seigneur des ténèbres, de régner sur la Terre du Milieu et de réduire en esclavage ses peuples. À moins que Frodon, aidé d'une Compagnie constituée de Hobbits, d'Hommes, d'un Magicien, d'un Nain, et d'un Elfe, ne parvienne à emporter l'Anneau à travers la Terre du Milieu jusqu'à la Crevasse du Destin, lieu où il a été forgé, et à le détruire pour toujours. Un tel périple signifie s'aventurer très loin en Mordor, les terres du Seigneur des ténèbres, où est rassemblée son armée d'Orques maléfiques... La Compagnie doit non seulement combattre les forces extérieures du mal mais aussi les dissensions internes et l'influence corruptrice qu'exerce l'Anneau lui-même.L'issue de l'histoire à venir est intimement liée au sort de la Compagnie.")
    embed.set_thumbnail(url = "https://wiflix.tel/checkimg.php?urli=dcd2-b969-59eb-4d3a.jpg")
    embed.set_image(url = "https://tse1.mm.bing.net/th?id=OIP.kYglOFVoDgUnSYiZyc1DwwHaEK&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed =embed)

@bot.command()
async def Le_seigneur_des_anneaux_les_deux_tours(ctx):
    embed = discord.Embed(title = "Voici le seigneur des anneaux: les deux tours", color=0xfa8072, url ="https://wiflix.land/film-ancien/10122-le-seigneur-des-anneaux-les-deux-tours-the-lord-of-the-rings-the-two-towers.html", description="Après la mort de Boromir et la disparition de Gandalf, la Communauté s'est scindée en trois. Perdus dans les collines d'Emyn Muil, Frodon et Sam découvrent qu'ils sont suivis par Gollum, une créature versatile corrompue par l'Anneau. Celui-ci promet de conduire les Hobbits jusqu'à la Porte Noire du Mordor. A travers la Terre du Milieu, Aragorn, Legolas et Gimli font route vers le Rohan, le royaume assiégé de Theoden. Cet ancien grand roi, manipulé par l'espion de Saroumane, le sinistre Langue de Serpent, est désormais tombé sous la coupe du malfaisant Magicien. Eowyn, la nièce du Roi, reconnaît en Aragorn un meneur d'hommes. Entretemps, les Hobbits Merry et Pippin, prisonniers des Uruk-hai, se sont échappés et ont découvert dans la mystérieuse Forêt de Fangorn un allié inattendu : Sylvebarbe, gardien des arbres, représentant d'un ancien peuple végétal dont Saroumane a décimé la forêt...")
    embed.set_thumbnail(url = "https://wiflix.tel/checkimg.php?urli=8e12-4847-d624-4a24.jpg")
    embed.set_image(url = "https://tse2.mm.bing.net/th?id=OIP.XdI7Y33yrtZ--VKtwwxWBQHaEb&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed =embed)

@bot.command()
async def Le_seigneur_des_anneaux_le_retour_du_roi(ctx):
    embed = discord.Embed(title = "Voici le seigneur des anneaux: le retour du roi", color=0xfa8072, url ="https://wiflix.land/film-ancien/9869-le-seigneur-des-anneaux-le-retour-du-roi-the-lord-of-the-rings-the-return-of-the-king.html", description="Les armées de Sauron ont attaqué Minas Tirith, la capitale de Gondor. Jamais ce royaume autrefois puissant n'a eu autant besoin de son roi. Mais Aragorn trouvera-t-il en lui la volonté d'accomplir sa destinée ? Tandis que Gandalf s'efforce de soutenir les forces brisées de Gondor, Théoden exhorte les guerriers de Rohan à se joindre au combat. Mais malgré leur courage et leur loyauté, les forces des Hommes ne sont pas de taille à lutter contre les innombrables légions d'ennemis qui s'abattent sur le royaume... Chaque victoire se paye d'immenses sacrifices. Malgré ses pertes, la Communauté se jette dans la bataille pour la vie, ses membres faisant tout pour détourner l'attention de Sauron afin de donner à Frodon une chance d'accomplir sa quête. Voyageant à travers les terres ennemies, ce dernier doit se reposer sur Sam et Gollum, tandis que l'Anneau continue de le tenter...")
    embed.set_thumbnail(url = "https://wiflix.tel/checkimg.php?urli=a74d-0fcc-c7c3-485c.jpg")
    embed.set_image(url = "https://tse4.mm.bing.net/th?id=OIP.tTqNRzIa7RM7E8ANBJqIswHaDF&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed =embed)

@bot.command()
async def Les_animaux_fantastiques(ctx):
    embed = discord.Embed(title = "Voici Les Animaux fantastiques", color =0xfa8072, url ="https://french-stream.re/film/16412-les-animaux-fantastiques-film-streaming-complet-vf.html", description = "Détenant dans sa valise des créatures interdites, Norbert Dragonneau, un magizoologiste, arrive à New York. Il ne se doute pas que la ville est sous tension. Une secte de Non-Majs, les fidèles de Salem, appelle à traquer les sorciers, et une ombre mystérieuse et destructrice fait parfois son apparition... Alors que son niffleur kleptomane s'échappe, Norbert rencontre Jacob, un Non-Maj maladroit, et Tina, une sorcière ambitieuse et rigoureuse.")
    embed.set_thumbnail(url = "https://tse2.mm.bing.net/th?id=OIP.JfN8Kxe6MjtCtAqnKh_ErAHaKo&pid=Api&P=0&w=300&h=300")
    embed.set_image(url = "https://tse1.mm.bing.net/th?id=OIP.s6PC-rqKWGe-eI8H7XVYSAHaEK&pid=Api&P=0&w=334&h=187")
    await ctx.send(embed = embed)

@bot.command()
async def Les_animaux_fantastiques_les_crimes_de_Grindelwald(ctx):
    embed = discord.Embed(title = "Voici Les Animaux fantastiques- Les crimes de Grindelwald", color =0xfa8072, url ="https://french-stream.re/film/16547-les-animaux-fantastiques-les-crimes-de-grindelwald-film-streaming-complet-vf.html", description = "1927. Quelques mois après sa capture, le célèbre sorcier Gellert Grindelwald s'évade comme il l'avait promis et de façon spectaculaire. Réunissant de plus en plus de partisans, il est à l'origine d'attaque d'humains normaux par des sorciers et seul celui qu'il considérait autrefois comme un ami, Albus Dumbledore, semble capable de l'arrêter. Mais Dumbledore va devoir faire appel au seul sorcier ayant déjoué les plans de Grindelwald auparavant : son ancien élève Norbert Dragonneau. L'aventure qui les attend réunit Norbert avec Tina, Queenie et Jacob, mais cette mission va également tester la loyauté de chacun face aux nouveaux dangers qui se dressent sur leur chemin, dans un monde magique plus dangereux et divisé que jamais.")
    embed.set_thumbnail(url = "https://tse3.mm.bing.net/th?id=OIP.n52u9ASRXs2_TT8gaHI4NgHaK_&pid=Api&P=0&w=300&h=300")
    embed.set_image(url ="https://tse4.mm.bing.net/th?id=OIP.iNnQWB-Le-henoCbXja03AHaEK&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

#Commandes Séries
@bot.command()
async def Game_of_thrones_saison_1(ctx):
    embed = discord.Embed(title = "Voici la saison 1 de Game of thrones", color=0xfa8072, url ="https://french-stream.re/serie/15108580-game-of-thrones-saison-1-streaming-complet-vf-vostfr.html", description ="A Westeros, un continent chimérique, de puissantes familles se disputent le trône de fer, symbole de pouvoir absolu sur le royaume des Sept Couronnes. Plusieurs années après la rébellion provoquée par les ambitions aveugles d’Aerys II Targaryen, surnommé le roi fou, Robert, de la maison Baratheon, siège sur le trône tant convoité et règne sur le royaume. A la mort de Jon Arryn, son premier conseiller et mentor, Robert se rend dans le nord afin de demander à son ami d’enfance, Eddard Stark, gouverneur du Nord et Seigneur de Winterfell, de devenir la nouvelle Main du roi. De son côté, Jon Snow, le fils bâtard d’Eddard, intègre la Garde de Nuit, une ancienne confrérie dont la mission est de défendre le Mur, une immense forteresse de glace protégeant le royaume de créatures mythiques. Pendant ce temps, sur le continent d’Essos, Viserys et Daenerys, les enfants exilés de la famille Targaryen, complotent pour revenir à Westeros et reprendre le trône de fer. Entre complots, trahisons et luttes de pouvoir, le trône de fer fera l’objet de toute les convoitises.")
    embed.set_thumbnail(url = "https://tse4.mm.bing.net/th?id=OIP.W8t44OSYSVFtxvQ89OUQsgHaLH&pid=Api&P=0&w=300&h=300")
    embed.set_image(url ="https://tse4.mm.bing.net/th?id=OIP.l_ed8yxOnA-1ste1glBV4gHaEK&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def Game_of_thrones_saison_2(ctx):
    embed = discord.Embed(title = "Voici la saison 2 de Game of thrones", color=0xfa8072, url ="https://french-stream.re/serie/15108029-game-of-thrones-saison-2-streaming-complet-vf-vostfr.html", description ="Les Sept Couronnes sont en guerre, et chaque camp cherche à nouer de nouvelles alliances. Grâce au soutien de la puissante Maison Lannister, Joffrey Baratheon, héritier de Robert, détient désormais le trône de fer. Mais la légitimité de son règne est contestée alors que Stannis et Renly, les oncles du jeune roi, revendiquent également la couronne. De son côté, Robb Stark poursuit sa rébellion pour venger son père et libérer sa sœur Sensa retenue captive à Port-Réal. Au Mur, le commandant Jeor Mormont, soutenu par Jon Snow, continue de mener la Garde de Nuit face aux Sauvageons. Pendant ce temps, Daenerys Targaryen arrive à la cité de Qarth où elle espère trouver de nouveaux alliés afin de reconquérir le trône.")
    embed.set_thumbnail(url = "https://frenchstream.top/original-150e003dd9781dee58fc4e555e6a9e8d.jpg")
    embed.set_image(url ="https://fr.web.img2.acsta.net/r_1920_1080/pictures/18/06/27/06/46/2159979.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def Game_of_thrones_saison_3(ctx):
    embed = discord.Embed(title = "Voici la saison 3 de Game of thrones", color=0xfa8072, url ="https://french-stream.re/serie/170940-game-of-thrones-saison-3-streaming-complet-vf-vostfr.html", description ="La lutte pour le trône de fer continue. Joffrey Baratheon a remporté une précieuse victoire et se retrouve désormais à la tête de la plus grande armée du royaume. Sur l’île de Peyredragon, Melisandre propose à Stannis Baratheon de recourir à une puissante magie pour conquérir le trône de fer. Au même moment, Robb Stark remet en question sa stratégie, et doit décider d'un plan d'action pour remporter la victoire finale. Alors que la Garde de Nuit fait face à la menace des Marcheurs Blancs, Jon Snow infiltre les Sauvageons pour découvrir les plans de Mance Rayder. Daenerys, quant à elle, se dirige vers la ville portuaire d’Astapor afin de lever une armée.")
    embed.set_thumbnail(url = "https://frenchstream.top/original-1d455ff0b71653dabc58740ae25e74a0.jpg")
    embed.set_image(url ="https://fr.web.img2.acsta.net/r_1920_1080/pictures/18/06/27/07/07/5180558.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def Game_of_thrones_saison_4(ctx):
    embed = discord.Embed(title = "Voici la saison 4 de Game of thrones", color=0xfa8072, url ="https://french-stream.re/serie/15107650-game-of-thrones-saison-4-streaming-complet-vf-vostfr.html", description ="Après de nombreuses victoires, la maison Lannister est plus puissante que jamais et détient désormais un pouvoir absolu sur le trône de fer. Le prince Oberyn Martell arrive à Port-Réal pour revendiquer sa place au Conseil restreint, et obtenir justice pour l’assassinat de sa sœur. Alors qu’il poursuit la reconstruction de son armée à Peyredragon, Stannis Baratheon vient en aide à la Garde de Nuit pour empêcher les Sauvageons de franchir le Mur. En parallèle, Daenerys Targaryen et son armée se dirigent vers la ville de Meereen qui pourrait lui fournir une aide précieuse.")
    embed.set_thumbnail(url = "https://frenchstream.top/original-750acb2900df5ce24ac643fed2bb11b4.jpg")
    embed.set_image(url ="https://fr.web.img2.acsta.net/r_1920_1080/pictures/18/06/27/07/27/0010980.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def Squid_Game(ctx):
    embed = discord.Embed(title = "Voici la saison 1 de Squid Game", color=0xfa8072, url = "https://wiflix.land/serie-en-streaming/22150-squid-game-saison-1.html", description ="    Tentés par un prix alléchant en cas de victoire, des centaines de joueurs désargentés acceptent de s'affronter lors de jeux pour enfants aux enjeux mortels.")
    embed.set_thumbnail(url ="https://wiflix.tel/checkimg.php?urli=stream-vf-8aea-ecf0-870b-4655.jpg")
    embed.set_image(url = "https://tse3.mm.bing.net/th?id=OIP.1Je3zEFXZv020UeMibnqewHaEK&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def Peaky_Blinders_saison_1(ctx):
    embed = discord.Embed(title = "Voici la saison 1 de Peaky Blinders", color = 0x3B3C63, url = "https://wiflix.land/vf/16998-peaky-blinders-saison-1.html", description ="Dans le Birmingham industriel de l’après Grande Guerre, les anciens soldats, mais aussi les révolutionnaires et les criminels luttent pour subsister. Alors qu’une féroce révolte ouvrière est sur le point d’éclater, le Parlement anglais dépêche ses forces spéciales pour maintenir l’ordre. De leur côté, les Peaky Blinders, une organisation criminelle particulièrement redoutée dans la ville, ont pris possession par erreur d’une cargaison d’armes à feu volées. Mais l’arrivée de Chester Campbell, un policier de Belfast aux méthodes expéditives, dont la mission est de purger la ville de ses gangs sanguinaires, pourrait bien compromettre les ambitions de leur impitoyable chef, Tommy Shelby.")
    embed.set_thumbnail(url = "https://fr.web.img6.acsta.net/c_210_280/pictures/15/03/11/17/20/597260.jpg")
    embed.set_image(url = "https://tse1.mm.bing.net/th?id=OIP.Y95EYTOBq9d3hNmsgTYQvwHaEO&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def Peaky_Blinders_saison_2(ctx):
    embed = discord.Embed(title = "Voici la saison 2 de Peaky Blinders", color = 0x3B3C63, url = "https://wiflix.land/vf/16999-peaky-blinders-saison-2.html", description ="Après avoir pris le contrôle de Birmingham, la famille Shelby, plus puissante que jamais, cherche à étendre son influence. Pour obtenir une place de choix dans les courses hippiques, Tommy Shelby décide de partir à la conquête de Londres, mais Darby Sabini, le chef d’un gang local, ne compte pas laisser son territoire lui échapper, quitte à entrer en conflit ouvert. Pendant ce temps, Polly intensifie ses recherches pour retrouver son fils disparu, tandis que Chester Campbell refait surface pour tendre un piège à Tommy.")
    embed.set_thumbnail(url="https://fr.web.img3.acsta.net/c_210_280/pictures/18/03/14/14/20/1756999.jpg")
    embed.set_image(url="https://admin-blogs.lalibre.be/app/uploads/sites/2/2016/03/1099454363-1-1.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def Peaky_Blinders_saison_3(ctx):
    embed = discord.Embed(title = "Voici la saison 3 de Peaky Blinders", color = 0x3B3C63, url = "https://wiflix.land/vf/17000-peaky-blinders-saison-3.html",description = "Désormais à la tête d’un empire, Tommy, qui est devenu un homme respecté, prévoit de transformer l’entreprise criminelle familiale en un business légal. Mais lorsque les hommes de Winston Churchill lui demandent de se mêler de la révolution russe, le chef du clan Shelby se retrouve pris au piège d’un trafic international qui risque de mettre en danger toute sa famille.")
    embed.set_thumbnail(url="https://fr.web.img3.acsta.net/c_210_280/pictures/18/03/14/14/20/1888249.jpg")
    embed.set_image(url="https://images.critictoo.com/wp-content/uploads/2017/06/Peaky-Blinders-Saison-3.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def Peaky_Blinders_saison_4(ctx):
    embed = discord.Embed(title = "Voici la saison 4 de Peaky Blinders", color = 0x3B3C63, url = "https://wiflix.land/vf/15943-peaky-blinders-saison-4.html", description = "Un an s’est écoulé depuis la dislocation du clan Shelby. Séparé de sa famille, Tommy est désormais un homme seul qui se concentre uniquement sur ses affaires. La veille de Noël, l’ancien gangster reçoit une mystérieuse lettre et réalise que les Peaky Blinders sont en danger. Alors que la mafia new-yorkaise est déterminée à se venger, Tommy fuit la campagne pour retourner dans les rues de Birmingham. Pour se défendre et préparer l'offensive, il devra rassembler ses proches et mettre de côté les querelles familiales.")
    embed.set_thumbnail(url="https://fr.web.img2.acsta.net/c_210_280/pictures/18/03/14/14/20/2069499.jpg")
    embed.set_image(url="https://static1.purebreak.com/articles/8/13/73/08/@/569248-peaky-blinders-saison-4-adrien-brody-m-opengraph_1200-1.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def Peaky_Blinders_saison_5(ctx):
    embed = discord.Embed(title = "Voici la saison 5 de Peaky Blinders", color = 0x3B3C63, url = "https://wiflix.land/vf/16422-peaky-blinders-saison-5.html", description = "Tommy Shelby restera-t-il député du Labour ? Alors que l’Angleterre plonge dans la crise de 1929 et voit monter le péril totalitaire, le chef des Peaky Blinders prend des décisions qui vont affecter la nation tout entière.")
    embed.set_thumbnail(url="https://fr.web.img2.acsta.net/c_210_280/pictures/19/12/16/20/51/5072603.jpg")
    embed.set_video(url="https://www.youtube.com/watch?v=OU1iZoOrkVo")
    await ctx.send(embed = embed)

@bot.command()
async def This_is_us_saison_1(ctx):
    embed = discord.Embed(title = "Voici la saison 1 de This is us", color = 0xfa8072, url = "https://wiflix.land/vf/18882-this-is-us-saison-1.html")
    embed.set_thumbnail(url="")
    embed.set_image(url="")
    await ctx.send(embed = embed)

@bot.command()
async def This_is_us_saison_2(ctx):
    embed = discord.Embed(title = "Voici la saison 2 de This is us", color = 0xfa8072, url = "https://wiflix.land/vf/18883-this-is-us-saison-2.html")
    embed.set_thumbnail(url="")
    embed.set_image(url="")
    await ctx.send(embed = embed)

@bot.command()
async def This_is_us_saison_3(ctx):
    embed = discord.Embed(title = "Voici la saison 3 de This is us", color = 0xfa8072, url = "https://wiflix.land/serie-en-streaming/15952-this-is-us-saison-3.html")
    embed.set_thumbnail(url="")
    embed.set_image(url="")
    await ctx.send(embed = embed)

@bot.command()
async def This_is_us_saison_4(ctx):
    embed = discord.Embed(title = "Voici la saison 4 de This is us", color = 0xfa8072, url = "https://wiflix.land/serie-en-streaming/15800-this-is-us-s-4.html")
    embed.set_thumbnail(url="")
    embed.set_image(url="")
    await ctx.send(embed = embed)

@bot.command()
async def This_is_us_saison_5(ctx):
    embed = discord.Embed(title = "Voici la saison 5 de This is us", color = 0xfa8072, url = "https://wiflix.land/serie-en-streaming/19661-this-is-us-saison-5.html")
    embed.set_thumbnail(url="")
    embed.set_image(url="")
    await ctx.send(embed = embed)

@bot.command()
async def Sugar_rush_saison_1(ctx):
    embed = discord.Embed(title = "Voici la saison 1 de Sugar rush", color = 0xfa8072, url = "https://french-stream.re/serie/165662-serie-sugar-rush-saison-1-stream-complet-vf.html")
    embed.set_thumbnail(url="")
    embed.set_image(url="")
    await ctx.send(embed = embed)

@bot.command()
async def Sugar_rush_saison_2(ctx):
    embed = discord.Embed(title = "Voici la saison 2 de Sugar rush", color = 0xfa8072, url = "https://french-stream.re/serie/1510668-sugar-rush-nol-sugar-rush-christmas-saison-2.html")
    embed.set_thumbnail(url="")
    embed.set_image(url="")
    await ctx.send(embed = embed)

@bot.command()
async def Sugar_rush_saison_3(ctx):
    embed = discord.Embed(title = "Voici la saison 3 de Sugar rush", color = 0xfa8072, url = "https://french-stream.re/serie/1496834-sugar-rush-saison-3.html")
    embed.set_thumbnail(url="")
    embed.set_image(url="")
    await ctx.send(embed = embed)


#Commandes Animés
@bot.command()
async def Assassination_classroom_saison_1(ctx):
    embed = discord.Embed(title = "Voici la saison 1 de Assassination Classroom")
    embed.set_thumbnail(url="")
    embed.set_image(url="")
    await ctx.send(embed = embed)

@bot.command()
async def Death_Note(ctx):
    embed = discord.Embed(title = "Voici Death Note", color = 0xfa8072, url = "https://vostfree.tv/802-death-note-vf-ddl-streaming.html")
    embed.set_thumbnail(url="")
    embed.set_image(url="")
    await ctx.send(embed = embed)

@bot.command()
async def Le_tombeau_des_lucioles(ctx):
    embed = discord.Embed( title = "Voici le tombeau des lucioles", color=0xfa8072, url ="https://ok.ru/video/317146860173", description = "Japon, été 1945. Après le bombardement de Kobé, Seita, un adolescent de quatorze ans et sa petite soeur de quatre ans, Setsuko, orphelins, vont s'installer chez leur tante à quelques dizaines de kilomètres de chez eux. Celle-ci leur fait comprendre qu'ils sont une gêne pour la famille et doivent mériter leur riz quotidien. Seita décide de partir avec sa petite soeur. Ils se réfugient dans un bunker désaffecté en pleine campagne et vivent des jours heureux illuminés par la présence de milliers de lucioles. Mais bientôt la nourriture commence cruellement à manquer.")
    embed.set_thumbnail(url = "https://tse3.mm.bing.net/th?id=OIP.srkIPEKDSVOeF50ILKEAZQHaKj&pid=Api&P=0&w=300&h=300")
    embed.set_image(url = "https://tse4.mm.bing.net/th?id=OIP.1cKgqLaaG9OgLZlek0mChQHaEK&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def Angel_Beats(ctx):
    embed = discord.Embed( title = "Voici Angel Beats", color = 0xfa8072, url = "https://vostfree.tv/204-angel-beats-vf-ddl-streaming-1fichier-uptobox.html", description = "Amnésique, Otonashi se réveille dans un lieu qui lui est inconnu. À peine conscient, une jeune fille nommée Yuri lui annonce de but en blanc qu'il est mort et qu'il se trouve dans l'au-delà. Cette dernière se présente comme le leader d'un groupe d'opposants tentant de défier les Dieux par les armes afin de se venger des souffrances qu'ils ont endurées dans leur vie antérieure. Bien que sceptique au premier abord, Otonashi découvrira qu'il ne peut mourir dans ce nouveau monde et que le conflit virulent confrontant l'équipe de Yuri à un ange est bel et bien réel. En quête de ses souvenirs, il s'engagera alors dans cette bataille qui paraît sans fin.")
    embed.set_thumbnail(url = "https://tse2.mm.bing.net/th?id=OIP.L-Fia7i-3pdCqw4ZVdoApgHaK6&pid=Api&P=0&w=300&h=300")
    embed.set_image(url ="https://tse2.mm.bing.net/th?id=OIP.TEhyuQFG51Iz0Nx-9Pn0ywHaFj&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def Worlds_finest_assassin(ctx):
    embed = discord.Embed( title = "Voici World's finest Assassin", color=0xfa8072, url = "https://vostfree.tv/1104-the-world-s-finest-assassin-gets-reincarnated-in-another-world-as-an-aristocrat-vf-ddl-streaming-1fichier-uptobox.html", description = "L'assassin numéro un au monde s'est réincarné en fils aîné d'une famille d'assassins aristocrates. En échange de sa réincarnation dans un autre monde, une déesse lui a imposé une condition. Tuez le héros qui est prophétisé pour détruire le monde. Ce devait être la mission de sa nouvelle vie. L'effet synergique des vastes connaissances et de l'expérience qu'il a acquises qui ont rendu possibles toutes sortes d'assassinats dans le monde moderne, ainsi que les techniques secrètes et la magie de la famille d'assassins la plus puissante du monde fantastique font de lui le plus grand assassin de tous les temps.")
    embed.set_thumbnail(url ="https://tse2.mm.bing.net/th?id=OIP.Co__J-K3thTlS6ECTJvqywHaLG&pid=Api&P=0&w=300&h=300")
    embed.set_image(url = "https://tse2.mm.bing.net/th?id=OIP.iHDDOD6v3fozQUgu8tamKgHaDt&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def Tokyo_revengers(ctx):
    embed = discord.Embed( title = "Voici Tokyo Revengers",color=0xfa8072, url = "https://vostfree.tv/1021-tokyo-revengers-vf-ddl-streaming-1fichier-uptobox.html", description = "À 26 ans, Takemichi a le sentiment d'avoir déjà raté sa vie. Vivotant de petits boulots ingrats tout juste bons à payer le loyer d'un studio miteux, il se lamente sur le désert de sa vie amoureuse lorsqu'il apprend la mort de Hinata, la seule petite amie qu'il ait eue... La jeune fille et son frère ont été les victimes collatérales d'un règlement de comptes entre les membres d'un gigantesque gang, le Tokyo Manji-kai. Encore sous le choc, Takemichi est à son tour victime d'un accident qui le ramène inexplicablement 12 ans en arrière, lorsqu'il était au collège et se donnait des airs de mauvais garçon. Et si c'était pour lui l'occasion de sauver Hinata ? Mais en tentant de modifier le futur, Takemichi se retrouvera inexorablement mêlé aux complots se tramant autour du Tokyo Manji-kai et de son charismatique et mystérieux leader...")
    embed.set_thumbnail(url = "https://tse3.mm.bing.net/th?id=OIP.3qq3ePwZ_WTuO3U9rJjdrgHaKj&pid=Api&P=0&w=300&h=300")
    embed.set_image(url ="https://tse4.mm.bing.net/th?id=OIP.TJ4l4H402DQGxAMjpoWsuwHaD5&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def yakusoku_no_neverland_saison_1(ctx):
    embed = discord.Embed(title = "Voici la saison 1 de yakusoku no neverland", color=0xfa8072, url = "https://vostfree.tv/804-yakusoku-no-neverland-vf-ddl-streaming-1fichier-uptobox.html", description ="Nous suivons le quotidien de Emma et de ses camarades qui vivent tous dans un étrange orphelinat. Les gouvernantes, qui s’occupent d’eux, les forment à exploiter pleinement leur capacité intellectuelle. Mais une seule règle régit ce petit lieu : Interdiction de sortir de l’enceinte de l’établissement. Bien qu’ils mènent une vie agréable, Emma et ses amis vont découvrir que les enfants « adoptés » connaissent un sombre sort et que ces femmes qui s’occupent d’eux ne le font pas pour leur bien être mais pour servir des monstres particulièrement machiavéliques et ingénieux… Dorénavant chaque jour devient une mission pour trouver des informations sur leur situation et tenter de sauver chaque résident.")
    embed.set_thumbnail(url ="https://vostfree.tv/uploads/posts/2020-03/1583118834_the-promised-neverland-vf.jpg")
    embed.set_image(url ="https://tse1.mm.bing.net/th?id=OIP.-ScTxuyBtflFQ9hXq2SoZwHaEK&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)


@bot.command()
async def Piano_no_Mori_saison_1(ctx):
    embed = discord.Embed(title = "Voici la saison 1 de Piano no Mori", color=0xfa8072, url = "https://vostfree.tv/400-piano-no-mori-vf-ddl-streaming-1fichier-uptobox.html", description ="Nous suivons l’amitié à travers les années de Shuhei Amamiya, un adolescent destiné à devenir un pianiste professionnel, et de l’énigmatique Ichinose Kai. C’est dans sa nouvelle école primaire en province que Shuhei entend parler d’une légende ; Au fin fond d’une forêt existerait un piano magique. Shuhei et son camarade de classe Kai partent à sa recherche. C’est en trouvant le vieux piano que Shuhei découvre les talents innés de Kai sans avoir pris une seule leçon. Bien que l’amitié des 2 garçons soient inébranlables depuis lors, ils participent au même concours national de piano qui fera naître leur première rivalité…")
    embed.set_thumbnail(url ="https://vostfree.tv/uploads/posts/2018-10/1539258565_piano-no-mori-vf-2018-anime-.jpg")
    embed.set_image(url ="https://tse1.mm.bing.net/th?id=OIP.L-InSJhyzXIyWrnGMBYW3AHaD4&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

@bot.command()
async def Piano_no_Mori_saison_2(ctx):
    embed = discord.Embed(title = "Voici la saison 2 de Piano no Mori", color=0xfa8072, url = "https://vostfree.tv/661-piano-no-mori-saison-2-vf-ddl-streaming-1fichier-uptobox.html", description ="Nous suivons l’amitié à travers les années de Shuhei Amamiya, un adolescent destiné à devenir un pianiste professionnel, et de l’énigmatique Ichinose Kai. C’est dans sa nouvelle école primaire en province que Shuhei entend parler d’une légende ; Au fin fond d’une forêt existerait un piano magique. Shuhei et son camarade de classe Kai partent à sa recherche. C’est en trouvant le vieux piano que Shuhei découvre les talents innés de Kai sans avoir pris une seule leçon. Bien que l’amitié des 2 garçons soient inébranlables depuis lors, ils participent au même concours national de piano qui fera naître leur première rivalité…")
    embed.set_thumbnail(url ="https://vostfree.tv/uploads/posts/2018-10/1539258565_piano-no-mori-vf-2018-anime-.jpg")
    embed.set_image(url ="https://tse1.mm.bing.net/th?id=OIP.L-InSJhyzXIyWrnGMBYW3AHaD4&pid=Api&P=0&w=300&h=300")
    await ctx.send(embed = embed)

#commandes slash


#Commandes jeux

#@bot.command()
#async def choix(ctx):
 #   buttons = [
  #      create_button(
   #         style=ButtonStyle.blue,
    #        label="Choisissez moi",
     #       custom_id="oui"
      #  ),
       # create_button(
           # style=ButtonStyle.danger,
            #label="SURTOUT PAS MOI!!!",
            #custom_id="non"
        #)
    #]
    #action_row = create_actionrow(*buttons)
    #fait_choix = await ctx.send("Faites votre choix !", components=[action_row])

    #def check(m):
     #   return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

    #button_ctx = await wait_for_component(bot, components=action_row, check=check)
    #if button_ctx.custom_id == "oui":
     #   await button_ctx.edit_origin(content="Bravo !")
    #else:
     #   await button_ctx.edit_origin(content="...")

#@bot.command()
#async def quiz(ctx):
 #   select = create_select(
  #      options=[
   #         create_select_option("Haha tRoP mArRaNt lOl", value="1", emoji="😂"),
    #        create_select_option("...", value="2", emoji="😏"),
     #       create_select_option("friendzone", value="3", emoji="💛"),
      #      create_select_option("renard", value="4", emoji="🦊")
      #  ],
       # placeholder="Choisis un emoji...",
        #min_values=1,
       # max_values=1
    #)
    #fait_choix = await ctx.send("Quel est le meilleur emoji de tout les temps ?", components=[create_actionrow(select)])

    #def check(m):
    #    return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

    #choice_ctx = await wait_for_component(bot, components=select, check=check)

    #if choice_ctx.values[0] == "4":
     #   await choice_ctx.send("Bonne réponse ! 🦊")
    #else:
     #   await choice_ctx.send("Mauvaise réponse... 😒")



@bot.command()
async def dire(ctx, *message):
    await ctx.send(" ".join(message))

@bot.command()
async def acheter(ctx):
    await ctx.send("Entrer le nom du produit que vous voulez acheter")
    def check_Message(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel
    try:
        produit = await bot.wait_for("message", timeout = 10, check = check_Message)
    except:
        await ctx.send("Veuillez réitérer la commande.")
        return
    message = await ctx.send(f"La préparation de {produit.content} va commencer. Veuillez valider en réagissant avec oui. Sinon réagissez avec ? pour annuler l'achat")
    await message.add_reaction("oui")
    await message.add_reaction("?")

@commands.command(name='8ball', description='Let the 8 Ball Predict!\n')
async def _8ball(self, ctx, question):
    responses = ['A ce que je vois, oui.',
             'oui.',
             'non',
             'Absolument pas',
             'personnellement non',
             'Most Likley.',
             'Chances High',
             'No.',
             'Negative.',
             'Not Convinced.',
             'Perhaps.',
             'Not Sure',
             'Mayby',
             'I cannot predict now.',
             'Im to lazy to predict.',
             'I am tired. *proceeds with sleeping*']
    response = random.choice(responses)
    embed=discord.Embed(title="The Magic 8 Ball has Spoken!")
    embed.add_field(name='Question: ', value=f'{question}', inline=True)
    embed.add_field(name='Answer: ', value=f'{response}', inline=False)
    await ctx.send(embed=embed)
    #@bot.command()
    #async def checker_Emoji(reaction, user):
        #return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "?" or str(reaction.emoji) == "?")
        #try:
         #   reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = checker_Emoji)    
        #if reaction.emoji == "oui":
         #   await ctx.send("Passez à la caisse .")
        #else:
          #  await ctx.send("Votre demande d'achat a bien été annulé.")
           # except:
            #    await ctx.send("Votre demande d'achat bien été annulé.")
bot.run("OTA4NzkwMDE5ODk0OTY0MjQ0.YY62qQ.MFMNTG_qqmbFlOHmD2pNmHCj1Mo") 