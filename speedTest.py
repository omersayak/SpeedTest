import speedtest 
from time import sleep
import os


sleep(6)
os.system("cls")
os.system("color a")
test = speedtest.Speedtest()
test.get_servers()
sleep(0.5)
best_server = test.get_best_server()
sleep(0.5)
print("Testing Download Speed...")
download = test.download()
print("Testing Upload Speed...")
upload = test.upload()
ping = test.results.ping
os.system("cls")
print("PROFESOR SpeedTest\n")
print("-------------------------------------------------")
print(f"Server : {best_server['host']}\nCountry : {best_server['country']}\nDOWNLOAD :{download / 1024 / 1024:.2f} Mbps\nUPLOAD :{upload / 1024 / 1024:.2f} Mbps\nPing :{ping}")
# print(best_server)
print("-------------------------------------------------\n")
input("Press Enter to exit...")
