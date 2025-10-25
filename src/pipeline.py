import pandas as pd
from pathlib import Path
from src.data_cleaner import clean_cement_data, load_to_sqlite

# --- Path Configuration ---
ROOT_DIR = Path.cwd()
RAW_DATA_PATH = ROOT_DIR.joinpath("data", "raw", "raw_cement_data.csv")
PROCESSED_DB_PATH = ROOT_DIR.joinpath("data", "processed", "cement_factory.db")
CLEANED_CSV_PATH = ROOT_DIR.joinpath("data", "processed", "cleaned_cement_data.csv")
TABLE_NAME = "cement_sales"

def run_pipeline():
    """Executes the simplified ETL process."""

    print("\n--- Starting Data Pipeline ---")

    # 1. EXTRACT: Read raw data
    print(f"1. Reading: {RAW_DATA_PATH.name}")
    try:
        raw_df = pd.read_csv(RAW_DATA_PATH)
    except FileNotFoundError:
        print(f"ERROR: Raw data not found at {RAW_DATA_PATH}")
        return
    except Exception as e:
        print(f"ERROR reading raw data: {e}")
        return

    # 2. TRANSFORM: Clean and feature engineer
    print("2. Transforming data...")
    try:
        cleaned_df = clean_cement_data(raw_df)
        print(f"   -> Cleaned data shape: {cleaned_df.shape}")
    except Exception as e:
        print(f"ERROR during data cleaning: {e}")
        return

    # 3. LOAD: Save results
    print("3. Loading results...")
    try:
        # Ensure 'processed' directory exists
        PROCESSED_DB_PATH.parent.mkdir(parents=True, exist_ok=True)

        # 3a. Load to SQLite
        load_to_sqlite(cleaned_df, PROCESSED_DB_PATH, TABLE_NAME)

        # 3b. Save cleaned CSV
        cleaned_df.to_csv(CLEANED_CSV_PATH, index=False, encoding='utf-8-sig')
        print(f"   -> Saved cleaned CSV to: {CLEANED_CSV_PATH.name}")

    except Exception as e:
        print(f"ERROR loading data: {e}")
        return

    print("\n--- Pipeline Completed Successfully --- ✅")

if __name__ == "__main__":
    run_pipeline()