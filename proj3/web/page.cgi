#!/usr/bin/python3
import psycopg2
import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Proj 3</title>')
print('</head>')
print('<body>')
print('<h1>SIBD Project Part 3 - Main Menu</h1>')
print('<h3>Group 7</h3>')
print('<h3> 90121 - Joaquim Inacio</h3>')
print('<h3> 98638	- Andre Luis</h3>')
print('<h3> 87734	- Pedro Santos</h3>')
connection = None
try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    print('<p><a href="bb_list.cgi">List Busbars</a></p>')
    print('<p><a href="tr_list.cgi">List Transformers</a></p>')
    print('<p><a href="sb_list.cgi">List Substations</a></p>')
    print('<p><a href="all_list.cgi">List All Elements</a></p>')
    print('<p><a href="inc_regform.cgi">Register Incident</a></p>')
    print('<p><a href="inc_list.cgi">Edit Incident Description</a></p>')

    #Closing connection
    cursor.close()

except Exception as e:
    print('<h1>An error occurred.</h1>')
    
finally:
    if connection is not None:
        connection.close()

print('</body>')
print('</html>')