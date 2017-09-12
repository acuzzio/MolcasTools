''' This script will paint energies diagram from one or multiple rasscf.h5
file'''

from molcastools import retrieve_hdf5_data

def main():
    '''
    description
    '''
    energies = retrieve_hdf5_data('ciclopropanone.rasscf.h5', 'ROOT_ENERGIES')
    print(energies) 


if __name__ == "__main__":
    main()

