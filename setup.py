import numpy as np
import os.path as osp
from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Build import cythonize


def readme():
    with open('README.md') as f:
        content = f.read()
    return content


def find_version():
    version_file = 'pyppbox_torchreid/__init__.py'
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']


def numpy_include():
    try:
        numpy_include = np.get_include()
    except AttributeError:
        numpy_include = np.get_numpy_include()
    return numpy_include


ext_modules = [
    Extension(
        'pyppbox_torchreid.metrics.rank_cylib.rank_cy',
        ['pyppbox_torchreid/metrics/rank_cylib/rank_cy.pyx'],
        include_dirs=[numpy_include()],
    )
]


def get_requirements(filename='requirements.txt'):
    here = osp.dirname(osp.realpath(__file__))
    with open(osp.join(here, filename), 'r') as f:
        requires = [line.replace('\n', '') for line in f.readlines()]
    return requires


def force_tags(force=True):
    if force:
        import sys
        sys.argv.extend(['--plat-name', 'win_amd64'])


def main():
    setup(
        name='pyppbox-torchreid',
        version=find_version(),
        description='A library for deep learning person re-ID in PyTorch',
        author='rathaROG',
        license='MIT',
        long_description=readme(),
        url='https://github.com/rathaumons/torchreid-for-pyppbox.git',
        packages=find_packages(),
        install_requires=get_requirements(),
        keywords=['Person Re-Identification', 'Deep Learning', 'Computer Vision'],
        ext_modules=cythonize(ext_modules)
    )


if __name__ == "__main__":
    force_tags()
    main()
