# Torchreid - Customized for [`pyppbox`](https://github.com/rathaumons/pyppbox)

Forked from original repo: https://github.com/KaiyangZhou/deep-person-reid

## How to prepare for [`pyppbox`](https://github.com/rathaumons/pyppbox)

* Clone and install requirements
```
git clone https://github.com/rathaumons/torchreid-for-pyppbox.git
cd torchreid-for-pyppbox
pip install -r requirements.txt
```

* Install the corresponding `opencv_contrib_python` if you haven't already 
  - For Python 3.9 & CUDA 11.6.x
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py39/cuda116/opencv_contrib_python-4.5.5-cp39-cp39-win_amd64.whl
    ```
  - For Python 3.9 & CUDA 11.7.x
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py39/cuda117/opencv_contrib_python-4.5.5-cp39-cp39-win_amd64.whl
    ```
  - For Python 3.10  & CUDA 11.6.x
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py310/cuda116/opencv_contrib_python-4.5.5-cp310-cp310-win_amd64.whl
    ```
  - For Python 3.10  & CUDA 11.7.x
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py310/cuda117/opencv_contrib_python-4.5.5-cp310-cp310-win_amd64.whl
    ```

* Install your preferred version of `torch`, for example `torch==1.13.0+cu117`
```
pip install torch==1.13.0+cu117 torchvision==0.14.0+cu117 torchaudio==0.13.0+cu117 --extra-index-url https://download.pytorch.org/whl/cu117
```

* Create WHL file (Should be in `torchreid-for-pyppbox\dist`)
```
python setup.py bdist_wheel
```
