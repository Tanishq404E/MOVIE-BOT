import discord
import random
#replace the world token with your discord bot token
my_secret = "TOKEN"
Horror=["1922","Alive (2020)","Apostle (2018)","Army of the Dead (2021)","Berlin Syndrome (2017)","The Conjuring (2013)","The Conjuring 2 (2016)","Creep (2014)","Fear Street (2021)(trilogy)","Hush (2016)","*Jaws (1975)","Pan’s Labyrinth (2006)"]
thriller=[" Venom: Let There Be Carnage (2021)","I See You (2019)","Red Dragon (2002)","Mulholland Drive (2001)","thesis","Buried (2010)","Run(2020)","The Revenant(2015)","Panic Room(2002)"]
adventure=["Free Guy (2021)","Black Widow (2021)","Shang-Chi and the Legend of the Ten Rings","Skyfall (2012)","THE THREE MUSKETEERS (1921)","THE WIZARD OF OZ (1939)","Star Wars: Episode VII - The Force Awakens (2015)","War for the Planet of the Apes (2017)","Shazam! (2019)","The Jungle Book (2016)","Mission: Impossible Rogue Nation (2015)","Harry Potter and the Deathly Hallows - Part 2 (2011)","Star Trek (2009)"]
animated=["Kubo and the two strings","Aladdin", "Lion King","Bambi","Megamind","Hotel Transylvania 1","Hotel Transylvania 2","Hotel Transylvania 3","Big Hero 6","Toy Story 1","Toy Story 2","Toy Story 3","Toy Story 4","Justice Leaugue Dark","Justice League Dark: Apokolips War"]
romcom=["Just go for it","17 again","New Year's Eve","La La Land","You've got mail","Music and Lyrics","The Holiday","Roxanne","Sleepless in Seattle","When Harry met Sally","Crazy Rich Asians","Tanu weds Manu","Varane Avashyamund","Kannum Kannum Kollaiyadithaal","qarib qarib singlle"]
all_movies=Horror+thriller+adventure+animated+romcom
client = discord.Client()
@client.event
async def on_read():
  print("Bot logged in as{0.user}".format(client))
@client.event
async def on_message(msg):
  if msg.author==client.user:
    return
  if msg.content.startswith('!movies-horror'):
    await msg.channel.send(random.choice(Horror))
  elif msg.content.startswith('!movies-thriller'):
    await msg.channel.send(random.choice(thriller))
  elif msg.content.startswith('!movies-adventure'):
    await msg.channel.send(random.choice(adventure))
  elif msg.content.startswith('!movies-animated'):
    await msg.channel.send(random.choice(animated))
  elif msg.content.startswith('!movies-romcom'):
    await msg.channel.send(random.choice(romcom))
  elif msg.content.startswith('!movies'):
    await msg.channel.send(random.choice(all_movies)) 
client.run(my_secret)