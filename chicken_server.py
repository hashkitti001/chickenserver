# Chicken Server v1.0 by Rene Geni
import webbrowser as wb
from tkinter import *
import http.server
import socketserver
import webbrowser as wb
import random
import os

# Define the IP address and port for the server
ip = "localhost"
port = random.randint(2000, 9000)

# Create a custom request handler that disables caching


class NoCacheRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header(
            'Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        super().end_headers()

# Function to start the server


def start_server():
    server_path = os.chdir(text_field.get())
    with socketserver.TCPServer((ip, port), NoCacheRequestHandler) as httpd:
        print(f'Serving directory "{server_path}" at http://{ip}:{port}')
        wb.open(f"http://{ip}:{port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


# GUI logic
window = Tk()
window.title("Chicken Server")
greeting = Label(text="Enter directory path")
text_field = Entry(width="30")
# Bind the button to the start_server function
submit = Button(text="Start server", command=start_server)
message = Label(text="To close the server, just close the window")
greeting.pack()
text_field.pack()
submit.pack()
message.pack()
window.mainloop()
