import sys
import schedule
import time
import os
import psutil
import smtplib
from email.message import EmailMessage
def createlog(foldername):
    border = "-" * 70
    print(border)
    
    
    ret = False
    ret = os.path.exists(foldername)
    if ret == True:
        ret = os.path.isdir(foldername)
        if ret == False:
            print("unable to create folder")
            return
        
    else:
        os.mkdir(foldername)
        print("Directory for log file created successfully")
        
    timestamp = time.strftime("%Y-%M-%d_%H_%M_%S")
    filename = os.path.join(foldername,"Marvellous_%s.log"%timestamp)
    print("log file creates successfully :",filename)
    
    fobj = open(filename,'w')
    
    fobj.write(border+"\n")
    
    fobj.write("-------------Marvellous platform Surveillance system---------")
    fobj.write(border+"\n")
    
    fobj.write("log file created at"+time.ctime()+"\n")
    fobj.write(border+"\n")
    
    fobj.write("--------------------system report------------------")
    
    fobj.write(border+"\n")
    
    
    
    for proc in psutil.process_iter(attrs=["pid","name"]):
        try:
            
            name =("process Name :",proc.info["name"])
            open_file =len( proc.open_files())

            pid =("PID :",proc.info["pid"])
            thread =("threads :",proc.num_threads())
            cpu = ("cpu usages :",proc.cpu_percent())
            mem = ("memory usages :",proc.memory_percent())
            
            data = f"{name}\n{pid}\n{thread}\ntimestamp : {timestamp}\nopen_file : {open_file}\ncpu usages : {cpu}%\nmemory usages : {mem}%\n"
            
            fobj.write(data)                           
        except:
            pass
        
    
    fobj.write(border+"\n")
    fobj.write("----------------------End of log file------------")
    fobj.write(border+"\n")
    fobj.close()

    
 
    sender = "potdardatta61@gmail.com"
    
    app_password = "hvmdrsyosvvbghjw"
    
    receiver_email = "shubhyapotdar@gmail.com",""
    log_file = filename
    
    
    schedule.every(30).seconds.do(Marvellous_send_mail,sender,app_password,receiver_email,log_file)
    while True:
         schedule.run_pending()
         time.sleep(1) 
    
    
    
def Marvellous_send_mail(sender,app_password,receiver_email,log_file):

    msg = EmailMessage()
    
    msg["From"]=sender
    msg["To"]=receiver_email
    msg["Subject"]=log_file
    
    
    msg.set_content("attached log file")
    
    
    with open(log_file,"rb") as f :
        msg.add_attachment(
            f.read(),
            maintype = "text",
            subtype ="plain",
            filename=log_file,
            
        )
    
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    
    smtp.login(sender,app_password)
    
    smtp.send_message(msg)
    
    smtp.quit()
    
    print(" Mail sent succesfully")
      
                   
def main():
    border = "- " * 70
    print(border)
    print("--------------------Thread monitouring system-------------")
    print(border)
    
    if(len(sys.argv) == 2):
        if(sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("this script is used to :")
            print("1 :create automatic log")
            print("2 :executes periodically")
            print("3 :sends mail with logs")
            print("4 :store information about process")
            print("5 :store information about cpu")
            print("6 :store information about RAM usages")
            print("7 :store information about secondary storage")
            
        elif(sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("use the automaton script as")
            print("Scriptname.py Time interval directoryname")
            print("timeinterval :the time in minutes for periodically schedulling")
            print("directory name : Naem of directory to create auto log")
            
        else:
            print("unable to proceed as there is no such option")
            print("please use --h or --u to get more details")  
                  
    elif(len(sys.argv) == 3):
        print("inside project  logic")
        print("time interval :",sys.argv[1])
        print("Directory name :",sys.argv[2])
        
        
        (createlog(sys.argv[2]))
        
        
        print("platform Survillence system started successfully")
        print("Directory created with name :",sys.argv[2])
        print("press ctrl + c to stop the execution")
        
        
        
        
    else:
        print("invalid number of command line arguments")
        print("unable to proceed as there is no such option")
        print("please use --h or --u to get more detials")
        
        
    print(border)
    print("-------------------Thankyou for using our script-----------")
    print(border)            
                
if __name__ =="__main__":
    main()