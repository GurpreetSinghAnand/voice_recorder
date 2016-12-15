from flask import Flask, request, redirect,  url_for
from flask import render_template
import xml.etree.ElementTree as ET
from google.cloud import storage
from oauth2client.client import GoogleCredentials
import base64
import apiai
import config
from config import *
from datetime import datetime
app = Flask(__name__)
app.config.from_object(config)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(PROJECT_ROOT, 'google.json')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/audio/save', methods=['POST'])
def save_audio():
    # print os.environ
    # print request.url_root
    # print "START TIME: {}".format(datetime.now())
    content = str(request.form['audio_file']).strip('\n').split(',')[1]
    # storage_client = storage.Client()
    # bucket_name = 'audio-recordings'
    # bucket = storage_client.create_bucket(bucket_name)
    # blob = open('{}/audio/{}.mp3'.format(STATICFILES_DIRS,datetime.now().strftime('%Y%m%d%H%M%S')))
    f = open('{}/audio/{}.mp3'.format(STATICFILES_DIRS,datetime.now().strftime('%Y%m%d%H%M%S')), 'wb')
    # blob.make_public()
    # blob.upload_from_string(
    #     content,
    #     content_type='audio/mp3')
    # print blob.public_url
    # f = open(, 'wb')
    if len(content) > 0:
        f.write(content.decode('base64'))
        f.close()
    print "\nEND TIME: {}".format(datetime.now())
    return redirect(request.url_root)


# @app.route('/audio/get')
# def voicemail():
#     url = 'https://aec54925.ngrok.io/static/audio/voicemail.wav'
#     tree = "<?xml version=\"1.0\"?><Response><Play>{}</Play></Response>".format(url)
#     return app.response_class(tree, mimetype='application/xml')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', ssl_context=('{}/server.crt'.format(PROJECT_ROOT), '{}/server.key'.format(PROJECT_ROOT)))
