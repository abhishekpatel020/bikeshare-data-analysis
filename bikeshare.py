import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '/Users/abhishekpatel/Desktop/chicago.csv',
              'new york city': '/Users/abhishekpatel/Desktop/new_york_city.csv',
              'washington': '/Users/abhishekpatel/Desktop/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Args:
        None.
    Returns:
        (str) city - name of the city to analyze.
        (str) month - name of the month to filter by, or "all" to apply no month filter.
        (str) day - name of the day of week to filter by, or "all" to apply no day filter.
    """
    print('\nHello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington)
    cities_list = ['chicago', 'new york city', 'washington']
    # taking user input for city and lower() method is used convert it to lowercase
    # throughout this codebase whenever a user input has been taken, this conversion has been done
    city_input = input('\nFor which city you would like to see some stats and data for? Chicago\
, New York City, or Washington?\n').lower()
    # while loop to ensure valid user input
    while city_input not in cities_list:
        city_input = input('Invalid input, please try again.\n').lower()

    # get user input for month (all, january, february, ... june)
    months_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month_input = input('\nWould you like to add the month filter? If yes then which month? \
(january, february,..., june) or type "all" for no month filter\n').lower()
    # while loop to ensure valid user input
    while month_input not in months_list:
        month_input = input('Invalid input, please try again.\n').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day_input = input('\nWould you like to add the day filter? If yes then which day? \
(monday, tuesday,..., sunday) or type "all" for no day filter\n').lower()
    # while loop to ensure valid user input
    while day_input not in days_list:
        day_input = input('Invalid input, please try again.\n').lower()

    return city_input, month_input, day_input

    print('-'*80)


def load_data(city_load, month_load, day_load):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze.
        (str) month - name of the month to filter by, or "all" to apply no month filter.
        (str) day - name of the day of week to filter by, or "all" to apply no day filter.
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day.
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city_load])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time and make their own column for each
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month_load != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_load = months.index(month_load) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month_load]

    # filter by day of week if applicable
    if day_load != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day_load.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
       Args:
           (DataFrame) df: The data frame of a particular city.
       Returns:
           None.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    # using time() function from time module for time taken to perform calculation
    # this function is used throughout this code base
    start_time = time.time()

    if month == 'all':
        # uses mode method to find the most popular month
        common_month = df['month'].mode()[0]
        # display the most common month
        print('The most common month (1 = January, 2 = February, ... 6 = June):', common_month)

    if day == 'all':
        # uses mode method to find the most popular day
        common_day = df['day_of_week'].mode()[0]
        # display the most common day of week
        print('The most common day:', common_day)

    # extract hour from the Start Time column to create an 'hour' column
    df['hour'] = df['Start Time'].dt.hour
    # uses mode method to find the most popular hour
    common_hour = df['hour'].mode()[0]
    # display the most common start hour
    print('The most common start hour:', common_hour)

    # prints the time taken to perform the calculation
    # it will be there throughout this codebase
    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df: The data frame of a particular city.
    Returns:
        None.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # uses value_counts() method to get frequency count of each unique start stations
    # then extracting index of the start station having the highest frequency count by using index attribution
    com_start_station = df['Start Station'].value_counts().index[0]
    # display the most commonly used start station
    print('The most commonly start station: {}'.format(com_start_station))

    # uses value_counts() method to get frequency count of each unique end stations
    # then extracting index of the end station having the highest frequency count by using index attribution
    com_end_station = df['End Station'].value_counts().index[0]
    # display the most commonly used start station
    print('The most commonly end station: {}'.format(com_end_station))

    # combining Start Station and End Station columns to make a new
    # column 'Start to End Station' by using str concatination
    df['Start to End Station'] = df['Start Station'] + ' to ' + df['End Station']
    # uses value_counts() method to get frequency count of each unique start station and end station
    # combination then extracting index of the start station and end station
    # combination having highest frequency count by using index attribution
    start_end_station = df['Start to End Station'].value_counts().index[0]
    # display the most frequent combination of start station and end station trip
    print('The most frequent trip from start to end station is {}'.format(start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df: The data frame of a particular city.
    Returns:
        None.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # uses sum() method to calculate the total trip duration
    total_duration_sec = df['Trip Duration'].sum()
    # converting to minutes and seconds
    minutes, seconds = divmod(total_duration_sec, 60)
    # display total travel time
    print('The total trip duration is {} minutes and {} seconds'.format(minutes, seconds))

    # uses mean() method to calculate the mean trip duration
    average_duration_sec = round(df['Trip Duration'].mean())
    # converting to minutes and seconds
    avg_mins, avg_sec = divmod(average_duration_sec, 60)
    # display mean travel time
    print('The average trip duration is {} minutes and {} seconds'. format(avg_mins, avg_sec))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*80)


def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df: The data frame of a particular city.
    Returns:
        None.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # uses value_counts() to count user type (example: subsriber and customer)
    user_types = df['User Type'].value_counts()
    # display counts of user types
    print('User types breakdown is given below:\n')
    print(user_types)

    # this try clause is implemented to display the numebr of users by Gender
    # because all the three city's data doesn't have gender data available
    try:
        gender = df['Gender'].value_counts()
        print('\n\nGender breakdown is given below:\n')
        print(gender)
    except:
        print('\nGender data is not available.')

    # this try clause is implemented to display some information related to birth but
    # all the three city's data doesn't have birth year data available
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('\n\nThe earliest year of birth is {}.\nThe most recent year of birth is {}.\nThe most \
common year of birth is {}.'.format(earliest, recent, common_year))
    except:
        print('\nBirth year data is not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*80)


def display_raw_data(city_raw_data):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        (DataFrame) df: The data frame of a particular city.
    Returns:
        None.
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city_raw_data])

    # location variable is initialized to display data from a particular row
    location = 0

    # asking for user input if user wants to see raw data
    answer = input('Would you like to see the raw data of your choosen city? Enter "yes" or "no".\n').lower()
    while True:
        # if user input is neither 'yes' nor 'no' then, asking user again to give only valid input (example: 'yes' or 'no')
        if answer not in ('yes', 'no'):
            answer = input('Invalid input, please try again.\n').lower()
        # if user input is 'yes' then, display the raw data
        if answer == 'yes':
            print(df[location : location + 5])
            # increament location by 5
            location += 5
            # asking user if they would like to see more raw data
            answer = input('Would you like to see more raw data? Enter "yes" or "no".\n').lower()
        # if user input is 'no' then, exit while loop
        if answer == 'no':
            break

    print('-'*80)


# initial execution starts from here
while True:
    # calling get_filters()
    city, month, day = get_filters()
    # calling load_data()
    df = load_data(city, month, day)
    # calling time_stats()
    time_stats(df)
    # calling station_stats()
    station_stats(df)
    # calling trip_duration_stats()
    trip_duration_stats(df)
    # calling user_stats()
    user_stats(df)
    # calling display_raw_data()
    display_raw_data(city)

    # asking for user input if user wants to restart
    restart = input('\nWould you like to restart? Enter "yes" or "no".\n')
    while True:
        # if user input is neither 'yes' nor 'no' then, asking user again to give only valid input (example: 'yes' or 'no')
        if restart not in ('yes', 'no'):
            restart = input('Invalid input, please try again.\n').lower()
        # if user input is 'yes' then, restart by exiting inner while loop
        if restart == 'yes':
            break
        # if user input is 'no' then, exit from inner while loop
        if restart == 'no':
            break
    # exit from outer while loop as well to end the program
    if restart == 'no':
        break
