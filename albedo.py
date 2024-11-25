import matplotlib.pyplot as plt
import numpy as np
import imageio

# Строим графики интенсивности и альбедо в зависимости от длины волны
def readIntensity(photoName):
    photo = imageio.imread(photoName)

    cut = photo[256:512, 300:700, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]
    # Заполняем массив длин волн
    line = np.zeros(len(luma))
    for i in range(len(luma)):
        line[i] = -3.213 * i + 889.926

    plt.title('Интенсивность отражённого излучения\n')
    plt.xlabel('Длина волны, нм')
    plt.ylabel('Яркость')
    plt.grid(True)
    plt.ylim(0, 35)
    if photoName[:-4] == "white":
        plt.plot(line, luma, 'black', label='white')
        return luma
    else:
        plt.plot(line, luma, photoName[:-4], label=photoName[:-4])

l = readIntensity('white.jpg')
readIntensity('red.jpg')
readIntensity('blue.jpg')
readIntensity('yellow.jpg')
readIntensity('green.jpg')
plt.legend()
plt.show()

def albedo(photoName):
    photo = imageio.imread(photoName)

    cut = photo[256:512, 300:700, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = (0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2])/l
    line = np.zeros(len(luma))
    for i in range(len(luma)):
        line[i] = -3.213 * i + 889.926

    plt.title('Альбедо\n')
    plt.xlabel('Длина волны, нм')
    plt.ylabel('Альбедо')
    plt.grid(True)
    plt.ylim(0, 1.2)
    if photoName[:-4] == "white":
        plt.plot(line, luma, 'black', label='white')
    else:
        plt.plot(line, luma, photoName[:-4], label=photoName[:-4])

albedo('white.jpg')
albedo('red.jpg')
albedo('blue.jpg')
albedo('yellow.jpg')
albedo('green.jpg')
plt.legend()
plt.show()
