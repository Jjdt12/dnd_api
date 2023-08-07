from marshmallow import post_load
from .character import Character, CharacterSchema

class Character(Character):
    def __init__(self, stats, name, race, cclass, backstory):
        super(Character, self).__init__(stats, name, race, cclass, backstory)

    def __repr__(self):
        return '<Income(name={self.description!r})>'.format(self=self)

class CharacterSchema(CharacterSchema):
    @post_load
    def make_income(self, data, **kwargs):
        return Income(**data)



