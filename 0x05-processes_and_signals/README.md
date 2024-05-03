a process is an instance of execution of a program
every process has its own id which is always positive
for small computers the PID is 32768 however processes in cloud may require even more id
what limits a processs ID is its RAM
ps - a command that means process status
ps is used to display the current running process and so unlike top, its output is not in realtime
to get more information about a process use ps -u
ps -A is used to list all the processes


TOP
used to give information about processses in real time along with cpu usage and memory


SIGNALS
they are a response to a user interruption for example CTRL D

TASK 1

$$ represents a pid in shell scripting
RESEARCH CONCLUSIONS AND OBSERVATIONS

$? shows exit status of the previous execution
$0 represents the script name i.e stores the file name f the current script
$# shows the number of command line arguenments passed to the shell program


TASK2

ps is a commmandthat gives the current process status 
it has some ways of representing the data e.g

ps -A - diplays both system processses and user processes
ps -x - displays all processes including those thatdont have a controling TTY
ps -u - displays information about processes owned by a specific user
ps -f -display process information including process hierachy i.e parent child information
