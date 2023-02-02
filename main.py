from server import httpserver
from api.browser import apiBrowser


api = apiBrowser()
api.load()
api.login("reditel", "opava1")
httpserver = httpserver.httpserver(8080, api)

httpserver.start()

httpserver.stop()
