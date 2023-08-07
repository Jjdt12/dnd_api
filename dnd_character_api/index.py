from flask import Flask, jsonify, request
from random import randint
app = Flask(__name__)
from dnd_character_api.model.expense import Expense, ExpenseSchema
from dnd_character_api.model.income import Income, IncomeSchema
from dnd_character_api.model.transaction_type import TransactionType

app = Flask(__name__)

def d20():
    return randint(1, 20)

transactions = [
        Income('Strength', randint(1, 20)),
        Income('Dividends', 200),
        Expense('Pizza', 50),
        Expense('Rock Concert', 100)
        ]

@app.route('/incomes')
def get_incomes():
    num = d20()
    print(num)
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
            filter(lambda t: t.type == TransactionType.INCOME, transactions)
            )
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return "", 204

@app.route('/expenses')
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
            filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
            )
    return jsonify(expenses)

@app.route('/expenses', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return "", 204

if __name__ == "__main__":
    app.run()
