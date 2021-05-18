#!/usr/bin/python3
import psycopg2
import cgi
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
    connection.autocommit	=	False	
    cursor = connection.cursor()
    
    # Making query
    sql = "SELECT 1 FROM element WHERE id = '{}';".format(form.getvalue('id'))
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)
    if num == 0:
      sql = "INSERT INTO element VALUES('{}');".format(form.getvalue('id'))
      data = (form.getvalue('id'))
      cursor.execute(sql)
      
    sql = 'INSERT INTO transformer VALUES (%s, %s, %s, %s, %s, %s, %s);'
    data = (form.getvalue('id'), form.getvalue('pv'), form.getvalue('sv'), \
        form.getvalue('gpslat'), form.getvalue('gpslong'), form.getvalue('pbbid'), form.getvalue('sbbid'))
    cursor.execute(sql, data)
    connection.commit()
    
    cursor.close()
    
    print('<h3>Transformer Inserted Successfully!</h3>')
    
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