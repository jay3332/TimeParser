# TimeParser
Time parser for Python. 
### Example Usage
```py
import timeparser

print(timeparser.parse("in 4s"))
```
### Example Usage (Discord Bot)
```py
import timeparser
from discord.ext import commands

bot = commands.Bot("!")

@bot.command()
async def parse_time(ctx, *, time: timeparser.TimeConverter):
  await ctx.send(f"This time is {time} in the {time.direction}.")

bot.run("TOKEN")
```
