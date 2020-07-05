#!/usr/bin/python3

import paramiko

try:
    con = paramiko.client.SSHClient()
    con.load_system_host_keys()
    con.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    con.connect(
        '127.0.0.1', 
        username='developer', 
        password='4linux', 
        port=22 #Parametro opcional
    )
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

stdin, stdout, stderr = con.exec_command('cat /etc/os-release')

#Se o comando for executado com sucesso
if stdout.channel.recv_exit_status() == 0:
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))

con.close()