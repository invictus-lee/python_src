import os,time

def parent(rfd,wfd):
    while True:
        line = os.read(rfd,60)
        print os.getpid(),'child read',line 
        time.sleep(1)
        os.write(wfd,'child write')
        time.sleep(1)

def child(rfd,wfd):
    while True:
        os.write(wfd,'child write')
        time.sleep(1)
        line = os.read(rfd,60)
        print os.getpid(),'parent read',line 
        time.sleep(1)

    
def main():
    p_r,c_w = os.pipe()
    c_r,p_w = os.pipe()
    if os.fork() == 0 :
        os.close(p_w)
        os.close(p_r)
        child(c_r,c_w)
    else:
        os.close(c_r)
        os.close(c_w)
        parent(p_r,p_w)

if __name__ == '__main__':
    main()
