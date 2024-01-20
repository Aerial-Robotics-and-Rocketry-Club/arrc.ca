import http.server
import socketserver

# Choose a port (e.g., 8000)
port = 8000

# Define the handler to use for incoming requests
handler = http.server.SimpleHTTPRequestHandler

# Create a TCP server with the specified port and handler
httpd = socketserver.TCPServer(("", port), handler)

print(f"Serving on port {port}")
print(f"http://localhost:{port}")

# Start the server
httpd.serve_forever()