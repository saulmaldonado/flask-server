from flask import Flask, render_template, abort, jsonify, request, redirect, url_for

from model import db

app = Flask(__name__)

@app.route('/')
def welcome():

    return render_template(
        'welcome.html',
        message="Here's a message from the view.",
        cards=db
        )

@app.route('/card/<int:index>')
def card_view(index):
    try:

        card = db[index]
        return render_template('card.html', card=card, index=index, maxindex=len(db)-1)
    except IndexError:
        abort(404)


@app.route('/api/card')
def api_card_list():
    return jsonify(db)


@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)

@app.route('/add_card', methods=['POST','GET'])
def add_card():
    if request.method == 'POST':
        card = {'question' : request.form['question'], 'answer': request.form['answer']}
        db.append(card)

        return redirect(url_for('card_view', index=len(db)-1))
    else:
        return render_template('add_card.html')
    