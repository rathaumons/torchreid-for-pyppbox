# Torchreid - Customized for [`pyppbox`](https://github.com/rathaumons/pyppbox)

Forked from original repo: https://github.com/KaiyangZhou/deep-person-reid

## How to prepare for [`pyppbox`](https://github.com/rathaumons/pyppbox)

* Clone and install requirements
  ```
  git clone https://github.com/rathaumons/torchreid-for-pyppbox.git
  cd torchreid-for-pyppbox
  pip install -r requirements.txt
  ```

* Install `opencv_contrib_python` or `cv2`
  - If you use CPU only:
    ```
    pip install opencv-contrib-python
    ```
  - If you use GPU (Python 3.10  & CUDA 11.8.x):
    ```
    pip install https://github.com/rathaumons/pyppbox-custpkg/raw/main/pyppbox_opencv/cp310_cu118/pyppbox_opencv-4.7.0-cp310-none-win_amd64.whl
    ```

* Install your preferred version of `torch`, for example `torch==2.0.1+cu118`
  ```
  pip install torch==2.0.1+cu118 torchaudio==2.0.2+cu118 torchvision==0.15.2+cu118 --extra-index-url https://download.pytorch.org/whl/cu118
  ```

* Finally, build and create WHL file (Look inside `torchreid-for-pyppbox/dist`)
  ```
  build_creat_whl.cmd
  ```
