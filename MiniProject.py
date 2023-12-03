import os
from sys import *
import smtplib,ssl
import urllib.error
import urllib.request

def is_connected():  #check only for internal connection
    try:
        urllib.request.urlopen('http://www.gmail.com')  
        return True #connection is true
    except urllib.error.URLError as err:
        return False #connection is false

def MailSender(mailid):
    try:
        fromadd = "patilparesh9112002@gmail.com" #from where
        toadd = mailid    # to send

        Message = """

        Hello %s,

        November 22, 2021 
        Mr. Sooraj 
        A S House No.25 Ghadoli Village, 
        Phase-3, Delhi-110096 
        Ph: +91-6238839813  
        
        DearSooraj, 
        Welcome to Infosys! 

            Today,the corporate landscape is dynamic and the world ahead is full of possibilities! 
            None of the amazing things we do at Infosys would be possible without an equally 
            amazing culture, the environment where ideas can flour is hand where you are empowered 
            to move for war far as your ideas will take you.

        Warm regards,

        RICHARD LOBO 
        EVP and Head Human Resources -InfosysLimited



                                                        INFOSYS LIMITED
                                                        CIN - L85110KA1981PLC013115
                                                        44, Infosys Avenue
                                                        Electronics City, Hosur Road
                                                        Bangalore 560 100, India

         """%(toadd)

        s = smtplib.SMTP('smtp.gmail.com',587)  #smtp is protocall #587 = port number

        s.starttls() #use of smtp only for security purpose

        s.login(fromadd,"whgr mobe vnwn lbgy")  # (user_name, password)

        s.sendmail(fromadd,toadd,Message)  #atual mail is send(from,to,msg)

        s.quit()  #our security is close and cache memory is clear
        
        print("Mail Successfully Send")
        print("\n")
        print("-------- END ----------")

    except Exception as E:
        print("Unable to send mail.",E)       

def main():

    if(len(argv) == 2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("This Script is used to send mail")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : ApplicationName")
            exit()

    try:
        print("\n")
        print("----------- PYTHON ACTIVITY TA-3 -------------")
        print("\n")
        print("----------- AUTO MAIL SENDER PROJECT ------------ ")
        print("\n")
        print("Please wait for send a mail few seconds ...")
        print("\n")

        MailSender("patilparesh2021@gmail.com")
        

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()    


#sender = on two step verication 