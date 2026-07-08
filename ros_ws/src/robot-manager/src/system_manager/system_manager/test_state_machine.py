from state_machine import StateMachine
from models import RobotState

sm = StateMachine()

print(sm.get_state())

print(sm.transition(RobotState.INITIALIZING))

print(sm.get_state())

print(sm.transition(RobotState.READY))

print(sm.get_state())

print(sm.transition(RobotState.UNKNOWN))

print(sm.get_state())