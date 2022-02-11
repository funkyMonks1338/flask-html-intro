from flask import Flask, url_for


PROMOTION_LINES = [
    'Человечество вырастает из детства.',
    'Человечеству мала одна планета.',
    'Мы сделаем обитаемыми безжизненные пока планеты.',
    'И начнем с Марса!',
    'Присоединяйся!']


app = Flask(__name__)


@app.route('/')
def root():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return ''.join(f'<p>{line}</p>' for line in PROMOTION_LINES)


@app.route('/image_mars')
def image_mars():
    return f"""
    <!DOCTYPE html>
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Привет, Марс!</title>
    </head>
    
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='img/mars_1.gif')}" alt="Гифка 'Марс'">
        <p>Вот она какая, красная планета.</p>
    </body>
    """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
