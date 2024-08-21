import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of rows
num_rows = 1000

# London boroughs for locations
boroughs = ['Camden', 'Greenwich', 'Hackney', 'Hammersmith and Fulham', 'Islington', 'Kensington and Chelsea', 'Lambeth', 'Lewisham', 'Southwark', 'Tower Hamlets', 'Wandsworth', 'Westminster']

# Generate synthetic data
data = {
    'Property ID': [fake.uuid4() for _ in range(num_rows)],
    'Date Listed': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_rows)],
    'Location': np.random.choice(boroughs, num_rows),
    'Property Type': np.random.choice(['Flat', 'Detached', 'Semi-Detached', 'Terraced'], num_rows),
    'Price': np.random.randint(200000, 3000000, num_rows),  # Prices range between 200K and 3M
    'Bedrooms': np.random.randint(1, 6, num_rows),
    'Bathrooms': np.random.randint(1, 4, num_rows),
    'Square Feet': np.random.randint(300, 4000, num_rows),
    'Year Built': np.random.randint(1850, 2021, num_rows),
    'Days on Market': np.random.randint(0, 365, num_rows),
    'Sale Status': np.random.choice(['Listed', 'Sold', 'Pending'], num_rows)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('real_estate_data.csv', index=False)

df.head()