class Robot:
    active_robots = 0

    def __init__(self, input_name):
        self.name = input_name
        Robot.active_robots += 1

    def introduce(self):
        print(f"Hi! I'm {self.name}")

    def remove(self):
        print(f"Removing {self.name}")
        Robot.active_robots -= 1
        print(f"{self.name} was succesfully removed!")
        if (Robot.active_robots > 0):
            print(f"There are still {Robot.active_robots} active robots")
        elif (Robot.active_robots == 0):
            print(f"{self.name} was the last robot")
        del self

    @classmethod
    def number_active_robots(cls):
        print(f"There are {Robot.active_robots} active robots")
