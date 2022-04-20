import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
   
    
    if subprocess.call(command) == 0:
        msg = 'Ping  ' + host +  ' successfully :)'
    else:
        msg= 'Ping  ' + host +  ' failed :('

    return msg
host = '172.24.0.3'
print('\n',ping(host),'\n')

def ping(host1):
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
 # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host1]
   
    
    if subprocess.call(command) == 0:

       msg = 'Ping  ' + host1 +  ' successfully :)'
    else:

     msg= 'Ping  ' + host1 +  ' failed :('
  
  
    return msg
host1 = '172.25.0.2'
print('\n',ping(host1),'\n')


def ping(host2):
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
 # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host2]
   
    
    if subprocess.call(command) == 0:

       msg = 'Ping  ' + host2 +  ' successfully :)'
    else:

     msg= 'Ping  ' + host2+  ' failed :('
  
  
    return msg
host2 = '172.25.0.3'
print('\n',ping(host2),'\n')



