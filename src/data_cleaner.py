import pandas as pd
import sqlite3
from pathlib import Path

def clean_cement_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs data cleaning, standardizes column names, 
    and engineers core KPI features (efficiency, fulfillment, gap).
    
    Args:
        df: The raw pandas DataFrame loaded from the source CSV.
        
    Returns:
        The cleaned and feature-engineered DataFrame.
    """
    
    # 1. Clean and standardize column names
    df.columns = df.columns.str.strip().str.lower()
    df = df.loc[:, ~df.columns.str.contains('^unnamed', case=False)]
    df = df.dropna(how='all')

    # 2. Fix date format and drop rows with missing dates
    df['month'] = pd.to_datetime(df['month'], format='%b-%y', errors='coerce') 
    
    # Log the number of rows dropped
    rows_before = len(df)
    df = df.dropna(subset=['month'])
    rows_dropped = rows_before - len(df)
    print(f"Data Cleaning: Dropped {rows_dropped} rows due to missing 'month' value.")

    # 3. Ensure numeric types and rounding
    cols_to_clean = ['production', 'sales', 'demand', 'population', 'gdp', 'disbusment', 'interestrate']
    for col in cols_to_clean:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(',', '', regex=False)
            .str.replace(' ', '', regex=False)
            .astype(float)
        )

    df['population'] = df['population'].round(2)
    df['gdp'] = df['gdp'].round(2)
    
    # 4. Feature Engineering (KPIs)
    df['efficiency'] = df['sales'] / df['production']
    df['fulfillment'] = df['sales'] / df['demand']
    df['production_gap'] = df['production'] - df['sales']

    # Final column order
    df = df[['month', 'production', 'sales', 'demand', 'population', 'gdp',
             'disbusment', 'interestrate', 'efficiency', 'fulfillment', 'production_gap']]
    
    return df

def load_to_sqlite(df: pd.DataFrame, db_path: Path, table_name: str = "cement_sales"):
    """
    Loads the cleaned DataFrame into a specified SQLite database.
    """
    try:
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, index=False, if_exists="replace")
        conn.close()
        print(f"Data loaded successfully to {db_path} table: {table_name}")
    except Exception as e:
        print(f"Error loading data to DB: {e}")