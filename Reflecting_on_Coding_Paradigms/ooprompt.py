from enum import Enum, auto

class Condition(Enum):
    PERFECT = auto()
    TRASHED = auto()
    REPAIRED = auto()

class Podracer:
    def __init__(self, max_speed, price, condition=Condition.PERFECT) -> None:
        self.max_speed = max_speed
        self.condition = Condition
        self.price = price

    def repair(self) -> None:
        self.condition = Condition.REPAIRED

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2
    
class SebulbasPod(Podracer):
    def flame_jet(self, other):
        if isinstance(other, Podracer):
            other.condition = Condition.TRASHED


def main():
    pod = Podracer(max_speed=3, price=1000)
    pod.repair()
    print(pod.condition)

    # Scenario 2
    new_pod = AnakinsPod(max_speed=2, price=2000)
    new_pod.boost()
    print(new_pod.max_speed)

    # Scenario 3
    third_pod = SebulbasPod(max_speed=5, price=3000)
    another_pod = Podracer(max_speed=3, price=1500)
    third_pod.flame_jet(another_pod)
    print(another_pod.condition) 

if __name__ == "__main__":
    main()




