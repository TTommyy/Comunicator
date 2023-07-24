# Author: Tomasz Koczar
# Year: 2023AD
# Brief: Executable for clients

from Logs import LOG_ENTER, LOG_INFO, LOG_ERROR
from Client import Client

if __name__ == "__main__":
  clinet = Client()
  clinet.connect()
  while True:
    clinet.sendMessage(input("Send message: "))