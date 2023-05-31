from matplotlib import pyplot as plt
import pickle
import statistics

def drawplot():
    with open ('outfile', 'rb') as fp:
        delayplot = pickle.load(fp)
    plt.plot(delayplot)
    plt.show()
    print('\n')
    print(statistics.median(delayplot))
    print(statistics.mean(delayplot))
    print('\n')

if __name__ == '__main__':
    drawplot()

