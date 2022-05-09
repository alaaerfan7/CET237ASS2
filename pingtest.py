import platform    # For getting the operating system name
import subprocess  # For executing a shell command


def ping(host,host1,host2):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    command2 = ['ping', param, '2', host1]
    command3 = ['ping', param, '3', host2]

  #call(...): Runs a command, waits for it to complete, then returns the return code.
    if subprocess.call(command) == 0:   #if the command provided above is equal to 0, show the msg succeccfully pinged, else ping failed)

        msg = 'Ping  ' + host +  ' successfully :)'
      
    else:
        msg= 'Ping  ' + host +  ' failed :('
    


    if subprocess.call(command2) == 0:
        msg = 'Ping  ' + host1 +  ' successfully :)'
    else:
        msg= 'Ping  ' + host1 +  ' failed :('


    if subprocess.call(command3) == 0:
        msg = 'Ping  ' + host2 +  ' successfully :)'
    else:
        msg= 'Ping  ' + host2 +  ' failed :('



    return msg
host = '172.24.0.3'
host1 = '172.25.0.2'
host2 = '172.25.0.3'
print('\n',ping(host,host1,host2),'\n') 




