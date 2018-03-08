#### Inception v3模型在一台配有 8 Tesla K40 GPUs，大概价值$30,000的野兽级计算机上训练了几个星期，因此不可能在一台普通的PC上训练。使用预训练好的Inception模型，然后用它来做图像分类。

* Inception模型有两个softmax输出。一个是在训练神经网络时使用，另一个是训练结束之后，在图像分类时使用，即推断阶段（inference）。

![](https://pic1.zhimg.com/80/v2-811dea8fc9901802e97df4fb7e9acf8f_hd.jpg)

ReginCode: https://research.googleblog.com/2016/08/improving-inception-and-image.html
Paper: https://arxiv.org/pdf/1512.00567v3.pdf