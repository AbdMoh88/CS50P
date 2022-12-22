# importing modules required for project
import time
import pandas as pd
from datetime import datetime


# dictionary to be used for loading data
cities_data = { "Chicago": "chicago.csv",
              "New York": "new_york_city.csv",
              "Washington": "washington.csv" }
# dictionary to be used for filtering data by month
months_dict = { "Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April",
              "May": "May", "Jun": "June", "All": "All" }
# dictionary to be used for filtering data by day
days_dict = { "Sat": "Saturday", "Sun": "Sunday", "Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday",
            "Thu": "Thursday", "Fri": "Friday", "All": "All" }


def check_city(c):
    """
    This fuction is used to check for user entry as city

    :param c: this is the user input as city name
    :type c: str
    :returns: this return the user input when it is right
    :rtype: str
    """
    if c in cities_data.keys():
        return c
    else:
        return False


def check_month(m):
    """
    This fuction is used to check for user entry as month

    :param m: this is the user input as month name or all in the supported format
    :type m: str
    :returns: this return the user input when it is right
    :rtype: str
    """
    if m in months_dict:
        m = months_dict[m]
        return m
    elif m in months_dict.values():
        return m
    else:
        return False


def check_day(d):
    """
    This fuction is used to check for user entry as day

    :param d: this is the user input as day name or all in the supported format
    :type d: str
    :returns: this return the user input when it is right
    :rtype: str
    """
    if d in days_dict:
        d = days_dict[d]
        return d
    elif d in days_dict.values():
        return d
    else:
        return False


def load_data(city, month, day):
    """
    This fuction Loads data for the specified city and filters by month and day if applicable.

    :param city: name of the city to analyze
    :param month: name of the month to filter by, or "all" to apply no month filter
    :param day: name of the day of week to filter by, or "all" to apply no day filter
    :type city: str
    :type month: str
    :type day: string
    :returns: city data filtered by month and day
    :rtype: DataFrame
    """
    # load data file into a dataframe
    sel_city_data = pd.read_csv(cities_data[city])

    # convert the Start Time  and End Time column to datetime
    sel_city_data["Start Time"] = pd.to_datetime(sel_city_data["Start Time"])
    sel_city_data["End Time"] = pd.to_datetime(sel_city_data["End Time"])

    # extract month and day of week from Start Time to create new columns with week and month names
    sel_city_data["month"] = sel_city_data["Start Time"].dt.month_name()
    sel_city_data["day_of_week"] = sel_city_data["Start Time"].dt.day_name()

    # pass the filter by month when all is chosen
    if month == "All":
        monthly_data = sel_city_data
        # filter by the chosen day of week
        if day != "All":
            chosen_data = monthly_data[monthly_data["day_of_week"] == day]
        else:
            chosen_data = monthly_data
    # filter by the chosen month
    elif month != "All":
        monthly_data = sel_city_data[sel_city_data["month"] == month]
        # then filter by the chosen day of week
        if day != "All":
            chosen_data = monthly_data[monthly_data["day_of_week"] == day]
        # pass the day filter when all days are chosen
        else:
            chosen_data = monthly_data
    return chosen_data


def time_stats(df, month, day):
    """
    This fuction displays the most frequent times of travel.

    :param df: the data of the previously selected city by the user
    :param month: name of the month to filter by, or "all" to apply no month filter
    :param day: name of the day of week to filter by, or "all" to apply no day filter
    :type df: DataFrame
    :type month: str
    :type day: str
    :returns: the most frequent times of travel
    :rtype: str
    """
    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()
    # display the most common month (if specific month is not selected)
    if month == "All":
        most_common_month = df["month"].mode()[0]
        print(f"Most frequent month is {most_common_month}")
    # display the most common day of week (if specific day is not selected)
    if day == "All":
        most_common_day = df["day_of_week"].mode()[0]
        print(f"Most frequent day is {most_common_day}")
    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    # calculating most common hour in AM/PM time format
    most_common_hour = datetime.strptime(str(df["hour"].mode()[0]), "%H").strftime("%I %p")
    print(f"Rush hour is {most_common_hour}")
    # calculate the time taken for calculations
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    # separate most frequent travel times statistics from other statistics
    print('-'*40)


def station_stats(df):
    """
    This fuction displays the most popular stations and trip.

    :param df: the data of the previously selected city by the user
    :type df: DataFrame
    :returns: the most popular stations and trip
    :rtype: str
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    most_popular_start_station = df["Start Station"].mode()[0]
    print(f"Most popular start station is {most_popular_start_station}")
    # display most commonly used end station
    most_popular_end_station = df["End Station"].mode()[0]
    print(f"Most popular end station is {most_popular_end_station}")
    # display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(["Start Station", "End Station"]).size().idxmax()
    print(f"Most frequent trip is \
        \nFrom: {most_frequent_combination[0]}     To:{most_frequent_combination[1]}")
    # calculate the time taken for calculations
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    # separate most popular stations statistics from other statistics
    print('-'*40)


def trip_duration_stats(df):
    """
    This fuction displays the total and average trip duration.

    :param df: the data of the previously selected city by the user
    :type df: DataFrame
    :returns: the total and average trip duration.
    :rtype: str
    """
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_trip_duration = df["Trip Duration"].sum()
    print(f"Total travel time is {round(total_trip_duration // 60)} hrs and {round(total_trip_duration % 60)} mins")
    # display mean travel time
    mean_travel_duration = df["Trip Duration"].mean()
    print(f"Average travel time is {round(mean_travel_duration // 60)} hrs and {round(mean_travel_duration % 60)} mins")
    # calculate the time taken for calculations
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    # separate most popular stations statistics from other statistics
    print('-'*40)


def user_stats(df, city):
    """
    This fuction displays statistics on bikeshare users.

    :param df: the data of the previously selected city by the user
    :param city: name of the city to analyze
    :type df: DataFrame
    :type city: str
    :returns: statistics on bikeshare users
    :rtype: str
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = df["User Type"].value_counts()
    print(f"The count of each user type: \n{user_types.to_string()}\n")
    # Display counts of gender in Chicago and New York Only
    if city != "Washington":
        user_gender = df["Gender"].value_counts()
        print(f"The count of users gender: \n{user_gender.to_string()}\n")
        # Display earliest, most recent, and most common year of birth
        youngest = df["Birth Year"].max()
        oldest = df["Birth Year"].min()
        most_common_age = df["Birth Year"].mode()
        print(f"The oldest user born: {int(oldest)}\nThe youngest user born: {int(youngest)}\nMost users birth year: {int(most_common_age)}")
    # calculate the time taken for calculations
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    # separate most popular stations statistics from other statistics
    print('-'*40)


def display_raw(df):
    """
    This fuction displays 5 rows of data for each user prompt.

    :param df: the data of the previously selected city by the user
    :type df: DataFrame
    :returns: 5 rows of data for each user prompt.
    :rtype: DataFrame
    """
    i = 0
    while True:
        # get user approval for displaying raw data
        raw = input("\nWould you like to see sample of raw data? Enter Yes or No.\n").title()
        # print the correct sequence of data rows
        if raw == "Yes" and i < len(df):
            print(df.iloc[i:(i + 5)])
            i += 5
        # the  loop breaks when the user reach the end of the data rows
        elif i >= len(df):
            print("The Data has ended")
            break
        # break the loop upon user request
        elif raw == "No":
            break


def main():
    # print welcoming message to the user
    print()
    print("Hello! Let's explore some US bikeshare data!\n\n".center(120))
    # looping the entire work for another analysis required by the user in the end
    while True:
        # looping each user input as city untill the correct entry is given
        while True:
            # asking the user to choose one city from Chicago, New York or Washington
            user_city = input("Which city would you like to explore it's data: Chicago, New York or Washington? \n").title().strip()
            # if the user input is incorrect display a message
            if check_city(user_city) == False:
                print("Please! insert a valid choice")
            # if the user input is correct proceed
            else:
                city = check_city(user_city)
                break
        # looping each user input as month untill the correct entry is given
        while True:
            # asking the user to choose one of the months or all to analyze
            user_month = input('\n\nWhich month are you interested in? \
                \nChoose either All or month name (January, ....., June)\
                N.B. "January" or "Jan" format \n'
                ).title().strip()
            # if the user input is incorrect display a message
            if check_month(user_month) == False:
                print("Please! insert a valid choice")
            # if the user input is correct proceed
            else:
                month = check_month(user_month)
                break
        # looping each user input as month untill the correct entry is given
        while True:
            # asking the user to choose one day of the week or all to analyze
            user_day = input('\n\nAre you interested in a specific day? \
                \nIf "Yes" type the day in either \"Monday\" or \"Mon\" format \
                \nIF \"No\" type All. \n'
                ).title().strip()
            # if the user input is incorrect display a message
            if check_day(user_day) == False:
                print("Please! insert a valid choice")
            # if the user input is correct proceed
            else:
                day = check_day(user_day)
                break
        # using our created functions to display statistical analysis of the user choice
        user_data = load_data(city, month, day)
        time_stats(user_data, month, day)
        station_stats(user_data)
        trip_duration_stats(user_data)
        user_stats(user_data, city)
        # asking if the user want to see raw data tables with 5 rows at a time
        display_raw(user_data)
        # prompting the user for another analysis or exit
        restart = input("\nWould you like to restart? Enter Yes or No.\n").title()
        if restart != "Yes":
            break


if __name__ == "__main__":
    main()
