from enum import Enum, auto
from typing import Dict

import pygame as pg
from pygame import Surface

from shape import ShapeData, draw_ellipse, draw_rect


class State(Enum):
    IDLE = auto()
    ACCELERATING = auto()
    SLOWING_DOWN = auto()


def get_shape_data(
    screen: Surface, position: tuple[float, float], state: State
) -> ShapeData:
    return {
        State.IDLE: ShapeData(screen, position, (80, 80), (0, 0, 255)),
        State.ACCELERATING: ShapeData(screen, position, (80, 60), (255, 0, 0)),
        State.SLOWING_DOWN: ShapeData(screen, position, (80, 80), (0, 255, 0)),
    }[state]


DRAW_MAP = {
    State.IDLE: draw_rect,
    State.ACCELERATING: draw_ellipse,
    State.SLOWING_DOWN: draw_rect,
}


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
    def __init__(self, initial_state: State = State.IDLE):
        self.state = initial_state

    def trigger(self, event: Event):
        if event in TRANSITIONS[self.state]:
            self.state = TRANSITIONS[self.state][event]

    def update(self, shape_data: ShapeData) -> pg.Rect:
        assert isinstance(self.state, State), f"FSM corrupted: {self.state!r}"
        return DRAW_MAP[self.state](shape_data)
