# Fashion MNIST Classification

This repository contains code for training Multi-Layer Perceptron (MLP) models on the Fashion MNIST dataset. Fashion MNIST is a dataset of Zalando's article images—consisting of a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image, associated with a label from 10 classes representing different clothing and accessory items.

## Dataset Overview

Fashion MNIST provides a more challenging alternative to the classic handwritten digits of MNIST. While both datasets share a similar structure, Fashion MNIST introduces more complex patterns and shapes, making it a more realistic representation of real-world image classification tasks. Additionally, Fashion MNIST helps researchers and practitioners evaluate the performance of machine learning algorithms in domains beyond digit recognition, such as fashion and clothing classification.

#### [Classes](https://github.com/shoryasethia/fashion-mnist/blob/main/class_list.py) in fashion-mnist
```
class_names = ['T-shirt/top', 
               'Trouser',
               'Pullover', 
               'Dress', 
               'Coat', 
               'Sandal', 
               'Shirt', 
               'Sneaker', 
               'Bag', 
               'Ankle boot']
```

#### Loading Fashion-Mnist
```
(X_train, y_train),(X_test,y_test) = datasets.fashion_mnist.load_data()
```
## Comparison with MNIST

Compared to the MNIST dataset, Fashion MNIST offers several advantages:

- **Real-world Relevance**: Fashion MNIST captures a broader range of visual patterns, making it more suitable for evaluating the robustness and generalization capabilities of machine learning models.
- **Increased Complexity**: Fashion MNIST images exhibit more intricate details and structures compared to the simple handwritten digits in MNIST, challenging models to learn richer representations.
- **Diverse Classes**: With 10 classes representing various clothing and accessory items, Fashion MNIST provides a more diverse set of classification tasks, reflecting real-world scenarios more accurately.

However, Fashion MNIST also presents some challenges:

- **Higher Dimensionality**: The increased complexity of Fashion MNIST images results in higher-dimensional input data, requiring more sophisticated models and longer training times.
- **Harder Discrimination**: Distinguishing between different clothing items can be more challenging than recognizing handwritten digits, requiring models to learn more nuanced features.

> Checkout my [this](https://github.com/shoryasethia/Digit-Recognition) repo on MNIST dataset as well

## Dropout Regularization

Dropout is a **regularization** technique commonly used in neural networks to prevent overfitting. It works by randomly dropping out (setting to zero) a fraction of input units during training, which helps prevent units from co-adapting too much to the training data. This encourages the network to learn more robust features that are useful across different input samples, improving generalization performance on unseen data.

#### Importing Dropout
```
from tensorflow.keras import layers
from layers import Dropout
```

#### Using Dropout
> **assuming we have already declared a model with name `model`**
```
model.add(Dropout(0.20))
```
> **It Drops 20% of total neurons from previous layer**
## Models

The repository contains implementations of three MLP models: `mlp1`, `mlp2`, and `mlp3` in [this](https://github.com/shoryasethia/fashion-mnist/blob/main/fashio-mnist.ipynb) notebook.



| Model   | Architecture File| Accuracy | Trained Model Link| 
|---------|------------------|----------|-------------------| 
| MLP1    | [mlp1.py](https://github.com/shoryasethia/fashion-mnist/blob/main/mlp1.py)|0.8823999762535095| [.h5](https://github.com/shoryasethia/fashion-mnist/blob/main/mlp1-fashion-mnist.h5)| 
| MLP2    | [mlp2.py](https://github.com/shoryasethia/fashion-mnist/blob/main/mlp2.py)|0.8848999738693237| [.h5](https://github.com/shoryasethia/fashion-mnist/blob/main/mlp2-fashion-mnist.h5)| 
| MLP3    | [mlp3.py](https://github.com/shoryasethia/fashion-mnist/blob/main/mlp3.py)|0.8859000205993652 | [.h5](https://github.com/shoryasethia/fashion-mnist/blob/main/mlp3-fashion-mnist.h5)| 

> **[Conclusion](https://github.com/shoryasethia/fashion-mnist/blob/main/fashio-mnist.ipynb) : All three models (mlp1, mlp2, mlp3) are bit in-accurate in distinguishing between shirt/t-shirt/pullover/coat**

## Results
>* model1 : mlp1
>* model2 : mlp2
>* model3 : mlp3

**![History vs Epochs](https://github.com/shoryasethia/fashion-mnist/blob/main/f343f54a-b101-4c96-b52d-c0545166135c.png)**
___________________________________________________________________________________________________________________________________________________________
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author : [@shoryasethia](https://github.com/shoryasethia)
> **If anything helps you from this repo, do give it a star**
