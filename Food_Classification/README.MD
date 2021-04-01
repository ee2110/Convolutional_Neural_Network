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

## Binary Classification

| Models        | F1 Score micro | F1 Score macro | F1 Score weighted|    Avg acc   | Avg val acc  |   Avg loss   | Avg val loss |
| ------------- | -------------- | -------------- |  --------------- | ------------ | ------------ | ------------ | ------------ |
| DNN_Softmax   |     1.00  	 |     1.00 	  |     1.00  	     |      0.77    |      0.76    |      0.74    |      0.66    |
| DNN_Sigmoid   |     0.75	 |     0.73  	  |     0.73  	     |      0.77    |      0.76    |      0.74    |      0.68    |
| Basic CNN     |     1.00  	 |     1.00 	  |     1.00  	     |      0.51    |      0.41    |      0.71    |      0.83    |
| MobileNet-v2  |     1.00	 |     1.00  	  |     1.00  	     |      0.99    |      0.99    |      0.033   |      0.008   |

## MultiClass Classification

| Models        | F1 Score micro | F1 Score macro | F1 Score weighted|    Avg acc   | Avg val acc  |   Avg loss   | Avg val loss |
| ------------- | -------------- | -------------- |  --------------- | ------------ | ------------ | ------------ | ------------ |
| DNN_Softmax   |     0.15  	 |     0.092  	  |     0.091  	     |      0.16    |      0.17    |      2.34    |      2.29    |
| Basic CNN     |     0.50	 |     0.44  	  |     0.44  	     |      0.50    |      0.39    |      1.33    |      1.89    |
| MobileNet-v2  |     0.85	 |     0.81  	  |     0.81  	     |      0.95    |      0.83    |      0.16    |      0.48    |
| Basic CNN     |     0.091	 |     0.091  	  |     0.73  	     |      0.77    |      0.76    |      0.74    |      0.68    |
| Basic CNN     |     0.091	 |     0.091  	  |     0.73  	     |      0.77    |      0.76    |      0.74    |      0.68    |


## References
1) Recipes5k dataset
Marc Bolaños, Aina Ferrà and Petia Radeva. “Food Ingredients Recognition through Multi-label Learning” In Proceedings of the 3rd International Workshop on Multimedia Assisted Dietary Management (ICIAP Workshops), 2017.