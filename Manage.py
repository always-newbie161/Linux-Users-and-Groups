import subprocess


def runcmd(command):
    try:
        subprocess.call(command)
        success = True 
    except subprocess.CalledProcessError as e:
        output = e.output.decode()
        success = False

    return success    

def addUser(accountname,homedir):
    command = ['sudo', 'useradd','-d',homedir,accountname]
    success = runcmd(command)

    
def addGroup(groupname):
    command = ['sudo' ,'groupadd',groupname]
    success = runcmd(command)

def addUserToGroup(accountname,*groupnames):
    command = ['sudo',usermod,'-a','-G']
    for gname in groupnames:
        command.append(gname)
    command.append(accountname)
    success = runcmd(command)

def groupDel(groupname):
    command = ['sudo','groupdel',groupname]
    success = runcmd(command)

def userDel(accountname,removedirfiles):
    command = ['sudo','userdel',accountname]
    if(removedirfiles):
        command.insert(2,'-r')
    success = runcmd(command)
    
def delUserFromGroup(accountname,groupname):
    command = ['sudo','gpasswd','-d',accountname,groupname]
    success = runcmd(command)
    
def setUserPassword(accountname):
    command = ['sudo','passwd',accountname]
    success = runcmd(command)

def setGroupPassword(groupname):
    command = ['sudo','gpasswd',groupname]
    success = runcmd(command)

def removeGroupPassword(groupname):
    command = ['sudo','gpasswd','-r',groupname]
    success = runcmd(command)

def giverootAccessToUser(accountname):
    addUserToGroup(accountname,'sudo')

def removerootAccessToUser(accountname):
    delUserFromGroup(accountname,'sudo')

    
      
        

adduser("newuser8","newuser5","shell","/home/qwerty")
