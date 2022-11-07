# Torchreid - Customized for pyppbox

Forked from original repo: https://github.com/KaiyangZhou/deep-person-reid

## How to prepare for pyppbox

* Clone and install requirements
```
git clone https://github.com/rathaumons/torchreid-for-pyppbox.git
cd torchreid-for-pyppbox
pip install -r requirements.txt
```

* Install the corresponding `opencv_contrib_python` if you haven't already 
  - Python 3.9 
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py39/opencv_contrib_python-4.5.5-cp39-cp39-win_amd64.whl
    ```
  - Python 3.10 
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py310/opencv_contrib_python-4.5.5-cp310-cp310-win_amd64.whl
    ```

* Install your preferred version of `torch`, for example `torch==1.13.0+cu116`
```
pip install torch==1.13.0+cu116 torchvision==0.14.0+cu116 torchaudio==0.13.0+cu116 --extra-index-url https://download.pytorch.org/whl/cu116
```

* Create WHL file (Should be in `torchreid-for-pyppbox\dist`)
```
python setup.py bdist_wheel
```
