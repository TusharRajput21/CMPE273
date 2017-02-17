import psutil

sockets = psutil.net_connections("tcp")
total_connections = []
group = {} 

for connection in sockets:
	if connection.pid in group:
		group[connection.pid] = group[connection.pid] + 1
	else:
		group[connection.pid] = 1

sortgroup = sorted(group.items(),  key = lambda x: x[1], reverse = True)


print "pid","laddr","raddr","status"


for sortgroup in sortgroup:
	for connection in total_connections:

		if sortgroup[0] == connection.pid:
			newladdr = str(connection.laddr).replace("(","").replace(")","").replace("'","").split(",")
			newraddr = str(connection.laddr).replace("(","").replace(")","").replace("'","").split(",")
			print '"' + str(connection.pid)+'","'+newladdr[0]+"@"+newladdr[1].strip()+'","'+newraddr[0]+"@"+newraddr[1].strip()+'","'+str(connection.status)+'"'
