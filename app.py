from flask import Flask, render_template, request  # Importing Flask, render_template and request

app = Flask(__name__)  # getting the import name


@app.route('/')
def root():
    active_page = 'root'
    return render_template('index.html', active_page=active_page)


@app.route('/peanut_immuno')
def peanut_immuno():
    active_page = 'peanut_immuno'
    return render_template('peanut_immuno.html', active_page=active_page)


@app.route('/tips')  # Route for the tips page
def tips():
    active_page = 'tips'
    # Add any specific logic for the tips page if needed
    return render_template('tips.html', active_page=active_page)

@app.route('/research')  # Route for the research page
def research():
    active_page = 'research'
    # Add any specific logic for the research page if needed
    return render_template('research.html', active_page=active_page)


@app.route('/sources')  # Route for the sources page
def sources():
    active_page = 'sources'
    # Add any specific logic for the sources page if needed
    return render_template('sources.html', active_page=active_page)


if __name__ == '__main__':
    app.run(debug=True)
