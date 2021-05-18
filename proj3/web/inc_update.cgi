#!/usr/bin/python3
import psycopg2
import login
import cgi

form = cgi.FieldStorage()
ID = form.getvalue('id')
instant = form.getvalue('instant')
description = form.getvalue('description')

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
    connection.autocommit	=	False	
    cursor = connection.cursor()
    
    sql = "UPDATE incident SET description = '{}' WHERE id = '{}' AND instant = '{}';".format(description, ID, instant)
    cursor.execute(sql)
    connection.commit()
        
    print('<h3>Incident Description Updated Successfully!</h3>')
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