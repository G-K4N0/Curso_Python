#!/usr/bin/python3

import re, sys, subprocess

if len(sys.argv) !=2:
    print("\n [!] Uso: python3" + sys.argv[0] + " <direccion-ip> \n")
    sys.exit(1)

def get_ttl(ip_addres):
    proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_addres,""],stdout = subprocess.PIPE, shell=True)
    (out,err) = proc.communicate()
    
    out = out.split()
    out = out[12].decode('utf-8')

    print(out)
if __name__ == '__main__':
    ip_addres =sys.argv[1]
    print(ip_addres)

    get_ttl(ip_addres)

