import numpy as np
import matplotlib.pyplot as plt
import imageio
from cycler import cycler
from scipy.signal import savgol_filter, find_peaks


def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.imread(photoName)
    background = photo[256:512, 400:600, 0:3].swapaxes(0, 1)

    cut = photo[256:512, 400:600, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 10), dpi=100)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'w', label='I')
    plt.legend()

    plt.imshow(background, origin='lower')
    plt.grid(True)
    # plt.savefig(plotName)
    plt.show()
    return rgb
