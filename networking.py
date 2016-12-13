# +U or -U depending on if server message or client message
# 0 or 1 for robot enabled
# rest are axis values, goes 0, 2, 3, 4
# $ for end
# "-U0:0.000:0.000:0.000:0.000$"
# "+U0:[24 char long message]"

# lol I totally stole this from somewhere

import RobotExceptions as rexept

def sendToDashboard(sock, msg):
	totalsent = 0
	while totalsent < len(msg):
		sent = sock.send(msg[totalsent:])
		if sent == 0:
			raise rexept.SocketClose()
		totalsent = totalsent + sent

def recieveFromDashboard(sock, length):
	chunks = []
	bytes_recd = 0
	while bytes_recd < length:
		chunk = sock.recv(min(length - bytes_recd, 2048))
		if chunk == '':
			raise rexept.SocketClose()
		chunks.append(chunk)
		bytes_recd = bytes_recd + len(chunk)
	return ''.join(chunks)
