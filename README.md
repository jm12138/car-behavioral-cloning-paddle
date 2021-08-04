# car-behavioral-cloning-paddle
## 简介
使用 Paddle 框架复现

## 测试视频
![](https://bj.bcebos.com/v1/ai-studio-online/d24f573eb9b54717ad8cde082eda5f5d92e8c6ddf057491f8d7790e90a80db44?responseContentDisposition=attachment%3B%20filename%3Dezgif.com-gif-maker.gif)

## 快速使用
### 模型测试
* 启动模拟器并启动自动驾驶模式
* 使用命令行启动模型服务
```shell
$ python drive.py [path to the pretrained model file]
```

### 模型训练
* 使用模拟器采集数据
* 使用命令行启动模型训练
```shell
$ python model.py -d [path to the data directory]
```