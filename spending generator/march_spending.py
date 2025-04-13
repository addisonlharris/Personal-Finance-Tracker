import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_monthly_spending(start_date, seed):
    np.random.seed(seed)  # Different seed for variation
    
    products = [
        'Groceries', 'Coffee', 'Restaurant Meal', 'Gas', 'Online Shopping',
        'Movie Ticket', 'Gym Membership', 'Uber Ride', 'Phone Bill', 'Streaming Service',
        'Fast Food', 'Bar/Drinks', 'Clothing', 'Home Supplies', 'Personal Care'
    ]
    
    # Generate 45 transactions
    end_date = pd.to_datetime(start_date) + pd.DateOffset(days=29)
    dates = pd.date_range(start=start_date, end=end_date, periods=45)
    purchases = np.random.choice(products, size=45)
    
    # Generate prices
    prices = []
    for product in purchases:
        if product == 'Groceries':
            prices.append(round(np.random.uniform(30, 120), 2))
        elif product == 'Coffee':
            prices.append(round(np.random.uniform(4, 7), 2))
        elif product == 'Restaurant Meal':
            prices.append(round(np.random.uniform(15, 45), 2))
        elif product == 'Gas':
            prices.append(round(np.random.uniform(35, 60), 2))
        elif product == 'Online Shopping':
            prices.append(round(np.random.uniform(20, 80), 2))
        elif product == 'Movie Ticket':
            prices.append(round(np.random.uniform(12, 18), 2))
        elif product == 'Gym Membership':
            prices.append(round(np.random.uniform(40, 60), 2))
        elif product == 'Uber Ride':
            prices.append(round(np.random.uniform(10, 25), 2))
        elif product == 'Phone Bill':
            prices.append(round(np.random.uniform(50, 90), 2))
        elif product == 'Streaming Service':
            prices.append(round(np.random.uniform(10, 15), 2))
        elif product == 'Fast Food':
            prices.append(round(np.random.uniform(8, 15), 2))
        elif product == 'Bar/Drinks':
            prices.append(round(np.random.uniform(20, 50), 2))
        elif product == 'Clothing':
            prices.append(round(np.random.uniform(25, 100), 2))
        elif product == 'Home Supplies':
            prices.append(round(np.random.uniform(15, 40), 2))
        else:  # Personal Care
            prices.append(round(np.random.uniform(10, 30), 2))
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Product': purchases,
        'Price': prices
    })
    
    # Add monthly bills
    monthly_bills = pd.DataFrame({
        'Date': pd.to_datetime([start_date] * 4),
        'Product': ['Rent Payment', 'Car Insurance', 'Electric Utility', 'Student Loan'],
        'Price': [1450.00, 175.00, 95.00, 325.00]
    })
    
    # Combine and sort
    df = pd.concat([df, monthly_bills], ignore_index=True)
    df = df.sort_values('Date')
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    
    return df

# Generate March data
march_spending = generate_monthly_spending('2024-03-01', 44)
print(march_spending)
march_spending.to_csv('march_spending.csv', index=False)