# car-behavioral-cloning-paddle
## 简介
使用 Paddle 框架复现论文 End to End Learning for Self-Driving Cars

## 测试视频
![](https://img-blog.csdnimg.cn/f11007092340466e8a64155ce0283141.gif)

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