# Bike Sharing Dataset Analysis Project
This project analyzes the Bike Sharing Dataset to understand the impact of weather conditions and weekdays on bike rentals. The analysis is performed using Python libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Streamlit for visualization and dashboard creation.

## Installation
1. Clone the repository
   ```
   git clone https://github.com/nasrull4/Project_Analisis_Data.git
   ```
2. Setup Environment
   ```
   cd Project_Analisis_Data
   ```
3. Install Required Packages
   ```
   pip install -r requirements.txt
   ```
4. Run steamlit app
   ```
   streamlit run ./dashboard/dashboard.py
   http://localhost:8501
   ```
## Project Structure
   ```
    submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───data_1.csv
| └───data_2.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
```
## Usage
# 1. Data Wrangling:
The collection, assessment, and cleaning of the bike sharing dataset was done by loading the day.csv and hour.csv datasets. The data was then checked and cleaned for missing values ​​and outliers to ensure the accuracy of the analysis.
# 2. Exploratory Data Analysis (EDA):
The data is grouped by weather conditions and day of the week. The results show that the number of bike rentals is higher in sunny weather conditions and weekdays.
# 3. Visualization:
The visualization shows that bike rentals are highest during sunny weather, while the number of rentals decreases during bad weather conditions. In addition, the rental frequency by day shows that weekdays (Monday to Friday) have a higher number of rentals compared to weekends, indicating that bikes are a more popular transportation option during weekdays.

