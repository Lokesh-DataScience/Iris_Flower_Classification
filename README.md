# Iris_Flower_Classification 

## Project Overview

Iris Flower Classification model which will classify the Iris flowers wthin it's three species (Iris-Setosa,Iris-Virginica,Iris-Versicolor).

## Repository Contents

- **IRIS.ipynb**: Jupyter notebook containing the complete code for training and evaluating the Iris Flower Classification model.
- **Iris_web_app.py**: Python script that provides a graphical user interface (GUI) using Streamlit to demonstrate the Iris Flower Classification model.
- **rf_model.pkl**: Pretraained model from `IRIS.ipynb`.
- **scaler.pkl**: Model to scale the inputs for `Iris_web_app.py`.
- **requirements.txt**: List of Python libraries required to run `IRIS.ipynb` and `Iris_web_app.py`.
- **Iris.csv**: Dataset of Iris Flower classification model.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.12
- pip

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Lokesh-DataScience/oibsip_1.git
    cd oibsip_1
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Demo

To run the GUI demo of the Iris Flower Classification model:

```bash
python Iris_web_app.py
```
### Usage
- **The Iris_web_app.py scripts open a window displaying the web page.**
- **The model will take inputs from user and predicts species of flower.**
- **The IRIS.ipynb notebook can be used to understand and reproduce the training process of the model.**

### Model Details
- **The Iris Flower Classification model used for Iris flower classification is saved in the rf_model.pkl file.**
- **This model is trained on a dataset of Iris flower and is capable of predicting Iris Species.**

### Contributing
- **Contributions are welcome! Please feel free to submit a Pull Request.**

### Acknowledgements
- **Streamlit for providing the tools for creating a web app.**
- **scikit-learn for the machine learning framework.**

