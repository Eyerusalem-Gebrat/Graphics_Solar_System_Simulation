import math


def degrees_to_radians(deg):
    return deg * (math.pi / 180.0)


def radians_to_degrees(rad):
    return rad * (180.0 / math.pi)


def orbit_x(orbit_radius, angle):
    return orbit_radius * math.cos(angle)


def orbit_y(orbit_radius, angle):
    return orbit_radius * math.sin(angle)


def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))


def compute_orbit_angle(sim_time, orbit_speed, speed_multiplier):
    return sim_time * orbit_speed * speed_multiplier


def generate_circle_vertices(radius, segments=64):
    vertices = []
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        vertices.append((x, y))
    return verticesimport math


def get_camera_position(pitch, yaw, distance, target):
    """
    Calculate camera eye position in Cartesian coordinates (x, y, z)
    from spherical angles (pitch, yaw), distance, and look-at target.
    """
    pitch_rad = math.radians(pitch)
    yaw_rad = math.radians(yaw)

    eye_x = target[0] + distance * math.cos(pitch_rad) * math.cos(yaw_rad)
    eye_y = target[1] + distance * math.cos(pitch_rad) * math.sin(yaw_rad)
    eye_z = target[2] + distance * math.sin(pitch_rad)

    return eye_x, eye_y, eye_z
