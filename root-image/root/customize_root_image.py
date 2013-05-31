import os
import commands
import sys

# configure lightdm
lightdmconfig = open("/etc/lightdm/lightdm.conf", "r")
newlightdmconfig = open("/etc/lightdm/lightdm.conf.new", "w")

for line in lightdmconfig:
    line = line.rstrip("\r\n")
    if(line.startswith("#greeter-session=")):
        newlightdmconfig.write("greeter-session=lightdm-bbqlinux-greeter\n")
    elif(line.startswith("#user-session=")):
        newlightdmconfig.write("user-session=mate\n")
    elif(line.startswith("#autologin-user=")):
        newlightdmconfig.write("autologin-user=bbqlinux\n")
    elif(line.startswith("#autologin-user-timeout=0")):
        newlightdmconfig.write("autologin-user-timeout=0\n")
    else:
        newlightdmconfig.write("%s\n" % line)

lightdmconfig.close()
newlightdmconfig.close()

os.system("rm /etc/lightdm/lightdm.conf")
os.system("mv /etc/lightdm/lightdm.conf.new /etc/lightdm/lightdm.conf")
