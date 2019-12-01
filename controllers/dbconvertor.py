# -*- coding: utf-8 -*-

##from __future__ import print_function

import socket
session.forget(response)

# vvv=True - включает секртную сессию и выдает страницу ошибки
def not_is_local(vvv=None):
    http_host = request.env.http_host.split(':')[0]
    remote_addr = request.env.remote_addr
    #http_host[7pay.in] remote_addr[91.77.112.36]
    #raise HTTP(200, T('appadmin is disabled because insecure channel http_host[%s] remote_addr[%s]') % (http_host, remote_addr))
    try:
        hosts = (http_host, socket.gethostname(),
                 socket.gethostbyname(http_host),
                 '::1', '127.0.0.1', '::ffff:127.0.0.1')
    except:
        hosts = (http_host, )

    if vvv and (request.env.http_x_forwarded_for or request.is_https):
        session.secure()

    if (remote_addr not in hosts) and (remote_addr not in TRUST_IP):
        #and request.function != 'manage':
        if vvv: raise HTTP(200, T('ERROR: not admin in local'))
        return True

# запустим сразу защиту от внешних вызов
not_is_local(True)
# тут только то что на локалке

def to_mysql():
    db_old = DAL('sqlite://storage.sqlite',
         auto_import=True
         )

    import convert_db
    return convert_db.to_mysql(db, db_old)
