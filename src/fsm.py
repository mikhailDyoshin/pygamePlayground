from enum import Enum, auto
from typing import Dict


class State(Enum):
    IDLE = auto()
    ACCELERATING = auto()
    SLOWING_DOWN = auto()


class Event(Enum):
    ACCELERATE = auto()
    SLOW_DOWN = auto()
    STOP = auto()


TRANSITIONS: Dict[State, Dict[Event, State]] = {
    State.IDLE: {
        Event.ACCELERATE: State.ACCELERATING,
    },
    State.ACCELERATING: {
        Event.SLOW_DOWN: State.SLOWING_DOWN,
    },
    State.SLOWING_DOWN: {
        Event.ACCELERATE: State.ACCELERATING,
        Event.STOP: State.IDLE,
    },
}


class FSM:
    def __init__(
        self,
        transitions: Dict[State, Dict[Event, State]],
        initial_state: State = State.IDLE,
    ):
        self.state = initial_state
        self._transitions = transitions

    def trigger(self, event: Event):
        if event in self._transitions[self.state]:
            self.state = self._transitions[self.state][event]
        print(f"State: {self.state}")


fsm_inst = FSM(transitions=TRANSITIONS)
