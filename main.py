from server import httpserver
from api.browser import apiBrowser


api = apiBrowser()
httpserver = httpserver.httpserver(8080, api)

httpserver.start()

httpserver.stop()
