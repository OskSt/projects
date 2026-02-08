from engine.body import Circle, Rectangle
from pygame import Vector2 
import math

class Collisions:
    def check(self, objects):
        n = len(objects)

        for i in range(n):
            for j in range(i + 1, n):
                obj1 = objects[i]
                obj2 = objects[j]

                if isinstance(obj1, Circle) and isinstance(obj2, Circle):
                    self.circleCircleCollision(obj1, obj2)
                elif isinstance(obj1, Circle) and isinstance(obj2, Rectangle):
                    self.circleRectangleCollision(obj1, obj2)

    def circleCircleCollision(self, obj1, obj2):
        # Check collison 
        distance = math.sqrt(math.pow((obj1.pos.x - obj2.pos.x), 2) + math.pow((obj1.pos.y - obj2.pos.y), 2))
        if  distance <= obj1.radius + obj2.radius:
            # do collision
            return True
        return False

    def circleRectangleCollision(self, circle, rect):
        """ Check the distance between circle center and closest point on rectabngle"""
        closestX = max(rect.pos.x, 
                       min(circle.pos.x, rect.pos.x + rect.width))
        
        closestY = max(rect.pos.y, 
                       min(circle.pos.y, rect.pos.y + rect.height))
        
        diff_x = circle.pos.x - closestX
        diff_y = circle.pos.y - closestY

        distance = math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))

        if distance <= circle.radius:

            if distance == 0:
                left = abs(circle.pos.x - rect.pos.x)
                right = abs(circle.pos.x - (rect.pos.x + rect.width))
                top = abs(circle.pos.y - rect.pos.y)
                bottom = abs(circle.pos.y - (rect.pos.y + rect.height))
                min_distance = min(left, right, top, bottom)

                if min_distance == left:
                    normal = Vector2(-1, 0)
                elif min_distance == right:
                    normal = Vector2(1, 0)
                elif min_distance == top:
                    normal = Vector2(0, -1)
                elif min_distance == bottom:
                    normal = Vector2(0, 1)             
            else: 
                normal = Vector2(diff_x, diff_y) / distance
            
            depth = circle.radius - distance
            circle.pos += normal * depth

            velocity_dot = circle.velocity.dot(normal)

            if velocity_dot < 0:
                circle.velocity -= (1 + 0.8) * velocity_dot * normal
                print(circle.velocity)

