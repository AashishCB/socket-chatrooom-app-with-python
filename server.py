import socket
import select
# to manage many connection, 
# gives os level io capabilites. will work same on any platform

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# When retrieving a socket option, or setting it, you specify the option name as well as the level. 
# When level = SOL_SOCKET, the item will be searched for in the socket itself.
# arguments -the thing we want to set, what we want to set of that thing, set the thing
# 1 means true, here with above line will allow us to reconnect

# port number keeps ticking up, so it's not in use, which we have to overcome


# You want to run a socket server always on a specific port even after it is closed intentionally or unexpectedly.
# This is useful in some cases where your client program always connects to that specific server port.
# So, you don't need to change the server port.

server_socket.bind((IP, PORT))

server_socket.listen()
# ------------------basic setup-----------------------------------------
sockets_list = [server_socket]
# list of clients, later we will port these clients with other clients

clients = {}
# client socket will be key and the user data will be the value


def receive_message(client_socket):
	try:
		message_header = client_socket.recv(HEADER_LENGTH)

		if not len(message_header):
			return False

		message_length = int(message_header.decode("utf-8").strip())
		return {"header": message_header, "data": client_socket.recv(message_length)}
		#  message_header containing size of message, data receving value at once depending on message length
		# here we are not controlling the message receiving part by part,
		# hoping no one is going to send message of very large size.
	except:
		# only reaches here if somone broke their script
		return False

while True:
	read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
	# we only care about read_sockets
	# select.select takes three parameters
	# first is readlist, second is write list and then error list
	# Python’s select() function is a direct interface to the underlying operating system implementation. 
	# It monitors sockets, open files, and pipes (anything with a fileno() method 
	# that returns a valid file descriptor) until they become readable or writable, 
	# or a communication error occurs.
	# select() makes it easier to monitor multiple connections at the same time,
	# and is more efficient than writing a polling loop in Python using socket timeouts,
	# because the monitoring happens in the operating system network layer, instead of the interpreter.
	for notified_socket in read_sockets:
		if notified_socket == server_socket:
		# it means someone just connected and we need to accept the connection and handle for it.
			client_socket, client_address = server_socket.accept()
			user = receive_message(client_socket)
			if user is False:
			# someone just disconnected, so we will continue
				continue

			sockets_list.append(client_socket)

			clients[client_socket] = user

			print(f"Accepted new connection form {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")

		else:
			message = receive_message(notified_socket)
			# message is receives 'False' on closed connection
			if message is False:
				print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
				sockets_list.remove(notified_socket)
				del clients[notified_socket]
				continue
			user = clients[notified_socket]
			print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

			for clients_socket in clients:
				if clients_socket != notified_socket:
					clients_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

	for notified_socket in exception_sockets:
		sockets_list.remove(notified_socket)
		del clients[notified_socket]
