import pygame
import os
def draw_triangle(surface, color, points, width):
    pygame.draw.polygon(surface, color, points, width)
def find_midpoint(point1, point2):
    x = (int)((point1[0] + point2[0]) / 2)
    y = (int)((point1[1] + point2[1]) / 2)
    point = [x, y]
    return tuple(point)
def sierpinski(degree, p1, p2, p3, color, line_width, screen):
    if degree == 0:
        return
    else:
        points = tuple([p1,p2,p3])
        draw_triangle(screen, color, points, line_width)
        p1 = find_midpoint(points[0], points[1])
        p2 = find_midpoint(points[0], points[2])
        p3 = find_midpoint(points[1], points[2])
        draw_triangle(screen, color, tuple([p1, p2, p3]), line_width)
        sierpinski(degree - 1, points[0], p1, p2, color, line_width, screen)
        sierpinski(degree - 1, points[1], p1, p3, color, line_width, screen)
        sierpinski(degree - 1, points[2], p2, p3, color, line_width, screen)
        pygame.display.update()
if __name__ == "__main__":
    pygame.init()
    size = (800,610)
    surface = pygame.display.set_mode(size)
    pygame.display.set_caption("Sierpinski Triangles")
    surface.fill((0,0,0))
    degree = 7
    color = (255,255,255)
    points = [(400,0),(0,600),(800,600)]
    width = 1
    sierpinski(degree, points[0], points[1], points[2], color, width, surface)
    os.system("pause")
    pygame.quit()
