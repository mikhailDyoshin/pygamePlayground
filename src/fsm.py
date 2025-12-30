from enum import Enum, auto
import pygame as pg
from dataclasses import dataclass
from typing import Dict


@dataclass
class ShapeData:
    screen: pg.Surface
    position: tuple[float]
    size: tuple[float]
    color: tuple[int]


def draw_ellipse(data: ShapeData) -> pg.Rect:
    rect = pg.Rect(data.position, data.size)
    pg.draw.ellipse(data.screen, data.color, rect)


def draw_rect(data: ShapeData) -> pg.Rect:
    rect = pg.Rect(data.position, data.size)
    return pg.draw.rect(data.screen, data.color, rect)


class State(Enum):
    IDLE = auto()
    ACCELERATING = auto()
    SLOWING_DOWN = auto()

def get_shape_data(screen, position: tuple[float], state: State) -> ShapeData:
    return {    
        State.IDLE: ShapeData(screen, position, (80, 80), (0, 0, 255)),
        State.ACCELERATING: ShapeData(screen, position, (80, 60), (255, 0, 0)),
        State.SLOWING_DOWN: ShapeData(screen, position, (80, 80), (0, 255, 0))
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


TRANSITIONS: Dict[State, Dict[Event, State]]  = {
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

