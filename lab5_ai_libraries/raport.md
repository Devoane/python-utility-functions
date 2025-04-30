# Report – Python Libraries for Artificial Intelligence

## Selected Domain
Artificial Intelligence (AI), with a focus on Machine Learning (ML) and Deep Learning (DL).

This report presents two widely used Python libraries in the field of AI:
- **scikit-learn** – for traditional machine learning algorithms.
- **TensorFlow (Keras)** – for building and training neural networks.

---

## 1. scikit-learn

**Description:**  
scikit-learn is a high-level Python library that provides simple and efficient tools for data mining and data analysis. It is built on top of NumPy, SciPy, and matplotlib. The library includes implementations of many classical machine learning algorithms such as decision trees, support vector machines, and clustering methods.

**Use Cases:**  
- Classification and regression  
- Clustering (e.g., k-means)  
- Dimensionality reduction  
- Model evaluation and validation

**Advantages:**  
- Easy to learn and use  
- Well-documented  
- Good for small to medium datasets  
- Seamless integration with NumPy and pandas

**Limitations:**  
- Does not support GPU acceleration  
- Not designed for deep learning or very large datasets

**Official Documentation:**  
🔗 [scikit-learn documentation](https://scikit-learn.org)

### Code Example: Iris Flower Classification using Decision Trees

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create and train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate and print accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
```

**Sample Output:**  
```
Accuracy: 1.00
```

---

## 2. TensorFlow (Keras)

**Description:**  
TensorFlow is a powerful open-source platform developed by Google for building and training machine learning and deep learning models. Keras is a high-level API integrated into TensorFlow, designed to enable fast experimentation with neural networks.

**Use Cases:**  
- Deep learning (image recognition, speech processing, etc.)  
- Natural language processing (NLP)  
- Time series forecasting  
- Custom AI models for research and production

**Advantages:**  
- Supports GPU and TPU acceleration  
- Scalable and flexible  
- Large community and ecosystem  
- Built-in support for model saving, exporting, and deployment

**Limitations:**  
- Higher complexity compared to scikit-learn  
- Requires more system resources  
- Initial learning curve can be steep for beginners

**Official Documentation:**  
🔗 [TensorFlow documentation](https://www.tensorflow.org/keras)

### Code Example: Handwritten Digit Classification using Neural Networks

```python
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize image data
x_train = x_train / 255.0
x_test = x_test / 255.0

# One-hot encode labels
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# Build the model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(x_train, y_train_cat, epochs=3, batch_size=32, validation_split=0.1)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test_cat)
print(f"Test accuracy: {accuracy:.2f}")
```

**Sample Output:**  
```
Test accuracy: 0.98
```

---

## Summary

Both **scikit-learn** and **TensorFlow (Keras)** are powerful tools for machine learning and deep learning in Python. **scikit-learn** is excellent for traditional ML algorithms and smaller datasets, while **TensorFlow** offers robust solutions for deep learning applications, supporting advanced models and GPU acceleration.

---



