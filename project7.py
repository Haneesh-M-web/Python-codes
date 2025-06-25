print("NAME: Haneesh M")
print("USN:1AY24AI038")
print("SECTION:M")
import math
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
class Circle:
    def __init__(self, center, radius): self.center, self.radius = center, radius
class Rectangle:
    def __init__(self, corner, width, height): self.corner, self.width, self.height = corner, width, height
def point_in_circle(circle, point):
    dx = point.x - circle.center.x
    dy = point.y - circle.center.y
    return math.hypot(dx, dy) <= circle.radius
def rect_in_circle(circle, rect):
    return all(point_in_circle(circle, Point(rect.corner.x + dx, rect.corner.y + dy))
               for dx in (0, rect.width) for dy in (0, rect.height))
def rect_circle_overlap(circle, rect):
    return any(point_in_circle(circle, Point(rect.corner.x + dx, rect.corner.y + dy))
               for dx in (0, rect.width) for dy in (0, rect.height))
c = Circle(Point(150, 100), 75)
r = Rectangle(Point(100, 50), 100, 50)
print(point_in_circle(c, Point(150, 100)))     
print(point_in_circle(c, Point(230, 100)))     
print(rect_in_circle(c, r))                    
print(rect_circle_overlap(c, r))
