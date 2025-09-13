from ratio_calculator import calculate_ratios
from database import save_to_db, load_from_db

def run_pipeline():
    # Step 1: Load & Calculate Ratios
    df = calculate_ratios("data/insurance_data.csv")

    # Step 2: Save to SQL
    save_to_db(df)

    # Step 3: Reload & Print Sample
    df_db = load_from_db()
    print(df_db.head())

if __name__ == "__main__":
    run_pipeline()
