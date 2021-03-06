#Author : BehzaDMagzer
import os
user_name=os.popen("echo %username%").read().replace('\n','')
path_="C:\\Users\\{}\\AppData\\ginfo.txt".format(user_name)
def oscommand(com,desk):
	res=os.popen(com).read().replace("\x00",'')
	res+="\n\n"
	title="--=[ {} ]=--\n\n".format(desk)
	f=open(path_,'a')
	f.write(title)
	f.write(res)
	f.close()
commmands=[
("netsh firewall show state","state of firewall")
,("whoami /all","user and privilege information")
,("net users","list users")
,("net accounts","net accounts")
,("gpresult /z","user settings")
,("systeminfo","system information")
,("ipconfig /all","ip configuration information")
,("route print","machines routing table")
,("ipconfig /displaydns","display the contents of the DNS resolver cache ")
,("arp -a","ARP table")
,("nbtstat -n","lists local NetBIOS names")
,("qwinsta /counter /vm","information about remote desktop dervices sessions")
,("net share","view shared resources on network")
,("fsutil fsinfo drives","drives on system")
,("tasklist /M","lists all tasks and dlls")
,("tasklist /V","displays verbose task information")
,("netstat -ano","to see what services are running on what ports")
,("netstat -r","displays the routing table")
,("net config workstation","information about the configuration of the workstation")
,("net start","view list processes started upon startup")
,("sc query state=all","enumerates all services & drivers")
,("wmic startup list full","view list processes started upon startup(wmic)")
,("wmic bios","show information about bios")
,("wmic qfe","show information about updates")
,("wmic service","show services")
,("wmic os","show information about os")
,("wmic process get caption,executablepath","show process")
,("wmic logicaldisk get name,freespace,systemname,filesystem,size,volumeserialnumber","show information about logicaldisk")
,("wmic useraccount get /all","")
,("wmic PRODUCT get name,version,installlocation","show list programs installed")
]
for i in commmands:
	oscommand(i[0],i[1])
