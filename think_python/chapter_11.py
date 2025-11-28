class Date:
    '''Represents a year, month, and day'''

    def make_date(year, month, day):
        s = f'The date is {month, day}, {year}. '
        print(s)

    def print_date(year, month, day):
        d = f'{year} - {month:02d} - {day:02d}'