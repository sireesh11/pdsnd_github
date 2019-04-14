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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        Cities = ['chicago', 'new york city', 'washington']
        city=input("Enter the city you want to search in (chicago, new york city, washington):")
        if city not in Cities :
            print('Please enter valid city name:')
            continue
        else:
            break
   # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        Months = ['january', 'february', 'march', 'april', 'may', 'june']
        month=input("Enter the month you want to search (all,january,february,march,april,may,june):")
        if month !='all':
            if month not in Months:
                print('Please enter valid month:')
                continue
            else:
                break

        break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ]
        day=input("Enter the day you want to search (all,monday,tuesday,wednesday,thursday,friday,saturday,sunday):")
        if day !='all':
            if day not in days:
                print('Please enter valid day:')
                continue
            else:
                break
        break

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
    df=pd.read_csv(CITY_DATA[city])
    # filter by month if applicable
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month_name()
    df['day_of_week']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month for travel is:')
    common_month=df['month'].mode()[0]
    print(common_month)

    # TO DO: display the most common day of week
    print('The most common day for travel is:')
    common_day=df['day_of_week'].mode()[0]
    print(common_day)

    # TO DO: display the most common start hour
    print('The most common hour for travel is:')
    common_hour=df['hour'].mode()[0]
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used Start station is:')
    common_start=df['Start Station'].mode()[0]
    print(common_start)


    # TO DO: display most commonly used end station
    print('The most commonly used End station is:')
    common_end=df['End Station'].mode()[0]
    print(common_end)

    # TO DO: display most frequent combination of start station and end station trip
    print('The most common Start and End station is:')
    df['Start End'] = df['Start Station'].map(str) + ' AND ' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print(popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total=df['Trip Duration'].sum()
    print('Total travel time:{}'.format(total))
    # TO DO: display mean travel time
    mean=df['Trip Duration'].mean()
    print('Average travel time:{}'.format(mean))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The count of user types is:')
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    print('The count of gender types is:')
    gender_t = df['Gender'].value_counts().fillna(0)
    print(gender_t)


    # TO DO: Display earliest, most recent, and most common year of birth

    earliest=df['Birth Year'].min()
    recent=df['Birth Year'].max()
    common_year=df['Birth Year'].mode()[0]
    print('Earliest year of birth:{},Most recent year of birth:{},Most common year of birth:{}'.format(earliest,recent,common_year))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
