#!/usr/bin/python

os = __import__('os')
from subprocess import check_output
import subprocess
import sys, traceback
import platform

def main():
       try:

                linux = "1"

                windows = "2"

                mac = "3"

                android = "4"


                print " "
                print " "
                print"                     /$$   /$$$$$$    /$$     /$$$$$$$$$$/
                print"        /        /   |__/ /     $$    |__/           /$$/
                print" /$$   | $$ |    | $$ /$$| $$ ___/     /$$|         /$$/
                print" |$$   | $$ |    | $$| $$| $$|        | $$|        /$$/
                print" |$$   | $$ |    | $$| $$| $$$$$      | $$|       /$$/
                print" |$$   | $$ |    | $$| $$| $$__/      | $$|      /$$/
                print" |$$   | $$ |    | $$| $$| $$|        | $$|     /$$/ 
                print" |$$$$$$$/$$$$$$$/   | $$| $$|        | $$|    /$$/
                print"  \_\____/ \____/____/___/___/        |___|   /__/
                print" "
                print"	Penulis: Riskis7 | Youtube: BENGKULU CYBER TEAM™| @risks7 V2.0			"

 
                print" "
                print "sistem apakah yang anda pakai ?."
                print " "
                print " 1) linux"
                print " 2) Windows"
                print " 3) Mac OS"
                print " 4) Android"
                print" "

                entrada = raw_input("> ")

                while entrada == linux and platform.system() == "Linux":
                        print " "
                        print "All wireless networks :"
                        print " "
                        command = "ls -1 /etc/NetworkManager/system-connections/"
                        proc = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
                        (out, err) = proc.communicate()
                        outwithoutreturn = out.rstrip('\n')
                        print outwithoutreturn
                        proc

                        print " "

                        print " Masukkan nama jaringan , setelah itu tekan (a) periksa jaringan anda."
                        print " "
                        nombre = raw_input("> ")
                        if nombre == "a":
                                print "\033[1;36m############################ - Informasi tentang semua jaringan - ############################\033[1;m" 	
                                wifi0 = os.system("egrep -h -s -A 9 --color -T 'ssid=' /etc/NetworkManager/system-connections/*")
                                print wifi0
                                print "\033[1;36m############################################################################################\033[1;m" 
                        else:
                                print "\033[1;36m###################################### - " + nombre + " - ######################################\033[1;m"
                                print " "

                                wifi0 = str(os.system("egrep -h -s -A 0 --color -T 'security=|key-mgmt=|psk=' /etc/NetworkManager/system-connections/" + nombre))
                                print " "
                                print "\033[1;36m#############################################################################################\033[1;m"
                                print " "

 

    

                while entrada == windows and platform.system() == "Windows":

 
                        print check_output("netsh wlan show profile key=clear", shell=True)
                        print "Insert the network name , or press (a) to see information about all networks. "
                        print " "
                        nombre = raw_input("> ")
                        if nombre == "a":

                                print "############################ - Informasi tentang semua jaringan - ############################" 
                                print " " 
                                wifi2 = check_output("netsh wlan show profile name=* key=clear", shell=True)
                                print wifi2
                                print " " 
                                print "#############################################################################################"
                       else:
                                print "###################################### - " + nombre + " - ######################################"
                                print " " 
                                wifi2 = check_output("netsh wlan show profile name=" + nombre +" key=clear", shell=True)
                                print " " 

                                print wifi2
                                print "#############################################################################################"
                                print " " 
                      guardar = raw_input(" Apakah Anda ingin menyimpan hasilnya ? [y/t] > ")
                      if guardar == "y":
                           f = open(nombre+'.txt','w')
                           f.write(wifi2 + '\n')
                           f.close()

 

           if entrada == mac:
                   print "android segera diluncurkan"

           else:
                   print " Silakan pilih satu opsi (1) for linux , (2) for windows , (3) for Mac OS and (4) for Android ."
    except KeyboardInterrupt:
            print " Shutdown diminta ... keluar "
    except Exception:
            traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
            main()

