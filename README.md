# Circulation

## 介绍

[![](https://img.shields.io/badge/israel--dryer-ttkbootstrap-blue?logo=github)](https://github.com/israel-dryer/ttkbootstrap) [![](https://img.shields.io/badge/PaddlePaddle-Paddle-blue?logo=github)](https://github.com/PaddlePaddle/Paddle) [![](https://img.shields.io/badge/PaddlePaddle-PaddleHub-blue?logo=github)](https://github.com/PaddlePaddle/PaddleHub) ![](https://img.shields.io/badge/support-python3-brightgreen?logo=python) [![](https://img.shields.io/github/last-commit/GavinSun0921/Circulation)](https://github.com/GavinSun0921/Circulation/commits/master)

本项目是一个基于 PaddleHub 的 [deeplabv3p_xception65_humanseg](https://www.paddlepaddle.org.cn/hubdetail?name=deeplabv3p_xception65_humanseg&en_category=ImageSegmentation) 模型和 [ttkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/)([tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter)) 实现的证件照一键换底色程序。

- 使用神经网络对人像进行分割，边缘清晰，效果较好
- 人像分割耗时较长

## 界面

#### 程序启动主界面

<div align=center><img src="img\ref\mainWindow.png" alt="mainWindow" width="300px" /></div>

#### 选择 demo.jpeg 图片后

<div align=center><img src="img\ref\openPic.png" alt="mainWindow" width="300px" /></div>

#### 点击转换底色后

<div align=center><img src="img\ref\transPic.png" alt="mainWindow" width="300px" /></div>

#### 可切换标签页到自选颜色

<div align=center><img src="img\ref\customColor.png" alt="mainWindow" width="800px" /></div>

## 项目结构

```bash
.
├── Application.py
├── humanseg.py
├── img
│   ├── blank.png
│   └── demo.jpeg
├── main.py
└── module/deeplabv3p_xception65_humanseg
```

### 功能实现

- Application.py 完成程序界面和事件绑定
- humanseg.py 完成人像与背景分离的任务

## 希望能有大佬帮忙进行一下打包

个人使用 pyinstaller 打包后一直出现问题
