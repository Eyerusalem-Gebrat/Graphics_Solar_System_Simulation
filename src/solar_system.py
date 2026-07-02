import math
from celestial_body import sun
from renderer import draw_planet, draw_orbit_ring, draw_saturn_rings, TILT


def get_position(cx, cy, orbit_radius, angle):
    x = cx + orbit_radius * math.cos(angle)
    y = cy + orbit_radius * math.sin(angle) * TILT
    return x, y


def collect_bodies(body, cx, cy, sim_time, speed_multiplier, scale_factor, is_moon=False):
    """
    Recursively collect all bodies with screen positions and depth.
    Depth = raw sin(angle) value — negative means BEHIND parent, positive means IN FRONT.
    """
    result = []

    if body.orbit_radius == 0:
        # Sun sits at exact center, depth = 0
        result.append({
            "body": body,
            "x": cx,
            "y": cy,
            "sin_angle": 0,
            "is_moon": False,
            "parent_cx": cx,
            "parent_cy": cy,
        })
        for child in body.children:
            result += collect_bodies(
                child, cx, cy, sim_time, speed_multiplier, scale_factor, is_moon=False
            )
        return result

    angle = sim_time * body.orbit_speed * speed_multiplier
    sin_a = math.sin(angle)
    scaled_radius = body.orbit_radius * scale_factor
    x, y = get_position(cx, cy, scaled_radius, angle)

    result.append({
        "body": body,
        "x": x,
        "y": y,
        "sin_angle": sin_a,   # negative = behind, positive = in front
        "is_moon": is_moon,
        "parent_cx": cx,
        "parent_cy": cy,
        "orbit_radius": scaled_radius,
    })

    for child in body.children:
        result += collect_bodies(
            child, x, y, sim_time, speed_multiplier, scale_factor, is_moon=True
        )

    return result


def draw_solar_system(surface, cx, cy, sim_time, speed_multiplier):
    # Dynamically scale orbits to occupy ~92% of the half-width of the screen,
    # but at least 1.35x the original size to prevent compaction.
    scale_factor = max(1.35, (cx * 0.92) / 470.0)

    all_bodies = collect_bodies(sun, cx, cy, sim_time, speed_multiplier, scale_factor)

    # Step 1 — draw all planet orbit rings first (always behind everything)
    for item in all_bodies:
        if not item["is_moon"] and item["body"].orbit_radius > 0:
            draw_orbit_ring(
                surface,
                item["parent_cx"],
                item["parent_cy"],
                item["orbit_radius"]
            )

    # Step 2 — sort by sin_angle so bodies behind (negative sin) draw first
    # Sun (sin=0) draws in the middle — bodies behind it draw under it,
    # bodies in front draw over it
    all_bodies_sorted = sorted(all_bodies, key=lambda b: b["sin_angle"])

    # Step 3 — draw in depth order
    for item in all_bodies_sorted:
        body = item["body"]
        x = item["x"]
        y = item["y"]

        if body.name == "Saturn":
            draw_saturn_rings(surface, x, y, body.radius)

        draw_planet(
            surface, x, y, body.radius, body.color,
            is_sun=(body.name.lower() == "sun")
        )