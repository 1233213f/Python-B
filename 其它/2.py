#使用数据报套接字
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
pid1 = os.fork()

if pid1 < 0:
    print("创建一级子进程失败")

elif pid1 == 0:
    #创建二级子进程
    pid2 = os.fork()
    if pid2 < 0:
        print("创建二级子进程失败")
    elif pid2 == 0:
        do_chile(s)
    else:
    #一级子进程退出，使二级进程成为孤儿
        os.exit()
else:
    #等待一级子进程退出
    os.wait()
    do_parent()
