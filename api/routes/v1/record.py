import json
import falcon
import numpy as np
import pickle

from api import app


class RecordDataResource:
    def on_post(self, req, resp):
        if len(req.media) > 10:
            # Minimise any unneccessary processing the server would do for
            # bad requests, thus reducing CPU use.
            resp.status = falcon.HTTP_400
            resp.media = json.dumps({
                "status": "fail",
            })
        else:
            N = len(req.media)
            with open('api/records.csv', 'a') as rf:
                for (idx, score) in enumerate(req.media):
                    if idx < N - 1:
                        rf.write(str(score) + ', ')
                    elif idx == N - 1:
                        rf.write(str(score) + '\n')
            resp.media = json.dumps({
                "status": "pass",
            })


app.add_route('/api/v1/record', RecordDataResource())
