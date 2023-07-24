from Logs import LOG_ENTER, LOG_INFO, LOG_ERROR
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM

ipAddress = '127.0.0.1'
port = 1000

class Client:
  def __init__(self):
    self.client = socket(AF_INET, SOCK_STREAM)
    self.name = input("Enter your name: ")

  def connect(self):
    self.client.connect((ipAddress, port))
    Thread(target=self.handleConnection, args=()).start()

  def sendMessage(self, message):
    self.client.send(message.encode())

  def handleConnection(self):
    while True:
      try:
        data = self.client.recv(1024)
        if data:
           print(data.decode()) # Show message to user
      finally:
          pass

  def isClientConnected(self, client):
    errorCode = client.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
    return errorCode == 0