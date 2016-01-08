#!/usr/bin/env python
import tornado.httpclient
from tornado.httpclient import HTTPRequest
from tornado.ioloop import IOLoop
# import tornado.httpserver
# import tornado.httpclient
# import tornado.ioloop
# import tornado.web
# import tornado.gen
# import json

# class TestHandler(tornado.web.RequestHandler):

#     @tornado.web.asynchronous
#     @tornado.gen.engine
#     def get(self):
#         url1 = "http://google.com"
#         url2 = "http://twitter.com"
#         http_client = tornado.httpclient.AsyncHTTPClient()        
#         http_client.fetch(tornado.httpclient.HTTPRequest(url1, method='GET'), callback=(yield tornado.gen.Callback('k1')))
#         http_client.fetch(tornado.httpclient.HTTPRequest(url2, method='GET'), callback=(yield tornado.gen.Callback('k2')))
#         response = yield tornado.gen.WaitAll(['k1', 'k2'])

#         resp = {}
#         for x in response:
#             z = json.loads(x.body)
#             resp[z.keys()[0]] = z[z.keys()[0]]
#         self.set_header('Content-Type', 'application/json')
#         self.write(resp)
#         self.finish()        

    
# application = tornado.web.Application([
#     (r"/stuff/", TestHandler),
# ])

# http_server = tornado.httpserver.HTTPServer(application)
# http_server.listen(8888)
# tornado.ioloop.IOLoop.instance().start()



def handle_request(response):
    if response.error:
        print "Error:", response.error
    else:
        print response.body
    # finish()

http_client = tornado.httpclient.AsyncHTTPClient()
# http_client.fetch("http://localhost:8182/lemmatizer?spelling=fantastick&standardize=true&wordClass=&wordClass2=&corpusConfig=eme&media=text&lemmatize=Lemmatize",handle_request)

# print res
# http_client.close()

# http_put_client = AsyncHTTPClient() 
# http_client.fetch("http://google.com",handle_request)
url="http://localhost:8182/lemmatizer"
data = "spelling=fantastick&standardize=true&wordClass=&wordClass2=&corpusConfig=eme&media=text&lemmatize=Lemmatize"
req = HTTPRequest(url, method="POST", body=data)
http_client.fetch(req,handle_request)
loop = IOLoop.instance()
if __name__ == "__main__":
    loop.start()
