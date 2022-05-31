import os, shutil, colorama

colorama.init()

print("""
\033[33m
  _____       _____                     _                      
 |___ /_  __ | ____|_ __   ___ ___   __| | ___ _ __            
   |_ \\ \\/ / |  _| | '_ \\ / __/ _ \\ / _` |/ _ \\ '__|           
  ___) >  <  | |___| | | | (_| (_) | (_| |  __/ |              
 |____/_/\\_\\ |_____|_| |_|\\___\\___/ \\__,_|\\___|_|_             
 |  _ \\  ___ / _ \\| |__  / _|_   _ ___  ___ __ _| |_ ___  _ __ 
 | | | |/ _ \\ | | | '_ \\| |_| | | / __|/ __/ _` | __/ _ \\| '__|
 | |_| |  __/ |_| | |_) |  _| |_| \\__ \\ (_| (_| | || (_) | |   
 |____/ \\___|\\___/|_.__/|_|  \\__,_|___/\\___\\__,_|\\__\\___/|_|   

                 \033[34mBy \033[37m@MrBlackX
    """)

def sendTo(filename, content):
    e = open(filename, "w")
    e.write(content)
    e.close()

def openF(filename):
    return open(filename, "r").read()

for file in sorted(os.listdir()):
    if file.endswith(".php"):
        print("\033[35m"+file)

filename = input("\n\033[34m[\033[37mFILENAME\033[34m] \033[32m: ")

shutil.copyfile(filename, filename+".bak")

layer = 1

while("eval" in openF(filename)):
    shutil.copyfile(filename, filename+".bak")
    r = openF(filename)
    print(f"\033[34m\n================================\n\033[37mLayer : \033[32m{layer}\033[34m\n================================\n")
    if 'eval("?>".' in r:
        print("\033[34m[\033[32mLOG\033[34m::\033[32mFOUND_EVAL\033[34m]")
        sendTo("temp.php", r.replace('eval("?>".', "print_r("))
        print("\033[34m[\033[32mLOG\033[34m::\033[32mSTRINGS_REPLACED\033[34m]")
        if os.system("php temp.php > temp") == 0:
            print("\033[34m[\033[32mLOG\033[34m::\033[32mSOURCE_EXTRACTED\033[34m]")
            os.remove("temp.php")
            shutil.move("temp", filename)
            print("\033[34m[\033[32mLOG\033[34m::\033[32mFILE_MOVED\033[34m]")
            layer+=1
            print("\033[34m[\033[32mLOG\033[34m::\033[32mLAYER_COMPLETED\033[34m]")
        else:
            print("\033[34m[\033[31mERROR\033[34m::\033[31mNO_PHP_EXECUTEABLE\033[34m]")
            break
    elif "eval('?>'." in r:
        print("\033[34m[\033[32mLOG\033[34m::\033[32mFOUND_EVAL\033[34m]")
        sendTo("temp.php", r.replace("eval('?>'.", "print_r("))
        print("\033[34m[\033[32mLOG\033[34m::\033[32mSTRINGS_REPLACED\033[34m]")
        if os.system("php temp.php > temp") == 0:
            print("\033[34m[\033[32mLOG\033[34m::\033[32mSOURCE_EXTRACTED\033[34m]")
            os.remove("temp.php")
            shutil.move("temp", filename)
            print("\033[34m[\033[32mLOG\033[34m::\033[32mFILE_MOVED\033[34m]")
            layer+=1
            print("\033[34m[\033[32mLOG\033[34m::\033[32mLAYER_COMPLETED\033[34m]")
        else:
            print("\033[34m[\033[31mERROR\033[34m::\033[31mNO_PHP_EXECUTEABLE\033[34m]")
            break
    else:
        print("\033[34m[\033[31mERROR\033[34m::\033[31mNO_EVAL_FOUND\033[34m]")
        break

print(f"\n\033[34m[\033[32mLOG\033[34m::\033[32mLAYERS_FOUND\033[34m::\033[32m{layer}\033[34m]")