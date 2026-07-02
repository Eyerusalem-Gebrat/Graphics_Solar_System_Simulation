# simulation.py

sim_time = 0.0
speed_multiplier = 1.0
paused = False


def update(delta):
    global sim_time

    if not paused:
        sim_time += delta * speed_multiplier


def get_time():
    return sim_time


def get_speed():
    return speed_multiplier


def is_paused():
    return paused


def increase_speed():
    global speed_multiplier
    speed_multiplier += 0.5


def decrease_speed():
    global speed_multiplier
    speed_multiplier = max(0.1, speed_multiplier - 0.5)


def reverse_time():
    global speed_multiplier
    speed_multiplier = -speed_multiplier


def toggle_pause():
    global paused
    paused = not paused
