# /menu.py
# App for linux that installs and is used as a hub for some KALI Linux tools
#
#
import os
import single_download

def gui_top():
	hash_main = "||####################################||"
	hash_up = " //##################################\\\\"	
	hash_up2 = "  //################################\\\\"
	#GUI
	print(hash_up2)
	print(hash_up)
	print(hash_main)
	print(hash_main)
		
				
def gui_bot():
	hash_main = "||####################################||"
	hash_dwn = " \\\\##################################//"
	hash_dwn2 = "  \\\\################################//"
	#GUI
	print(hash_main)
	print(hash_main)
	print(hash_dwn)
	print(hash_dwn2)


def gui_logo():
	print("||____________________________________||")
	print("||_____________Welcome To_____________|| ")
	print("||______________RiSTART_______________||")
	print("||____________________________________||")
	print("||____________________________________||")
	print("||____________________________________||")
#
#
#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  MAKE THEMES FOR TABS IN THE CREAT TAB
#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#
#

	
def gui_two_top():
	print("  _____________________________________     _____________________________________")
	print("//#############################TAB 1##\\\\  //#############################TAB 2##\\\\")
	print("||##########  APPLICATION  ###########||  ||##########    SELECTED    ##########||")
	print("||##########  INFORMATION  ###########||  ||##########  APPLICATIONS  ##########||")
	print("||####################################||  ||####################################||")
	print("||####################################||  ||####################################||")
	

def gui_two_bot():
	print("\\\\####################################//  \\\\####################################//")
	print(" \\\\##################################//    \\\\##################################//")

def gui_two_blank():
	print("||########                    ########||  ||########                    ########||")


def console():
	print("  _______________________|||__________")
	print("//______INPUT____________|||__________\\\\")
	print("||_________BELLOW________|||__________||")
	print("\\\\_____________________\\\\___//________//")
	print(" \\\\_____________________\\\\_//________//")
	
			
def main():
	start()


def start():
	gui_top()
	gui_logo()
	gui_bot()
	menu_gui()
	menu_select()


def menu_gui():
	space = "||                                    ||"
	sep = "||####################################||"
	gui_top()
	print("||____________________________________||")
	print("||           Welcome to The           ||")
	print("||            RiSTART Menu            ||")
	print("||____________________________________||")
	print(space)
	print(sep)
	print(space)
	print("||      1  )     Single Download      ||")
	print(space)
	print(sep)
	print(space)
	print("||      2  )     System Search        ||")
	print(space)
	print(sep)
	print(space)
	print("||      3  )     Create System        ||")
	print(space)
	print(sep)
	print(space)
	print("||      4  )     RiSTART Help         ||")
	print(space)
	print(sep)
	print(space)
	print("||      5  )     Contact & Forums     ||")
	print(space)
	print(sep)
	print(space)
	print("||      6  )     Guides & Links       ||")
	print(space)
	gui_bot()
	
# Input and calls the selected function
def menu_select():
	console()
	selection = int(input("  Enter Menu Number  :   "))
	if selection == 1:
		single_download.main()
	elif selection == 2:
		search()
	elif selection == 3:
		create()
	elif selection == 4:
		help()
	elif selection == 5:
		contact()
	elif selection == 6:
		guide()
	else:
		print("||####################################||")
		print("||######!!! NOT A VALID INPUT !!!#####||")
		print("||####################################||")
		menu_select()
	

	
def search():
	gui_top()

#  DOUBLE SCREEN
# THE SELECTED GO ON TAB 2 AND ARE ABBREVIATED
# MAKE THEMES
# 15 MAX Apps in System for now
def create():
	ab = "AB"
	gui_two_top()
	gui_two_blank()
	print("||########  1  )  NMAP        ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  2  )  WIRE SHARK  ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  3  )  HYDRA       ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  4  )  TOR         ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  5  )  PROXYS      ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  6  )  DUCKDUCKGO  ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  7  )  DROPBOX     ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  8  )  VPN         ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  9  )  METASPLOIT  ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  10 )  METASPLOIT  ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  11 )  METASPLOIT  ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  12 )  METASPLOIT  ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  13 )  METASPLOIT  ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  14 )  METASPLOIT  ########||  ||########          ",ab,"      ########||")
	gui_two_blank()
	print("||########  15 )  METASPLOIT  ########||  ||########          ",ab,"      ########||")
	
	gui_two_blank()
	gui_two_bot()
def help():
	gui_top()


def contact():
	gui_top()


def guide():
	gui_top()



main()
