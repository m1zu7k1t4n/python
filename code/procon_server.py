from __future__ import print_function
import socket
import select
import mysql.connector
import http.server

def main():
  host = '153.126.176.44'
  port = 4000
  backlog = 10
  bufsize = 4096
  http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler)
  server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  readfds = set([server_sock])
  try:
    server_sock.bind((host, port))
    server_sock.listen(backlog)

    while True:
      rready, wready, xready = select.select(readfds, [], [])
      for sock in rready:
        if sock is server_sock:
          conn, address = server_sock.accept()
          readfds.add(conn)
          request =''
        else:
          msg = sock.recv(bufsize)
          tmp = msg.split(",")
          num = len(tmp)
          if num == 3:
            request = sql_mountain(tmp)
            if len(request) == 1:
              sock.send(request)
            else:
              num = len(request)
              for i in range(num):
                sock.send(request[i])
          else:
            request = ctrl_sql(tmp)
            sock.send(request)
  finally:
    for sock in readfds:
      sock.close()
  return

def sql_mountain(order):
  mt_name = order[0]
  dl_info = order[2]
  switch_dl = 'map'
  try:
    cnn = mysql.connector.connect(host='localhost',
      port=3306,
      user='root',
      passwd='18Co27-g85-da',
      database='procon_app',
      charset="utf-8")
    cur = cnn.cursor(buffered=True)
    if dl_info == 0:
      cur.execute('select mapdata from procon_app where mtid = %s and coordinate = %s', (mt_name,switch_dl))
      dl_path = cur.fetchone()
      cnn.close()
      return dl_path

    if dl_info == 1:
      i = 0
      cur.execute('select * from procon_app where mtid = %s and coordinate != %s',(mt_name,switch_dl))
      for (mtid, coordinate, timedate, judgment, userid, comment, picture) in cur:
        tmp = [mtid, coordinate, timedate, judgment, userid, comment, picture]
        request[i] = ",".join(tmp)
        i = i + 1
      cnn.close()
      return deng_info

def ctrl_sql(order):
  mtid = order[0]
  coordinate = order[1]
  timedate = order[2]
  judgment = order[3]
  userid = order[4]
  comment = order[5]
  picture = order[6]
  try:
    cnn = mysql.connector.connect(host='localhost',
      port=3306,
      user='root',
      passwd='18Co27-g85-da',
      database='procon_app',
      charset="utf-8")
    cur = cnn.cursor()
    if comment != 0:
      cur.execute('insert into student_table (mtid, coordinate, timedate, judgment, userid, picture) values (%s, %s, %s, %s, %s, %s)',(mtid, timedate, judgment, userid, picture))
      cnn.close()
    else:
      cur.execute('insert into student_table (mtid, coordinate, timedate, judgment, userid, comment, picture) values (%s, %s, %s, %s, %s, %s, %s)',(mtid, timedate, judgment, userid, comment, picture))
      cnn.close()

if __name__ == '__main__':
  main()
