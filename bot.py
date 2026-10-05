import discord
import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$sugal'):
            results = random.choices(symbols, k=3)
            slot_display = f"{results[0]} | {results[1]} | {results[2]}"

            if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
                outcome = "🎉 *JACKPOT!* 💰 Galeng mo talaga busseng!"
            else:
                outcome = "Sayang busseng! Puro sugal yarn?"

            await message.channel.send(f"{slot_display}\n{outcome}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTU********************CENSORED DISCORD TOKEN')
