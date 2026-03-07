import pygame as pg
from dataclasses import dataclass


@dataclass
class ShapeData:
    position: tuple[float, float]
    size: tuple[float, float]
    color: tuple[int, int, int]


def draw_ellipse(
        *,
        screen: pg.Surface, 
        data: ShapeData
    ) -> pg.Rect:
    rect = pg.Rect(data.position, data.size)
    return pg.draw.ellipse(screen, data.color, rect)


def draw_rect(
        *,
        screen: pg.Surface,
        data: ShapeData
    ) -> pg.Rect:
    rect = pg.Rect(data.position, data.size)
    return pg.draw.rect(screen, data.color, rect)
