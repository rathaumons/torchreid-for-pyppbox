[![Test Multi](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/test_multi.yaml/badge.svg)](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/test_multi.yaml) 
[![Test Build Python [3.9-3.13]](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/test_build.yaml/badge.svg)](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/test_build.yaml) 
[![Publish to PyPI](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/publish_pypi.yaml/badge.svg)](https://github.com/rathaumons/torchreid-for-pyppbox/actions/workflows/publish_pypi.yaml)

# Customized Torchreid for pyppbox

`Torchreid` is a library for deep-learning person re-identification using [PyTorch](https://pytorch.org/), and `pyppbox-torchreid` is a customized `Torchreid` for [`pyppbox`](https://github.com/rathaumons/pyppbox) and:
- Ensures that `Cython` natively works on all OS platforms (Windows/Linux/macOS), 
- Enables freedom of passing local model/weight files from anywhere, 
- Disables some models which are not used in [`pyppbox`](https://github.com/rathaumons/pyppbox).

All source credit and more info -> [Original KaiyangZhou's repo](https://github.com/KaiyangZhou/deep-person-reid). 

## 💽 Install

Use the pre-built [wheel in releases](https://github.com/rathaumons/torchreid-for-pyppbox/releases) or install from [PyPI](https://pypi.org/project/pyppbox-torchreid/): 

```
pip install pyppbox-torchreid
```

<details><summary>Other options</summary>

### Install from GitHub repo (Require C++ compiler):

```
pip install git+https://github.com/rathaumons/torchreid-for-pyppbox.git
```

### Build and install (Require C++ compiler):

```
git clone https://github.com/rathaumons/torchreid-for-pyppbox/
cd torchreid-for-pyppbox
python -m pip install --upgrade pip
pip install wheel build
python -m build --sdist
python -m build --wheel
cd dist
```

</details>

## 🔬 Test

Make sure you install `pyppbox-torchred`, [OpenCV](https://github.com/opencv/opencv-python), [PyTorch](https://pytorch.org/) and other [requirements](https://github.com/rathaumons/torchreid-for-pyppbox/blob/main/requirements.txt); for example, with GPU support on Windows:

```
pip install opencv-contrib-python
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install pyppbox-torchreid
```

Test Cython `rank_cylib`

```
git clone https://github.com/rathaumons/torchreid-for-pyppbox.git
cd torchreid-for-pyppbox/pyppbox_torchreid/metrics/rank_cylib
python test_cython.py
```
