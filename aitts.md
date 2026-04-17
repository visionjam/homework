
# NVIDIA的Personaplex本地部署实战，小白向
## [什么是Personaplex?](https://github.com/NVIDIA/personaplex)
PersonaPlex 是一种实时、全双工语音转语音对话模型，通过文本角色提示和音频语音条件控制实现角色控制
如果你想本地练习英语口语或者是想在本地跑一个tts模型，那么你来对的地方了！
* 特色：以较少的参数实现了较流利、真实的对话，甚至还可以插话。这为我们在本地部署提供了可能

## **前提条件**
* 硬件条件：
至少32G的内存
N卡
至少16G的显存(这点十分非常重要，我是RTX5060 8G的显卡，后面就遭殃了)
50G左右的磁盘空间
* 软件条件：
科学上网的网络环境
拥有github账号
拥有hugging face的账号
Python
conda
git
[安装最新的显卡驱动](https://www.nvidia.cn/geforce/drivers/)。可以使用```nvidia-smi```查看驱动是否更新好以及支持的CUDA版本
[CUDA工具包](https://developer.nvidia.com/cuda-downloads)，CUDA工具包记得一定要下载对应的版本哦
别忘了重启电脑
* 注：本文不会再强调以上前提条件，有不懂的请自行咨询AI或者使用搜索引擎查询，csdn bilibili和知乎等
  请学会查询官方文档和对应项目readme以及issue的良好习惯，这也是我在跑这个项目时最大的感悟
***
如果对AI领域感兴趣的同学相信都会知道。AI领域Linux系统占有主导地位。但是，Linux的纯命令行界面劝退了不少小白。
这里有两条路可以走，第一是在Windows 11上运行WSL2的虚拟环境；另一条就是直接在Windows 11上运行本地模型。不过这会遇到依赖地狱，但是管他呢，我就要图形界面。所以本文着重介绍后者，对前者有兴趣的同学也可以留言。

你也可以访问[官方的项目页面](https://github.com/NVIDIA/personaplex)来一步步动手操作，说不定你有别的解决方案
那么打开power shell让我们开始吧!
```
#我们利用conda创造一个叫做learn_ai的虚拟环境Python版本为3.10
#在这里提醒一些同学们Python 3.10是较为稳定的版本，如果选择较高的版本的话，有些包会不支持并且不稳定
conda create -n learn_ai python=3.10
#进入环境
conda activate learn_ai
```

Personaplex需要opus，你可以上[官网](https://opus-codec.org/downloads/)直接下载添加到环境变量，但是我想在这里介绍一个包管理工具 **vcpkg**
因为它开源并且和vscode高度适配，所以我也推荐同学们使用它
vcpkg是C++的一个包管理工具，所以下载它之前，我们需要先配置一下C++的环境
[vs下载官网](https://visualstudio.microsoft.com/zh-hans/downloads/)
所有文件，我推荐下载到D盘一个你找得到位置的地方,因为后续我们要添加到环境变量。善用``cd``
![vs下载示例]()
```
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.\bootstrap-vcpkg.bat
```
记得添加环境变量到系统 PATH和重启电脑
```
#终于可以下载了
vcpkg install opus
```
hf auth login
python -m moshi.server --ssl "$SSL_DIR" --cpu-offload --device cpu

$SSL_DIR = "$env:TEMP\moshi_ssl"
New-Item -ItemType Directory -Path $SSL_DIR -Force

python -m moshi.server --ssl "$SSL_DIR" --cpu-offload --device cpu

pip list | findstr torch

HF_TOKEN=<TOKEN> \
python -m moshi.offline \
  --voice-prompt "NATF2.pt" \
  --input-wav "assets/test/input_assistant.wav" \
  --seed 42424242 \
  --output-wav "output.wav" \
  --output-text "output.json"

