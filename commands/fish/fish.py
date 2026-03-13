from discord.ext.commands import Context
import sqlite3
import commands.fish.catches as catches
import random

connection = sqlite3.connect("../../db.sqlite")
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS fishing_data (userID INTEGER PRIMARY KEY, points DECIMAL)')

def get_random_rarity():
    random_value = random.random()
    cumulative_probability = 0

    for rarity in catches.RARITIES:
        cumulative_probability += rarity["probability"]
        if random_value < cumulative_probability:
            return rarity

    return catches.RARITIES[0]

def fish(context: Context):
    rarity = get_random_rarity()
    item = random.choice(catches.CATCHES)

    worth = item["value"] * rarity["multiplier"]

    cursor.execute(f"INSERT INTO fishing_data VALUES ({context.author.id}, {worth})")

    if rarity["name"] == "uncommon":
        suffix = "n"
    else:
        suffix = ""

    print(f"{context.author.name} caught a {item["name"]} of rarity {rarity["name"]}")
    print(f"{context.author.name} gained {worth} points ({item["value"]} * {rarity["multiplier"]})\n")
    return f"You caught a{suffix} {rarity["name"]} {item["name"]}\n+{worth} points"