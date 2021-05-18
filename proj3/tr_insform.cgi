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

# The string has the {}, the variables inside format() will replace the {}
print('<h3>Insert New Transformer Data</h3>')
# The form will send the info needed for the SQL query
print('<form action="tr_insert.cgi" method="post">')
print('<p>Transformer ID: <input type="text" name="id"/></p>')
print('<p>Primary busbar ID: <input type="text" name="pbbid"/></p>')
print('<p>Primary Voltage: <input type="number" name="pv"/></p>')
print('<p>Secondary busbar ID: <input type="text" name="sbbid"/></p>')
print('<p>Secondary Voltage: <input type="number" name="sv"/></p>')
print('<p>GPS Latitude: <input type="number" name="gpslat" step="0.000001"/></p>')
print('<p>GPS Longitude: <input type="number" name="gpslong" step="0.000001"/></p>')
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')

connection = None
try:
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()


    # Displaying substations
    sql = 'SELECT * FROM substation;'
    cursor.execute(sql)
    result = cursor.fetchall()
    print('<h3>Available Substations</h3>')
    print('<table border="5">')
    print('<tr><td>gpslat</td><td>gpslong</td><td>locality</td></tr>')
    for row in result:
        print('<tr>')
        for value in range(len(row)-2):
            print('<td>{}</td>'.format(row[value]))
        print('</tr>')
    print('</table>')
    
    # Displaying busbars
    sql = 'SELECT * FROM busbar;'
    cursor.execute(sql)
    result = cursor.fetchall()
    print('<h3>Available Busbars</h3>')
    print('<table border="5">')
    print('<tr><td>ID</td><td>voltage</td></tr>')
    for row in result:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('</tr>')
    print('</table>')
    
    
    # Displaying transfomers
    sql = 'SELECT * FROM transformer;'
    cursor.execute(sql)
    result = cursor.fetchall()
    print('<h3>Already Existing Transformers</h3>')
    print('<table border="5">')
    print('<tr><td>ID</td><td>pv</td><td>sv</td><td>gpslat</td><td>gpslong</td><td>pbbid</td><td>sbbid</td></tr>')
    for row in result:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('</tr>')
    print('</table>')
    #Closing connection
    cursor.close()
    
except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<form action="page.cgi" method="get">')
    print('<p><input type="submit" value="Return"/></p>')
    print('</form>')
    
finally:
    if connection is not None:
        connection.close()


print('<form action="page.cgi" method="get">')
print('<p><input type="submit" value="Return"/></p>')
print('</form>')

print('</body>')
print('</html>')