import platform    # For getting the operating system name
import subprocess  # For executing a shell command


def ping(Assigncontainer2,Assigncontainer3,Assigncontainer4):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', Assigncontainer2]
    command2 = ['ping', param, '2', Assigncontainer3]
    command3 = ['ping', param, '3', Assigncontainer4]

  #call(...): Runs a command, waits for it to complete, then returns the return code.
    if subprocess.call(command) == 0:   #if the command provided above is equal to 0, show the msg succeccfully pinged, else ping failed)

        msg = 'Ping  ' + Assigncontainer2 +  ' successfully :)'
      
    else:
        msg= 'Ping  ' + Assigncontainer2 +  ' failed :('
    


    if subprocess.call(command2) == 0:
        msg = 'Ping  ' + Assigncontainer3 +  ' successfully :)'
    else:
        msg= 'Ping  ' + Assigncontainer3 +  ' failed :('


    if subprocess.call(command3) == 0:
        msg = 'Ping  ' + Assigncontainer4 +  ' successfully :)'
    else:
        msg= 'Ping  ' + Assigncontainer4 +  ' failed :('



    return msg
Assigncontainer2 = 'Assigncontainer2'
Assigncontainer3 = 'Assigncontainer3'
Assigncontainer4 = 'Assigncontainer4'
print('\n',ping(Assigncontainer2,Assigncontainer3,Assigncontainer4,),'\n')





