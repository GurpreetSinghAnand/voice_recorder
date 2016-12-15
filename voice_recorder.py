from flask import Flask, request
from flask import render_template
import xml.etree.ElementTree as ET

import config
app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/voicemail')
def voicemail():
    url = 'https://aec54925.ngrok.io/static/audio/voicemail.wav'
    tree = "<?xml version=\"1.0\"?><Response><Play>{}</Play></Response>".format(url)
    return app.response_class(tree, mimetype='application/xml')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
