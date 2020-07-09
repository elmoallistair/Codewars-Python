def bouncingBall(h, bounce, window):
    if not(0 < bounce < 1): return -1
    count = 0
    while h > window:
        count += 1 # falling
        h *= bounce
        if h > window: count += 1 # bouncing
    return count if count else -1 # 0 considered as -1
