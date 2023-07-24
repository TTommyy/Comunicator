import socket
import threading

class Hub:
  def __init__(self):
    self.hub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.ipAddress = '0.0.0.0'
    self.port = 1000
    self.hub.bind((self.ipAddress, self.port))
    self.numberOfConnections = 1
    self.clients = []
    self.hub.listen(self.numberOfConnections)

    connLeft = self.numberOfConnections
    while connLeft > 0:
      print("Waiting for more clients")
      client, addr = self.hub.accept()
      self.clients.append(client)
      connLeft -= 1
      threading.Thread(target=self.handleConnection, args=(client,)).start()

    self.hub.close()

  def handleConnection(self, client):
    try:
      while True:
        data = client.recv(1024)
        if not data:
          break  # Exit the loop if no data is received
        # Send the received data to other clients
        for fclient in self.clients:
          # if fclient != client:  # Exclude the sending client itself
          fclient.send(data)
    except socket.error:
      # Handle any socket errors that occur during recv() or send()
      # Close the client socket or perform any necessary error handling
      pass
