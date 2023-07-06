# ML - Engineering challenge

## Overview

* The simple linear regression model is implemented in [simple_linear_regr.py](./src/simple_linear_regr.py).
* The [main.py](./src/main.py) is updated to invoke API, which is defined at [api.py](./src/api.py).
* The code is packaged in the folder of [python_package](./python_package).
* The [Dockerfile](Dockerfile) package the code into a container.
* The CI/CD pipeline is established through GitHub Actions. 
* The components of an enterprise machine learning system can be found at [machine_learning_component.md](./docs/machine_learning_component.md).


## Objective

This system aims to predict the progress of diabetes in one year using bmi(body mass index). The input of the system is 
patient bmi number. The system outputs a response of interest, a quantitative measure of disease progression one year 
after baseline.

## Diagram
<img src="diagram.png" alt="drawing" width="60%" height="60%">

### Model training pipeline
#### Model training 
The model is a linear regression model. The loss function is minimised through SGD (Stochastic Gradient Descent), in which
the slope and the intercept of the linear equation is updated iteratively by randomly selecting one
training sample. The algorithm greatly improves the computational efficiency compared to the gradient descent algorithm.

#### Model validation 
The model is validated through coefficient of determination. When the model performance is greater than the threshold
value, i.e. `0.4` in this case, the model is used for prediction.

Benchmark result:

![image](https://github.com/niufuren/ML-ENGINEERING-CHALLENGE/assets/2469706/ba479773-a8c9-48c9-b719-2de73b471764)


### CI/CD
The CI/CD pipeline is established through GitHub Actions. When the code is pushed to GitHub repository, the GitHub Action
triggers a sequences of events. First, it runs tests to ensure the code and model quality. Next, it proceeds to build a Docker 
container image and pushes it to the AWS.

Subsequently, the pipeline initiates the deployment process to the staging environment on AWS ECS (Elastic Container Service).
Once the staging environment is deployed, the pipeline executes integration tests against the staging environment 
(this is a concept demo, no real tests running). Following the integration tests, the pipeline runs deployment to the AWS ECS production 
environment.

<img width="1851" alt="image" src="https://github.com/niufuren/ML-ENGINEERING-CHALLENGE/assets/2469706/af4dac64-4ff1-4940-90e1-7db59f652458">


### Model servicing 
The application is hosted on the AWS ECS service.  
To test the staging environment, you can access the API documentation at [here](http://load-balancer-staging-865855441.ap-southeast-2.elb.amazonaws.com/docs).  
To test production environment, the API documentation is available at [here](http://load-balancer-production-866833777.ap-southeast-2.elb.amazonaws.com/docs).

