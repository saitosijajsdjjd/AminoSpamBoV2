from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.CYAN)
print("Script by Zevi/Скрипт сделан Zevi")
print("┌────────────────────────────────────┐")
print("│Author :  LilZevi                   │")
print("│Github : https://github.com/LilZevi │")
print("└────────────────────────────────────┘")
print("YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ")
print("Telegram: @NowNameBo")
print("▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄ ▄▀▀ █▀▄ ▄▀▄ █▄░▄█ █▀▄ ▄▀▄")
print("█▀█ █░█░█ █ █░▀█ █░█ ░▀▄ █░█ █▀█ █░█░█ █▀█ █░█")
print("▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░ ▀▀░ █▀░ ▀░▀ ▀░░░▀ ▀▀░ ░▀░")
print("▐▌░▐▌ █▀▀ █▀▀▄ ▄▀▀ ▀ ▄▀▄ █▄░█ ▒▄▀▄")
print("░▀▄▀░ █▀▀ █▐█▀ ░▀▄ █ █░█ █░▀█ ░▒▄▀")
print("░░▀░░ ▀▀▀ ▀░▀▀ ▀▀░ ▀ ░▀░ ▀░░▀ ▒█▄▄")
chatlist = []
chatnames = {}
import amino
email = input("Email/Почта: ")
password = input("Password/Пароль: ")
message = input("Message/Сообщение: ")
msgtype = input("MessageType/Тип сообщения: ")
client = amino.Client()
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Выберите сообщество/Select the community: "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)
z=0
chats = sub_client.get_chat_threads(size=1000)
for name, id in zip (chats.title, chats.chatId):
	if name!=None:
		print(f"{z + 1}.{name}")  
		chatnames[x]=str(name)
		chatlist.append(str(id))
		z+=1
chatx = chatlist[int(input("Выберите чат/Select the chat: "))-1]

sub_client.send_message(chatId=chatx, message=message, messageType=msgtype)

while True:
	with concurrent.futures.ThreadPoolExecutor(max_workers=1000000) as executor:
		_ = [executor.submit(sub_client.send_message, chatx, message, msgtype) for _ in range(5000000)]
		
