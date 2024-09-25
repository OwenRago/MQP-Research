cd /sys/kernel/debug/tracing
echo 1 > tracing_on
#cat available_tracers
echo schedule > set_ftrace_filter
echo $$ > set_ftrace_pid
echo > trace
sleep 1
cat trace
echo 0 > tracing_on