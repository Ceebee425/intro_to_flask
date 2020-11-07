from app  import app
from flask import render_template


@app.route('/')
def index():
    
     return render_template('index.html',)

@app.route('/favorite')
def favorite():
    context = {
        "customer_name": "Tony",
        "customer_username": "Montana",
        "items": {
            1: 'Beyonce',
            2: 'Jay Z',
            3: 'Jeezy',
            4: 'Yo Gotti',
            5: 'Rihanna'
        }

    }
    return render_template('favorite.html', **context)
