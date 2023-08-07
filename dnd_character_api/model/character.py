from marshmallow import Schema, fields

class Character(object):
    def __init__(self, stats, name, race, cclass, backstory):
        self._stats = [stats]
        self._name = name
        self._race = race
        self._class = cclass
        self._backstory = backstory

    def __repr__(self):
        return '<Character(name={self.description!r})>'.format(self=self)

class CharacterSchema(Schema):
    _stats = fields.Str()
    _name = fields.Str()
    _race = fields.Str()
    _class = fields.Str()
    _backstory = fields.Str()
