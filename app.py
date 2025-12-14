from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', active_page='index')

@app.route('/monika')
def monika():
    return render_template('monika.html', active_page='monika')

@app.route('/sayori')
def sayori():
    return render_template('sayori.html', active_page='sayori')

@app.route('/yuri')
def yuri():
    return render_template('yuri.html', active_page='yuri')

@app.route('/natsuki')
def natsuki():
    return render_template('natsuki.html', active_page='natsuki')

@app.route('/glossary')
def glossary():
    return render_template('glossary.html', active_page='glossary')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

if __name__ == '__main__':
    app.run(debug=True)