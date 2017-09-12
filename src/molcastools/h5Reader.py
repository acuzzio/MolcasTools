'''
This module is taking care to read, write, correct and handle H5 files.

The main functions are:
retrieve_hdf5_keys(path_hdf5)
retrieve_hdf5_data(path_hdf5, paths_to_prop)
'''

import h5py

def retrieve_hdf5_keys(path_hdf5):
    '''
    Get key values from file path_hdf5.
    '''
    try:
       with h5py.File(path_hdf5, 'r') as hf:
          return list(hf.keys())
    except FileNotFoundError:
       msg = "there is not HDF5 file with that name"
       raise RuntimeError(msg)

def retrieve_hdf5_data(path_hdf5, paths_to_prop):
    '''
    Read Numerical properties from ``paths_hdf5``.
    :params path_hdf5: Path to the hdf5 file
    :type path_hdf5: string or list of strings
    '''
    try:
        with h5py.File(path_hdf5, 'r') as f5:
            if isinstance(paths_to_prop, list):
                return [f5[path].value for path in paths_to_prop]
            else:
                return f5[paths_to_prop].value
    except KeyError:
        msg = "There is not {} stored in the HDF5\n".format(paths_to_prop)
        raise KeyError(msg)
    except FileNotFoundError:
        msg = "there is not HDF5 file containing the numerical results"
        raise RuntimeError(msg)

def writeH5file(fn, tuplesLabelValues):
    '''
    writes a h5 file with name fn and [(label, value)] structure
    '''
    with h5py.File(fn, 'w') as hf:
            for (label,value) in tuplesLabelValues:
                hf.create_dataset(label, data=value)


if __name__ == "__main__":
    print("Not a lot of stuffs to do")
