class CelestialBody:

    def __init__(
        self,
        name,
        radius,
        orbit_radius,
        orbit_speed,
        rotation_speed,
        color,
        children=None
    ):
        self.name = name
        self.radius = radius
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.rotation_speed = rotation_speed
        self.color = color
        self.children = children if children else []

    def add_child(self, body):
        self.children.append(body)

# Moons

moon = CelestialBody(
    name="Moon",
    radius=2,
    orbit_radius=12,
    orbit_speed=4.0,
    rotation_speed=2.0,
    color=(0.8, 0.8, 0.8)
)

io = CelestialBody(
    name="Io",
    radius=2,
    orbit_radius=15,
    orbit_speed=5.0,
    rotation_speed=2.0,
    color=(1.0, 0.9, 0.5)
)

# Planets

mercury = CelestialBody(
    name="Mercury",
    radius=3,
    orbit_radius=25,
    orbit_speed=4.8,
    rotation_speed=1.0,
    color=(0.7, 0.7, 0.7)
)

venus = CelestialBody(
    name="Venus",
    radius=5,
    orbit_radius=40,
    orbit_speed=3.5,
    rotation_speed=0.8,
    color=(1.0, 0.8, 0.3)
)

earth = CelestialBody(
    name="Earth",
    radius=5,
    orbit_radius=60,
    orbit_speed=3.0,
    rotation_speed=2.0,
    color=(0.2, 0.5, 1.0),
    children=[moon]
)

mars = CelestialBody(
    name="Mars",
    radius=4,
    orbit_radius=80,
    orbit_speed=2.4,
    rotation_speed=1.8,
    color=(0.9, 0.3, 0.2)
)

jupiter = CelestialBody(
    name="Jupiter",
    radius=11,
    orbit_radius=110,
    orbit_speed=1.3,
    rotation_speed=3.0,
    color=(0.9, 0.7, 0.5),
    children=[io]
)

saturn = CelestialBody(
    name="Saturn",
    radius=9,
    orbit_radius=145,
    orbit_speed=1.0,
    rotation_speed=2.7,
    color=(0.9, 0.8, 0.5)
)

uranus = CelestialBody(
    name="Uranus",
    radius=7,
    orbit_radius=180,
    orbit_speed=0.7,
    rotation_speed=2.2,
    color=(0.5, 0.9, 1.0)
)

neptune = CelestialBody(
    name="Neptune",
    radius=7,
    orbit_radius=215,
    orbit_speed=0.5,
    rotation_speed=2.0,
    color=(0.2, 0.4, 1.0)
)


# Sun

sun = CelestialBody(
    name="Sun",
    radius=18,
    orbit_radius=0,
    orbit_speed=0,
    rotation_speed=0.5,
    color=(1.0, 0.9, 0.0),
    children=[
        mercury,
        venus,
        earth,
        mars,
        jupiter,
        saturn,
        uranus,
        neptune
    ]
)

# Exportable list of planets
PLANETS = [
    mercury,
    venus,
    earth,
    mars,
    jupiter,
    saturn,
    uranus,
    neptune
]
