	<<<0-transfer_file>>>
Write a Bash script that transfers a file from our client to a server:

Requirements:

Accepts 4 parameters
The path to the file to be transferred
The IP of the server we want to transfer the file to
The username scp connects with
The path to the SSH private key that scp uses
Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
scp must transfer the file to the user home directory ~/
Strict host key checking must be disabled when using scp
	
we use apt-get -y install what_u_want_to_install to install something in ubuntu without the system asking for permission
to install nginxwe use apt-get -y install nginx
to start nginx we use - service nginx start