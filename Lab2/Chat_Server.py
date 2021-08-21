from  http.server import HTTPServer, BaseHTTPRequestHandler
import select
import sys

# Checks if the number of arguments is given is correct.
if len(sys.argv) != 3:
    print ("Correct usage: script, IP address, port number")
    exit()

# The first argument from the prompt is saved in IP_ADDRESS as a IP address.
IP_ADDRESS = str(sys.argv[1])

# The second argument from the prompt is saved in PORT as a port number.
PORT = int(sys.argv[2])

msgs={}

class message_Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        n_name = ""
        m = msgs.get(n_name)
        msgs[n_name] = ""
        msg = "nada"
        self.wfile.write(msg.encode())

    def do_POST(self):
        if(self.path.endswith("/nickname")):
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            post_body = post_body.decode()
            
            if msgs.get(post_body) == None:
                msgs[post_body] = ""
                self.send_response(201)
                self.send_header('content-type','text/html')
                self.end_headers()
                print("Nickname registered " + post_body)
            else:
                self.send_response(401)
                self.send_header('content-type','text/html')
                self.end_headers()
 
        elif(self.path.endswith("/getM")):
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len).decode()
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            message = msgs.get(post_body)
            msgs[post_body] = ""
            self.wfile.write(message.encode())

        else:
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            post_body = post_body.decode()
            n_name = post_body.split(":")[0]
            for name in msgs:
                if name != n_name:
                    msg = msgs.get(name)
                    msg = msg + "\n" + post_body
                    msgs[name] = msg
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            #self.wfile.write('POST'.encode())


def main():
    server = HTTPServer((IP_ADDRESS,PORT),message_Handler)
    print("Server running on port {}".format(PORT))
    server.serve_forever()

if __name__ == "__main__":
    main()
