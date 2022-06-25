############################
## IMPORTING WHAT WE NEED ##
############################

import sys
import os
import time
import subprocess
from colorama import init, Fore, Back, Style
init()


########################################################################################################


##########################
## THE IP PINGER ITSELF ##
##########################

def main():
	
	os.system("cls")
	# set the title to "En attente..."
	os.system("title Waiting for a ip...")
	print(Fore.MAGENTA + "\n▀█▀ █▀▀█ ░░ ▒█▀▀█ ▀█▀ ▒█▄░▒█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ ")
	print(Fore.MAGENTA + "▒█░ █░░█ ▀▀ ▒█▄▄█ ▒█░ ▒█▒█▒█ ▒█░▄▄ ▒█▀▀▀ ▒█▄▄▀ ")
	print(Fore.MAGENTA + "▄█▄ █▀▀▀ ░░ ▒█░░░ ▄█▄ ▒█░░▀█ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█")

	ip = input(Fore.LIGHTYELLOW_EX + "[" + Fore.BLUE + "Ip-Pinger" + Fore.LIGHTYELLOW_EX + "]" + Fore.WHITE + " Please enter an ip : ")
	
	# fait une boucle infini
	print("\n")
	while True:
		# check if ip is online without making the cmd "ping" appear
		if subprocess.call("ping -n 1 " + ip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
			os.system("title Pinging " + ip + " [-] Status { ONLINE }")
			print(Fore.LIGHTYELLOW_EX + "[" + Fore.BLUE + "Ip-Pinger" + Fore.LIGHTYELLOW_EX + "]" + Fore.GREEN + " IP is online")
		else:
			os.system("title Pinging " + ip + " [-] Status { OFFLINE }")
			print(Fore.LIGHTYELLOW_EX + "[" + Fore.BLUE + "Ip-Pinger" + Fore.LIGHTYELLOW_EX + "]" + Fore.RED + " IP Offline")
			time.sleep(0.5)

	
########################################################################################################


#####################
## END OF THE FILE ##
#####################

if __name__ == "__main__":
	main()
	sys.exit(0)
	
