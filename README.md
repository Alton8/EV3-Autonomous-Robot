# Autonomous EV3 Robot 🤖

This project controls a LEGO EV3 robot to **autonomously navigate an obstacle course** using color sensors and motor control.  
The robot detects different colored tape on the floor and performs programmed maneuvers — such as turning, stopping, or accelerating — based on the color identified.

## 🚀 Features
- Real-time **color detection** using the EV3 Color Sensor  
- **Motor control** for precise turns and speed adjustments  
- Configurable **RGB threshold ranges** for multiple tape colors (red, blue, yellow, black)  
- Continuous loop for responsive decision-making and navigation  
- Designed and tuned for **LEGO EV3 MicroPython v2.0**  

## 🧠 How It Works
1. The color sensor reads RGB values from the surface.  
2. The program compares them to predefined color ranges.  
3. Depending on the detected color, the robot performs an action — such as turning or stopping.  
4. If no color is detected, it drives straight until a new color is found.  

## 🧩 Tech Stack
- **Language:** Python (Pybricks MicroPython)  
- **Hardware:** LEGO Mindstorms EV3  
- **Libraries:** `pybricks.hubs`, `pybricks.ev3devices`, `pybricks.robotics`, `pybricks.tools`  

## 🏁 Getting Started
1. Flash your EV3 Brick with **Pybricks MicroPython v2.0 or higher**.  
2. Upload the script `autonomous_ev3_robot.py` to your EV3.  
3. Place colored tape strips on the floor and position the robot at the starting point.  
4. Run the program and watch it navigate autonomously!  

