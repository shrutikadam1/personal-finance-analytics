#Personal Finance Analytics End to End Data Pipeline

A personal finance tool that extracts real bank transactions 
from PDF statements, cleans and categorizes them using Python 
and visualizes spending patterns through an interactive 
Tableau dashboard.


## Why I Built This

I'm 21, in college, and broke by the end of every month.

I always knew I was spending money but never really knew 
WHERE it was going. Bank statements are scattered, hard 
to read and don't give you a clear picture. I never had 
time to sit down and go through them line by line.

So I built a tool that does it for me.

This project takes my real Chase bank statements, cleans 
them, categorizes every transaction and visualizes exactly 
where my money goes so I can stop guessing and start 
being intentional with my finances.

## What Surprised Me

I went into this project thinking I already knew 
where my money was going. I was wrong.

The first version of my dashboard was lying to me.
Misc was my highest category because my categorization 
wasn't smart enough yet. So I kept digging. I refined 
the logic, added amount based rules, questioned every 
assumption. That process alone taught me more about 
data cleaning than any tutorial ever could.

When I finally got the categorization right, the 
truth was uncomfortable.

My grocery spending was almost nothing. My food 
delivery spending was enormous. I was paying extra 
money, eating worse food and wondering why I was 
broke every month. The answer was sitting in my 
bank statement the whole time. I just never had 
a way to see it clearly until now.

That's what data does. It doesn't tell you something 
new. It shows you what you already knew but couldn't 
see.

## What It Does 

Extracts transactions from PDF bank statements using 
pdfplumber with no manual data entry

Removes sensitive information automatically

Cleans and categorizes 115 transactions across 12 
spending categories using pandas

Uses amount based logic for ambiguous stores where 
the same store gets categorized differently based on 
purchase amount

Stores everything in a MySQL database with proper 
relational structure

Python CLI app to view, add, update and delete expenses

Interactive Tableau dashboard for visual analysis

There were two real challenges in this project.

## The Hardest Part

The first was extracting clean data from PDFs. Bank 
statement PDFs are messy. The text comes out unstructured 
with weird characters, subscript numbers and no consistent 
formatting. I had to write regex patterns to identify 
only transaction lines and filter out everything else 
like account numbers, headers and bank messages.

The second was categorization. My first approach was 
simple — match store names to categories. That worked 
until I realized the same store could mean completely 
different things depending on how much was spent. A 
$4 purchase at a liquor store is probably a snack. 
A $40 purchase at the same store is probably alcohol.

So I built amount based logic — if the purchase is 
under $15 at an ambiguous store it goes to groceries. 
Over $15 it goes to social spending. That one decision 
made my data twice as accurate and changed what my 
dashboard was actually telling me.

The lesson was that data cleaning is never just about 
removing bad data. Sometimes it is about understanding 
the context behind the numbers.

## What It Does

Extracts transactions from PDF bank statements using 
pdfplumber with no manual data entry

Removes sensitive information automatically

Cleans and categorizes 115 transactions across 12 
spending categories using pandas

Uses amount based logic for ambiguous stores where 
the same store gets categorized differently based on 
purchase amount

Stores everything in a MySQL database with proper 
relational structure

Python CLI app to view, add, update and delete expenses

Interactive Tableau dashboard for visual analysis

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core app and data pipeline |
| MySQL | Database and queries |
| pandas | Data cleaning and transformation |
| pdfplumber | PDF text extraction |
| Tableau Public | Interactive dashboard |

## How It Works

PDF Bank Statement
      ↓
pdfplumber extracts raw transactions
      ↓
pandas cleans, formats and categorizes
      ↓
MySQL stores structured data
      ↓
Python CLI app to manage expenses
      ↓
Tableau dashboard for visualization

## How To Run It

1. Clone this repository

git clone https://github.com/shrutikadam1/personal-finance-analytics

2. Install required libraries

pip install mysql-connector-python pandas pdfplumber

3. Set up MySQL
Create a database called expense_tracker in MySQL
Run expense_tracker.py to set up the table structure

4. Add your own bank statement
Place your PDF bank statement in the same folder
Update the filename in clean_statement.py
Run clean_data.py to extract and load your transactions

5. Launch the app
python3 expense_tracker.py

## Key Insights From My Data

Transfers were my highest spending category mostly 
splitting bills and expenses with friends

Food delivery was my biggest personal expense 
at 21% of total spending

Social spending was double what I initially 
estimated after better categorization

October was my highest spending month by far

## Live Dashboard

https://public.tableau.com/views/PersonalFinanceAnalyticsEndtoEndDataPipeline/Dashboard1?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link




