import matplotlib.pyplot as plt

def move(dir, dis):
    xpoints = [0, 8]
    ypoints = [0, dis]

    plt.plot(xpoints, ypoints)
    plt.show()
    return dir, dis

imp = input('Enter direction, distance e.g. l,4: ')

imp = imp.upper()
dir = imp[0]
dis = int(imp[2:])
# print(imp, dir, dis)
move(dir, dis)


