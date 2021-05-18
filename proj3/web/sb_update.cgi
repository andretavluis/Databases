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
    sql = "SELECT * FROM substation WHERE sname = '{}' AND saddress = '{}';".format(form.getvalue('sname_old'), form.getvalue('saddress_old')) #AND saddress = '{}'
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
      sql = "UPDATE substation SET sname = '{}', saddress = '{}' WHERE sname = '{}';".format(form.getvalue('sname'), form.getvalue('saddress'), form.getvalue('sname_old'))
      cursor.execute(sql)
    # Commit the update (without this step the database will not change)
    connection.commit()
    
    cursor.close()
    
    
    print('<h3>Substation Updated Successfully!</h3>')
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