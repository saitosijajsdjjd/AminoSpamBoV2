import amino
import concurrent.futures
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.CYAN)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminospambov2", font="drpepper"))
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
chats = sub_client.get_chat_threads(size=150)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chatx = chats.chatId[int(input("Выберите чат/Select the chat: "))-1]

def threadpoolspam():
	while True:
		with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
			print("Spamming")
			_ = [executor.submit(sub_client.send_message, chatx, message, msgtype) for _ in range(5000000)]
			
def threadpoolboost():
	while True:
		with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
			_ = [executor.submit(threadpoolspam) for _ in range(5000000)]
			
threadpoolboost()
