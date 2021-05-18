#!/usr/bin/python3
import psycopg2
import login
import cgi

form = cgi.FieldStorage()
ID = form.getvalue('id')
instant = form.getvalue('instant')

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
    
    
    print('<h3>Update incident description</h3>')
    sql = "SELECT * FROM incident WHERE id = '{}' AND instant = '{}';".format(ID, instant)
    cursor.execute(sql)
    result = cursor.fetchall()
    print('<table border="5">')
    print('<tr><td>Instant</td><td>ID</td><td>Description</td><td>Severity</td></tr>')
    for row in result:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('</tr>')
    print('</table>')

    # The form will send the info needed for the SQL query
    print('<form action="inc_update.cgi" method="post">')
    print('<input type="hidden" name="id" value="{}">'.format(ID))
    print('<input type="hidden" name="instant" value="{}">'.format(instant))
    print('<p>\nNew Description:</p>')
    print('<textarea rows = "5" cols = "60" name = "description"> </textarea><br>')
    print('<p><input type="submit" value="Submit"/></p>')
    print('</form>')

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