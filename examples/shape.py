#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import sf


def main():
    window = sf.RenderWindow(sf.VideoMode(640, 480), 'Shape example')
    window.framerate_limit = 60
    running = True
    circle0 = sf.Shape.circle(50, 50, 50, sf.Color.YELLOW)
    circle0.position = (100, 100)
    
    rect0 = sf.Shape.rectangle(0, 0, 100, 50, sf.Color.GREEN, 2, sf.Color.BLUE)
    rect0.position = (200, 400)
    
    rect1 = sf.Shape.rectangle(0.0, 0.0, 50.0, 50.0,
                                         sf.Color.CYAN)
    rect1.position = (400, 100)
    
    line0 = sf.Shape.line(0, 0, 640, 480, 5, sf.Color.RED)
    
    points = [(0.0, 50.0), (50.0, 50.0), (25.0, 0.0)]
    shape0 = sf.Shape()

    for point in points:
        shape0.add_point(point[0], point[1])

    shape0.position = (300, 200)
    shape0.color = sf.Color(50, 100, 200, 128)
    shape0.origin = (25.0, 32.0)
    
    shapes = [line0, circle0, rect0, rect1, shape0]

    while running:
        for event in window.iter_events():
            if event.type == sf.Event.CLOSED:
                running = False

        window.clear(sf.Color.WHITE)
        shape0.rotate(2)

        for s in shapes:
            window.draw(s)

        window.display()

    window.close()


if __name__ == '__main__':
    main()
