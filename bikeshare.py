import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}
def get_filters():
    """
    Prompts the user to specify a city, month, and day for data analysis.
    Returns:
        city (str): The city selected by the user
        month (str): The month selected for filtering, or 'none' if no filter
        day (int): The day of the week as an integer (1=Sunday, ..., 7=Saturday), or 0 if no filter
    """
    print("Hello! Let's analyze some US bikeshare data!")
    valid_cities = ['Chicago', 'New York City', 'Washington']
    city = input_with_validation(
        'Choose a city: Chicago, New York City, or Washington: ', 
        valid_cities, 
        case_insensitive=True
    )
    
    # Prompt user for filter type

    valid_filters = ['month', 'day', 'both', 'none']
    choice = input_with_validation(
        'Filter data by month, days, both, or none? (Type "none" for no filter): ', 
        valid_filters, 
        case_insensitive=True
    ).lower()
    
    month = 'none'
    day = 0

    if choice in ['both', 'month']:
        valid_months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = input_with_validation(
            'Which month? January, February, March, April, May, or June: ', 
            valid_months, 
            case_insensitive=True
        ).title()
    if choice in ['both', 'day']:
        day = input_integer_within_range(
            'Which day? Enter an integer (1=Sunday, ..., 7=Saturday): ', 
            1, 
            7
        )

    print('-' * 40)
    return city, month, day

def input_with_validation(prompt, valid_options, case_insensitive=False):
    """
    Prompts the user with a message until valid input is received.

    Args:
        prompt (str): The input prompt message.
        valid_options (list): List of valid responses.
        case_insensitive (bool): Whether to compare options case-insensitively.

    Returns:
        str: Validated user input.
    """
    while True:
        user_input = input(prompt).strip()
        if case_insensitive:
            valid_options = [option.lower() for option in valid_options]
            user_input = user_input.lower()
        if user_input in valid_options:
            return user_input
        print("Invalid input. Please choose a valid option.")

def input_integer_within_range(prompt, min_val, max_val):
    """
    Prompts the user for an integer input within a specific range.

    Args:
        prompt (str): The input prompt message.
        min_val (int): Minimum allowable integer.
        max_val (int): Maximum allowable integer.

    Returns:
        int: Validated integer input.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def load_data(city, month, day):
    """
    Loads and filters data for the specified city, month, and day.

    Args:
        city (str): City name
        month (str): Month name or 'none' for no filter
        day (int): Day of the week as an integer (1=Sunday, ..., 7=Saturday), or 0 for no filter

    Returns:
        DataFrame: Filtered bikeshare data
    """
    df = pd.read_csv(CITY_DATA[city.lower()])

    # Convert 'Start Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Hour'] = df['Start Time'].dt.hour
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # Apply month filter if specified
    if month != 'none':
        month_index = ['January', 'February', 'March', 'April', 'May', 'June'].index(month) + 1
        df = df[df['Month'] == month_index]

    # Apply day filter if specified
    if day != 0:
        day_name = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][day - 1]
        df = df[df['Day of Week'] == day_name]

    return df

def time_stats(df):
    """Displays the most frequent travel times."""
    print('\nCalculating the most frequent travel times...\n')
    start_time = time.time()
    print(f"Most common month: {df['Month'].mode()[0]}")
    print(f"Most common day of the week: {df['Day of Week'].mode()[0]}")
    print(f"Most common start hour: {df['Hour'].mode()[0]}")
    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trips."""
    print('\nCalculating station statistics...\n')
    start_time = time.time()
    print(f"Most common start station: {df['Start Station'].mode()[0]}")
    print(f"Most common end station: {df['End Station'].mode()[0]}")
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"Most common trip: {most_common_trip}")
    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on trip durations."""
    print('\nCalculating trip duration statistics...\n')
    start_time = time.time()
    print(f"Total travel time: {df['Trip Duration'].sum()}")
    print(f"Mean travel time: {df['Trip Duration'].mean()}")
    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def user_stats(df, city):
    """Displays user statistics, including user types, gender, and birth year data."""
    print('\nCalculating user statistics...\n')
    start_time = time.time()
    print(f"User types:\n{df['User Type'].value_counts()}")
    if city.lower() in ['chicago', 'new york city']:
        print(f"\nGender counts:\n{df['Gender'].value_counts()}")
        print(f"Earliest birth year: {int(df['Birth Year'].min())}")
        print(f"Most recent birth year: {int(df['Birth Year'].max())}")
        print(f"Most common birth year: {int(df['Birth Year'].mode()[0])}")
    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def display_data(df):
    """
    Displays raw data in increments of 5 rows upon user request.
    
    Args:
        df (DataFrame): The bikeshare dataset.
    """
    start_loc = 0  # Starting index
    while True:
        show_data = input('Do you want to see 5 rows of raw data? Enter yes or no: ').lower()
        if show_data == 'yes':
            # Display the next 5 rows of data
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            
            # Check if we reached the end of the data
            if start_loc >= len(df):
                print('No more data to display.')
                break
        elif show_data == 'no':
            break
        else:
            print('Invalid input. Please type "yes" or "no".')

def main():
    """
    The main loop to run the bikeshare analysis script.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        # Call display_data to handle raw data display
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
