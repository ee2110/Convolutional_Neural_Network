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

## References
1) https://cs231n.github.io/convolutional-networks/
2) https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53
3) https://indoml.com/2018/03/07/student-notes-convolutional-neural-networks-cnn-introduction/