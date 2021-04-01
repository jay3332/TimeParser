import os
import asyncio
from discord.ext import commands
from timeparser import TimeConverter

TOKEN = os.environ['TOKEN']


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            case_insensitive=True
        )

    def run(self):
        super().run(TOKEN)


bot = Bot()


@bot.command()
async def remind(ctx, *, time: TimeConverter):
    await ctx.send(f"Okay, reminding you about {time.reason} in {time}.")
    await asyncio.sleep(time.raw_delta)
    await ctx.send(f"{ctx.author.mention}, {time} ago you wanted me to remind you about {time.reason}.")


if __name__ == '__main__':
    bot.run()
