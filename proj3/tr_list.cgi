#!/usr/bin/python3
import psycopg2
import login

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
    
    sql = 'SELECT * FROM transformer;'
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)

    # Displaying transfomers
    print('<table border="5">')
    print('<tr><td>ID</td><td>pv</td><td>sv</td><td>gpslat</td><td>gpslong</td><td>pbbid</td><td>sbbid</td></tr>')
    for row in result:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('<td><a href="tr_remove.cgi?id={}">Remove Transformer</a></td>'.format(row[0]))
        print('</tr>')
    print('</table>')
    print('<td><a href="tr_insform.cgi">Insert Transformer</a></td>')



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