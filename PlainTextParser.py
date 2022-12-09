import string
import re
import subprocess, platform


user_input = input("Please enter your input: ")

a_string = user_input
new_string = a_string.translate(str.maketrans('', '', string.punctuation))

def multiple_replace(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in sorted(rep_dict,key=len,reverse=True)]), flags=re.DOTALL)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)
   

clean_string = multiple_replace(new_string, {'Backslash':'','Semicolon':';','Comma':',','RTT':'','Key':'','Ping':'','board':'','Type':'','Backspace':'','LeftShift':'','LeftWindows':'','Return':'','Space':' ','LeftAlt':'','Period':'.'})

if platform.system()=="Windows":
    if platform.release() in {"10", "11"}:
        subprocess.run("", shell=True) #Needed to fix a bug regarding Windows 10; not sure about Windows 11
        print("\033c", end="")
    else:
        subprocess.run(["cls"])
else: #Linux and Mac
    print("\033c", end="")

print(clean_string)
