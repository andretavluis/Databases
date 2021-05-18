#!/usr/bin/python3
import psycopg2
import cgi
import login

form = cgi.FieldStorage()
transformer_id = form.getvalue('id')

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
    
    # Making query
    sql = "DELETE FROM transformer WHERE id = '{}'".format(transformer_id)
    cursor.execute(sql)
    
    sql = "DELETE FROM analyses WHERE id = '{}';".format(transformer_id)
    cursor.execute(sql)
    
    sql = "DELETE FROM incident WHERE id = '{}'".format(transformer_id)
    cursor.execute(sql)
    
    sql = "DELETE FROM element WHERE id = '{}'".format(transformer_id)
    cursor.execute(sql)
    connection.commit()
    
    
    cursor.close()
    
    
    print('<h3>Transformer Removed Successfully!</h3>')
    print('<form action="page.cgi" method="get">')
    print('<p><input type="submit" value="Return"/></p>')
    print('</form>')


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