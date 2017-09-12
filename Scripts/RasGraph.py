''' This script will paint energies diagram from one or multiple rasscf.h5
file'''

from collections import namedtuple
from argparse import ArgumentParser
from molcastools import retrieve_hdf5_data

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

def main():
    '''
    description
    '''
    inputs = single_inputs("ciclopropanone.rasscf.h5"   # default input
                          )
    new_inp = read_arguments(inputs)
    energies = retrieve_hdf5_data(new_inp.h5_file, 'ROOT_ENERGIES')
    print(energies)


if __name__ == "__main__":
    main()

