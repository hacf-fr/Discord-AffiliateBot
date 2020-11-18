# bot.py
import gettext
import os
import re
import urllib.parse

import discord
from dotenv import load_dotenv

load_dotenv()

try:
    traduction = gettext.translation('discord_affiliatebot', localedir='locale')
    traduction.install()
except FileNotFoundError:
    traduction = gettext.translation('discord_affiliatebot', localedir='locale', languages=["en"])
    traduction.install()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
AMAZON_TAG = os.getenv('AMAZON_TAG')
ALIEXPRESS_TAG = os.getenv('ALIEXPRESS_TAG')
COMMUNITY = os.getenv('COMMUNITY')

ALIEXPRESS_REGEX = "(http[s]?://[a-zA-Z0-9.-]+aliexpress.com[^ ]*.html)"
AMAZON_REGEX = "(http[s]?://[a-zA-Z0-9.-]+(?:amazon|amzn).[a-zA-Z]+(?:.+?(?:ref=[^?]+)|.+(?= )|.+))"

client = discord.Client()


@client.event
async def on_ready():
    print(_('{} has connected to Discord!').format(client.user.name))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!affiliate check':
        await message.channel.send(_('{} affiliate bot is running !').format(COMMUNITY))
        return

    affiliate_links = []

    if ALIEXPRESS_REGEX:
        for match in re.findall(ALIEXPRESS_REGEX, message.content):
            affiliate_links.append(get_aliexpress_affiliate_link(match))
    if AMAZON_TAG:
        for match in re.findall(AMAZON_REGEX, message.content):
            affiliate_links.append(get_amazon_affiliate_link(match))

    if affiliate_links:
        response = traduction.ngettext('Support {} by using this affiliate link posted by {} :',
                                       'Support {} by using these affiliate links posted by {} :',
                                       len(affiliate_links)).format(COMMUNITY, message.author.name)
        for affiliate_link in affiliate_links:
            response += "\n" + affiliate_link

        print(traduction.ngettext('Replaced {} link in {} channel from {} message on {} server',
                                  'Replaced {} links in {} channel from {} message on {} server',
                                  len(affiliate_links))
              .format(len(affiliate_links), message.channel.name, message.author.name, message.guild.name))

        await message.channel.send(response)

        if message.content.startswith('!affiliate '):
            await message.delete()


@client.event
async def on_guild_join(guild):
    print(_('{} joined guild {}').format(client.user.name, guild.name))


def get_aliexpress_affiliate_link(url):
    return f'https://s.click.aliexpress.com/deep_link.htm?aff_short_key={ALIEXPRESS_TAG}&dl_target_url={urllib.parse.quote_plus(url)}'


def get_amazon_affiliate_link(url):
    return url + f'?tag={AMAZON_TAG}'


client.run(DISCORD_TOKEN)
