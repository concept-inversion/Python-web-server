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
              <th>Id</th>
              <th>Name</th>
              <th>Email</th> 
              <th>Bio</th>
              <th>Gender</th>
              <th>Link</th>
              <th>Address</th>
              <th>Longitude</th>
              <th>Latitude</th>
              <th>Image</th>
              <th>Phone</th>
              <th>Dob</th>
              
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

            if path[1]==("Update"):
                
                Id = path[2]
                data = self.db.Read(f"Id = {Id}")
                print(data)
                self.output += self.start 
                self.output =   '''
                                <form method = 'POST' enctype= 'multipart/form-data' action ='update'
                                '''
                form = f'''
                     <br>Name:<br>
                     <input type="text" name="Name" value="{data[0][1]}">
                     <br>Email:<br>
                     <input type="text" name="Email" value="">
                     <br>Bio:<br>
                     <input type="text" name="Bio" value="">
                     <br>Gender:<br>
                     <input type="text" name="Gender" value="">
                     <br>Link:<br>
                     <input type="text" name="Link" value="">
                     <br>Address:<br>
                     <input type="text" name="Address" value="">
                     <br>Longitude:<br>
                     <input type="text" name="Longitude" value="">
                     <br>Latitude:<br>
                     <input type="text" name="Latitude" value="">
                     <br>Image:<br>
                     <input type="text" name="Image" value="">
                     <br>Phone:<br>
                     <input type="text" name="Phone" value="">
                     <br>Dob:<br>
                     <input type="text" name="Dob" value="">
                     <br><br>
                     <input type = "submit" value="submit">
                     </form>
                    '''
                if data: 
                
                    self.output += form
                    self.output += '</body></html>'
                self.setHeaders()
                self.wfile.write(self.output.encode())
                return

            if path[1] == ("Create"):
                
                
                self.output =   '''
                                <form method = 'POST' enctype= 'multipart/form-data' action ='create'
                                '''
                form = '''
                     
                     <br>Name:<br>
                     <input type="text" name="Name" value="">
                     <br>Email:<br>
                     <input type="text" name="Email" value="">
                     <br>Bio:<br>
                     <input type="text" name="Bio" value="">
                     <br>Gender:<br>
                     <input type="text" name="Gender" value="">
                     <br>Link:<br>
                     <input type="text" name="Link" value="">
                     <br>Address:<br>
                     <input type="text" name="Address" value="">
                     <br>Longitude:<br>
                     <input type="text" name="Longitude" value="">
                     <br>Latitude:<br>
                     <input type="text" name="Latitude" value="">
                     <br>Image:<br>
                     <input type="text" name="Image" value="">
                     <br>Phone:<br>
                     <input type="text" name="Phone" value="">
                     <br>Dob:<br>
                     <input type="text" name="Dob" value="">
                     <br><br>
                     <input type = "submit" value="submit">
                     </form>
                    '''
                self.output += form
                self.output += '<html><body>Create</body></html>'
                self.setHeaders()
                self.wfile.write(self.output.encode())
                return

            if path[1] == ("Delete"):
                Id = path[2]
                data=self.db.Delete(f"Id={Id}")
                self.output += '<html><body>Deleted</body></html>'
                self.setHeaders()
                self.wfile.write(self.output.encode())
                return

            if path[1] == ("View"):
                Id = path[2]
                data = self.db.Read(f"Id = {Id}")
                self.output = self.start + self.table
                if data: 
                    
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

        except IOError:
            self.send_error(400)

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()    
            contentType,paramDict = cgi.parse_header(self.headers.getheader('content-type'))
            if contentType== 'multipart/form-data':
                fields= cgi.parse_multipart(self.rfile,paramDict)
                messageContent = fields.get('message')

        except:
            IOError
            self.send_error(400)


if __name__=='__main__':
    server = classServer()


