import http.server
import socketserver

PORT = 8080  # Вы можете выбрать любой доступный порт

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Сервер запущен на порту {PORT}")
    httpd.serve_forever()