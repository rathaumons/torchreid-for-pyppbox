# Torchreid - Customized for pyppbox

Forked from original repo: https://github.com/KaiyangZhou/deep-person-reid

## How to prepare for pyppbox

* Clone and install requirements
```
git clone https://github.com/rathaumons/torchreid-for-pyppbox.git
cd torchreid-for-pyppbox
pip install -r requirements.txt
```

* Install your preferred version of `torch`, for example `torch==1.13.0+cu116`
```
pip install torch==1.13.0+cu116 torchvision==0.14.0+cu116 torchaudio==0.13.0+cu116 --extra-index-url https://download.pytorch.org/whl/cu116
```

* Create WHL file (Should be in `torchreid-for-pyppbox\dist`)
```
python setup.py bdist_wheel
```
