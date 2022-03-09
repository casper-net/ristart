# /menu.py/single_download.py
# single download page
#
import os

# GUI
def main():
	mid = "||####################################||"
	blank = "||########                    ########||"
	print(mid)
	print("||#########    APPLICATION   #########||")
	print("||########      DOWNLOAD      ########||")
	print(blank)
	print("||########  1  )  NMAP        ########||")
	print(blank)
	print("||########  2  )  WIRESHARK   ########||")
	print(blank)
	print("||########  3  )  HYDRA       ########||")
	print(blank)
	print("||########  4  )  TOR         ########||")
	print(blank)
	print("||########  5  )  PROXYS      ########||")
	print(blank)
	print("||########  6  )  DUCKDUCKGO  ########||")
	print(blank)
	print("||########  7  )  METASPLOIT  ########||")
	print(blank)
	print("||########  8  )  DROPBOX     ########||")
	print(blank)
	print("||########  9  )  VPN         ########||")
	print(blank)
	print("||########  10 )  DOWNLOAD    ########||")
	print(blank)
	print("||########  11 )  DOWNLOAD    ########||")
	print(blank)
	print("||########  12 )  DOWNLOAD    ########||")
	print(blank)
	print("||########  13 )  DOWNLOAD    ########||")
	print(blank)
	print("||########  14 )  DOWNLOAD    ########||")
#Make Console GUI
	app = input("  Enter Application Number  :  ")
	if app == "back":
		import menu
	elif app == '1':
		pass

	elif app == '2':
		pass

	elif app == '3':
		pass

	elif app == '4':
		print("Downloading Tor...")
		tor()


	else:
		pass


# Functions to Download Apps
def tor():
	cd = "sudo cd ~/RiStart/apps/Tor"
	download = "bash install_tor64.sh"
	os.system(cd)
	os.system(download)