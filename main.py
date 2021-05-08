from flask import Flask

app = Flask('__name__')


@app.route('/username')
def home(username):
	return '<h1>Good morning %s</h1>' % username


if __name__ == '__main__':
	app.run(debug=True)
