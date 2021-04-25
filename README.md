# Convolutional Neural Network (CNN)


Convolutional neural networks therefore constitute a very useful tool for machine learning practitioners. However, learning to use CNNs for the first time is generally an intimidating experience. A convolutional layer�s output shape is affected by the shape of its input as well as the choice of kernel shape, zero padding and strides, and the relationship between these properties is not trivial to infer. This contrasts with fully-connected layers, whose output size is independent of the input size. (<a href="https://arxiv.org/abs/1603.07285" target="_blank">Vincent Dumoulin and Francesco Visin, 2016</a>)

## Here are some highlights about CNN
<ol>
<li>once the CNN has learned to recognize a pattern in one location, it can recognize it in any other location. In contrast, once a regular DNN has learned to recognize a pattern in one location, it can recognize it only in that particular location.</li>
</ol>

## Techniques to handle overfitting issue:
1) Check on training and validation accuracy over the training to identify overfitting issue.
2) Image augmentation
3) Dropout

# CNN Architectures

<ul>
<li>Deep Neural Network</li>
<li>Basic Convolutional Network</li>
<li>MobileNet-v2</li>

<li>ResNet-V2-50</li>
<p>ResNet is a residual learning framework</p>

<li>VGG Net 16</li>
<p>The key innovation on the inception model is called the inception module. This is a block of parallel convolutional layers with different sized filters (e.g. 1�1, 3�3, 5�5) and a and 3�3 max pooling layer, the results of which are then concatenated.</p>

<li></li>
<p>The key innovation on the inception model is called the inception module. This is a block of parallel convolutional layers with different sized filters (e.g. 1�1, 3�3, 5�5) and a and 3�3 max pooling layer, the results of which are then concatenated.</p>
</ul>

## References
1) https://cs231n.github.io/convolutional-networks/
2) https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53
3) https://towardsdatascience.com/understanding-your-convolution-network-with-visualizations-a4883441533b
4) https://indoml.com/2018/03/07/student-notes-convolutional-neural-networks-cnn-introduction/
5) Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun: "<a href="https://arxiv.org/abs/1512.03385">Deep Residual Learning for Image Recognition</a>", 2015.
6) Karen Simonyan, Andrew Zisserman: "<a href="https://arxiv.org/abs/1409.1556">Very Deep Convolutional Networks for Large-Scale Image Recognition</a>", 2015.
7) Christian Szegedy, et al. : "<a href="https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Szegedy_Going_Deeper_With_2015_CVPR_paper.pdf">Going Deeper With Convolutions</a>", 2015.