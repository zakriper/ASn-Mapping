#!/usr/bin/python3
import requests
import pyfiglet
import socket
from dns import reversename
import dns.resolver
import ipaddress


class bcolors:
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightblue='\033[94m'
    lightcyan='\033[96m'

text = "Cybersecurity_DZ "
print(pyfiglet.figlet_format(text))
print(bcolors.green + "ASn-mapping is simple Tool To Map A Large Company Network By Getting Autonomous System  Number , IPs Addresses And Domains To Each IP Address")
print(bcolors.cyan + "contact us on : \n Website : https://itsecuritydz.wordpress.com/ \n Instagrame : @cybersecurity_dz \n Facebook : https://www.facebook.com/cisco2bit")
print("\n")

try:
    domain = input(str(bcolors.cyan + "Enter Target Domain : "))
except:
    print(bcolors.red + 'OPS are sure you put a string format')

def org(domain) :
    try : 
        resolver = dns.resolver.resolve(domain , "A")
    except:
        print(bcolors.red + "please check your connection or your target domain")
    for result in resolver:
        org = domain.split(".")[0]
        print(bcolors.blue + "=========================================================================")
        print(bcolors.lightcyan + "{}  Has Adress : ".format(org) + "{}".format(result))
        print(bcolors.blue + "=========================================================================")

        
    url = "https://api.hackertarget.com/aslookup/?q={}".format(result)
    AS_req = requests.get(url)
    ASn = AS_req.text.split(",")[1].replace('"' , "")
    print(bcolors.lightcyan + '{} autonomous system number :'.format(org) ,bcolors.green + "{}".format(ASn))
    print("=========================================================================")
    AS_url = "https://api.hackertarget.com/aslookup/?q=AS{}".format(ASn)
    IPs_req = requests.get(AS_url)
    print(bcolors.orange + "{}".format(IPs_req.text))
    
    while True:
        
        choice = input(str(bcolors.cyan + 'Do You Want Get Domains From this addresses yes/no ?? : '))
        if choice == "no" or choice == "NO":
            print(bcolors.lightcyan +"Very smart people are often tricked by hackers, by phishing. I don't exclude myself from that. It's about being smarter than a hacker. Not about being smart.\n")
            print(bcolors.green + "Happy Hac****")
            quit()
        elif choice == "yes" or choice == "YES":
            
            ip = input(str(bcolors.cyan + "choose IP/prefix  : "))
            network = ipaddress.IPv4Network(ip)
            
            for addr in network:
                try:
                    domain = socket.gethostbyaddr(str(addr))[0]
                    print(bcolors.green + "{} --------------->".format(addr) , domain)
                except:
                    print(addr , bcolors.red +  ' --------------->  No PTR Record')
    
org(domain)   

