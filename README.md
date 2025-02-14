# Bike Share Data Analysis Project

## Project Overview

This project involves analyzing data from bike share systems in three major U.S. cities: Chicago, New York City, and Washington. Using Python, you will process and explore the data to answer various questions by calculating descriptive statistics. Additionally, you’ll develop an interactive script that takes user input to present these statistics dynamically in the terminal.

![Divvy Bike Sharing System](https://video.udacity-data.com/topher/2018/March/5aa7718d_divvy/divvy.jpg)  
*Image: [Wikipedia](https://en.wikipedia.org/wiki/Divvy)*

---

## Required Software

To complete this project, ensure the following tools and software are installed:

- **Python 3**, along with libraries **NumPy** and **pandas** (via Anaconda is recommended)
- A text editor like [Sublime Text](https://www.sublimetext.com/) or [Atom](https://atom.io/)
- A terminal application (Mac/Linux Terminal or Cygwin on Windows)

---

## About Bike Share Data

Bicycle-sharing systems allow short-term bike rentals, enabling users to travel between locations or take recreational rides. These systems are supported by technologies that track rentals and returns, offering a rich dataset for analysis. The focus of this project is on data from the first six months of 2017, provided by [Motivate](https://www.motivateco.com/), a major bike share operator.

This data includes information on:

- **Start Time** and **End Time**
- **Trip Duration** (in seconds)
- **Start Station** and **End Station**
- **User Type** (Subscriber or Customer)  
  Additionally, the Chicago and New York City datasets include **Gender** and **Birth Year** columns.

You will analyze how bike-sharing services are used and compare patterns among Chicago, New York City, and Washington.

---

## The Datasets

Randomly selected data for the first half of 2017 is provided for analysis. Each dataset contains the following **six columns**:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (e.g., 776 seconds)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)  

The Chicago and New York City datasets include additional columns:

- Gender
- Birth Year  

**Example**:  
![NYC Data Preview](https://video.udacity-data.com/topher/2018/March/5aa771dc_nyc-data/nyc-data.png)  

These files are pre-processed to focus on the core six columns. If interested, you can explore the original datasets here: [Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), and [Washington](https://www.capitalbikeshare.com/system-data).

---

## Statistics to Compute

Your goal is to calculate the following descriptive statistics:

### 1. **Popular Times of Travel**

   - Most common month
   - Most common day of the week
   - Most common hour of the days

### 2. **Popular Stations and Trips**

   - Most common start station
   - Most common end station
   - Most frequent trip (start to end station combination)

### 3. **Trip Duration**

   - Total travel time
   - Average travel time

### 4. **User Information**

   - Count of user types
   - Count of genders (only for NYC and Chicago)
   - Earliest, most recent, and most common birth years (only for NYC and Chicago)

---

## Files for the Project

To complete this project, you will work with the following files:

- **chicago.csv**
- **new_york_city.csv**
- **washington.csv**
- **bikeshare.py** (template script with helper code and comments)

These files can be downloaded as a zipped package in the resource tab of the classroom or included in the Project Workspace.

---

## Suggested Libraries

It is highly recommended to use **NumPy** and **pandas** for this project. These libraries are industry-standard tools for data analysis in Python and provide efficient methods for handling and analyzing data.

---

## Data Exploration

Begin by exploring the dataset using pandas. Here’s how you can get started:

### Questions to Answer:

1. What are the column names in the dataset?
2. Are there missing values?
3. What data types are in each column?

### Useful pandas Methods:

- `df.head()` – Displays the first few rows of the dataset.
- `df.columns` – Lists the column names.
- `df.info()` – Provides a summary of the dataset, including data types and missing values.
- `df.describe()` – Summarizes statistics for numerical columns.
- `df['column_name'].value_counts()` – Shows the count of unique values in a column.
- `df['column_name'].unique()` – Lists unique values in a column.