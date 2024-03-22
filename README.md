[![Test Build Python [3.8-3.12]](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/test_build.yaml/badge.svg)](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/test_build.yaml) 
[![Publish to PyPI](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/publish_pypi.yaml/badge.svg)](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/publish_pypi.yaml)

# Customized Torchreid for pyppbox

`Torchreid` is a library for deep-learning person re-identification using [PyTorch](https://pytorch.org/). 

`pyppbox-torchreid` is a customized `Torchreid` for [`pyppbox`](https://github.com/rathaumons/pyppbox) and:
- Ensures that `Cython` natively works on all OS platforms (Windows/Linux/macOS), 
- Enables freedom of passing local model/weight files from anywhere, 
- Disables some models which are not used in [`pyppbox`](https://github.com/rathaumons/pyppbox).

All source credit and more info -> [Original KaiyangZhou's repo](https://github.com/KaiyangZhou/deep-person-reid). 

## Install

Use [wheels in releases](https://github.com/rathaumons/torchreid-for-pyppbox/releases) or install from [PyPI](https://pypi.org/project/pyppbox-torchreid/): 

```
pip install pyppbox-torchreid
```

Or install from GitHub repo directly (Require C++ compiler):

```
pip install git+https://github.com/rathaumons/torchreid-for-pyppbox.git
```

To be able to run, you must install [OpenCV](https://github.com/opencv/opencv-python) and [PyTorch](https://pytorch.org/); for example, with GPU support:

```
pip install opencv-contrib-python
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

***Note*: [PyTorch](https://pytorch.org/) doesn't have GPU support for macOS.**

## Build from source

(Optional, auto install) Building Wheels or source distribution only requires these modules:

```
pip install "setuptools>=67.2.0"
pip install "Cython>=0.29.32"
pip install "numpy>=1.23.5"
```

Recommend using `build` for building both `.whl` and `.tar.gz`:

```
git clone https://github.com/rathaumons/torchreid-for-pyppbox/
cd torchreid-for-pyppbox
python -m pip install --upgrade pip
pip install wheel build
python -m build --sdist
python -m build --wheel
cd dist
```

After you install `pyppbox-torchred`, [OpenCV](https://github.com/opencv/opencv-python) and [PyTorch](https://pytorch.org/), you can check if Cython `rank_cy` works:

```
cd pyppbox_torchreid/metrics/rank_cylib
python test_cython.py
```
