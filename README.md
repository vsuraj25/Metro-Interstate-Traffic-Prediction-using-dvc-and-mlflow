[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<div id="top"></div>

<div align="center">
  <a href="https://github.com/vsuraj25">
    <img src="https://img.icons8.com/clouds/100/null/traffic-jam.png" alt="Logo" width="80" height="80"/> 
  </a>

    
<h3 align="center">Metro Interstate Traffic Prediction</h3>

 <p align="center">
    Machine Learning Project (Internship)
    <br />
    <a href="https://github.com/vsuraj25"><strong>Explore my Repositories. »</strong></a>
    <br />
    <br />
    <a href="#intro">Introduction</a>
    ·
    <a href="#data"> Data Information</a>
    ·
    <a href="#contact">Contact</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## **Problem Statement**
* Nowadays, traffic is a major issue for everyone, and it is a source of stress for anyone
who has to deal with it on a daily basis. The growth of the population delays traffic and
makes it worse day by day. The settlement of modern civilization looks at it, but it is
unable to act in such a way as to protect people. We can watch traffic, collect data, and
anticipate the next and subsequent observations using a variety of approaches and
patterns. The observation agency then makes observations, which are then required out
and predictions are made. Being stuck in a cosmopolitan city's traffic is the most
common occurrence in one's life.
The goal of this project is to build a prediction model using multiple machine learning
techniques and to use a template to document the end-to-end stages. We're trying to
forecast the value of a continuous variable with the Metro Interstate Traffic Volume
dataset, which is a regression issue.



## **Deployed app**
[![App Screenshot](https://user-images.githubusercontent.com/55409076/210774151-24799ff0-dbf3-4240-8334-6b96d8cd4673.PNG)](https://web-production-35a4.up.railway.app/)

[Deployed app link](https://web-production-35a4.up.railway.app/)

<!-- GETTING STARTED -->
<div id="intro"></div>

## **Introduction**
*  This project aims to build a prediction model which will help us to find out the traffic volume based on different factors such as time, weather conditions and holidays. We have used ensemble learning algorithms to develop the prediction model. This entire project is build using DVC (Data Version Control) and MLFlow for retraining, experimenting and model monitoring purpose. 
  
 
<div id="data"></div>
<!-- USAGE EXAMPLES -->

## **Dataset Information**

* Download the original dataset here : 
  [Metro Interstate Traffic Volume Data](https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume)

 
* The dataset used in this project is a UCI machine learning dataset. 
* The data at every transformation is uploaded and extracted from mongoDB database. 
* The dataset contains hourly interstate 94 westbound traffic volume for MN DoT ATR
station 301. 
* The region of data lies between regions of Minneapolis. 
* It includes features such as holiday, time, weather, etc. which impacts the traffic volume traffic volume directly.
* Shape of Original Data - (48204, 9)

* **Attribute Information**

1. `holiday`: Indicates if the date is a holiday and if it specifies the holiday, if not None.
2.	`temp`: Indicates the temperature in Kelvin.
3.	`rain_1h`: Amount in mm of rain that occurred in the hour.
4.	`snow_1h`: Amount in mm of snow that occurred in the hour.
5.	`clouds_all`: Percentage of cloud cover.
6.	`weather_main`: Short textual description of the current weather.
7.	`weather_description`: Longer textual description of the current weather.
8.	`date_time`: Hour of the data collected in local CST time.
9.	`traffic_volume`: Hourly I-94 ATR 301 reported westbound traffic volume.


<p align="right">(<a href="#top">back to top</a>)</p> 

<!-- USAGE EXAMPLES -->
## **Project Architecture**

[![Project Architecture](https://user-images.githubusercontent.com/55409076/210779327-7d46df01-760d-4162-97cc-b3fe405985a9.png)](https://github.com/vsuraj25)

## **Latency for model response**
 
* 01.60 Seconds

## **Project Demo Youtube Video**
[![Project Youtube Video](https://user-images.githubusercontent.com/55409076/210784070-12f54e09-e5c0-417f-b7cd-1941a1247865.png)](https://www.youtube.com/watch?v=-gdZvsES43Q)

## **Linkedin Post**
[![Metro Interstate Traffic Predction Project](https://img.shields.io/badge/Metro_Interstate_Traffic_Predction_Project-eeeeee?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=0A66C2)](https://www.linkedin.com/posts/suraj-verma-982b31157_machinelearning-internship-datascience-activity-7016772812791001088-QBcp/?utm_source=share&utm_medium=member_desktop)


## **About this Internship Project**

* Project Title : Metro Interstate Prediction
* Technologies : Machine Learning
* Domain : Transport
* Project Difficulties level : Intermediate

## **Requirements**
* Python 3.7
* Numpy
* Pandas
* Flask
* Pytest
* Tox
* DVC
* MLFlow
* MongoDB
* Checkout requirements.txt for more information.

## **Technologies used**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-945DD6?style=for-the-badge&logo=dataversioncontrol&logoColor=white)
![MLFlow](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=for-the-badge&logo=numpy&logoColor=blue)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)


## **Tools used**
![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-131415?style=for-the-badge&logo=railway&logoColor=white)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)
![MLFlow](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=for-the-badge&logo=numpy&logoColor=blue)

<!-- CONTACT -->
<div id="contact"></div>

## **Contact**
[![Suraj Verma | LinkedIn](https://img.shields.io/badge/Suraj_Verma-eeeeee?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=0A66C2)][reach_linkedin]
[![Suraj Verma | G Mail](https://img.shields.io/badge/sv255255-eeeeee?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=EA4335)][reach_gmail]
[![Suraj Verma | G Mail](https://img.shields.io/badge/My_Portfolio-eeeeee?style=for-the-badge)][reach_gmail]

[reach_linkedin]: https://www.linkedin.com/in/suraj-verma-982b31157/
[reach_gmail]: mailto:sv255255@gmail.com?subject=Github


<p align="right">(<a href="#top">back to top</a>)</p>



