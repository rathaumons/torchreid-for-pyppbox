# # # # # # # # # # # # # # # # # # # # # #
#    Rewrote on 2023/06/26 by rathaROG    #
#    Updated on 2024/11/07 by rathaROG    #
# # # # # # # # # # # # # # # # # # # # # #


from setuptools import Extension, setup, find_packages

license = "MIT"
description = "Customized Torchreid for pyppbox: Deep learning person re-identification."
long_description = open("README.md", encoding="utf-8").read()
requirements_txt = "requirements.txt"
package_name = "pyppbox-torchreid"
package_path = "pyppbox_torchreid"

def get_version_string():
    with open("pyppbox_torchreid/__init__.py") as version_file:
        for line in version_file.read().splitlines():
            if line.startswith('__version__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]

def read_requirements():
    with open(requirements_txt) as requirements_file:
        return [line for line in requirements_file.read().splitlines()]

def compile_cpp(cython_file):
    """Compile a C++ file from Cython's pyx or py.
    """
    import os
    import subprocess
    cpp_file = os.path.splitext(cython_file)[0] + ".cpp"
    flags = ['--fast-fail', '--cplus']
    rc = subprocess.call(['cython'] + flags + ['-o', cpp_file, cython_file])
    if rc != 0: raise Exception('Cythonizing %s failed' % cython_file)
    else: return cpp_file

def numpy_include():
    import numpy as np
    try:
        numpy_include = np.get_include()
    except AttributeError:
        numpy_include = np.get_numpy_include()
    return numpy_include

def main_setup():
    import os
    from Cython.Build import cythonize
    ext_name = "pyppbox_torchreid.metrics.rank_cylib.rank_cy"
    rank_cy_pyx = os.path.join(package_path, "metrics/rank_cylib/rank_cy.pyx")
    rank_cy_cpp = compile_cpp(rank_cy_pyx)
    ext_modules = [
        Extension(
            name=ext_name,
            sources=[rank_cy_cpp],
            include_dirs=[numpy_include()],
        )
    ]
    setup(
        name=package_name,
        version=get_version_string(),
        description=description,
        author="Ratha SIV",
        maintainer="rathaROG",
        license=license,
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='https://github.com/rathaumons/torchreid-for-pyppbox',
        packages=find_packages(),
        keywords=['Person Re-Identification', 'Deep Learning', 'pyppbox'],
        install_requires=read_requirements(),
        python_requires=">=3.8",
        classifiers=['Development Status :: 4 - Beta',
                     'Environment :: Console',
                     'Intended Audience :: Developers',
                     'Intended Audience :: Education',
                     'Intended Audience :: Information Technology',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: MIT License',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.8',
                     'Programming Language :: Python :: 3.9',
                     'Programming Language :: Python :: 3.10',
                     'Programming Language :: Python :: 3.11',
                     'Programming Language :: Python :: 3.12',
                     'Programming Language :: Python :: 3.13',
                     'Topic :: Education',
                     'Topic :: Education :: Testing',
                     'Topic :: Scientific/Engineering',
                     'Topic :: Scientific/Engineering :: Image Recognition',
                     'Topic :: Scientific/Engineering :: Information Analysis',
                     'Topic :: Software Development',
                     'Topic :: Software Development :: Libraries',
                     'Operating System :: Microsoft :: Windows',                                  
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS',],
        ext_modules=cythonize(ext_modules),
    )

if __name__ == "__main__":
    """
    Recommend using :py:mod:`build` to build the package as it does not 
    mess up your current enviroment.

    >>> pip install wheel build
    >>> python -m build --sdist
    >>> python -m build --wheel
    """ 
    main_setup()
