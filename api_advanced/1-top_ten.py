#!/usr/bin/python3
"""
1-main
"""
import sys

if __name__ == '__main__':
    try:
        # Import the top_ten function from 1-top_ten
        top_ten = __import__('1-top_ten').top_ten
    except AttributeError:
        print("Error: '1-top_ten' module does not contain 'top_ten' function.")
        sys.exit(1)

    # Check if an argument is provided
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        # Call the top_ten function with the subreddit argument
        top_ten(sys.argv[1])
