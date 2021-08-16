import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyorkcity': 'new_york_city.csv',
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
    city = ''
    month = ''
    day = ''
    while city not in ('chicago' , 'newyorkcity' , 'washington'):
        city = str(input("Which city do you want to explore? You can choose only between Chicago, New York City, Washington: ")).lower().replace(' ','')


    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in ('all' , 'january' , 'february' , 'march' , 'april' , 'may' , 'june'):
        month = str(input("Which month do you want to explore? If you don't care, enter all, you can only enter the month before july: ")).lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in ('all' , 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday'):
        day = str(input("Which day do you want to explore? If you don't care, enter all: ")).lower()

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day Of Week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        
        df[df['Day Of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_count = df['Month'].value_counts()
    print("The most common month : {}".format(month_count.idxmax()))

    # TO DO: display the most common day of week
    day_count = df['Day Of Week'].value_counts()
    print("The most common day of week : {}".format(day_count.idxmax()))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    start_hour_count = df['hour'].value_counts()
    print("The most common hour : {}".format(start_hour_count.idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    SS_count = df['Start Station'].value_counts()
    print("The most commonly used Start Station : {}".format(SS_count.idxmax()))

    # TO DO: display most commonly used end station
    ES_count = df['End Station'].value_counts()
    print("The most commonly used End Station : {}".format(ES_count.idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    station_combi = df.groupby(['Start Station','End Station'])
    print("The most frequent combination of start station and end station trip : {}".format(station_combi.size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_t = df['Trip Duration'].sum()
    print("Total travel time: {}".format(total_travel_t))

    # TO DO: display mean travel time
    avg_travel_t = df['Trip Duration'].mean()
    print("Average travel time: {}".format(avg_travel_t))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("*User Type\n", user_type)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("*Gender\n", gender)
    else:
        print("\nNo gender information for this city!")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        e_birth = df['Birth Year'].min()
        r_birth = df['Birth Year'].max()
        c_birth = df['Birth Year'].mode()[0]
        print("The earliest birth Year is {}.\nThe most recent birth year is {}\nThe most common year of birth year is {}".format(e_birth,r_birth,c_birth))
    else:
        print("\nNo birth year information for this city!")
    # washington.csv file has no birth year information

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data != 'yes':
        if view_data == 'no':
            break
        else:
            view_data = input("Please enter only yes or no: ").lower()
            
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        
        while view_data != 'yes':
            if view_data == 'no':
                break
            else:
                view_data = input("Please enter only yes or no: ").lower()
    

    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
