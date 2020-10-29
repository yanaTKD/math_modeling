def energy_func(m, h, v):
    ek = (m * (v ** 2)) / 2
    ep = m * 10 * h
    ee = ek + ep
    return ee
t = energy_func(1, 2, 3)
print(t)