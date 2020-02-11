#!/usr/bin/env python
import os, sys

def main():
    #Code to generate policy source module installation
    f=open("policy_source_installation.sh","w+")
    f.write("#!/bin/sh\n")
    f.write("#commands for installing policy source module\n")
    f.write("#set SELinux in permissive mode by changing /etc/selinux/config file (Don't forget to put the command touch /.autorelabel before SELinux mode change)\n")
    f.write("wget https://raw.githubusercontent.com/wiki/TresysTechnology/refpolicy/files/refpolicy-2.20180114.tar.bz2\n")
    f.write("tar -jxvf refpolicy-2.20180114.tar.bz2 -C /tmp\n")
    f.write("cd /tmp/refpolicy\n")
    f.write("make install-src\n")
    f.write("cd /etc/selinux/refpolicy/src/policy\n")
    f.write("#open build.conf file and uncomment DISTRO = redhat, make UNK_PERMS = allow, DIRECT_INITRC = y, SYSTEMD = y, MONOLITHIC = y and save the file\n")
    f.write("make install\n")
    f.write("make load\n")
    f.write("#change SELinux type as refpolicy in /etc/selinux/config file (Don't forget to put the command touch /.autorelabel before changing SELinux type)\n")
    f.close()

    #code to generate policy loading script
    path = os.getcwd()
    print(path)
    for file in os.listdir(path):
        if file.endswith(".te"):
            print("file found\n")
            print(file)
            #filename = os.path.splitext(file)[0]
            filename = path+file
            #print(filename)
    f=open("policy_integration.sh","w+")
    f.write("******Start of Adding new policy module********\n")
    f.write("sestatus\n")
    f.write("#check if SELinux status is enabled in permissive mode and Loaded policy name is refpolicy.\n")
    f.write("#create the .te file, write the policy and save it\n")
    f.write("make -f /usr/share/selinux/devel/Makefile ")
    f.write(filename+".pp\n")
    f.write("semodule -i ")
    f.write(filename+".pp\n")
    f.close()

if __name__ == '__main__':
    main()
