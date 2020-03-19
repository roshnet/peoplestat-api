from api import app


class TrainResource:
    def on_put(self, req, resp):
        resp.media = 'hello'


app.add_route('/api/v1/train', TrainResource())
