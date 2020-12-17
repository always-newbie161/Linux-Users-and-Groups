# Users and Groups in Linux

  -   Linux is a multiuser Operating system. So multiple users can access a system simultaneously. So to make this possible, linux has a user and group management system which protects one’s resources from others.
    
-   Permissions to system files and directories are controlled through this user and group relation.
    

## Users:

-   There are three types of accounts in Linux/Unix system:
    

    1.)root

    2.)system account

    3.)user account(general users)

  

-   **Root user** is the one who has complete control of the Unix system and has all types of permission to all the files and directories and is able to run any commands in the shell.He is also called a superuser.
    
-   **System account** is a type of account in linux OS which is specific to a component of a system and is used for system defined purposes.These accounts are pre-created during installation of the OS.
    
-   **User account** are the type of accounts which are created for general users.These accounts have limited access to the system resources.Usually created to make a certain group of users as the owner of a particular directory/files.
    
   ## Groups: 
- To make file permissions and process management easier, Unix has a concept of **groups** which is a collection of user accounts. A user can be present in more than one group, however every user has one **primary group.**
- Primary group for every user is created with the same username by default, when the user account is created and it can be changed for every user.  

All the commands to create/delete/modify users and groups are root-only accessible commands. So only users  with `sudo` privileges are able to execute these commands.But this can be changed by changing the permissions in the `/etc/sudoers/` file but is it not preferable.

## Creating a new user:
All the user account information including password are stored at **etc/passwd/** file. So a new user account will be created in this file.
To create new user, one of these two commands can be used in Linux.

    sudo useradd username
    sudo adduser username

By default only root(sys-admin) has the access to add a user.But any user account who's given access to these commands can create a user.

`useradd` cmd is the native command but `adduser` command which has the former at the back-end is more user-friendly and easy to create default directories and required information of the user.

Along with the user account, a home dir a primary group(discussed later) will be created and the shell, userid, accountname  of the user can be specified through `useradd` cmd.

    sudo useradd -d homedir -g groupname -m -s shell -u userid accountname


 
 

## Creating a new group
All the groups are stored in **/etc/groups** ,So any new group added will be updated in this file.

    sudo groupadd groupname

More representable syntax is

     groupadd [-g gid [-o]] [-r] [-f] groupname
Here.  through 

 - ` gid`  we can specify the group id.

 - `-r` adds a system account.
 - `-o` permits to add non-unique id.
 - `-f` checks whether the given id already exists, if it is then it selects an other available unique id. 




## Adding a user to a Group
Groups in which a user is present is an attribute of the user.
To change he attributes of a user `usermode` command is used.
So to add the user to a group(s), group attribute of that particular user has to be updated.

    sudo usermode -a -G groupname groupname2 username
`-a -G` flag (also `--append --groups`)  is used to add the user to the groups specified in the command.These groups are the supplementary groups of the user along with the primary group.
### Changing the user's primary group
This can be done by using `-g` flag in the `usermod` command 

    sudo usermod -g  groupname username


## Deleting a Group
A group can be deleted from the system by using the `groupdel` command. Deletion of the group removes it from the `/etc/groups` file, but the files which are owned by this group will not be deleted and privileges of the users of this file will not be vanished. i.e they are still accessible by the users of the group.

    sudo groupdel groupname

## Deleting a User
A user can be deleted from the system and they are removed from their respective groups.`userdel` is the  command used to delete a user account from the unix system.The option/flag `-r` or `--remove` is used to remove the respective home directory and the files present in it.

    sudo userdel -r username
### Deleting a user from a group
This can be done by using `gpasswd` command. `-d`  flag is used to remove the user from the group.

    sudo gpasswd -d username groupname

## Setting and changing password of a user
Password is a must for a user and setting up of password for the user is automatically prompted when `adduser` is used.But to change the password again `passwd` command can be used.

    sudo passwd username
user is prompted to provide the current password and the new password.

## Setting and changing password of a group
Groups also have password and it is generally used when a user wants to login to a certain group to access and execute the files owned by it, then it can be restricted only the users who are members of the group and have the group password are allowed to access the files/directories owned by this group.

This can be done by using `gpasswd` command which is a group administration command with no flags.

    sudo gpasswd groupname


## Giving sudo root access to a user
Root access can be given to a certain user in a safer way is  by adding the user to the sudo group.

    sudo usermod -aG sudo username
## Removing sudo root access of a user
If the sudo root access is given to the user by adding the user into sudo group, then removing the user from the sudo group removes the sudo access for the user from the next login.

    sudo gpasswd -d username sudo
If the access is given to the user by editing  the `/etc/sudoers` file, then the file has to be again edited so that the permission is withdrawn.

`/etc/sudoers` has to be opened through `visudo`

    sudo visudo
    
## Giving Users/Groups permissions to certain tools
Users and Groups can be given access to some specific commands by specifying the same in the `/etc/sudoers` file.

This can be done as follows.

open `/etc/visudo` file by

    sudo visudo

This opens the vim editor.

This can  be done only by the users who have sudo root access.


In the file, `Cmnd_Alias` can be made for the commands that are to be given access. Users are specified by  their names and groups are specified by adding `%` prefix to the group name.

Now the user/group are assigned the commands.
Eg:
giving user "special_user" and the group "special_group", the access to /bin/ss and /bin/top  commands.

    Cmnd_Alias SS_TOP = /bin/ss, /usr/top
    special_user  ALL=(root) SS_TOP
    %special_group ALL = (root)SS_TOP
The access is given to all the hosts ( irrespective of the machine in the network)

## File Permissions
File permissions are access rights for a file/directory.(directory is also a file with 4096b size.)
The type of permissions are read `r`, write`w`, execute`x`.
These access rights are divided into three sets.
   

 - For the owner of the file/directory.
 - For the group of users in which owner is also a member.
 - Other than the owner and the users of group.
 
 Permissions are represented by ten characters.The first character specifies whether it is a file(`-`), directory(`d`), link(`l`) . The next 9 characters specify the access rights for the owner, group and others respectively 3 at a time.
 Eg:
 

    drwx-rw--r 
This shows that the file is a directory, the owner has all the permissions, group has read and write permission and others have only read permission

### Numerical representation of permission
The 9 digit code(excluding the first character) can be represented by a unique 3-digit number.

 - `r` contributes 4 ,`w` contributes 2  and  `x` contributes 1 to a digit number.
 - So each digit of the number ranges from 0-7 and uniquely represents all the 8 possible type of permissions.
 - Eg: 6 represents `rw-` ,4 represents `r--` , 760 represents `rwxrw----`.

### Special Permissions
There are some special permissions whichare used in some cases to have better security.

 - **sticky bit** is used to ensure that only the owner of the directory is able to rename/delete the files contained in the directory.This is not useful on a single file.
     - Eg:`chmod +t /spc/dir` to add sticky bit.
     - `chmod -t /spc/dir` to remove sticky bit.
    
 - **setuid** is used to allow the users who have executable permissions to have the privilege equivalent to the file owner. 
     - Eg: `chmod u+s /spc/dir` to setuid for the directory /spc/dir 
     - `chmod u-s /spc/dir` to remove setuid.
   
   
 - **setgid** is similar to setuid but the privilege is equivalent to the users of the group associated withe the file/directory.
    - Eg: `chmod g+s /spc/dir` to setgid for the directory /spc/dir 
     - `chmod g-s /spc/dir` to remove setgid.
   
 

## Modifying File Permissions
File permissions can be modified using the `rwx` representation or the numerical representation of the permission.

  `chmod` command is used to change the permission of a file/directory in both cases.

#### Using `rwx`


 - `u` represents owner of the file.
 - `g` represents the group of the file.
 - `o` represents others.
 - To add a certain access `+` is used and `-` is used to remove a access.
 - Eg: `chmod g+w filename`  gives write permission to the group associated to that file.

#### Using numerical

 - The 3-digit number is used to change the permissions
 - Eg:`chmod 760 /home/foo` this command changes the permissions of /home/foo directory to read, write, execute for the owner, only read and write for the group and no access to others.

## Changing Ownership
File/directory have default user_owner and group_owner as the one who created them.But the ownership can be changed by the root or the current owner of the file/directory by using `chown` command

#### Syntax of `chown` command

    chown user:group /path/to/file
Using this command the user and group ownership can be changed for the file and the directory.

If only user need to be changed group can be omitted and vice-versa.

Eg:
To make the user "special_user" the owner of the file "/spc/spc_file"
and change the permissions to read and write for the owner.

    chown special_user /spc/spc_file 
    chmod u+rw /spc/spc_file

Similarly to change the group owner to "special_group" and set the permissions to only read

    chown :special_group /spc/spc_file
    chmod g+r /spc/spc_file

But in the case of directory, the change in ownership is only limited to the directory but not the files contained in it.
So to change the ownership of the contents too `-R` flag can be used to recursively change the ownership.
Eg: `chown -R newowner:newgroup /spc/dir`
