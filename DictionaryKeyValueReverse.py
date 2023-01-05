def get_swap_dict(d):
    return {v: k for k, v in d.items()}



cheerlight_colours = {'red':'0xFF0000', 'green':'0x008000', 'blue':'0x0000FF', 'cyan':'0x00FFFF', 'white':'0xFFFFFF',
                      'oldlace':'0xFDF5E6', 'purple':'0x800080', 'magenta':'0xFF00FF', 'yellow':'0xFFFF00',
                      'orange':'0xFFA500', 'pink':'0xFFC0CB'}

d_swap = get_swap_dict(cheerlight_colours)
print(d_swap)