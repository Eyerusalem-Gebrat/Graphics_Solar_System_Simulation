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
moon      = CelestialBody("Moon",       3,  14, 4.0, 2.0, (200, 200, 200))
phobos    = CelestialBody("Phobos",     2,  10, 6.0, 3.0, (180, 160, 140))
deimos    = CelestialBody("Deimos",     2,  14, 4.5, 2.0, (160, 140, 120))
io        = CelestialBody("Io",         3,  18, 5.0, 2.0, (255, 230, 130))
europa    = CelestialBody("Europa",     3,  23, 4.0, 2.0, (230, 210, 190))
ganymede  = CelestialBody("Ganymede",   4,  29, 3.0, 1.5, (180, 160, 130))
callisto  = CelestialBody("Callisto",   4,  36, 2.0, 1.0, (130, 110,  90))
titan     = CelestialBody("Titan",      4,  20, 3.5, 1.5, (230, 180, 100))
enceladus = CelestialBody("Enceladus",  2,  15, 5.0, 2.0, (230, 240, 255))
mimas     = CelestialBody("Mimas",      2,  12, 6.0, 2.5, (200, 200, 200))
titania   = CelestialBody("Titania",    3,  15, 3.0, 1.5, (180, 200, 220))
oberon    = CelestialBody("Oberon",     3,  20, 2.5, 1.2, (150, 155, 175))
triton    = CelestialBody("Triton",     3,  16, 3.5, 1.8, (150, 175, 230))


# Planets — orbit radii scaled to fit 1920x1080 fullscreen
mercury = CelestialBody(
    name="Mercury", radius=6,
    orbit_radius=70,  orbit_speed=4.8, rotation_speed=1.0,
    color=(180, 180, 180)
)
venus = CelestialBody(
    name="Venus", radius=10,
    orbit_radius=110, orbit_speed=3.5, rotation_speed=0.8,
    color=(255, 200, 80)
)
earth = CelestialBody(
    name="Earth", radius=11,
    orbit_radius=155, orbit_speed=3.0, rotation_speed=2.0,
    color=(50, 130, 255),
    children=[moon]
)
mars = CelestialBody(
    name="Mars", radius=8,
    orbit_radius=200, orbit_speed=2.4, rotation_speed=1.8,
    color=(220, 80, 50),
    children=[phobos, deimos]
)
jupiter = CelestialBody(
    name="Jupiter", radius=22,
    orbit_radius=265, orbit_speed=1.3, rotation_speed=3.0,
    color=(210, 170, 120),
    children=[io, europa, ganymede, callisto]
)
saturn = CelestialBody(
    name="Saturn", radius=18,
    orbit_radius=340, orbit_speed=1.0, rotation_speed=2.7,
    color=(220, 200, 130),
    children=[titan, enceladus, mimas]
)
uranus = CelestialBody(
    name="Uranus", radius=14,
    orbit_radius=410, orbit_speed=0.7, rotation_speed=2.2,
    color=(130, 230, 255),
    children=[titania, oberon]
)
neptune = CelestialBody(
    name="Neptune", radius=13,
    orbit_radius=470, orbit_speed=0.5, rotation_speed=2.0,
    color=(60, 100, 255),
    children=[triton]
)

sun = CelestialBody(
    name="Sun", radius=45,
    orbit_radius=0, orbit_speed=0, rotation_speed=0.3,
    color=(255, 220, 0),
    children=[mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
)

PLANETS = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]