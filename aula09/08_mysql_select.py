#!/usr/bin/python3

import MySQLdb

try:
    con = MySQLdb.connect(host='localhost', user='admin', passwd='4linux', db='projeto')
    cur = con.cursor()
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    cur.execute("select * from usuarios;")
    #for dado in cur:
    #    print(dado)
    #print(cur.fetchone())
    print(cur.fetchall())
except Exception as e:
    print('Erro: {}'.format(e))
finally:
    cur.close()
    con.close()