# Socket Chatroom-Creating chat application with sockets in python
Sockets and the socket API are used to send messages across a network. They provide a form of inter-process communication (IPC).
Python’s socket module provides an interface to the Berkeley sockets API.

> The objective is to create a chat application having a server and multiple clients.

### Prerequisites

#### socket
Python’s socket module provides an interface to the Berkeley sockets API.

#### select
a direct interface to the underlying operating system implementation. It monitors sockets, open files, and pipes (anything with a fileno() method that returns a valid file descriptor) until they become readable or writable, or a communication error occurs.

#### errno
The errno module defines a number of symbolic error codes, such as ENOENT (“no such directory entry”) and EPERM (“permission denied”).

#### sys
The sys module provides information about constants, functions and methods of the Python interpreter.

### to run the client and server .py file:
You must have python3 installed on your computer to run it.

1. Open cmd on the file stored location and:

` $ python server.py `

or 

` $ python3 server.py `

2. Open multiple another cmd on the file stored location without closing any terminals and run below command to open multiple clients:

` $ python client.py `

or 

` $ python3 client.py `

3. In the client terminals you opened. enter your username:

` Username: [client_name_you_like_to_give] `

4. You will have a server terminal with a message 'accepted new connection from ...... username: [your_client_name].' 

5. After entering username, you will get area for entering and receiving the messages.

` username >  `

6. Enter message from any client. The message will immediately be received by the server. But, for other clients to get the message, press 'Enter' in the client terminal and it will load.

> This is the socket chatroom working.