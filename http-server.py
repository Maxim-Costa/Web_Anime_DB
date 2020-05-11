#!/usr/bin/python3.8
# coding:utf-8
import http.server

port = 8080
address = ("", port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)

print(f"serveur démarré sur la port {port}")

httpd.serve_forever()
