writer :leonar
the project is on shell permissions .
its main use is to know how to gain permission into files from another source so as to work on the files
the permissions are shown better in the long format where read has a value of 4,write has a value of 2 and execute has a value of 1
commands learnt will include :
a)sudo and su to become a super user
chown to change ownership,chgrp to change group
b)whoami to identify yourself with the shell
c)add user which is used to add a nw user account
NB:syntax for add user is;
	sudo adduser nameof new user
NB: to remove youself from being a super user ,one presses exit
	an alternate method is used. Rather than using su, these systems employ the sudo command instead. With sudo, one or more users are granted superuser privileges on an as needed basis. To execute a command as the superuser, the desired command is simply preceded with the sudo command.
eg sudo ls
   sudo cd
   sude pwd
NB: sudo can also be used to change ownership for example if we wanted to change ownership from katana to leo,we would write;
	sudo chown leo file_name
wc -l -> prints the number of lines in a file
in scripting it is always important to use chmod u+x file name
and the file script inside should contain #!/bin/bash
