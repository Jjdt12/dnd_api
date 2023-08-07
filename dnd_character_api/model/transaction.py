import datetime as dt
from marshmallow import Schema, fields

class Character(object):
    def __init__(self, stats, name, race, cclass, backstory):
        self.stats = [stats]
        self.name = name
        self.race = race
        self.cclass = cclass
        self.backstory = backstory

    def __repr__(self):
        return '<Transaction(name={self.description!r})>'.format(self=self)

class CharacterSchema(Schema):
    stats = fields.Str()
    name = fields.Str()
    race = fields.Str()
    cclass = fields.Str()
    backstory = fields.Str()
