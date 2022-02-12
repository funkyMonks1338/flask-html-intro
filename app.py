from flask import Flask, request, url_for


BOOTSTRAP_HREF_CSS = 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css'
BOOTSTRAP_INTEGRITY_CSS = 'sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3'
BOOTSTRAP_HREF_JS = 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js'
BOOTSTRAP_INTEGRITY_JS = 'sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p'
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
        <link href="{}" rel="stylesheet" integrity="{}" crossorigin="anonymous">
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
        <script src="{}" integrity="{}" crossorigin="anonymous"></script>
    </body>
    """.format(
        BOOTSTRAP_HREF_CSS, BOOTSTRAP_INTEGRITY_CSS,
        url_style, url_img, *PROMOTION_LINES,
        BOOTSTRAP_HREF_JS, BOOTSTRAP_INTEGRITY_JS)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    ENG_JOBS = [
        'research engineer', 'pilot', 'builder', 'exobiologist', 'doctor',
        'terraforming engineer', 'climatologist', 'radiation protection specialist',
        'astrogeologist', 'glaciologist', 'life support engineer', 'meteorologist',
        'rover operator', 'cyber engineer', 'navigator', 'drone pilot']
    RUS_JOBS = [
        'инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
        'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
        'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
        'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
    TEMPLATES = [
        'surname',
        'name',
        'email',
        [
            'education',
            'Начальное',
            'Среднее',
            'Высшее',
            'Послевузовское'],
        ['job', *zip(ENG_JOBS, RUS_JOBS)],
        [
            'sex',
            ('male', 'Мужской'),
            ('female', 'Женский')],
        'motivation',
        'photo',
        'agreement'
    ]
    if request.method == 'GET':
        BOOTSTRAP_CSS = [BOOTSTRAP_HREF_CSS, BOOTSTRAP_INTEGRITY_CSS]
        BOOTSTRAP_JS = [BOOTSTRAP_HREF_JS, BOOTSTRAP_INTEGRITY_JS]
        url_style = url_for('static', filename='css/style.css')
        return """
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="{0[0]}" rel="stylesheet" integrity="{0[1]}" crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{1}" />
            <title>Отбор астронавтов</title>
        </head>

        <body>
            <h2>Анкета претендента</h2>
            <h4>на участие в миссии</h4>
            <div>
                <form class="login_form" method="post">
                    <div class="form-group">
                        <input type="text" class="form-control" id="{2}" placeholder="Введите фамилию" name="{2}">
                        <input type="text" class="form-control" id="{3}" placeholder="Введите имя" name="{3}">
                    </div>
                    <div class="form-group">
                        <input type="email" class="form-control" id="{4}" aria-describedby="emailHelp"
                            placeholder="Введите адрес почты" name="{4}">
                    </div>
                    <div class="form-group">
                        <label for="{5[0]}">Какое у вас образование?</label>
                        <select class="form-control" id="{5[0]}" name="{5[0]}">
                            <option>{5[1]}</option>
                            <option>{5[2]}</option>
                            <option>{5[3]}</option>
                            <option>{5[4]}</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="form-check">Ваша основная профессия?</label>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[1][0]}" value="{6[1][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[1][0]}">{6[1][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[2][0]}" value="{6[2][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[2][0]}">{6[2][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[3][0]}" value="{6[3][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[3][0]}">{6[3][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[4][0]}" value="{6[4][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[4][0]}">{6[4][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[5][0]}" value="{6[5][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[5][0]}">{6[5][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[6][0]}" value="{6[6][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[6][0]}">{6[6][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[7][0]}" value="{6[7][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[7][0]}">{6[7][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[8][0]}" value="{6[8][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[8][0]}">{6[8][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[9][0]}" value="{6[9][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[9][0]}">{6[9][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[10][0]}" value="{6[10][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[10][0]}">{6[10][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[11][0]}" value="{6[11][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[11][0]}">{6[11][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[12][0]}" value="{6[12][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[12][0]}">{6[12][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[13][0]}" value="{6[13][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[13][0]}">{6[1][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[14][0]}" value="{6[14][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[14][0]}">{6[14][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[15][0]}" value="{6[15][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[15][0]}">{6[15][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{6[16][0]}" value="{6[16][0]}" name="{6[0]}">
                            <label class="form-check-label" for="{6[16][0]}">{6[16][1]}</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="form-check">Укажите пол</label>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{7[1][0]}" value="{7[1][0]}" name="{7[0]}" checked>
                            <label class="form-check-label" for="{7[1][0]}">{7[1][1]}</label>
                        </div>
                        <div class="form-check">
                            <input type="radio" class="form-check-input" id="{7[2][0]}" value="{7[2][0]}" name="{7[0]}">
                            <label class="form-check-label" for="{7[2][0]}">{7[2][1]}</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="{8}">Почему Вы хотите принять участие в миссии?</label>
                        <textarea class="form-control" id="{8}" rows="3" name="{8}"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="{9}">Приложите фотографию</label>
                        <input type="file" class="form-control-file" id="{9}" name="{9}">
                    </div>
                    <div class="form-group form-check">
                        <input type="checkbox" class="form-check-input" id="{10}" name="{10}">
                        <label class="form-check-label" for="{10}">Готовы ли Вы остаться на Марсе?</label>
                    </div>
                    <button type="submit" class="btn btn-primary">Отправить</button>
                </form>
            </div>
            <script src="{11[0]}" integrity="{11[1]}" crossorigin="anonymous"></script>
        </body>

        </html>
        """.format(BOOTSTRAP_CSS, url_style, *TEMPLATES, BOOTSTRAP_JS)
    elif request.method == 'POST':
        field_names = tuple(fld[0] if isinstance(
            fld, (list, tuple)) else fld for fld in TEMPLATES)
        return repr({field: request.form.get(field) for field in field_names})


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
