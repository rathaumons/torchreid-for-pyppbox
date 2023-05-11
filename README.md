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
  - For Python 3.10  & CUDA 11.8.x
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py310/opencv_contrib_python-4.7.0+cu118-cp310-cp310-win_amd64.whl
    ```
  - For Python 3.10  & CUDA 11.7.x
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py310/opencv_contrib_python-4.7.0+cu117-cp310-cp310-win_amd64.whl
    ```
  - For Python 3.9 & CUDA 11.8.x
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py39/opencv_contrib_python-4.7.0+cu118-cp39-cp39-win_amd64.whl
    ```
  - For Python 3.9 & CUDA 11.7.x
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/py39/opencv_contrib_python-4.7.0+cu117-cp39-cp39-win_amd64.whl
    ```

* Install your preferred version of `torch`, for example `torch==2.0.0+cu118`
```
pip install torch==2.0.1+cu118 torchaudio==2.0.2+cu118 torchvision==0.15.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
```

* Finally, build and create WHL file (Look inside `torchreid-for-pyppbox/dist`)
```
build_creat_whl.cmd
```
