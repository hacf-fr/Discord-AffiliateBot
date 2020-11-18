# Getting started

## Introduction

Discord AffiliateBot is a small Python app to contribute to one's community.  
It will read users messages and look for Amazon/Aliexpress links.
It will then send a message after the original one with the affiliate version of the links.  

This allows Discords users to contribute to one's community by using these links.

## Prerequisites

**(Required) - A Discord bot token :** Follow instructions [here](https://discordpy.readthedocs.io/en/latest/discord.html) to create your bot, get its token and connect it to your server  
**(Optional) - An Amazon affiliate tag**  
**(Optional) - An Aliexpress affiliate tag**

## Installation

From Docker Hub :
```bash
docker pull hacffr/discord-affiliatebot
```

Or by building it locally, pull the git repository then run :
```bash
docker build -t discord-affiliatebot .
```

## Quickstart

Run the application :
```bash
docker run --name discord-affiliatebot hacffr/discord-affiliatebot
```

## Configuration

You can use the following environment variables :
```bash
docker run --name discord-affiliatebot \ 
    -e DISCORD_TOKEN="MY_TOKEN" \
    -e AMAZON_TAG="MY_AMAZON_TAG" \
    -e ALIEXPRESS_TAG="MY_ALIEXPRESS_TAG" \
    -e COMMUNITY="My community" \
    -e LANGUAGE="en_US:en" \
    hacffr/discord-affiliatebot
```

You can also bind a .env file containing these variables to /app/.env :
```bash
docker run --name discord-affiliatebot \ 
    -v sample.env:/app/.env \
    hacffr/discord-affiliatebot
```

### Docker-Compose

With environment variables :
```bash
version: "3"

services:
  discord-affiliatebot:
    container_name: discord-affiliatebot
    image: hacffr/discord-affiliatebot
    environment:
      - DISCORD_TOKEN=MY_TOKEN
      - AMAZON_TAG=MY_AMAZON_TAG
      - ALIEXPRESS_TAG=MY_ALIEXPRESS_TAG
      - COMMUNITY=My community
      - LANGUAGE=en_US:en
```

With a .env file containing these variables bound to /app/.env :
```bash
version: "3"

services:
  discord-affiliatebot:
    container_name: discord-affiliatebot
    image: hacffr/discord-affiliatebot
    volumes:
      - sample.env:/app/.env
```
