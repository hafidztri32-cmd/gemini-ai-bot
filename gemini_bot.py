import discord
from discord.ext import commands
from google import genai
import os

# ====== Setup Gemini API ======
client_gemini = genai.Client()
MODEL_ID = "gemini-2.5-flash"

# ====== Setup Discord Bot ======
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ====== Event: Bot siap ======
@bot.event
async def on_ready():
    print(f"Bot sudah online sebagai {bot.user}")

# ====== Command !ask ======
@bot.command()
async def ask(ctx, *, question):
    """Bertanya ke Gemini AI"""
    try:
        response = client_gemini.models.generate_content(
            model=MODEL_ID,
            contents=question
        )
        await ctx.send(response.text)
    except Exception as e:
        await ctx.send(f"Ada kesalahan: {e}")

# ====== Command !helpme ======
@bot.command()
async def helpme(ctx):
    """Menampilkan daftar command"""
    help_text = """
    **Command Bot Gemini Discord**
    !ask <pertanyaan> → Bertanya ke Gemini AI
    !helpme → Menampilkan bantuan
    """
    await ctx.send(help_text)

# ====== Menjalankan bot ======
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(DISCORD_TOKEN)
