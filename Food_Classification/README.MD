# Food Classification with Machine Learning Techniques

The dataset used in this repo is Recipes5k comprehensive dataset for ingredients recognition which can be highlighted as:
<ul>
<li>Consists of 4,826 unique recipes composed of an image and the corresponding list of ingredients.</li>
<li>contains a total of 3,213 unique ingredients (10 per recipe on average)</li>
<li>Each recipe represents an alternative way to prepare one of the 101 food types contained in Food101</li>
<li>Nearly 50 alternative recipes belonging to each of the 101 classes were divided in train, val and test splits in a balanced way.</li>
</ul>

## General Process Flow
1) Import libraries
2) Load dataset
3) Data inspection
4) Preprocess data
5) Build and compile model
6) Training data
7) Testing data
8) Tuning and further experiment with various settings.

### Notes: These models are trained with limited small datasets and only tested with small amount of samples, thus, it is insufficient for production. Further research works and improvement on dataset and models will be carried out continuously.


## Test results
Here are some simple test results for a glance on various model performance.

| Models        | F1 Score 	|
| ------------- | ------------- |
| DNN_Softmax   |     0.66  	|
| DNN_Sigmoid   |     0.50	|

## References
1) Recipes5k dataset
Marc Bolaños, Aina Ferrà and Petia Radeva. “Food Ingredients Recognition through Multi-label Learning” In Proceedings of the 3rd International Workshop on Multimedia Assisted Dietary Management (ICIAP Workshops), 2017.