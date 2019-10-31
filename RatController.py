# led controller optimized for use in 

import os
import socket

class RatController:
	'''open tcp connection with nodemcu board. Provides capability to flash led on and off'''
	def __init__(self, ip, port, bs=1024):
		'''setup necessary variables'''
		self.IP = ip
		self.PORT = port
		self.BUFFER_SIZE = bs
		self.s = None			# socket
	
	def set_ip(self, ip):
		'''mutator for ip address'''
		self.IP = ip
		
	def set_port(self, port):
		'''mutator for port'''
		self.PORT = port
		
	def connect(self):
		'''attempt to open connection to ip:port'''
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.s.connect((self.IP, self.PORT))
			return 0
		except TimeoutError:
			self.s.close()
			self.s = None
			return 1
	
	def send_message(self, m):
		'''*safely* send a message through the socket connection'''
		try:
			self.s.send(m);
			return 0
		except ConnectionResetError:
			self.s.close()
			return 1
			
	# functions for sending motor controls 
	def left_forward(self):
		self.send_message(b'LF\r')
	def left_backward(self):
		self.send_message(b'LB\r')
	def left_stop(self):
		self.send_message(b'LO\r')
	
	def right_forward(self):
		self.send_message(b'RF\r')
	def right_backward(self):
		self.send_message(b'RB\r')
	def right_stop(self):
		self.send_message(b'RO\r')
	
			
	
		
	def close(self):
		self.s.close()
		


# COMMAND ENCODING: RO, RF, RB
#					LO, LF, LB
# FUTURE : R[-1..1], L[-1...1]