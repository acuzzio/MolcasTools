'''
My setup !
'''

from setuptools import setup


setup(
    name='molcastools',
    version='0.1.0',
    description='Some python tools to deal with Molcas outputs',
    license='',
    url='https://github.com/acuzzio/MolcasTools',
    author_email='acuzzio@gmail.com',
    keywords='Molcas graphics',
    package_dir={'': 'src'},
    packages=["molcastools"],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry'
    ],
    scripts=['Scripts/RasGraph.py'],
    install_requires=['h5py', 'numpy', 'pandas', 'matplotlib'],
    extras_require={'test': ['nose', 'coverage']}
)
