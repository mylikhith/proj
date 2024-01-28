from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

# Define the server address
server_address = ("192.168.124.64", 8000)

# Define the videos available on the server
videos = {
    "video1": {"title": "Video 1", "src": "videos/video1.mp4"},
    "video2": {"title": "Video 2", "src": "videos/video2.mp4"},
    "video3": {"title": "Video 3", "src": "videos/video3.mp4"},
    "video4": {"title": "Video 4", "src": "videos/video4.mp4"},
    "video5": {"title": "Video 5", "src": "videos/video5.mp4"},
    "video6": {"title": "Video 6", "src": "videos/video6.mp4"},
    "video7": {"title": "Video 7", "src": "videos/video7.mp4"},
    "video8": {"title": "Video 8", "src": "videos/video8.mp4"},
    "video9": {"title": "Video 9", "src": "videos/video9.mp4"},
}

# Define the clients and their allowed videos
clients = {
    "client1": {
        "videos": ["video1", "video2"],
        "message": "Welcome to Client 1's videos!",
    },
    "client2": {
        "videos": ["video2", "video3"],
        "message": "Welcome to Client 2's videos!",
    },
}


# Create a custom request handler to serve videos and client information
class CustomRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/videos":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(videos).encode())
        elif self.path.startswith("/client"):
            client_id = self.path.split("/")[-1]
            if client_id in clients:
                client_info = clients[client_id]
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(client_info).encode())
            else:
                self.send_error(404, "Client not found")
        else:
            super().do_GET()


# Create the HTTP server
httpd = HTTPServer(server_address, CustomRequestHandler)

# Start the server
print("Server running on port 8000...")
httpd.serve_forever()
