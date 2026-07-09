# Published by the Dashboard Backend whenever the global Robot State
# Machine changes state, or the Recovery Manager starts/finishes a recovery.

string robot_state    # BOOTING, READY, MAPPING, NAVIGATING, BUSY, ERROR, RECOVERY, SHUTDOWN
bool healthy
string[] failed_nodes
string last_event
builtin_interfaces/Time stamp
