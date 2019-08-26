from SearchWindow import SearchWindow
from VideoWindow import VideoWindow
from http.server import HTTPServer, BaseHTTPRequestHandler
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QThread
from PyQt5 import QtWebEngineWidgets
from io import BytesIO
from urllib.parse import parse_qs
from collections import deque
import sys
import _thread
import time
import json
import tornado.ioloop
import tornado.web
import tornado.websocket

queue = deque([])
currentVideo = ""


NODATA = "No data received!"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Window():
    appctxt = ApplicationContext()
    v_window = VideoWindow()


class QueueWebSocketHandler(tornado.websocket.WebSocketHandler):
    connections = set()

    def open(self):
        self.connections.add(self)
        self.write_message(createQueueResponse())
    
    def on_close(self):
        self.connections.remove(self)


class AddVideoHandler(tornado.web.RequestHandler):    
    def post(self):
        global queue
        title = self.get_argument("title", NODATA)
        video_id = self.get_argument('video_id', NODATA)
        queue.appendleft({'title': title, 'video_id': video_id})

        time.sleep(0.3)
        self.write(createQueueResponse())

        
def createQueueResponse():
    response_queue = [elem['title'] for elem in reversed(queue)]
    return {"currentVideo": currentVideo, "queue": response_queue}


def setPlayer():
    global currentVideo
    global queue
    while True:
        if not window.v_window.mediaPlayer.is_playing():
            if queue:
                temp_dict = queue.pop()
                currentVideo = temp_dict['title']
                Window.v_window.PlayVideo(videoId = temp_dict['video_id'])
                [client.send(createQueueResponse()) for client in QueueWebSocketHandler.connections]
    

def make_app():
    return tornado.web.Application([
        (r"/add", AddVideoHandler),
        (r"/queue",QueueWebSocketHandler)
    ])

if __name__ == '__main__':
    print("server")
    app = make_app()
    app.listen(8000)
    _thread.start_new_thread(tornado.ioloop.IOLoop.current().start, ())
    
    print("Qt")
    window = Window()
    window.v_window.show()
    
    _thread.start_new_thread(setPlayer, ())

    exit_code = window.appctxt.app.exec_()
    sys.exit(0)