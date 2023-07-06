# Machine Learning Component

For an enterprise machine learning system, it is worthwhile to add the following components to cover
the lifecycle of machine learning system development. These components are divided into critical parts and
nice to have parts according to the impacts.

## Critical components:
* Model monitoring and reporting

    Model monitoring and reporting oversee the model performance in production. It monitors from the aspects 
of operational wise and model wise. A good model monitoring system helps to quickly identify the root cause of failure of 
machine learning system. Also, it is used to decide the need to retrain a model.


* Experiment tracking and versioning

    The experiment tracking and versioning works to track the versions of data and model. It plays a critical role in model 
maintenance and to reproduce the model results. During the model development, multiple models may be developed, and only 
one model is used for production. An experiment tracking and versioning system effectively locates the versions of data and 
model in production.


* Data governance

  Data governance involves the data collection, storage, the control of data quality and compliance with regulations.
As data is a fundamental part in machine learning system, it is critical to perform data governance to ensure the reliability of the 
model outputs. Besides, for an enterprise machine learning system, data governance is a critical tool to reduce the data related 
risk, such as in this case the personal information of patients are not misused for other purposes.  

## Nice to have:
* Automated model selection

  A manual model selection takes time and effort. It would be good to select the best model automatically to improve the efficiency.


* User-friendly interface
  
  It would be good to have an interface for the users to easily access the prediction results and provide feedback. This can be
a mobile app or a web client. The feedback can be used in the model redevelopment. 
