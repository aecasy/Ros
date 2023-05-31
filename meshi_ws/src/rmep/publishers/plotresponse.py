from matplotlib import pyplot as plt
import numpy as np
import pickle
import statistics

def drawplot():
    #with open ('outfile', 'rb') as fp:
    #    commandplot = pickle.load(fp)
    with open ('outfile2', 'rb') as fp2:
        RPMplot = pickle.load(fp2)
    with open ('outfile3', 'rb') as fp3:
        timevalues = pickle.load(fp3)
    #print(len(commandplot))
    timevalues=[0,0,0,0,0,0,0,0,0,0,0]+timevalues
    print(len(RPMplot))
    


    timevalues = [float(item) for item in timevalues]
    first=timevalues[0]
    #timevalues = [item-first for item in timevalues]
    RPMplot = [float(item) for item in RPMplot]
    #commandplot = [float(item) for item in commandplot]
    plt.plot(timevalues, RPMplot)
    x1, y1 = [2000, 2000], [-100, 600]
    x2, y2 = [5000, 5000], [-100, 600]
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    #plt.plot(timevalues, commandplot)
    plt.show()
    #print('\n')
    #print(statistics.median(delayplot))
    #print(statistics.mean(delayplot))
    #print('\n')

if __name__ == '__main__':
    drawplot()

