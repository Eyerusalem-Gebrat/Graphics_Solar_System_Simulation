# Graphics Solar System Simulation
A real-time 3D solar system simulation built with Python and PyOpenGL. The Sun and eight planets (plus a couple of moons) orbit and rotate continuously, with a mouse-controlled camera and an on-screen HUD showing simulation status and controls.

WHAT IT DOES
The program opens a window and renders the Sun at the center with Mercury, Venus, Earth (with its Moon), Mars, Jupiter (with its moon Io), Saturn (with rings), Uranus, and Neptune all orbiting around it. Each body spins on its own axis while orbiting at its own speed. You can freely rotate and zoom the camera around the scene, and control the flow of time (pause, reverse, speed up, slow down) while it runs.

FEATURES
- 3D rendered solar system with Sun, 8 planets, and moons
- Independent orbit radius, orbit speed, and rotation speed per body
- Recursive rendering so moons follow their parent planet correctly
- Free orbital camera controlled with the mouse (rotate and zoom)
- Time controls: pause, reverse, and speed up/down
- Dynamic lighting from the Sun, with the Sun itself rendered as a glowing self-lit body
- On-screen HUD showing current speed, pause state, and control instructions

FILES
- main.py: entry point; sets up the window, render loop, and input callbacks
- simulation.py: simulation clock: tracks time, speed, pause, and reverse state
- input_handler.py: handles mouse/keyboard input and camera state, draws the HUD
- math_utils.py: converts camera angles/distance into a 3D camera position
- celestial_body.py: defines the CelestialBody class and sets up the Sun, planets, and moons
- solar_system.py: recursively walks the body tree each frame to position and draw everything
- render.py: low-level OpenGL drawing code for spheres, rings, and orbit paths

CONTROLS
- Left-click drag   - Rotate/orbit the camera
- Right-click drag  - Zoom camera in/out
- Scroll wheel      - Zoom in/out
- plus / minus             - Increase / decrease simulation speed
- R                 - Reverse time direction
- P                 - Pause / resume simulation
- Q                 - Quit

PREREQUISITES
- Python 3.9 or higher
- PyOpenGL and PyOpenGL_accelerate (pip install PyOpenGL PyOpenGL_accelerate)
- FreeGLUT (system-level GLUT implementation)
  - Linux: sudo apt-get install freeglut3-dev
  - macOS: brew install freeglut (if you hit a GLUT import error)
  - Windows: usually bundled with PyOpenGL

RUNNING IT
cd src
python main.py

A window titled "3D Solar System Simulation" will open and the simulation starts immediately.
