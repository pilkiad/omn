# Published by the Dashboard Backend whenever the Task Scheduler changes
# the state of a task. One message = one task's current status.

string task_id
string task_name
string state          # QUEUED, RUNNING, INTERRUPTED, REJECTED, DONE, FAILED
uint8 priority
string reason
builtin_interfaces/Time stamp
