[![Windows/Linux + Python [3.8-3.11] .](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/build_all.yaml/badge.svg)](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/build_all.yaml) 
[![Build `tar.gz` PyPI](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/build_pypi.yaml/badge.svg)](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/build_pypi.yaml)

# Customized `Torchreid` for [`pyppbox`](https://github.com/rathaumons/pyppbox)

`Torchreid` is a library for deep-learning person re-identification using [PyTorch](https://pytorch.org/). 

All source credit and more info -> [Original KaiyangZhou's repo](https://github.com/KaiyangZhou/deep-person-reid). 

`pyppbox-torchreid` is a customized of `Torchreid` for [`pyppbox`](https://github.com/rathaumons/pyppbox) and:
- Ensures that `Cython` works on all OS platform (Windows/Linux), 
- Enables freedom of passing local model/weight files from anywhere, 
- Disables some unused models.

## Install

Use [Wheels fron releases](https://github.com/rathaumons/torchreid-for-pyppbox/releases) or directly install from PyPI: 

```
pip install pyppbox-torchreid
```

Or install from GitHub directly:

```
pip install git+https://github.com/rathaumons/torchreid-for-pyppbox.git
```

To be able to import or run, you must install [PyTorch](https://pytorch.org/) with ***GPU***:

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

***Note*: [PyTorch](https://pytorch.org/) doesn't support GUP on macOS.**

## Build from source

(Optional, auto install) Building Wheels or source distribution only requires these modules:

```
pip install "setuptools>=67.2.0"
pip install "Cython>=0.29.32"
pip install "numpy>=1.21.6"
```

Recommend using `build` for building both `.whl` and `.tar.gz`:

```
git clone https://github.com/rathaumons/torchreid-for-pyppbox/
cd torchreid-for-pyppbox
pip install wheel build
python -m build --sdist
python -m build --wheel
cd dist
```

After you install `pyppbox-torchred` and [PyTorch](https://pytorch.org/), you can check if Cython `rank_cy` works:

```
cd pyppbox_torchreid/metrics/rank_cylib
python test_cython.py
```
