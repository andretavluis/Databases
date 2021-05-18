#!/usr/bin/python3
import psycopg2
import login
import cgi



form = cgi.FieldStorage()
sname_old = form.getvalue('sname')
saddress_old = form.getvalue('saddress')

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
    
    sql = "SELECT * FROM substation WHERE sname = '{}' AND saddress = '{}';".format(sname_old, saddress_old)
    cursor.execute(sql)
    result = cursor.fetchall()

    # Displaying supervisors
    print('<h3>Changing Substation Supervisor:</h3>')
    print('<table border="5">')
    for row in result:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('</tr>')
    print('</table>')
    
    
    sql = 'SELECT * FROM supervisor WHERE (name, address) NOT IN (SELECT sname, saddress FROM substation);'
    cursor.execute(sql)
    result = cursor.fetchall()

    # Displaying supervisors
    print('<h3>Available Supervisors:</h3>')
    print('<table border="5">')
    print('<tr><td>Name</td><td>Address</td></tr>')
    for row in result:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('</tr>')
    print('</table>')
    
    
    print('<h3>New Substation Supervisor:</h3>')
    print('<form action="sb_update.cgi" method="post">')
    print('<input type="hidden" name="sname_old" value="{}">'.format(sname_old))
    print('<input type="hidden" name="saddress_old" value="{}">'.format(saddress_old))
    print('<p>New Supervisor Name: <input type="text" name="sname"/></p>')
    print('<p>New Supervisor Address: <input type="text" name="saddress"/></p>')
    print('<p><input type="submit" value="Submit"/></p>')
    
    # Closing connection
    cursor.close()
except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
    print('<form action="page.cgi" method="get">')
    print('<p><input type="submit" value="Return"/></p>')
    print('</form>')
finally:
    if connection is not None:
        connection.close()

print('</body>')
print('</html>')