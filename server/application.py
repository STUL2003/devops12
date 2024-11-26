"""import"""
import http.server
import socketserver

PORT = 8000

"""class """
class TestMe:
    """возвращает  4"""
    def take_five(self):
        """Возвращает число 4"""
        return 4

    def port(self):
        """Возвращает значение порта"""
        return PORT

if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
