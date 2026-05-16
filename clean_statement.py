import pdfplumber
import re

transactions = []
skip_keywords = ['Online Transfer', 'Transfer To', 'Transfer From','International', 'Book Transfer','Wire Fee','Zolve Zolve']

with pdfplumber.open("chase_novdec.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        lines = text.split('\n')
        for line in lines:
            # look for lines that start with a date pattern like 09/18
            match = re.match(r'(\d{2}/\d{2})\s+(.+?)\s+(-?\d+\.\d{2})\s+(\d+\.\d{2})', line)
            if match:
                description = match.group(2)
                if any(keyword in description for keyword in skip_keywords):
                    continue
                date = match.group(1)
                description = match.group(2)
                amount = match.group(3)
                balance = match.group(4)
                transactions.append((date, description, amount, balance))

for t in transactions:
    print(t)