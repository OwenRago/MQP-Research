## Ftrace

### Requirements

Linux is required, WSL works as well but doesn't support all tracing features

Must have root access

### Pre tutorial/Bash script

Make sure to have root access, either change user to root through:

* sudo -s

or run sudo before each command

### Bash Script

Make sure to run the script as root, it will give the same final output as if you followed the tutorial

### Basic tutorial

First go to your tracing diretory

* cd /sys/kernel/debug/tracing

Next turn on tracing

* echo 1 > tracing_on

From here you can view which tracers you are able to access

* cat available_tracers

From here start tracing a function for example the schedule function

* echo schedule > set_ftrace_filter

Next pick which process you want to trace, here I trace the terminal

* echo $$ > set_ftrace_pid

Next clear your past traces

* echo > trace

Next you can do something that will trigger the function you are tracing, in this case sleep

* sleep 1

Now you can view the trace

* cat trace

When done disable tracing

* echo 0 > tracing_on
