import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of rows
num_rows = 1000

# Define the channels
channels = ['Social Media', 'Influencer Ad', 'Google Ad', 'Email']
campaigns = ['Prime Day 2024', 'Prime Day 2023', 'Prime Day 2022', 'Prime Day 2021']
products = ['Electronics', 'Clothing', 'Food', 'Furniture']

# Define Prime Day dates
prime_day_dates = {
    'Prime Day 2024': ('2024-07-15', '2024-07-16'),
    'Prime Day 2023': ('2023-07-11', '2023-07-12'),
    'Prime Day 2022': ('2022-07-12', '2022-07-13'),
    'Prime Day 2021': ('2021-06-21', '2021-06-22')
}

# Generate synthetic data
data = {
    'Customer ID': [fake.uuid4() for _ in range(num_rows)],
    'Date': [fake.date_between(start_date='-3y', end_date='today') for _ in range(num_rows)],
    'Campaign': np.random.choice(campaigns, num_rows),
    'Channel': np.random.choice(channels, num_rows),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], num_rows),
    'Age': np.random.randint(18, 70, num_rows),
    'Gender': np.random.choice(['Male', 'Female'], num_rows),
    'Income': np.random.randint(20000, 120000, num_rows),
    'Purchase Amount': np.random.uniform(10, 1000, num_rows).round(2),
    'Response': np.random.choice(['Yes', 'No'], num_rows),
    'Ad Spend': np.random.uniform(100, 5000, num_rows).round(2),
    'Clicks': np.random.randint(100, 10000, num_rows),
    'Impressions': np.random.randint(1000, 50000, num_rows),
    'Bounce Rate': np.random.uniform(0, 100, num_rows).round(2),
    'Engagement Rate': np.random.uniform(0, 100, num_rows).round(2),
    'Product Type': np.random.choice(products, num_rows),
    'Campaign Duration': np.random.randint(1, 2, num_rows),  # Duration is typically 2 days
    'Campaign Objective': np.random.choice(['Brand Awareness', 'Lead Generation', 'Sales'], num_rows),
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the correct start and end dates for each campaign
def set_campaign_dates(row):
    start_date, end_date = prime_day_dates[row['Campaign']]
    row['Start Date'] = start_date
    row['End Date'] = end_date
    return row

df = df.apply(set_campaign_dates, axis=1)

# Adjust values to reflect clear performance differences among channels, campaigns, and products
def adjust_values(df):
    for index, row in df.iterrows():
        # Adjusting values based on Campaign
        if row['Campaign'] == 'Prime Day 2024':
            df.at[index, 'Ad Spend'] = np.random.uniform(1000, 2000)
            df.at[index, 'Purchase Amount'] = np.random.uniform(20000, 30000)
        elif row['Campaign'] == 'Prime Day 2023':
            df.at[index, 'Ad Spend'] = np.random.uniform(2000, 3000)
            df.at[index, 'Purchase Amount'] = np.random.uniform(15000, 25000)
        elif row['Campaign'] == 'Prime Day 2022':
            df.at[index, 'Ad Spend'] = np.random.uniform(3000, 4000)
            df.at[index, 'Purchase Amount'] = np.random.uniform(10000, 20000)
        elif row['Campaign'] == 'Prime Day 2021':
            df.at[index, 'Ad Spend'] = np.random.uniform(4000, 5000)
            df.at[index, 'Purchase Amount'] = np.random.uniform(5000, 15000)
        
        # Adjusting values based on Channel
        if row['Channel'] == 'Social Media':
            df.at[index, 'Clicks'] = np.random.randint(7000, 10000)
            df.at[index, 'Impressions'] = np.random.randint(40000, 50000)
            df.at[index, 'Bounce Rate'] = np.random.uniform(20, 30)
            df.at[index, 'Engagement Rate'] = np.random.uniform(40, 50)
        elif row['Channel'] == 'Google Ad':
            df.at[index, 'Clicks'] = np.random.randint(5000, 8000)
            df.at[index, 'Impressions'] = np.random.randint(30000, 40000)
            df.at[index, 'Bounce Rate'] = np.random.uniform(30, 40)
            df.at[index, 'Engagement Rate'] = np.random.uniform(30, 40)
        elif row['Channel'] == 'Email':
            df.at[index, 'Clicks'] = np.random.randint(2000, 5000)
            df.at[index, 'Impressions'] = np.random.randint(10000, 30000)
            df.at[index, 'Bounce Rate'] = np.random.uniform(40, 50)
            df.at[index, 'Engagement Rate'] = np.random.uniform(20, 30)
        elif row['Channel'] == 'Influencer Ad':
            df.at[index, 'Clicks'] = np.random.randint(1000, 3000)
            df.at[index, 'Impressions'] = np.random.randint(5000, 20000)
            df.at[index, 'Bounce Rate'] = np.random.uniform(50, 60)
            df.at[index, 'Engagement Rate'] = np.random.uniform(10, 20)

        # Adjusting values based on Product Type
        if row['Product Type'] == 'Electronics':
            df.at[index, 'Purchase Amount'] = np.random.uniform(800, 1000)
            df.at[index, 'Impressions'] = np.random.randint(40000, 50000)
            df.at[index, 'Clicks'] = np.random.randint(7000, 10000)
        elif row['Product Type'] == 'Food':
            df.at[index, 'Purchase Amount'] = np.random.uniform(600, 900)
            df.at[index, 'Impressions'] = np.random.randint(30000, 40000)
            df.at[index, 'Clicks'] = np.random.randint(5000, 8000)
        elif row['Product Type'] == 'Furniture':
            df.at[index, 'Purchase Amount'] = np.random.uniform(400, 800)
            df.at[index, 'Impressions'] = np.random.randint(20000, 30000)
            df.at[index, 'Clicks'] = np.random.randint(3000, 6000)
        elif row['Product Type'] == 'Clothing':
            df.at[index, 'Purchase Amount'] = np.random.uniform(200, 600)
            df.at[index, 'Impressions'] = np.random.randint(10000, 20000)
            df.at[index, 'Clicks'] = np.random.randint(1000, 4000)

    return df

# Adjust values in the DataFrame
df = adjust_values(df)

# Calculate CTR and Conversion Rate
df['CTR (Click-Through Rate)'] = (df['Clicks'] / df['Impressions']) * 100
df['Conversion Rate'] = (df['Purchase Amount'] / df['Clicks']) * 100

# Calculate ROAS
df['ROAS'] = df['Purchase Amount'] / df['Ad Spend']

# Display the DataFrame
df.head(10)

# Save to CSV
df.to_csv('marketing_data.csv', index=False)

df.head()
