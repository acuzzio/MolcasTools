'''
First tests suite
'''

import numpy as np
from molcastools import retrieve_hdf5_keys, retrieve_hdf5_data

def test_ret_keys():
    '''
    small test to read keys and data (this should always pass)
    '''
    fn = 'tests/test_files/ciclopropanone.rasscf.h5'
    listKey = retrieve_hdf5_keys(fn)
    shouldbe = ['AO_FOCKINT_MATRIX', 'AO_MLTPL_X', 'AO_MLTPL_XX',
                'AO_MLTPL_XY', 'AO_MLTPL_XZ', 'AO_MLTPL_Y', 'AO_MLTPL_YY',
                'AO_MLTPL_YZ', 'AO_MLTPL_Z', 'AO_MLTPL_ZZ', 'AO_OVERLAP_MATRIX',
                'BASIS_FUNCTION_IDS', 'CENTER_CHARGES', 'CENTER_COORDINATES',
                'CENTER_LABELS', 'CI_VECTORS', 'DENSITY_MATRIX', 'FOCK_MATRIX',
                'MO_ENERGIES', 'MO_OCCUPATIONS', 'MO_TYPEINDICES', 'MO_VECTORS',
                'PRIMITIVES', 'PRIMITIVE_IDS', 'ROOT_ENERGIES', 'SPINDENSITY_MATRIX',
                'SUPSYM_IRREP_INDICES']
    test1 = listKey == shouldbe
    energies = retrieve_hdf5_data(fn, 'ROOT_ENERGIES')
    ene_zero_shouldbe = -190.8223234124598
    test2 = energies[0] == ene_zero_shouldbe
    assert all([test1,test2])

