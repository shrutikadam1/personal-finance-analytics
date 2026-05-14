# personal-finance-analytics
Personal Finance Analytics End to End Data Pipeline

## Why I Built This

I'm 21, in college, and broke by the end of every month.

I always knew I was spending money but never really knew 
WHERE it was going. Bank statements are scattered, hard 
to read and don't give you a clear picture. I never had 
time to sit down and go through them line by line.

So I built a tool that does it for me.

This project takes my real Chase bank statements, cleans 
them, categorizes every transaction and visualizes exactly 
where my money goes — so I can stop guessing and start 
being intentional with my finances.

## What Surprised Me

I went into this project thinking I already knew 
where my money was going. I was wrong.

The first version of my dashboard was lying to me — 
misc was my highest category because my categorization 
wasn't smart enough yet. So I kept digging. I refined 
the logic, added amount-based rules, questioned every 
assumption. That process alone taught me more about 
data cleaning than any tutorial ever could.

When I finally got the categorization right, the 
truth was uncomfortable.

My grocery spending was almost nothing. My food 
delivery spending was enormous. I was paying extra 
money, eating worse food and wondering why I was 
broke every month. The answer was sitting in my 
bank statement the whole time — I just never had 
a way to see it clearly until now.

That's what data does. It doesn't tell you something 
new — it shows you what you already knew but couldn't 
see.

## The Hardest Part

Cleaning and categorizing the data was the most 
challenging part — it pushed my analytical thinking 
to its limit. Figuring out that the same store could 
mean groceries OR social spending depending on how much 
was spent was a real world data problem I hadn't 
anticipated.

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

## Key Insights From My Data

- Transfers were my highest spending category — 
  mostly splitting bills and expenses with friends
- Food delivery was my biggest personal expense 
  at 21% of total spending
- Social spending was double what I initially 
  estimated after better categorization
- October was my highest spending month by far

## Live Dashboard

[View on Tableau Public]
https://public.tableau.com/views/PersonalFinanceAnalyticsEndtoEndDataPipeline/Dashboard1?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link



