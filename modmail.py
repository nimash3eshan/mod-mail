import discord, asyncio, random
from itertools import cycle
import aiohttp
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
all_intents = []
if intents.bans:
    all_intents.append("bans = True")
else:
    all_intents.append("bans = False")
if intents.dm_messages:
    all_intents.append("dm_messages = True")
else:
    all_intents.append("dm_messages = False")
if intents.dm_reactions:
    all_intents.append("dm_reactions = True")
else:
    all_intents.append("dm_reactions = False")
if intents.dm_typing:
    all_intents.append("dm_typing = True")
else:
    all_intents.append("dm_typing = False")
if intents.emojis:
    all_intents.append("emojis = True")
else:
    all_intents.append("emojis = False")
if intents.guild_messages:
    all_intents.append("guild_messages = True")
else:
    all_intents.append("guild_messages = False")
if intents.guild_reactions:
    all_intents.append("guild_reactions = True")
else:
    all_intents.append("guild_reactions = False")
if intents.guild_typing:
    all_intents.append("guild_typing = True")
else:
    all_intents.append("guild_typing = False")
if intents.guilds:
    all_intents.append("guilds = True")
else:
    all_intents.append("guilds = False")
if intents.integrations:
    all_intents.append("integrations = True")
else:
    all_intents.append("integrations = False")
if intents.invites:
    all_intents.append("invites = True")
else:
    all_intents.append("invites = False")
if intents.members:
    all_intents.append("members = True")
else:
    all_intents.append("members = False")
if intents.messages:
    all_intents.append("messages = True")
else:
    all_intents.append("messages = False")
if intents.presences:
    all_intents.append("presences = True")
else:
    all_intents.append("presences = False")
if intents.reactions:
    all_intents.append("reactions = True")
else:
    all_intents.append("reactions = False")
if intents.typing:
    all_intents.append("typing = True")
else:
    all_intents.append("typing = False")
if intents.value:
    all_intents.append("value = True")
else:
    all_intents.append("value = False")
if intents.voice_states:
    all_intents.append("voice_states = True")
else:
    all_intents.append("voice_states = False")
if intents.webhooks:
    all_intents.append("webhooks = True")
else:
    all_intents.append("webhooks = False")
print(f"Intents: {all_intents}\n")

client = discord.Client(intents=intents)
client=commands.Bot(command_prefix='!!',intents=intents)

verboten = ["arsch", "penis", "fuck"]
katze = ["```කැම්පස් කියන්නෙ සෙලවෙන මනස පුතා!```", "```අවුරුදු 40 දී විතර කැම්පස් අවුට් වෙන්න පුලුවන් 🔥!```", "```සර් අපිව කැම්පස් ගන්නවා ලගදීම බය වෙන්න එපා \U0001f648: !```"]
fights = ["fight1.gif", "fight2.gif", "fight3.gif", "fight4.gif", "fight5.gif", "fight6.gif", "fight7.gif", "fight8.gif", "fight9.gif"]
status = ["Rise Of Kingdom Srilanka", "Reports , Mails & Ideas", "For more help Contact Eshan💚🥦🍏🥎🎄#6666"]
status2 = [0, 1, 2]
status3 = [discord.Status.online, discord.Status.idle, discord.Status.dnd]
modmail_mods = [689935084027248641]

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    msgs2 = cycle(status2)
    msgs3 = cycle(status3)

    while True:
        current_status = next(msgs)
        current_status2 = next(msgs2)
        current_status3 = next(msgs3)
        if current_status == "Rise Of Kingdom Srilanka":
            await client.change_presence(activity=discord.Game(name=current_status), status=discord.Status.online)
            await asyncio.sleep(10)

        if current_status == "Reports , Mails & Ideas":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Reports , Mails & Ideas"), status=discord.Status.idle)
            await asyncio.sleep(10)

        if current_status == "For more help Contact Eshan💚🥦🍏🥎🎄#6666":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="For more help Contact Eshan💚🥦🍏🥎🎄#6666"), status=discord.Status.dnd)
            await asyncio.sleep(10)



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return

    if type(message.channel) == discord.DMChannel:
        if message.content.startswith("!reply") and message.author.id in modmail_mods:
            name = message.content.replace("!reply ", "")
            namel = name.split()
            id1 = int(namel[0])
            id2 = int(namel[1])
            name = name.replace(namel[0], "")
            name = name.replace(namel[1], "")
            to = await client.fetch_user(id1)
            msg = await to.fetch_message(id2)
            name = name.lstrip()
            await message.author.send(f"messege send {to} moderators!")
            mmangehängt = message.attachments
            try:
                try:
                    bild1 = mmangehängt[0]
                    bild1 = bild1.url
                    embed = discord.Embed(title="Message from the moderators:", description=f"{name}\n{bild1}")
                except:
                    embed = discord.Embed(title="Message from the moderators:", description=name)
                await msg.reply(embed=embed)
            except:
                await message.author.send("Not possible!")
            return

        embed = discord.Embed(title="Thank you for your message!")
        try:
            await message.channel.send(embed=embed)
        except:
            return
        mmangehängt = message.attachments
        try:
            bild1 = mmangehängt[0]
            bild1 = bild1.url
            mod1 = await client.fetch_user(689935084027248641)
            embed = discord.Embed(title="New ModMail request", description=f"{message.content}\n{bild1}")
            embed.add_field(name=f"by {message.author} ({message.author.id})", value=f"!reply {message.author.id} {message.id}")
            await mod1.send(embed=embed)
        except:
            mod1 = await client.fetch_user(689935084027248641)
            embed = discord.Embed(title="New ModMail request", description=f"{message.content}")
            embed.add_field(name=f"by {message.author} ({message.author.id})", value=f"!reply {message.author.id} {message.id}")
            await mod1.send(embed=embed)
        return

    content_raw = message.content.lower()
    for word in verboten:
        if word in content_raw:
            await message.delete()
            msg = await message.channel.send(f"Hey, the word {word} is not allowed!")
            await asyncio.sleep(5)
            await msg.delete()

    if "discord.gg" in message.content:
        await message.delete()
        msg = await message.channel.send(f"Hey, Invitations are not allowed!")
        await asyncio.sleep(5)
        await msg.delete()
    
    if message.content.startswith("hello"):
        await message.reply("```hello!```")

    if message.content.startswith("test"):        #836956144278175764 = Modmail Mod
        if not discord.utils.get(message.author.roles, id=836956144278175764) is None:
            await message.reply("```This is just a test!```")

    if message.content.startswith("embed"):
        embed = discord.Embed(title="```Ein Embed!```", description="is much nicer!", color=0x4b49d8)
        embed.set_footer(text="Footer!")
        embed.set_image(url="https://i.stack.imgur.com/zeJPU.png")
        embed.set_thumbnail(url="https://images.idgesg.net/images/article/2017/07/random-vladimer_shioshvili-100729292-large.jpg")
        embed.set_author(name="hello World!")
        embed.add_field(name="Field 1", value="Wert 1", inline=False)
        embed.add_field(name="Field 2", value="Wert 2", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("clear"):
        if not discord.utils.get(message.author.roles, id=836956144278175764) is None:
            anzahl = message.content.replace("clear ", "")
            try:
                del_msgs = await message.channel.purge(limit=int(anzahl)+1)
                embed = discord.Embed(title=f"{len(del_msgs)-1} Messages have been deleted!", color=0x9b9ae5)
                msg = await message.channel.send(embed=embed)
                await asyncio.sleep(3)
                await msg.delete()
            except:
                embed = discord.Embed(title="Invalid number!", color=0xf30c01)
                msg = await message.channel.send(embed=embed)
                await asyncio.sleep(3)
                await msg.delete()
        else:
            await message.channel.send("```Not right!```")

    if message.content.startswith("campus"):
        antwort = random.choice(katze)
        msg = await message.channel.send(antwort)
        await msg.add_reaction("😆") 

    if message.content.startswith("fight"):
        selected = random.choice(fights)
        try:
            selector = message.mentions[0]
        except:
            await message.channel.send("```Please mention someone!```")
            return
        await message.channel.send(f"{message.author.name} fight against {selector.name}.", file=discord.File(selected, filename="fight.gif"))

    if message.content.startswith("info"):
        try:
            m = message.mentions[0]
            embed = discord.Embed(title=m.name, color=0x00ffe0)
            embed.add_field(name="Joined on", value=m.joined_at, inline=False)
            embed.add_field(name="Account created on", value=m.created_at, inline=False)
            embed.add_field(name="Name#tag", value=m, inline=False)
            embed.add_field(name="ID", value=m.id, inline=False)
            embed.add_field(name="Nick", value=m.nick, inline=False)
            embed.add_field(name="Highest rank", value=m.top_role, inline=False)
            await message.channel.send(embed=embed)
        except:
            embed = discord.Embed(title=message.author.name, color=0x00ffe0)
            embed.add_field(name="Joined on", value=message.author.joined_at, inline=False)
            embed.add_field(name="Account created on", value=message.author.created_at, inline=False)
            embed.add_field(name="Name#tag", value=message.author, inline=False)
            embed.add_field(name="ID", value=message.author.id, inline=False)
            embed.add_field(name="Nick", value=message.author.nick, inline=False)
            embed.add_field(name="Highest rank", value=message.author.top_role, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith("webhook"):
        nachricht = message.content.replace("webhook ", "")
        nachrichtl = nachricht.split()
        url = nachrichtl[0]
        nachrichtl.remove(url)
        text = nachricht.replace(url, "")
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(url, adapter=discord.AsyncWebhookAdapter(session))
            await webhook.send(text, username=message.author.name)

    if message.content.startswith("xwebhook"):
        nachricht = message.content.replace("xwebhook ", "")
        for webhook in await message.channel.webhooks():
            if webhook.name == "WH":
                await webhook.send(nachricht, username=message.author.name)



client.loop.create_task(change_status())
client.run("ODM1NjIwMDgyMjg5NDc1NjU0.YISF2A.qO2XqJT-JKo0Ewx1FwbepB7z-RE")
