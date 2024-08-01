server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Retrieving information
def get_server_status(server_name):
    server = server_config.get(server_name)
    if server:
        return server.get('status', 'Status not found')
    return 'Server not found'

# Example usage
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")

# Retrieve status for 'server1'
status_server1 = server_config.get('server1', {}).get('status', 'Status not found')
print(f"server1 status: {status_server1}")

# Check if port 8080 is present
def check_port_existence(port):
    for server in server_config.get.items():
        if server.get('port') == port:
            return True
    return False

port = 8081
if check_port_existence(port):
    print(f"Port {port} is present")
else:
    print(f"Port {port} is not present")

