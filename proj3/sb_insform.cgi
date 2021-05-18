#!/usr/bin/python3
import psycopg2
import login
import cgi

form = cgi.FieldStorage()
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Proj 3</title>')
print('</head>')
print('<body>')
connection = None
try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()
    
    # The string has the {}, the variables inside format() will replace the {}
    print('<h3>Insert New Substation Data</h3>')
    # The form will send the info needed for the SQL query
    print('<form action="sb_insert.cgi" method="post">')
    print('<p>GPS Latitude: <input type="number" name="gpslat" step="0.000001"/></p>')
    print('<p>GPS Longitude: <input type="number" name="gpslong" step="0.000001"/></p>')
    print('<p>Locality: <input type="text" name="locality"/></p>')
    print('<p>Supervisor Name: <input type="text" name="sname"/></p>')
    print('<p>Supervisor Address: <input type="text" name="saddress"/></p>')
    print('<p><input type="submit" value="Submit"/></p>')
    print('</form>')
    
    # Displaying free supervisors
    
    print('<h3>Free Supervisors</h3>')
    sql = 'SELECT * FROM supervisor WHERE (name, address) NOT IN (SELECT sname, saddress FROM substation);'
    cursor.execute(sql)
    result = cursor.fetchall()
    print('<table border="5">')
    print('<tr><td>Name</td><td>Address</td></tr>')
    for row in result:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('</tr>')
    print('</table>')
    
    
    print('<h3>Existing Substations</h3>')
    # Displaying existing substations
    sql = 'SELECT * FROM substation;'
    cursor.execute(sql)
    result = cursor.fetchall()
    print('<table border="5">')
    print('<tr><td>gpslat</td><td>gpslong</td><td>locality</td><td>sname</td><td>saddress</td></tr>')
    for row in result:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('</tr>')
    print('</table>')
    
    
    print('<form action="page.cgi" method="get">')
    print('<p><input type="submit" value="Return"/></p>')
    print('</form>')
    
    # Closing connection
    cursor.close()
except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<form action="page.cgi" method="get">')
    print('<p><input type="submit" value="Return"/></p>')
    print('</form>')
finally:
    if connection is not None:
        connection.close()

print('</body>')
print('</html>')