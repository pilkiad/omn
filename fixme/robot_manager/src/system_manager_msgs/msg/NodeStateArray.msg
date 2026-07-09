# Published by the Health Monitor on every poll cycle. Parallel arrays:
# node_names[i] is in states[i]. Kept flat instead of a nested message
# array because it's simpler for a future dashboard frontend to consume.

string[] node_names
string[] states       # unconfigured, inactive, active, finalized, unknown
builtin_interfaces/Time stamp
