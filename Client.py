# Author: Tomasz Koczar
# Year: 2023AD
# Brief: Class implementing hub client

from Logs import LOG_ENTER, LOG_INFO, LOG_ERROR
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM
from Messages.Py.Message_pb2 import Message


ipAddress = '127.0.0.1'
port = 1000

class Client:
  def __init__(self):
    self.client = socket(AF_INET, SOCK_STREAM)
    self.name = input("Enter your name: ")

  def connect(self):
    self.client.connect((ipAddress, port))
    self.sendMessage()
    Thread(target=self.handleConnection, args=()).start()

  def sendMessage(self, message = None):
    serializedMessage = Message(name = self.name, content = message).SerializeToString()
    self.client.send(serializedMessage)

  def handleConnection(self):
    while True:
      try:
        data = self.client.recv(1024)
        message = Message()
        message.ParseFromString(data)
        if data:
           print(f"User {message.name}: {message.content}") # Show message to user
      finally:
          pass

  def isClientConnected(self, client):
    errorCode = client.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
    return errorCode == 0