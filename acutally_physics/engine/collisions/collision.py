from engine.body import Circle, Rectangle
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

    def circleRectangleCollision(self, obj1, obj2):
        print("circle, rect")