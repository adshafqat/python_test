from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    ###########################
    # Change these parameters #
    ###########################
    API_UID = ""
    FILE = "file.txt"
    ###########################

    # pyjwt library: https://pyjwt.readthedocs.io/en/latest/
    # install with `pip install pyjwt`
    import jwt
    # requests library: http://docs.python-requests.org/en/latest/index.html
    # install with `pip install requests`
    import requests

    from urllib.parse import urlparse
    from time import time

    uri = urlparse('https://skillshop.exceedlms-staging.com/oauth2/token.json')

    my_txt_f = open(FILE, 'r')
    my_txt = my_txt_f.read()
    my_txt_f.close()
    claim_set = {
      'iss':API_UID,
      'aud':'%s://%s' % (uri.scheme, uri.hostname),
      'scope':'admin_read',
      'exp':time() + 60,
      'iat':time()
    }

    encoded_jwt = jwt.encode(claim_set, my_txt, algorithm='RS256')

    req = requests.post(uri.geturl(), data={'grant_type':
    'urn:ietf:params:oauth:grant-type:jwt-bearer', 'assertion': encoded_jwt})
    print(req.json())
    return req.json()

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
