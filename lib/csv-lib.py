#!/usr/bin/python -u
# -*- coding: latin-1 -*-
def csvreader(csvfil, deli=','):
        import csv
        data = []
        for row in csv.reader(open(csvfil), delimiter=deli):
                data.append(row)
        return data

def csvwriter(udfil, liste):
        import csv
        filen = open(udfil, 'wb')
        csv_writer = csv.writer(filen)
        for row in liste:
                csv_writer.writerow(row)
        filen.close()
        return

if __name__ == "__main__":
        import sys
        for line in csvreader(sys.argv[1]):
                print line
        exit()
        
