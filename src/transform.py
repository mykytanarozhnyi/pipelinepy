import pandas as pd


def calculate_kpis(df):
    """Clean data and calculate business metrics."""
    df['date'] = pd.to_datetime(df['date'])

    # Aggregate to daily level
    daily = df.groupby('date').agg({
        'sessions': 'sum',
        'orders': 'sum',
        'revenue': 'sum',
        'ad_spend': 'sum'
    }).reset_index()

    # Performance metrics
    daily['conversion_rate'] = (daily['orders'] / daily['sessions']).round(4)
    daily['aov'] = (daily['revenue'] / daily['orders']).round(2)
    daily['roas'] = (daily['revenue'] / daily['ad_spend']).round(2)
    daily['cac'] = (daily['ad_spend'] / daily['orders']).round(2)

    return daily