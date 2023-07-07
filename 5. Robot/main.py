from robot import Robot

if __name__ == "__main__":
    robot1 = Robot('R1')
    robot1.introduce()
    Robot.number_active_robots()

    robot2 = Robot('R2')
    robot2.introduce()
    Robot.number_active_robots()

    robot1.remove()

    robot3 = Robot('R3')
    robot3.introduce()
    Robot.number_active_robots()

    robot2.remove()
    robot3.remove()

    Robot.number_active_robots()
    print(robot1)
