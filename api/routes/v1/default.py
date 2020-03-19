from api import app
import json

class DefaultResource:
    def on_get(self, req, resp):
        resp.body = json.dumps({'status': 'Welcome!'})


app.add_route('/', DefaultResource())
