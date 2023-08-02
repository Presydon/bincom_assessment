import pandas as pd
from bs4 import BeautifulSoup
import requests
import random as rd

# ----------------- Extraction of Data ----------------------#
response = requests.get(url='http://127.0.0.1:5500/index.html')
html_page = response.text
soup = BeautifulSoup(html_page, 'html.parser')

colour_rows = soup.find_all('td')[1]
colour_content = soup.find_all('td')
colours = [colour_content[col_index].text for col_index in range(1, 10, 2)]
merged_list = [item.strip() for sublist in [entry.split(', ') for entry in colours] for item in sublist]

# ----------------- Converting to Series for Analysis ----------------------#
working_data = pd.Series(merged_list)

# Question 1: Which color of shirt is the mean color?
""" Colour is a nominal variable and can't be statistically evaluated """

# Question 2: Which color is mostly worn throughout the week??
mostly_worn = working_data.mode()
# print(mostly_worn)

# Question 3: Which color is the median?
""" Colour is a nominal variable and can't be statistically evaluated """

# Question 4: BONUS Get the variance of the colors
""" Colour is a nominal variable and can't be statistically evaluated """

# Question 5: BONUS if a colour is chosen at random, what is the probability that the color is red?
""" Colour is a nominal variable and can't be statistically evaluated """
color_count = working_data.value_counts()
probability_of_red = color_count.get('RED', 0) / len(working_data)


# print(probability_of_red)

# Question 6: Save the colours and their frequencies in postgresql database

#Question 7: write a recursive searching algorithm to search for a number entered by user in a list of numbers.


# Question 8: Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to
# base 10.

def binary_number():
    get_binary = ''.join(rd.choice('01') for i in range(4))
    base_ten = int(get_binary, base=2)
    print(f"Binary Number is: {get_binary}")
    print(f'Converted to Base Ten is: {base_ten}')


# binary_number()

# Question 9: Write a program to sum the first 50 fibonacci sequence.
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


fibonacci_sequence = sum(fibonacci(50))
# print("First 50 Fibonacci Numbers:", fibonacci_sequence)