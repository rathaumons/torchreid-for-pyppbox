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
  - For Python 3.10  & CUDA 12.0.x (Experimental)
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py310/cu120/opencv_contrib_python-4.7.0+cu120-cp310-cp310-win_amd64.whl
    ```
  - For Python 3.10  & CUDA 11.7.x
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py310/cu117/opencv_contrib_python-4.7.0+cu117-cp310-cp310-win_amd64.whl
    ```
  - For Python 3.10  & CUDA 11.6.x
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py310/cu116/opencv_contrib_python-4.7.0+cu116-cp310-cp310-win_amd64.whl
    ```
  - For Python 3.9 & CUDA 12.0.x (Experimental)
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py39/cu120/opencv_contrib_python-4.7.0+cu120-cp39-cp39-win_amd64.whl
    ```
  - For Python 3.9 & CUDA 11.7.x
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py39/cu117/opencv_contrib_python-4.7.0+cu117-cp39-cp39-win_amd64.whl
    ```
  - For Python 3.9 & CUDA 11.6.x
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py39/cu116/opencv_contrib_python-4.7.0+cu116-cp39-cp39-win_amd64.whl
    ```

* Install your preferred version of `torch`, for example `torch==1.13.1+cu117`
```
pip install torch==1.13.1+cu117 torchaudio==0.13.1+cu117 torchvision==0.14.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117
```

* Create WHL file (Should be in `torchreid-for-pyppbox\dist`)
```
python setup.py bdist_wheel
```
