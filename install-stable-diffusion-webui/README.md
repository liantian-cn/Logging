
# 首先安装cuda

打开 https://pytorch.org/get-started/locally/

根据当前稳定版本的pytorch对应的cuda版本。下载cuda

下载地址在 https://developer.nvidia.com/cuda-toolkit-archive

这里使用的是11.6.2

# 下载pytorch

因为pytorch安装包实在太大，根据python版本，先单独下载pytorch的whl

https://download.pytorch.org/whl/cu116/torch-1.13.1%2Bcu116-cp310-cp310-win_amd64.whl

# 下载Stable Diffusion web UI

使用git

git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

或者下载并解压

https://github.com/AUTOMATIC1111/stable-diffusion-webui/archive/refs/heads/master.zip

到工作路径

```
# 先创建Venv环境
C:\Python310\python.exe -m venv venv
# 激活venv环境
.\venv\Scripts\Activate.ps1
# 安装pytorch
pip3 install G:\下载路径\torch-1.13.1+cu116-cp310-cp310-win_amd64.whl
# 安装其他组件
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
# 安装Stable Diffusion web UI的依赖
pip3 install -r requirements.txt
```

# 

# 运行

正常的..

```commandline
python launch.py
```

https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Optimizations

低显存的


```commandline
python launch.py --medvram
```

xformers加速的..

```
python launch.py --xformers
```


基础的tags

```
正面的
(masterpiece:1.331), best quality,(full body)

负面的
signature,watermark,text,username,missing arms,fewer digits,bad anatomy,bad hands,error,cropped,worst quality,parody,thick thighs,
```

