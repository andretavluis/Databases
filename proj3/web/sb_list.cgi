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

    # Making query
    sql = 'SELECT * FROM substation;'
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)

    # Displaying substations
    print('<table border="5">')
    print('<tr><td>gpslat</td><td>gpslong</td><td>locality</td><td>sname</td><td>saddress</td></tr>')
    for row in result:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('<td><a href="sb_remove.cgi?gpslat={};gpslong={}">Remove Substation</a></td>'.format(row[0], row[1]))
        print('<td><a href="sb_chgsup.cgi?sname={};saddress={}">Change Supervisor</a></td>'.format(row[3], row[4]))
        print('</tr>')
    print('</table>')
    print('<td><a href="sb_insform.cgi">Insert Substation</a></td>')

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
        con