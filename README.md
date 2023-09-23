<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django project." title="A Django project." /></a>![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Python](https://img.shields.io/badge/Python-3.8-blue)

<div style="text-align:center"><img src="./home_page.jpg" alt="pic" width="500"/>
</div>
# ai-proj

**License: MIT**

  This project is licensed under the terms of the [MIT](https://github.com/Polly7357/ai-proj/blob/master/LICENSE) LICENSE

**Contact Information**
---

  You can reach out to the project maintainer through https://polly7357.github.io/

We welcome contributions to this project. To contribute, follow these guidelines:

1. Fork the project repository.
2. Create a new branch for your contribution.
3. Make your changes and commit them.
4. Submit a pull request, explaining the purpose of your changes.

For more details, please refer to our [Contributing Guidelines](link-to-contributing-guidelines).

**Changelog**
---

**Version 0.2.0 (2023/09/21)**

- Fixed Database migration

**Version 0.1.0 (2023/09/20)**


### 1. Electricity Usage Estimation

**Content:**
+ This section allows users to input information about their household appliances and calculates daily electricity consumption, monthly electricity usage, and estimates electricity costs based on different pricing structures.

#### 1.1. Input Household Appliances
  Users can input details about their household appliances, including power consumption in watts (W) and daily usage hours.

#### 1.2. Daily and Monthly Electricity Consumption
  The function calculates the daily and monthly electricity consumption based on the user's input.

#### 1.3. Time-of-Use Pricing Estimates
- **Two-Tier Pricing**: Calculate estimated electricity costs based on a two-tier pricing structure.
- **Three-Tier Pricing**: Calculate estimated electricity costs based on a three-tier pricing structure.
- **Two-Tier Summer Pricing**: Calculate estimated electricity costs based on a two-tier pricing structure for the summer season.
- **Three-Tier Summer Pricing**: Calculate estimated electricity costs based on a three-tier pricing structure for the summer season.

 #### 1.4. Progressive Pricing Estimates
- **Input Bill Expense**: Users can input their electricity bill amount to understand their monthly electricity consumption.
 ```http
 /api/power/accu_usage/?total_expense=
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `total_expense`      | `string` | **Required**. total_expense of electricity bill |

- **Input desired electricity usage**: Users can input their electricity usage to estimate their electricity costs.
```http
 /api/power/accu_cost/?usage=xxx
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `usage`      | `string` | **Required**. Desired electricity consumption |

#### 1.5. Energy Saving Recommendations
Provide energy-saving recommendations based on the user's electricity usage and pricing options. These recommendations can help users evaluate the best pricing structure for their needs.

### 2. Carbon Footprint Estimation

**Content:**
This section allows users to input information about their daily consumption of various goods and services (food, clothing, housing, transportation) to estimate their carbon footprint (CDE - Carbon Dioxide Equivalent).

### 3. Management of Tariff Tables

**Content:**
This section helps Admins to manage electricity tariff tables and time-of-use rates.

#### 3.1. Electricity Tariff Table Management
- Admin can add, edit, or delete tariff tables.
- Each tariff table includes information about pricing tiers, peak/off-peak hours, and seasonal rates (if applicable).

#### 3.2. Time-of-Use Rate Management
- Admin can manage different time-of-use rate schedules, including regular and seasonal rates.

### 4. Real-Time AIoT Data Collection

**Content:**
This section discusses the real-time collection of AIoT (Artificial Intelligence of Things) data related to electricity usage.

>#### 4.1. AIoT Sensors
- [Describe the sensors and devices used to collect electricity usage data in real-time.]

>#### 4.2. Data Collection Frequency
- information collects hourly

>#### 4.3. Data Storage
- cloud sorage

### 5. System Environment


### 5. Installation
**Content:**
>1. Download the entire package by executing the command `git clone git@github.com:Polly7357/ai-proj.git`

>2. Make sure Django virtual environment is activated.

>3. To set up and run this project, you'll need to install the required Python packages and libraries listed in the "requirements.txt" file. You can do this using pip by running the following command:`pip install -r requirements.txt`

>4. Under /ai-proj directory, verify by checking if there's manage.py file in the same directory. If yes, you may start the server by executing the command
> `python manage.py runserver`


