# Three USA cities Bike-Share Data Analysis

### Video Demo:  <URL https://youtu.be/cVxzEO19HgE>

### Description:

Over the past decade, bike-sharing systems have been employed in many major cities -especially touristic- over the world.

#### What is Bike-Share System?
Bike-Share system allows users to rent bike from one point and return it to another point or the same point again and they pay in a hourly-based price. This allow bikes to be used by several users each day. The users lunlock the selected bicycle electronically through scanning a QR-code of the bicycle and supplying the mobile application with the information od the credit card to charge the user upon usage for the specified time and safe return to the station. This technology also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

#### Our Project:
In this project, I will use data -already had from previous project- of a bike-share system provider for three major cities in USA, which are Chicago, New York, and Washington. I will use this data to analyse bike-share usage statistics between these three cities.

#### Our Dataset:
Three files each of them with the name of one city of the three USA cities in .csv format is provided. Each file contains data of the first six months of 2017 for the specified city file. The three files contain Start Time, End Time, Trip Duration, Start Station, End Station, and User Type columns, while chicago and new_york files have additionally Gender and Birth Year columns.

#### Project flow:
The project is divide into three phases.
###### Get user preferentials
The program will ask the user three questions. First question `Which city would you like to explore it's data: Chicago, New York or Washington?` to determine which city file to load and start analysis on it. After getting the answer in the correct format we will move to the second question `Which month are you interested in?` and accepting the full or abbreviated format to decide which month to analyse or analyse all six months. The third question `Are you interested in a specific day?` which allow the user to dig deeper and specify a certain day of the week.
###### Display Statistics of the users' choices
In this section, the program will display the answers for several questions which are, the most frequent times of travel either in month, week or hour, the most popular station for starting the trip and the most common trip between two stations, the total time of trips and the average trip duration in the users' specified month or day or both, and statistics of the Bike-Share users as gender and age.
###### prompting for raw data and repeating analysis
In the end, the program will ask the user if he/she wishes to see raw data as 5 rows of the data at each time untill enough is reached by the user or the end of the data. Finally, the program will ask the user if he/she wants to start another round of analysis or exiting the program.


### Files:
chicago.csv: data of the first six months of 2017 for Chicago city bike-share system
new_york_city.csv: data of the first six months of 2017 for New York city bike-share system
washington.csv: data of the first six months of 2017 for Washington city bike-share system
requirments.txt: iteration of the required modules to successfully run the project file
README.md: readme file for documentation anf description of the project
project.py: the project code file in python
test_project.py: the testing code file for the project file


### Functions in the project.py file:

###### check_city:
This fuction is used to ask the user to choose one of the three cities (Chicago, Washington, and New York) and when the user enter the city only in the correct format it passes user entry to another function to filter data by city.

###### check_month:
This fuction is used to ask the user to choose one of the available six months (January, February, March, April, May, and June) or All for no specific month and when the user enter the month only in the correct format it passes user entry to another function to filter data by month.

###### def check_day:
This fuction is used to ask the user to choose one of the week days (Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, and Friday) or All for no specific day and when the user enter the day name only in the correct format it passes user entry to another function to filter data by day.

###### load_data:
This fuction uses the returns of the previous functions to load the specific data that the user select to be used for analysis by the following functions.

###### time_stats:
This fuction calculates and displays the most frequent times of travel.


###### station_stats:
This fuction calculates and displays the most popular stations and trip.

###### trip_duration_stats:
This fuction calculates and displays the total and average trip duration.

###### user_stats:
This fuction calculates and displays statistics on bike-share system users.

###### display_raw(df):
This fuction displays 5 rows of data for each time user answers with yes and terminate function when user answers with no.
