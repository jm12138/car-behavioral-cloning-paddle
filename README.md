# car-behavioral-cloning-paddle
## 一、简介
* 本项目基于 Paddle 框架复现论文 End to End Learning for Self-Driving Cars
* 可实现模拟器中的简易自动驾驶功能
* 论文：[End to End Learning for Self-Driving Cars](https://arxiv.org/abs/1604.07316)
* 参考实现：[naokishibuya/car-behavioral-cloning](https://github.com/naokishibuya/car-behavioral-cloning)
* AIStudio 项目：[论文复现：实现简单的端到端自动驾驶模型](https://aistudio.baidu.com/aistudio/projectdetail/2253679)

## 二、Demo 演示
* 模拟器自动驾驶测试：

  ![](https://img-blog.csdnimg.cn/f11007092340466e8a64155ce0283141.gif)

## 三、数据集
* 本项目数据集需要通过模拟器进行手动采集
* 采集完成的数据列表 csv 文件还需要添加如下表头信息并且确保其中的图片路径与其真实路径保持一致

    | center | left | right | steering | lefting | righting | speed |
    | -------- | -------- | -------- | -------- | -------- | -------- | -------- |

## 四、依赖环境
* 本项目依赖如下几个模块：

  ```python
  astor==0.8.1
  bidict==0.21.2
  certifi==2021.5.30
  charset-normalizer==2.0.4
  click==8.0.1
  colorama==0.4.4
  cycler==0.10.0
  decorator==5.0.9
  dnspython==1.16.0
  eventlet==0.31.1
  Flask==2.0.1
  gast==0.3.3
  greenlet==1.1.0
  idna==3.2
  itsdangerous==2.0.1
  Jinja2==3.0.1
  joblib==1.0.1
  kiwisolver==1.3.1
  MarkupSafe==2.0.1
  matplotlib==3.4.2
  numpy==1.19.3
  opencv-python==4.5.3.56
  paddlepaddle==2.1.2
  pandas==1.3.1
  Pillow==8.3.1
  protobuf==3.17.3
  pyparsing==2.4.7
  python-dateutil==2.8.2
  python-engineio==3.13.0
  python-socketio==4.6.1
  pytz==2021.1
  requests==2.26.0
  scikit-learn==0.24.2
  scipy==1.7.1
  six==1.16.0
  threadpoolctl==2.2.0
  urllib3==1.26.6
  Werkzeug==2.0.1
  ```

* 可通过如下命令一键安装依赖：

  ```bash
  $ pip install -r requirements.txt
  ```

## 五、快速使用
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

## 六、代码结构和详细信息
* 代码结构

  ```python
  │  train.py # 训练脚本
  │  drive.py # 测试脚本
  │
  ├─car
  │      model.py # 模型代码
  │      utils.py # 功能代码
  │
  ├─pretrained_models # 模型参数文件
  │      model_keras.pdparams # 转换自参考项目的参数文件
  │      model_paddle_test1.pdparams # 使用本项目训练的模型参数文件
  │      model_paddle_test2.pdparams # 使用本项目训练的模型参数文件
  ```
* 参数说明：

  |参数|默认值|说明|适用脚本|
  |:-:|:-:|:-:|:-:|
  |d|data|数据集目录|train|
  |s|save|保存目录|train|
  |t|0.2|测试集切分比例|train|
  |k|0.5|dropout 概率|train|
  |n|100|训练轮次|train|
  |b|40|数据处理批大小|train|
  |l|1.0e-4|学习率|train|
  |e|False|是否提前终止|train|

## 七、模型信息
* 模型的总体信息如下：

  |信息|说明|
  |:-:|:-:|
  |框架版本|Paddle 2.1.2|
  |应用场景|自动驾驶|
  |支持硬件|CPU / GPU|
 
* 具体的网络结构如下图所示：

  ![](https://ai-studio-static-online.cdn.bcebos.com/227e1a2847af4658a8ae5d9172d30b715cd424fd4a7a490cbbaad525c8adb8d6)
