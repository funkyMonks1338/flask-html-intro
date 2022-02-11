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


@app.route('/promotion_image')
def promotion_image():
    url_img = url_for('static', filename='img/mars_1.gif')
    url_style = url_for('static', filename='css/style.css')
    return """
    <!DOCTYPE html>

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Привет, Марс!</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <link rel="stylesheet" href="{}">
    </head>
    
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{}" alt="Гифка 'Марс'">
        <div class="alert alert-dark" role="alert">
            {}
        </div>
        <div class="alert alert-success" role="alert">
            {}
        </div>
        <div class="alert alert-secondary" role="alert">
            {}
        </div>
        <div class="alert alert-warning" role="alert">
            {}
        </div>
        <div class="alert alert-danger" role="alert">
            {}
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
            crossorigin="anonymous"></script>
    </body>
    """.format(url_style, url_img, *PROMOTION_LINES)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
