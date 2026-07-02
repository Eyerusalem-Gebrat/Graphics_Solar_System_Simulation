import math


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

