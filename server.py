import http.server, socketserver, webbrowser
from pathlib import Path

PORT = 8000
STATIC_DIR = Path(__file__).parent

class PortfolioHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)
    def log_message(self, format, *args):
        print(f"  {self.address_string()}  {args[0]}  {args[1]}")

def main():
    print("\n" + "="*50)
    print("  Dimakatso Molefe - Portfolio Server")
    print("="*50)
    print(f"  URL: http://localhost:{PORT}")
    print("  Press Ctrl+C to stop\n")
    with socketserver.TCPServer(("", PORT), PortfolioHandler) as httpd:
        httpd.allow_reuse_address = True
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Server stopped. Goodbye!\n")

if __name__ == "__main__":
    main()
