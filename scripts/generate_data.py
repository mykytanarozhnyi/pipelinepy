import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os


def generate_pro_data(days=500):
    os.makedirs('data', exist_ok=True)
    np.random.seed(42)

    start_date = datetime.now() - timedelta(days=days)
    dates = [start_date + timedelta(days=x) for x in range(days)]

    data = []
    for i, date in enumerate(dates):
        # Weekend sales boost
        multiplier = 1.3 if date.weekday() >= 5 else 1.0
        # Organic growth trend
        trend = 1 + (i / days) * 0.4

        sessions = int(np.random.randint(900, 1100) * multiplier * trend)
        cr = np.random.uniform(0.025, 0.045)  # Conversion Rate 2.5-4.5%
        orders = int(sessions * cr)

        # Financials
        revenue = round(orders * np.random.uniform(1200, 1600), 2)
        ad_spend = round(revenue * np.random.uniform(0.15, 0.35), 2)

        data.append({
            'date': date.strftime('%Y-%m-%d'),
            'sessions': sessions,
            'orders': orders,
            'revenue': revenue,
            'ad_spend': ad_spend,
            'region': np.random.choice(['NA', 'EU', 'APAC'], p=[0.4, 0.4, 0.2])
        })

    df = pd.DataFrame(data)
    df.to_csv('data/sample_data.csv', index=False)
    print(f"Generated {days} rows in data/sample_data.csv")


if __name__ == "__main__":
    generate_pro_data()