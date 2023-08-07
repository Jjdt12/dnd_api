from marshmallow import post_load
from .transaction import Character, CharacterSchema
from .transaction_type import TransactionType

class Character(Character):
    def __init__(self, stats, name, race, cclass, backstory):
        super(Character, self).__init__(stats, name, race, cclass, backstory, TransactionType.CHARACTER)

    def __repr__(self):
        return '<Income(name={self.description!r})>'.format(self=self)

class CharacterSchema(CharacterSchema):
    @post_load
    def make_income(self, data, **kwargs):
        return Income(**data)



