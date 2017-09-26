''' This script will paint energies diagram from one or multiple rasscf.h5
file'''

from collections import namedtuple
from argparse import ArgumentParser
from molcastools import retrieve_hdf5_data
import pandas as pd
import numpy as np

def read_arguments(single_inputs):
    '''
    Command line parser like a hero
    '''
    parser = ArgumentParser()
    parser.add_argument("-i", "--h5file",
                        dest="i",
                        type=str,
                        required=True,
                        help="input h5 file")

    args = parser.parse_args()

    if args.i != None:
        single_inputs = single_inputs._replace(h5_file=args.i)
    return single_inputs

single_inputs = namedtuple("inputs",
        ("h5_file"))

def HartoEv(n):
    ''' From Hartree to ElectronVolt conversion '''
    return (n * 27.211402)

def HartoKcal(n):
    ''' From Hartree to Kcal/mol '''
    return (n * 627.503)


def main():
    '''
    from a rasscf h5 file to a pandas table
    '''
    inputs = single_inputs("ciclopropanone.rasscf.h5"   # default input
                          )
    new_inp = read_arguments(inputs)
    ene = retrieve_hdf5_data(new_inp.h5_file, 'ROOT_ENERGIES')
    nstates = ene.size
    enezero = ene - (ene[0])
    indexes = np.arange(nstates)
    ener = pd.DataFrame([enezero, HartoEv(enezero), HartoKcal(enezero)],
           index=['Hartree','Ev','kcal/mol'], columns=indexes)
    print(' ')
    print(ener.transpose().iloc[::-1])
    print(' ')


if __name__ == "__main__":
    main()

