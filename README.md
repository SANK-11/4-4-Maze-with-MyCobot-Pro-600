# 🧭 Solving a 4×4 Maze with MyCobot Pro 600

## 📘 Overview
This project develops an end-to-end pipeline to **solve 4×4 rectangular mazes** using the **MyCobot Pro 600**.  
A maze is printed on a plastic board within the AI Kit camera’s field of view. An algorithm detects the **entrance**, finds the **solution path** as **straight-line segments**, and determines the **exit** from a camera image. The solution is **validated in a digital twin** and then **executed on the robot**, where the end effector follows the path autonomously.

---

## 🎯 Objectives
- Detect maze entrance and exit from an image captured by the AI Kit camera.
- Compute a solution path composed of straight-line segments between grid cells.
- Convert image-space path to **physical waypoints** in the robot’s workspace.
- Validate the plan (FK/IK + path) in a **digital twin** before execution.
- Execute the path on the **MyCobot Pro 600** via **socket programming**.

---

## ⚙️ Prerequisites
- **MyCobot Pro 600** (calibrated) + monitor/keyboard/mouse (Roboflow OS)
- **AI Kit camera** mounted with a clear top-down view of the maze board
- **Ethernet** connection between robot and your computer
- **Python 3.x** (or MATLAB; other languages OK for sockets)
- Digital twin environment (e.g., MATLAB/Simscape, RoboDK, Gazebo, or your Lab 3/4 twin)
- Printed **4×4 maze** board, sized and placed within **3.5 × 3.5 inches** workspace

> ⚠️ **Safety**: Keep workspace clear, verify calibration, and simulate before real motion.

---

## 🧩 1) Maze Generation & Solving

### 1a. Generate a 4×4 Maze
- Use the provided **maze generation tool** to create a **4×4** (width=4, height=4) maze.
- **Inner width/height**: 0.
- Entrance may be **top** or **bottom** (not the inner room).
- **E** and **R** parameters ∈ [0, 100] (affect generation).
- Scale and position the printed maze within **3.5 × 3.5 in** workspace.
- Consult the tool’s help panel for parameter details.



### 1b. Solve the Maze (Vision → Path → Waypoints)
- Input: **Top-down image** from AI Kit camera.
- Detect grid, walls, and **entrance/exit** (binarization, line/contour detection, or template-based).
- Run a solver (e.g., BFS/DFS/A*) to get a **cell-to-cell path**.
- Convert the pixel path to **physical coordinates** (camera calibration + scaling).
- Output **ordered waypoints** (start → goal) as straight-line segments.
  - Waypoint count depends on maze layout.
  - Numbering can start at the **entrance** (top-entrance mazes count downward).


---

## 🦾 2) Digital Twin Path Planning

### 2a. Digital Twin (FK/IK + Motion)
Re-use your Lab 3/4 digital twin:
- **FK**: Compute end-effector pose from given joint angles.
- **IK**: Compute **realistic joint angles** for given end-effector waypoints.
- Given an ordered waypoint list, simulate robot motion to each waypoint.

> ❗ **Important**: You must perform **inverse kinematics**.  
> **Directly sending XYZ coordinates** to the real robot **without IK** is **strictly prohibited**.

### 2b. Path Planning Logic
- Define a **home pose** near the board that does **not** block the camera.
- Start pose may be **top or bottom** (examiner’s choice); handle both.
- After tracing the maze, **return to home**.
- Validate joint limits, self-collisions, and reachable workspace in sim.

---

## ▶️ 3) Execution & Recording

### 3a. System Setup
1. Position and secure the **AI Kit** and maze board.
2. Connect **AI Kit camera** to your computer.
3. Connect **robot** to your computer via **Ethernet**.
4. On the robot (Roboflow OS):
   - `Tools → Configuration → Network/Serial Port`
   - **Start** the **TCP Server**
5. Bring robot to **Home** (Return to Home).

### 3b. Socket Programming & Run
- Implement a **socket client** (Python/MATLAB/other) that:
  - Connects to robot’s IP (TCP)
  - Sends motion commands derived from your **IK** results
  - Sets a reasonable **speed** for safe, smooth tracing
- Execute and verify the robot follows waypoints **straight** and **accurately**.
- Cross-check actual motion vs. **digital twin** results.

---

## 🗂️ Suggested Repo Structure
