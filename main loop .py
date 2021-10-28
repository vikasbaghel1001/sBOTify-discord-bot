@client.event
async def on_ready():
  print('we have logged in as {0.user}'. format(client))

@client.event
async def on_message(message):
  if message.author == client .user:
    return

  msg = message.content
  options = start_engoragements
  if "encoragements" in db.keys():
    options = options + db["encoragements"].value

  if any (words0 in msg for words0 in starters ):
     await message.channel.send('hello , how are you ')   

  if message.content.startswith('@motivate'):
    quote = get_quote()
    await message.channel.send(quote) 

  
  if message.content.startswith('@jokes') :
    await message.channel.send(random.choice(pj))
  
  if message.content.startswith('@funny') :
    await message.channel.send(random.choice(random_jokes))

  if message.content.startswith('@bored'):
     activity = get_activity()
     await message.channel.send(activity)
  
   
  if message.content.startswith('@functions'): 
     await message.channel.send('@motivate - gives you a motivation quote') 
     await message.channel.send('@jokes / @funny - gives you a fuuny joke') 
     await message.channel.send('@bored - gives you a random suggestion') 
     await message.channel.send('@new  -  you can add a new encoraging message') 
     await message.channel.send('@del  -  you can delete the newly adddd encoraging message') 

  
    
  if any (word in msg for word in sad_words) :
    await message.channel.send(random.choice(options))   

  if any (words in msg for words in normal_words ):
     await message.channel.send('yes , you are the best person')

  
  if any (words2 in msg for words2 in thanks_words ):
     await message.channel.send('welcome , take care and have a nice day')      
  
  if msg.startswith("@new"):
    encouraging_message = msg.split("@new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("@del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("@del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
    await message.channel.send( " encouraging message deleted")
    await message.channel.send( " Use @new command to add new encouraging message")
