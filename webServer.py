from http.server import BaseHTTPRequestHandler, HTTPServer
from Config.crudController import CRUD
from urllib.parse import parse_qs        

class webServer(BaseHTTPRequestHandler):
        
    db =CRUD()
    output = ''
    start= '<html><body>'
    table = '''<table border="1">
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
              <th>Actions</th>
              
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
                          <td>  <a href="http://localhost:1995/View/{each[0]}" class="button">View</a>
                                <a href="http://localhost:1995/Delete/{each[0]}" class="button">Delete</a>
                                <a href="http://localhost:1995/Update/{each[0]}" class="button">Update</a>
                        </tr>
                    ''')
                self.output += '</table></body></html>'
                self.setHeaders()
                self.wfile.write(self.output.encode())
                return

            if path[1]==("Update"):
                
                Id = path[2]
                data = self.db.Read(f"Id = {Id}")
                
                self.output += self.start 
                self.output =   '''
                                <form method = "POST" enctype= "multipart/form" >
                                '''
                form = f'''
                     Name:
                     <input type="text" name="Name" value="{data[0][1]}">
                     <br>Email:<br>
                     <input type="text" name="Email" value="{data[0][2]}">
                     <br>Bio:<br>
                     <input type="text" name="Bio" value="{data[0][3]}">
                     <br>Gender:<br>
                     <input type="text" name="Gender" value="{data[0][4]}">
                     <br>Link:<br>
                     <input type="text" name="Link" value="{data[0][5]}">
                     <br>Address:<br>
                     <input type="text" name="Address" value="{data[0][6]}">
                     <br>Longitude:<br>
                     <input type="text" name="Longitude" value="{data[0][7]}">
                     <br>Latitude:<br>
                     <input type="text" name="Latitude" value="{data[0][8]}">
                     <br>Image:<br>
                     <input type="text" name="Image" value="{data[0][9]}">
                     <br>Phone:<br>
                     <input type="text" name="Phone" value="{data[0][10]}">
                     <br>Dob:<br>
                     <input type="text" name="Dob" value="{data[0][11]}">
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
                                <form method = 'POST' enctype= 'multipart/form' >
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
                     <input type="number" name="Longitude" value="">
                     <br>Latitude:<br>
                     <input type="number" name="Latitude" value="">
                     <br>Image:<br>
                     <input type="text" name="Image" value="">
                     <br>Phone:<br>
                     <input type="number" name="Phone" value="">
                     <br>Dob:<br>
                     <input type="date" name="Dob" value="">
                     <br><br>
                     <input type = "submit" value="submit">
                     </form>
                    '''
                self.output += form
                self.output += '<html><body></body></html>'
                self.setHeaders()
                self.wfile.write(self.output.encode())
                return

            if path[1] == ("Delete"):
                Id = path[2]
                data=self.db.Delete(f"Id={Id}")
                self.output += '<html><body>Deleted<br><a href="http://localhost:1995/Home" class="button">Home</a></body></html>'
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
                              <td> 
                                <a href="http://localhost:1995/Delete/{each[0]}" class="button">Delete</a>
                                <a href="http://localhost:1995/Update/{each[0]}" class="button">Update</a>

                                </tr>
                            ''')
                self.output += '</table><br><a href="http://localhost:1995/Home" class="button">Home</a></body></html>'
                self.setHeaders()
                self.wfile.write(self.output.encode())
                return 

        except IOError:
            self.send_error(400)

    def do_POST(self):
    
        #self.send_response(301)
        #self.end_headers()
        length = int(self.headers.get('content-length'))
        field_data = self.rfile.read(length).decode()
        fields = parse_qs(field_data,keep_blank_values=1)
        for key in fields:                
            fields[key]=fields[key][0]
        path = self.path.split("/")
        if path[1] == 'Create':
            self.db.Create(fields) 
            self.output += '<html><body>Created<br><a href="http://localhost:1995/Home" class="button">Home</a></body></html>'
            self.setHeaders()
            self.wfile.write(self.output.encode())
                          
        elif path[1] == 'Update':
            each = fields
            Id =path[2]
            data=self.db.Update(fields,Id)
            self.output += '<html><body>Updated<br><a href="http://localhost:1995/Home" class="button">Home</a></body></html>'
            self.setHeaders()
            self.wfile.write(self.output.encode())
        else:
            print('Pass')
    


