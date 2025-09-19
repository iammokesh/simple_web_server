from http.server import HTTPServer,BaseHTTPRequestHandler
content='''<html
><h1>configuration of laptop</h2>
<h2>laptop specification</h2>
<pre>Device name       Hp zbook furry g17
Device Name	Mokesh
Processor	    Intel(R) Xeon(R) W-10885M CPU @ 2.40GHz   2.40 GHz
Installed RAM	64.0 GB (63.8 GB usable)
Storage     	954 GB SSD SAMSUNG MZVL21T0HCLR-00BH1
Graphics Card	NVIDIA Quadro RTX 3000 (6 GB), Intel(R) UHD Graphics P630 (128 MB)
Device ID	    F8CDCC10-A1B4-41F6-BEE2-F05A4A397DD3
Product ID  	00391-70000-00000-AA518
System Type 	64-bit operating system, x64-based processor
Pen and touch	No pen or touch input is available for this display
</pre>
<h2>Window specification</h2>
<pre>
Edition	Windows 10 Pro for Workstations
Version	22H2    OS Build	19045.6332
</pre>


<\html>
'''
class myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")        
server_address =('',8000)
httpd =HTTPServer(server_address,myserver)

httpd.serve_forever()        
    
