# car-behavioral-cloning-paddle
## 简介
使用 Paddle 框架复现论文 End to End Learning for Self-Driving Cars

## 测试视频
![](https://img-blog.csdnimg.cn/f11007092340466e8a64155ce0283141.gif)

## 预训练模型
* model_convert_from_keras.pdparams -> 官方项目中的预训练模型，模型输出与 Keras 实现对齐，可用于模拟器中第二个赛道的自动驾驶
* model_paddle_test1.pdparams / model_paddle_test2.pdparams -> 使用本项目训练的模型，可用于模拟器中第一个赛道的自动驾驶

## 模拟器下载
* [linux](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f0f7_simulator-linux/simulator-linux.zip)
* [max](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f290_simulator-macos/simulator-macos.zip)
* [windows_32](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f4b6_simulator-windows-32/simulator-windows-32.zip)
* [windows_64](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f3a4_simulator-windows-64/simulator-windows-64.zip)

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