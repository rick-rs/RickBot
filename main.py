https://RickBot.kadolthar.repl.co
import discord
import os
import requests
import json
from keep_alive import keep_alive
from deep_translator import GoogleTranslator

client = discord.Client()


def translate(text, to):
	translated = GoogleTranslator(source='english', target=to).translate(text)
	return translated

def get_json_response(link):
	response = requests.get(link)
	json_data = json.loads(response.text)
	return json_data


def get_quote():
	json_data = get_json_response('https://zenquotes.io/api/random/')
	quote = json_data[0]['q']
	author = json_data[0]['a']
	return f'{translate(quote, to="portuguese")} - {author}'


@client.event
async def on_ready():
	print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
	msg = message.content
	if message.author == client.user:
		return

	if msg.startswith('$motivacional'):
		quote = get_quote()
		await message.channel.send(quote)


keep_alive()
client.run(os.environ['TOKEN'])
