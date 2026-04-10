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
                    self.CircleCircleCollision(obj1, obj2)
                elif isinstance(obj1, Circle) and isinstance(obj2, Rectangle):
                    self.circleRectangleCollision(obj1, obj2)

    def CircleCircleCollision(self, circle1, circle2):
        diff_x = circle1.pos.x - circle2.pos.x
        diff_y = circle1.pos.y - circle2.pos.y

        distance = math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))
        radius_sum = circle1.radius + circle2.radius

        if distance < radius_sum:
            if distance == 0:
                normal = Vector2(1, 0)
            else:
                normal = Vector2(diff_x, diff_y) / distance

            depth = radius_sum - distance
            circle1.pos += normal * depth / 2
            circle2.pos -= normal * depth / 2

            relative_velocity = circle1.velocity - circle2.velocity

            velocity_dot = relative_velocity.dot(normal)

            if velocity_dot > 0:
                return

            circle1.velocity += -(1 + 0.8) * velocity_dot * normal * 0.5
            circle2.velocity -= -(1 + 0.8) * velocity_dot * normal * 0.5

            

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
                """ Manually decide the normal since divison by 0 does not work """
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
                if abs(circle.velocity.y) < 15: #treat small velocities as 0
                    circle.velocity.y = 0
            print("Y speed: ", circle.velocity)

