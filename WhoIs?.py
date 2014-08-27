from subprocess import call


IP = raw_input("Enter an IP : ")
print  call(["whois", IP])
