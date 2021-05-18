#!/usr/bin/python3
import cgi
import psycopg2
import login

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
    
    print('<h3>Register New Report</h3>')
    # The form will send the info needed for the SQL query
    print('<form action="inc_insert.cgi" method="post">')
    print('<p>ID: <input type="text" name="id"/></p>')
    print('<p>Instant: <input type="datetime-local" name="instant"/></p>')
    print('<p>Description: </p>')
    print('<textarea rows = "5" cols = "60" name = "description"> </textarea><br>')
    print('<p>Severity: <input type="text" name="severity"/></p>')
    print('<p><input type="submit" value="Submit"/></p>')
    print('</form>')
    
    
    print('<h3>Existing Elements</h3>')
    sql = 'SELECT * FROM element;'
    cursor.execute(sql)
    result = cursor.fetchall()

    print('<table border="5">')
    print('<tr><td>ID</td></tr>')
    for row in result:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('</tr>')
    print('</table>')

    print('<form action="page.cgi" method="get">')
    print('<p><input type="submit" value="Return"/></p>')
    print('</form>')
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


print('</body>')
print('</html>')