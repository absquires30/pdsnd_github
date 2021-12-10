import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('What city would you like to explore - Chicago, New York City, or Washington? ').lower()
    
    while city not in (CITY_DATA.keys()):
        print('\nDarn! That city is not available. Please try again. ')
        city = input('\nWhat city would you like to explore - Chicago, New York City, or Washington? ').lower()
               
    # get user input for month (all, january, february, ... , june)
    month = input('\nFor what month? January, February, March, April, May, June or all? ').lower()
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nFor which day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all? ').lower()
    
    print('-'*40)
    return city, month, day
    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
   
    return df
city = 'chicago'
month = 'january'
day = 'monday'        
df = load_data(city, month, day)
print(df.head())  

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    popular_month = df['month'].mode()
    print('Most popular month (January, February, March, April, May, June):', popular_month)
    
    # display the most common day of week
    popular_day = df['day_of_week'].mode()
    print('\nThe most popular day of the week:', popular_day)
    
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    common_hour = df['hour'].mode()
    print('\nThe most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()
    print('The most popular start station is:', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()
    print('\nThe most popular end station is:', end_station)

    # display most frequent combination of start station and end station trip
    start_end_station = df['Start Station']+df['End Station']
    print('\nThe most popular start-end combo is:', start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    travel_time = df['Trip Duration'].sum()
    avg_travel_time = df['Trip Duration'].mean()
    
    # display total travel time
    print('Total travel time:', travel_time)

    # display mean travel time
    print('\nAverage travel time:', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
format

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The count of users by type are:', user_type)

    # Display counts of gender
    gender_type = df['Gender'].value_counts()
    print('\nThe count of users by gender are:', gender_type)

    # Display earliest, most recent, and most common year of birth
    oldest = df['Birth Year'].min()
    youngest = df['Birth Year'].max()
    common_year = df['Birth Year'].mode()
    
    print('\nThe oldest rider\'s year of birth was:', oldest)
    print('\nThe youngest rider\'s year of birth was:', youngest)
    print('\nThe most common year of birth was:', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

            
def display_raw_data(df):
    """
    Asks if the user would like to see some lines of data from the filtered dataset.
    Displays 5 (show_rows) lines, then asks if they would like to see 5 more.
    Continues asking until they say stop.
    """
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1    # use index values for rows
    
    print_line = lambda char: print(char[0] * 90)
    
    print('\n    Would you like to see some raw data from the current dataset?')
    while True:
        raw_data = input('      (y or n):  ')
        if raw_data.lower() == 'y':
            # display show_rows number of lines, but display to user as starting from row as 1
            # e.g. if rows_start = 0 and rows_end = 4, display to user as "rows 1 to 5"
            print('\n    Displaying rows {} to {}:'.format(rows_start + 1, rows_end + 1))
            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows
            print_line('.')
            print('\n    Would you like to see the next {} rows?'.format(show_rows))
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
          
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
