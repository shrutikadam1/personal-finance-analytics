import pandas as pd
from clean_statement import transactions


# create dataframe
df = pd.DataFrame(transactions, columns=['date', 'description', 'amount', 'balance'])
def fix_date(date_str):
    month, day = date_str.split('/')
    if month == '11':
        return f'2025-11-{day}'
    elif month == '12':
        return f'2025-12-{day}'

df['date'] = df['date'].apply(fix_date)

# convert amount to number
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df= df.dropna(subset=['amount'])
# keep only expenses (negative amounts) — remove incoming Zelle, wire transfers
df = df[df['amount'] < 0]

# make amount positive
df['amount'] = df['amount'].abs()

# auto categorize based on keywords
def categorize(description, amount):
    description = description.lower()
    if any(word in description for word in ['sun stop', 'tempe market tempe', 'el paisano']):
        if amount > 15:
            return 'nightlife'
        else:
               return 'groceries'
    #food
    elif any(word in description for word in ['doordash', 'pizza', 'subway', 'india', 'cava', 'hoagies', 'in-n-out', 'wetzel','thirsty lion','catch','lion gastro', 'coca cola', 'guss', 'irasema']):
        return 'food'
    #transport
    elif any(word in description for word in ['lyft', 'uber', 'waymo']):
        return 'transport'
    #shopping
    elif any(word in description for word in ['target', 'temu', 'victoria', 'spencer', 'fivebelow','sephora', 'windsor','q 151','pitaya']):
        return 'shopping'
    #groceries
    elif any(word in description for word in ['cvs', 'market','amk','desi plaza','ace mini', 'trader joe','trader', 'safeway', 'walmart','kroger']):
        return 'groceries'
    #entertainment 
    elif any(word in description for word in ['spotify', 'amc','cinema', 'movie']):
        return 'entertainment'
    #education
    elif any(word in description for word in ['edfinity']):
        return 'education'
    #greek life
    elif any(word in description for word in ['alphaomicronpi', 'bhy']):
        return 'greek life'
    #bills
    elif any(word in description for word in ['visible','monthly service fee']):
        return 'bills'
    #nightlife
    elif any(word in description for word in ['sun stop', 'liquor']):
        return 'nightlife'
    #transfers
    elif any(word in description for word in ['zelle payment to']):
        return 'transfers'
    else:
        return 'misc'


df['category'] = df.apply(lambda row: categorize(row['description'], row['amount']), axis=1)

print(df)

df.to_csv('cleaned_expenses.csv', index=False)
print("Exported to cleaned_expense.csv!")

import mysql.connector

category_map ={
    'food': 1,
    'movie': 2,
    'misc': 3,
    'shopping': 4,
    'transport': 5,
    'greek life': 6,
    'groceries': 7,
    'entertainment': 8,
    'education': 9,
    'bills': 10,
    'nightlife': 11,
    'transfers': 12
}

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="expense_tracker"
)

cursor = connection.cursor()
# clear old bank data before reloading
#cursor.execute("DELETE FROM expense WHERE payment_method = 'chase' AND date BETWEEN '2025-11-15' AND '2025-12-14'")
#connection.commit()
#print("Cleared old data!")

for _, row in df.iterrows():
    category_id = category_map.get(row['category'], 3)  # default to misc if not found
    query = """INSERT INTO expense (date, amount, payment_method, note, category_id) 
               VALUES (%s, %s, %s, %s, %s)"""
    values = (row['date'], row['amount'], 'chase', row['description'], category_id)
    cursor.execute(query, values)

connection.commit()
print(f"Loaded {len(df)} expenses into MySQL!")