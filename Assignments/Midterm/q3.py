# COSC4427A Midterm Question 3
# Michael Buffone
import pandas as pd

# Loading the CSV file
csvData = pd.read_csv("Midterm/goodreads.csv")

# Add columns and Show Columns and first 10 / last 10 rows
csvData.columns = ["title", "subtitle", "series", "author", "my_rating", "avgrating", "publisher",
                    "binding", "pages", "year_published", "month_read", "month_read_num",
                    "year_read", "bookshelf"]
print("\nFirst 10 rows:\n", csvData.head(10))
print("\nLast 10 rows:\n", csvData.tail(10))

# List books that have NaN subtitle and series
result = csvData.loc[(csvData["subtitle"].isna()) & (csvData["series"].isna())]
print("\nNaN values:\n", result)

# Function that take's author's last name and returns all books:
def authorBooks(author):
    return csvData[csvData["author"].str.match(author + ",")]
print("\nReturn books based on author's last name:\n", authorBooks("Parks"))

# List the books that receive average rating > 3.5
print("\nThe books with an average rating > 3.5 are:\n", csvData[csvData["avgrating"] > 3.5])

# List the books that receive average rating > 3.5 and published in the year >= 2000
result = csvData.loc[(csvData["avgrating"] > 3.5) & (csvData["year_published"] >= 2000)]
print("The books with an average rating > 3.5 and published during and after 2000 are:\n", result)