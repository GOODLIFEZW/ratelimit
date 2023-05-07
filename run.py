import tornado.ioloop
import tornado.web
from ratelimit import limits, sleep_and_retry

FIFTEEN_MINUTES = 60

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class TestHandler(tornado.web.RequestHandler):
    @sleep_and_retry
    @limits(calls=100, period=FIFTEEN_MINUTES)
    def get(self):
        self.write("test")

app = tornado.web.Application([
    (r"/", MainHandler),
    (r"/test", TestHandler),
])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
