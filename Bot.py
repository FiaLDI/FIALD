import discord
import json
import requests
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hi(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Приветствую, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def calculate(ctx, arg):  # создаем асинхронную фунцию бота
    try:
        await ctx.send(eval(arg))  # отправляем обратно аргумент
    except:
        await ctx.send('Операция невозможна')


@bot.command()
async def sait(ctx):
    embed = discord.Embed(
        title="Тык для перехода",
        description="Ссылка для перехода на гайд",
        url='https://wowtbc.gg/class-rankings/pve-rankings',
    )
    await ctx.send(embed=embed)

@bot.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random dog') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random cat') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random fox') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed



bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена