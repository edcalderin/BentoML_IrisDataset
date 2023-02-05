# First contact with BentoML: Deploying a model

## Introduction

Since this is just a test using BentoML I create a naive Machine Learning model with Iris dataset. It consists of a classifier to predict one of the 4 corresponding labels.  
Then, I used BentML to persist the models and leveraging BentoML features in order to automatically set a version tag to these ones.  
Finally, FastAPI takes an important rol here by loading the saved model and making predictions through an API using the same neat features provided by BentoML.

## Steps to reproduce (Jumping some steps)

1. Execute the notebook until the end, the goal here is having a saved model into your user directory.
2. Install tox with ´pip install tox´.
3. Browse to ´fastapi´ directory and run ´tox -e python3.11-run´.
4. Go to http://127.0.0.1:3000/