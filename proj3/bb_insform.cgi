#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Proj 3</title>')
print('</head>')
print('<body>')

print('<h3>Insert New Busbar Data</h3>')
# The form will send the info needed for the SQL query
print('<form action="bb_insert.cgi" method="post">')
print('<p>Busbar ID: <input type="text" name="id"/></p>')
print('<p>Busbar Voltage: <input type="number" name="voltage"/></p>')
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')
print('<form action="page.cgi" method="get">')
print('<p><input type="submit" value="Return"/></p>')
print('</form>')

print('</body>')
print('</html>')