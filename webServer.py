from http.server import BaseHTTPRequestHandler, HTTPServer
from Config.crudController import CRUD
import cgi

class classServer:
    def __init__(self, *args, **kwargs):
        
        port = 1995
        server = HTTPServer(('',port),webServer)
        print("Web server running at : ",port)
        server.serve_forever()

        

class webServer(BaseHTTPRequestHandler):
        
    db =CRUD()
    output = ''
    start= '<html><body>'
    table = '''<table style="width:100%">
            <tr>
              <th>Name</th>
              <th>Address</th> 
              <th>Bio</th>
              <th>Age</th>
              <th>Gender</th>
              <th>Link</th>
              <th>Address</th>
              <th>Longitude</th>
              <th>Latitude</th>
              <th>Image</th>
              <th>Dob</th>
              <th>Phone</th>
            </tr> ''' 
    
    def setHeaders(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def do_GET(self):
        try:
            path = self.path.split("/")
            if path[1]== "Home":
                data = self.db.View()
                self.output += self.start + self.table
                for each in data:
                    self.output +=   (f'''
                        <tr>
                          <td>{each[0]}</td>
                          <td>{each[1]}</td>
                          <td>{each[2]}</td>
                          <td>{each[3]}</td>
                          <td>{each[4]}</td>
                          <td>{each[5]}</td>
                          <td>{each[6]}</td>
                          <td>{each[7]}</td>
                          <td>{each[8]}</td>
                          <td>{each[9]}</td>
                          <td>{each[10]}</td>
                          <td>{each[11]}</td>
                        </tr>
                    ''')
                self.output += '</table></body></html>'
                self.setHeaders()
                self.wfile.write(self.output.encode())
                return

            if self.path.endswith("/Update"):
                output = ''
                output += '<html><body>Update</body></html>'
                self.setHeaders()
                self.wfile.write(output.encode())
                return

            if self.path.endswith("/Create"):
                output = ''
                output += '<html><body>Create</body></html>'
                self.setHeaders()
                self.wfile.write(output.encode())
                return

            if path[1]==("View"):
                Id = path[2]
                print(Id)
                data = self.db.Read(f"Id = {Id}")
                output = start + table
                for each in data:
                    output +=   (f'''
                        <tr>
                          <td>{each[0]}</td>
                          <td>{each[1]}</td>
                          <td>{each[2]}</td>
                          <td>{each[3]}</td>
                          <td>{each[4]}</td>
                          <td>{each[5]}</td>
                          <td>{each[6]}</td>
                          <td>{each[7]}</td>
                          <td>{each[8]}</td>
                          <td>{each[9]}</td>
                          <td>{each[10]}</td>
                          <td>{each[11]}</td>
                        </tr>
                    ''')
                output += '</table></body></html>'
                self.setHeaders()
                self.wfile.write(output.encode())
                return 

        except IOError:
            self.send_error(400)

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()
        
        except:
            IOError
            self.send_error(400)


if __name__=='__main__':
    server = classServer()


