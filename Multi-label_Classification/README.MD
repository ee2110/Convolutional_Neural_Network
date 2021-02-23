# Multi-Label Classification



## Advantages of Multi-Label Classification:
<ul>
<li><b>Content-Based Retrieval</b></li>
<p>Nowadays, we can easily search desired items just by using the photo or item image without mention the item's name. For example, we can search many objects on google or some large e-commerce application by just upload the photo of the object we looking for. The Multi-Label Classification function provide convenience to online users search multiple target items easily, it enhance the ability of search engines to retrieve very specific queries of a given product photo.</p>

<li><b>Frame Translation</b></li>
<p>By using advantages of computer vision techniques, we can convert picture into words! Multiple object detection in single photo or video frames can contribute to scene understanding.</p>
</ul>

## Methods of multi-label classification
<ul>
<li><b>Full Softmax</b></li>
<p>Full softmax is consider one of the method, but it is inpractical when there is many class or category label.</p>
<li><b>Modify final layer of neural networks</b></li>
<p>One of the easier way is just to modify the neural network layer. In the last layer before output prediction, we can use sigmoid activation to replace the softmax activation layer. <i>Recall note: Softmax assigns decimal probabilities to each class in a multi-class problem. Those decimal probabilities must add up to 1.0.</i></p>
</ul>


## References:
<ol>
<li><a href="https://nanonets.com/blog/multi-label-classification-using-deep-learning/">Nanonets</a></li>
<li><a href="http://www.ub.edu/cvub/recipes5k/">Recipes5k</a></li>
</ol>