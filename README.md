# Instant Mildew Detector

* Instant Mildew Detector is an app that uses predictive analytics to detect and predict the presence of powdery mildew on cherry leaves. The app takes an image of a cherry leaf as input and produces an output indicating whether the leaf is healthy or infected with powdery mildew. This app helps clients ensure that they are not supplying a compromised quality product to the market. 
* Instant Mildew Detector is designed using the classification model in machine learning. Therefore, it suggests a binary classifier, indicating whether a particular cherry leaf is healthy or contains powdery mildew.

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* We suspect that powdery mildew leaves show clear signs of infection, such as light, roughly circular, powdery patches on young, susceptible leaves (light green expanding leaves). These patches can be distinguished from healthy leaves.

* An Image Montage shows that typically powdery mildew leaves have fine white marks across. Average Image, Variability Image, and Difference between Averages studies didn't reveal any clear pattern to differentiate one from another


## The rationale to map the business requirements to the Data Visualisations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.


## ML Business Case
* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
* Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Numpy is used to handle multi-dimensional arrays and includes a wide set of mathematical functions to operate on these arrays. 
* Pandas is used for data analysis including performing statstical analysis. 
* Matplotlib is used for data visualization and helps in embedding plotts in Jupyter notebooks. 
* Seaborn provides a high-level intetrface for statstiical graphics and it offers a built-in themes for styling Matplot graphics. 
* Plotly is used for plotting data and and functions, add intteractivity and animation to data visualization. 
* Scikit-learn contain tools for predictive analysis. allows to train machine learning models for classification and clustetring. 
* tensorflow used to reduce the error in every iteration while fitting the model by using an optimiser and loss function.
* keras provides the python interface for artificial neural networks. 
* itertools used to iterate over data structures than can be sttepped over using a for-loop. 
* random is used to generate random numbers. 


## Credits 

* This app is built by forking the template proven by Code Institute and the codes are 
similar to the walkthrough project 1. 
* The description for data Analysis and Machine Learning Libraries are taken from the CI lecture notes/videos. 


### Content 

- The information regarding powdery mildew is taken from [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew).

### Media

- The cherry leave images dataset are taken from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).


## Acknowledgements (optional)
* Thank you to the people at code institute and in the slack who have been an increidble resource throughout my time working on this project.
