import openai
from flask import Flask, jsonify
from random import randint
from dnd_character_api.model.income import Character, CharacterSchema

app = Flask(__name__)


def d20():
    return randint(9, 18)


def rand_four():
    return randint(0, 3)


def get_backstory(race, cclass):
    backstory_q = "Generate a three sentence dungeons and dragons backstory for a {race} {cclass}, \
                   make the characters name the first word followed by a comma.".format(
        race=race, cclass=cclass
    )
    openai.api_key = "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"
    message = [{"role": "system", "content": backstory_q}]
    backstory = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
    backstory = backstory.choices[0].message.content
    return backstory


@app.route("/characters")
def get_incomes():

    cclass = ["Warrior", "Cleric", "Ranger", "Thief"]
    race = ["Human", "Elf", "Halfling", "Dwarf"]
    cclass = cclass[rand_four()]
    race = race[rand_four()]
    backstory = get_backstory(race, cclass)
    name = backstory.split(",")
    name = name[0]
    character = [
        Character(
            [
                "Str: " + str(d20()),
                "Dex: " + str(d20()),
                "Con: " + str(d20()),
                "Int: " + str(d20()),
                "Wis: " + str(d20()),
                "Chr: " + str(d20()),
            ],
            name,
            race,
            cclass,
            backstory,
        ),
    ]
    schema = CharacterSchema(many=True)
    character = schema.dump(character)
    return jsonify(character)


if __name__ == "__main__":
    app.run()
