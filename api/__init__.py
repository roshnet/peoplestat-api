import falcon


class CORSMiddleware:
    def process_response(self, req, resp, ressource, req_succeeded):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')


app = falcon.API(middleware=[
    CORSMiddleware(),
])

import api.routes    # noqa
