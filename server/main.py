#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script made by papi
# p4p1 Server, this works on mac and linux and windows if you hve the python
# interpreter. this script will listen on port 4441 and will pop a prompt
# if a connection is received by the p4p1 remote shell.

import sys, os
import socket

class server():
	'''server class that received the connection and set it up'''

	def __init__(self, port, encryption=False):
		self.port = port
		self.log_file = open("server.log", "a")
		self.prompt = "<p4p1 /> "
		self.buf = ""
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	def handle_client(self, client_sock):
		while True:
			self.buf = raw_input(self.prompt)
			client_sock.send(self.buf)
			if self.buf == "exit":
				break
			if self.buf == "ip":
				self.buf = addr[0]
			else:
				self.buf = client_sock.recv(2048)
			print self.buf

	def main(self):
		self.sock.bind(("0.0.0.0", self.port))
		self.sock.listen(5)
		client, addr = self.sock.accept()
		self.log_file.write("connection from : {0}".format(addr[0]))
		self.handle_client(client)

if __name__ == "__main__":
	s = server(4441)
	s.main()
