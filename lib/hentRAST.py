#!/usr/bin/python -u
# -*- coding: latin-1 -*-
def hentRAST(liste, mappe='./', delay=1):
        import os, time
        from subprocess import Popen, PIPE
        user = raw_input('RAST-server User:')
        password = raw_input('RAST-server Password:')
        while liste:
                ID = liste.pop(0)
                status = Popen(["./RAST-lib/svr_status_of_RAST_job " + user + ' ' + password + ' ' + str(ID)], stdout=PIPE, shell=True, executable='/bin/bash').communicate()[0]
                if 'complete' in status:
                        os.system("./RAST-lib/svr_retrieve_RAST_job " + user + ' ' + password + ' ' + str(ID) + ' genbank > ' + mappe + '/' + str(ID) + '.tar')
                else:
                        liste.append(ID)
                        time.sleep(delay)
                print '\rMangler:', str(len(liste)),
        return

if __name__ == "__main__":
        import sys
        hentRAST(sys.argv[1])
        exit()
