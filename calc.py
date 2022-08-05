# Author:      Ahmad Sayad
# File Name:   calc.py
# Description: A very simple calculator that calculates how many pages to read per day
#              to finish a book in any number of weeks. 

if __name__ == "__main__":
    # Get the number of pages needed to read to complete a book
    num_pages = int(input("Enter the number of pages in your book: "))

    # Get the timeframe in weeks
    num_weeks = int(input("How many weeks will you dedicate to finishing the book: "))

    # Calculate the number of pages per day  
    pages_per_day = (num_pages / (7 * num_weeks)).__ceil__()

    # Print the result
    print(f"You need to read {pages_per_day} pages per day to finish the book in {num_weeks} week(s)!") 
    
    # Print the number of pages per reading session 
    for i in range(2, 4):
        print(f"\tThat is {i} {(pages_per_day / i).__ceil__() }-page reading sessions each day!")