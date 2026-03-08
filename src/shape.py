import pygame as pg
from dataclasses import dataclass


@dataclass(frozen=True)
class ShapeData:
    position: tuple[float, float]
    size: tuple[float, float]
    color: tuple[int, int, int]


def draw_ellipse(
        *,
        screen: pg.Surface, 
        shape: ShapeData
    ):
    rect = pg.Rect(shape.position, shape.size)
    pg.draw.ellipse(screen, shape.color, rect)


def draw_rect(
        *,
        screen: pg.Surface,
        shape: ShapeData
    ):
    rect = pg.Rect(shape.position, shape.size)
    pg.draw.rect(screen, shape.color, rect)
