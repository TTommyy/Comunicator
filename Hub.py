# Author: Tomasz Koczar
# Year: 2023AD
# Brief: File implementing Hub class that will serve 
# as connector between clients in star topology

from Logs import LOG_ENTER, LOG_INFO, LOG_ERROR
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_ERROR
from threading import Thread

# Constants
ipAddress = ''
port = 1000
numberOfConnections = 2

def getSocketParams():
  return ipAddress, port

def getMaxNumberOfConnections():
  return numberOfConnections

class Hub:
  def __init__(self):
    self.hub = socket(AF_INET, SOCK_STREAM)
    self.hub.bind(getSocketParams())
    self.clients = []
    self.hub.listen(getMaxNumberOfConnections())

    connLeft = getMaxNumberOfConnections()
    while connLeft > 0:
      LOG_INFO(f"Waiting for {connLeft} more clients")
      client, addr = self.hub.accept()
      LOG_INFO(f"Client connected")
      self.clients.append(client)
      connLeft -= 1
      Thread(target=self.handleConnection, args=(client,)).start()

    LOG_INFO("All spots occupied")
    self.hub.close()


  def isClientConnected(self, client):
    errorCode = client.getsockopt(SOL_SOCKET, SO_ERROR)
    if errorCode != 0:
      LOG_INFO(f"Connection with client ")
    return errorCode == 0

  def stopCondition(self, client):
      return self.isClientConnected(client)

  def handleConnection(self, client):
    LOG_INFO("Starting theread")
    while self.stopCondition(client):
      self.clients = [client for client in self.clients if self.isClientConnected(client)]
      try:
        data = client.recv(1024)
        if not data:
          LOG_INFO("No data recived")
        else:
          for fclient in self.clients:
            if fclient != client:  # Exclude the sending client itself
              if self.isClientConnected(fclient):
                fclient.send(data)

      finally:
        pass
