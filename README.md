# TimeParser
Time parser for Python. 
### Example Usage
```py
import timeparser

print(timeparser.parse("in 4s"))
```
### Example Usage (Discord Bot)
```py
import discord
import timeparser

client = discord.Client()

@client.event
async def on_message(message):
  if message.author.bot:
    return
  if parsed := timeparser.parse(message.content):
    print(parsed)
    print(repr(parsed))

client.run("TOKEN")
```
