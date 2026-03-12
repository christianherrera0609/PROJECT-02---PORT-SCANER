#Port Scaner
import socket

def check_port1(x):
    ports={}
    y=x+1

    for i in range(1,y):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                answer=s.connect_ex(("scanme.nmap.org",i))
                if answer == 0:
                    ports[f"Port {i}"]= "Open"
                else:
                    ports[f"Port {i}"]= "Close"
        except socket.gaierror:
            ports[f"Port {i}"]= "No Found"
    
    return ports

def check_port(lista):
    ports2={}
    for i in lista:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                answer=s.connect_ex(("scanme.nmap.org",i))
                if answer == 0:
                    ports2[f"Port {i}"]= "Open"
                else:
                    ports2[f"Port {i}"]= "Close"
        except socket.gaierror:
            ports2[f"Port {i}"]= "No Found"
    return ports2

x="y"
while x == "y":
    x = input("Do you have the ports to scan? (Y/N): ").lower()
    if x == "y":
        list1=input("type the port's number with ',': ").split(",")
        list1=[int(p.strip()) for p in list1]
        results=check_port(list1)
        print (results)
    else:
        amount=int(input("Until wich port do you want to scan: "))
        results=check_port1(amount)
        print (results)
    
    x= input("Do you want to scan another port?: ")



            











