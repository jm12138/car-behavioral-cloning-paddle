# car-behavioral-cloning-paddle
## 一、简介
* 使用 Paddle 框架复现论文 End to End Learning for Self-Driving Cars
* 复现指标： 能在模拟器上运行不偏离路面
* AIStudio：项目：[论文复现：实现简单的端到端自动驾驶模型](https://aistudio.baidu.com/aistudio/projectdetail/2253679)（包含模型训练、训练日志、训练 Checkpoints 等）

## 二、Demo 演示
* 模拟器自动驾驶测试：

  ![](https://img-blog.csdnimg.cn/f11007092340466e8a64155ce0283141.gif)

## 三、快速使用
* 模拟器下载
  * [linux](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f0f7_simulator-linux/simulator-linux.zip)
  * [max](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f290_simulator-macos/simulator-macos.zip)
  * [windows_32](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f4b6_simulator-windows-32/simulator-windows-32.zip)
  * [windows_64](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f3a4_simulator-windows-64/simulator-windows-64.zip)

* 模型训练
  * 使用模拟器采集数据
  * 使用命令行启动模型训练

    ```shell
    $ python train.py -d [path to the data directory]
    ```

* 模型测试
  * 启动模拟器并启动自动驾驶模式
  * 使用命令行启动模型服务

    ```shell
    $ python drive.py [path to the pretrained model file]
    ```

