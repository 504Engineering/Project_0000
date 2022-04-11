# Project_0000
Project 0000

- About:
    This is a revamped 6-axis robotic manipulator aimed to handle weights in excess of 10kg with ease. This manipulators construction/design/trouble-shooting will be throughly documented here on 
        Github, on Youtube, and on our website. This will be using NEMA 14 and NEMA 17 stepper motors for each one of the 6-axis of movement. 

- Requirements:
    - 6-axis of movement: Base rotation / Tilt 1 / Tilt 2 / Tilt 3 / Twist on claw / claw
    - Constrolled by a custom designed control board based on the Raspberry Pi Pico
    - Custom firmware written in C/C++ (research needing to be done for this)
    - Flexibility in required function
    - Modularity / Ease to repair

- Timeline: 
    Since I am an active college student, this project will be a do-as-I-please project. Meaning there is no deadline.

- Reasons for this project:
    To prove the effectiveness of 504 Engineering to others.
    This is the starting point for another project that will be created later
    To show others the fun and creativity that can go into robotics

- Progress:
    - 3/21/2022: Started / Creation of project 0000
    - 3/22/2022: Research into different gearing systems and manipulator designs from other companies. 
    - 3/23/2022: Gear ratio web based simulator found       http://www.thecatalystis.com/gears/
                 Using a series of planetary gear speed reducers should work, however the speed reducing part is a problem.
                 Using several 5-1 planetary gear boxes to increase torque.
    - 4/4/2022: Designed the first prototype of the base tilting mechanism. 
                Using 3 planetary gearboxes to increase torque. 
                Using a bevel gear system to translate the axis of rotation by 90 degrees.
                