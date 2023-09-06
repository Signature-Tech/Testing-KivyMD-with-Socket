from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
import socket


class MyApp(MDApp):

    def build(self):

        ### EDITING SCREEN
        self.title = "Using Socket in Kivy"

        ### CONNECT TO NETWORK
        self.connect()

        return Builder.load_file("main.kv")
    
    def connect(self):
        ### CREATING NETWORK CONNECTION
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = ("192.168.0.103", 5555)
        try:
            self.server.connect((self.addr))
        except ConnectionRefusedError or TimeoutError:
            pass
       
    def data(self):
        
        try:
            self.server.send(("hello").encode())
        except OSError:
            pass


App = MyApp()

if __name__ == "__main__":
    App.run()