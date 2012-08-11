#!/usr/bin/python -u
# -*- coding: latin-1 -*-
def find(mappe, cpu=6, minLengde=5):
    import os, time
    from multiprocessing import Process, Queue, active_children
    arbejdsliste = os.listdir(mappe)
    while arbejdsliste and len(active_children()):
        while len(active_children()) < cpu:
            #spawn child
        time.sleep(1)
    print 'Færdig med arbejdet!'
    return

def child(fil, mappe):
    #indlæs filen
    udfil = open(mappe +'/homopolymer-'+fil, 'wb')
    for sekvens in filen:
        for base in ('A', 'T', 'C', 'G'):
            ind = 0
            while 1:
                try:
                    homopolymer = sekvens[ind:].index(base)
                    udfil.write('>|' + str(homopolymer) + '|\n' + sekvens[homopolymer-100:homopolymer+100])
                    ind = homopolymer + 100
                except ValueError:
                    break
    udfil.close()
    return

if __name__ == "__main__":
    import sys
    find(sys.argv[1])
    exit()
