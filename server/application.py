"""import"""
import http.server
import socketserver
PORT = 8000
"""class """
class TestMe():
"""возвращает  4"""
    def take_five(self):
        return 4
"""возвращает порт"""
    def port(self):
        return PORT
"""запуск сервера"""
if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()


