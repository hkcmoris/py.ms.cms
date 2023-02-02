from server import httpserver

httpserver = httpserver.httpserver(8080)
httpserver.start()

httpserver.stop()
