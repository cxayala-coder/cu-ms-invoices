#!/usr/bin/env python3
"""
Servidor HTTP simple que actúa como cliente de cu-ms-payments
"""
import http.server
import socketserver
import sys
import os
import json
import urllib.request
import urllib.error
from datetime import datetime

PORT = 3000

# Configuración de cu-ms-payments desde variables de entorno
PAYMENTS_HOST = os.environ.get('PAYMENTS_SERVICE_HOST', 'cu-ms-payments-svc.cx-ayala-dev.svc.cluster.local')
PAYMENTS_PORT = os.environ.get('PAYMENTS_SERVICE_PORT', '3000')
PAYMENTS_URL = f"http://{PAYMENTS_HOST}:{PAYMENTS_PORT}"

def get_users():
    """Consulta el endpoint /users de cu-ms-payments"""
    try:
        url = f"{PAYMENTS_URL}/users"
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Consultando {url}", file=sys.stdout)
        sys.stdout.flush()
        
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data
    except urllib.error.URLError as e:
        return {"error": f"No se puede conectar a cu-ms-payments: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"error": f"Respuesta inválida de cu-ms-payments: {str(e)}"}
    except Exception as e:
        return {"error": f"Error consultando cu-ms-payments: {str(e)}"}

class HolaMundoHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Solicitud GET recibida PEPITO", file=sys.stdout)
        print(f"[{timestamp}] Path: {self.path}", file=sys.stdout)
        
        if self.path == '/startup':
            print(f"[{timestamp}] se llamo al endpoints /startup", file=sys.stdout)
            sys.stdout.flush()
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'OK')
        elif self.path == '/liveness':
            print(f"[{timestamp}] se llamo al endpoints /liveness", file=sys.stdout)
            sys.stdout.flush()
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'OK')
        elif self.path == '/readiness':
            print(f"[{timestamp}] se llamo al endpoints /readiness", file=sys.stdout)
            sys.stdout.flush()
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'OK')
        elif self.path == '/users':
            print(f"[{timestamp}] se llamo al endpoints /users", file=sys.stdout)
            sys.stdout.flush()
            result = get_users()
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode('utf-8'))
        else:
            print(f"[{timestamp}] se llamo al endpoints raiz", file=sys.stdout)
            sys.stdout.flush()
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'<h1>Hola Mundo</h1>')
    
    def log_message(self, format, *args):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {self.address_string()} - {format%args}", file=sys.stdout)
        sys.stdout.flush()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), HolaMundoHandler) as httpd:
        print(f"Servidor corriendo en puerto {PORT}")
        print("Presiona Ctrl+C para detener")
        httpd.serve_forever() 