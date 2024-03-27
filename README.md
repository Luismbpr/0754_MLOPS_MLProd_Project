# Project Customer Score
### 0754_MLOPS_MLProd_Project


## Table of Contents
* [About](#about)
* [General Information](#general-information)
* [Languages](#languages)
* [Libraries Used](#libraries-used)
* [Dataset Information](#dataset-information)
* [More Information](#more-information)
* [Resources](#resources)


<br>
<br>

## About
Project to predict customer satisfaction given a set of inputs regarding customer's E-commerce data.

<br>

## General Information

Project development to predict the customer satisfaction given a series of inputs regarding customer's E-commerce data using MLOPS.

<br>

## Languages
    - Python

<br>

## Libraries Used
Some of the libraries used are:
    - Docker
    - Numpy
    - Pandas
    - Scikit-Learn
    - ZenML
    - MlFlow
    - Streamlit
    - MermaidJS

<br>


## Dataset Information
This dataset contains customer information of a Brazilian E-commerce site by Olist.

[Brazilian E-Commerce Public Dataset by Olist, and André Sionek](https://doi.org/10.34740/KAGGLE/DSV/195341)

<br>

## More Information

The project started with the development of a Machine Learning model that could predict customer satisfaction.
The following processes from  amd diagram_002 needed to be followed.

###### Diagram_001

```mermaid
flowchart LR;
    A[Data Input] --> B;
    B[Data Preprocessing] --> C;
    C[Model Training] --> D;
    D[Model Deployment];
```

<br>

###### Diagram_002
Creating a pipeline that could do these processes locally was important to see that the principal steps of the pipeline were working correctly.

![ Diagram_001](/README/0754_README_Images/Diagram_002_001.png?raw=true "Diagram_002_01")

<br>

The following process steps were thought out so that the old pipeline could be changed in order to work by deploying it on the cloud. On this case the model would be deployed on a Streamlit app.
ZenML was used to standardize the MLOPs processes along with MLFlow for tracking experiments.

###### Diagram_003
<!-- ![ Diagram_003](/README/0754_README_Images/Diagram_003_001.png?raw=true "Diagram_003_01") -->
![Diagram_003](README/0754_README_Images/Diagram_003_001_modif_001.png?raw=true "Diagram_001_001_modif_001")

<br>

###### Diagram_004
![Diagram_004_003](/README/0754_README_Images/Diagram_004_003.png?raw=true "Diagram_004_003")

<br>

<br>


## Resources

###### *Code based on [Free Code Camp](https://www.freecodecamp.org/). Special Thanks to Free Code Camp and instructor [Ayush Singh](https://github.com/ayush714)*

###### Dataset [Olist, and André Sionek. (2018). Brazilian E-Commerce Public Dataset by Olist [Data set]. Kaggle.](https://doi.org/10.34740/KAGGLE/DSV/195341)

<br>

## Acknowledgements

##### Thanks to Olist for releasing this dataset.
##### Thank you kindly to all who make information and knowledge available for free.

----
