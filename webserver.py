from flask import Flask, Response, send_file


app = Flask(__name__, static_url_path='')


@app.route('/rss')
def send_rss():
	return send_file('hello_cortex.xml')


if __name__ == "__main__":
	app.run(host="0.0.0.0")