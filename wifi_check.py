import getpass
import paramiko
import time

HOST = raw_input("Office #: ")
ip_address = "172." + "18." + HOST + ".253"
username = ("username")
password = ("password")


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print("Successful connection")

remote_connection = ssh_client.invoke_shell()


remote_connection.send("show dot11 ass\n")


time.sleep(1)
output = remote_connection.recv(65535)
print(output)

ssh_client.close 
