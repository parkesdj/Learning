def hex_to_rgb(hex, value) :
    rgb = []
    for i in (0, 2, 4) :
        decimal = int(hex[i :i + 2], 16)
        rgb.append(int(decimal * value))
    return rgb

value = 0.5
neo = hex_to_rgb('ffffff', value)
print(neo)
