bgreen="\033[1;32m"       # Green
bblack="\033[1;30m"       # Black
r="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
y="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
p="\033[1;35m"      # Purple
c="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White
logo=bgreen+str("""
$$$$$$$$\          $$\                 
\____$$  |         $$ |                
    $$  /$$\   $$\ $$$$$$$\   $$$$$$\  
   $$  / $$ |  $$ |$$  __$$\ $$  __$$\ 
  $$  /  $$ |  $$ |$$ |  $$ |$$ /  $$ |
 $$  /   $$ |  $$ |$$ |  $$ |$$ |  $$ |
$$$$$$$$\\$$$$$$  |$$$$$$$  |\$$$$$$  |
\________|\______/ \_______/  \______/ 
                                       

$$$$$$$\                
$$  __$$\               
$$ |  $$ | $$$$$$\  $$\ 
$$$$$$$  | \____$$\ \__|
$$  __$$<  $$$$$$$ |$$\ 
$$ |  $$ |$$  __$$ |$$ |
$$ |  $$ |\$$$$$$$ |$$ |
\__|  \__| \_______|$$ |
              $$\   $$ |
              \$$$$$$  |
               \______/ 
               
               
               
               
=================================================================
     ★★★ [✓] Devoloper : Zuboraj ★★★     
=================================================================

""")
import os
while True:
	os.system("clear")
	print(logo)
	print(r+""" [1] Start Sms bombing\n [0] Exit """)
	a=str(input(c+""" 
[✓] Select your option : """+y))
	if a=="1":
		os.system("python3 01z.py")
		a=input()
	elif a=="0":
		print(c+""" 
		Thanks for using 
		★★★Zubo Raj Tool★★★       
		""")
		quit()
		a=input()
	else:
		print(p+"Wrong Value Enterd")
		a=input()