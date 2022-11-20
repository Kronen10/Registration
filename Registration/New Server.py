from http.server import BaseHTTPRequestHandler,HTTPServer
import sqlite3
import json

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print('Get')
        if self.path == "/greeting":
            con = sqlite3.connect('users2.db')
            cur = con.cursor()

            data = cur.execute("SELECT * FROM 'visitors';")
            data_list = []
            for i in data:
                data_list += [i[1:2]]

            data_list_dict = [] 
            for i in data_list:
                data_list_dict += [{'login':i[0],'password':i[1]}]

            data_str = json.dumps({'data':data_list_dict})    
            
            
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            self.wfile.write(bytes(data_str,"utf-8"))
            
        else:
            self.send_response(400)

    def do_OPTIONS(self):
        print('Options')
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
       

    def do_POST(self):
        print('Post')
        content_length = int(self.headers.get_all('Content-Length')[0])

        body_str = self.rfile.read(content_length)
        body = json.loads(body_str)
        con = sqlite3.connect('users2.db')
        cur = con.cursor()
        print(body)
        user = [body.get('login'), body.get('password')]
        cur.execute("INSERT INTO visitors(login,password) VALUES(?, ?);", user)
        con.commit()

        self.send_response(201, 'created')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    



WebServer=HTTPServer(("127.0.0.1",8080),MyServer)
WebServer.serve_forever()

