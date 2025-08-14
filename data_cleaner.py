import pandas as pd
import os

print("\nThe code does the following :-")
print("1. Changes column names to UPPER CASE")
print("2. Replaces missing or empty values with 'NULL'")
print("3. Removes duplicate rows")

def standardize_column_names(df):
    df.columns = df.columns.str.strip().str.upper().str.replace(" ", "_")
    return df

def handle_missing_values(df, fill_value="NULL"):
    if fill_value is None:
        fill_value = "NULL"
    return df.fillna(fill_value)

def clean_csv(input_file, output_file, fill_value="NULL"):
    df = pd.read_csv(input_file)
    
    print("\n--- BEFORE CLEANING ---")
    print(df)

    df = df.drop_duplicates()

    df = standardize_column_names(df)

    df = handle_missing_values(df, fill_value=fill_value)

    df.to_csv(output_file, index=False)

    print("\n--- AFTER CLEANING ---")
    print(df)

    print(f"\n✅ Cleaned data saved to: {output_file} in the same folder.")

if __name__ == "__main__":
    # add the input csv file which should be cleaned
    input_file = "sample.csv" 
    # output csv file is created 
    output_file = "cleaned_sample.csv" 

    if not os.path.exists(input_file):
        print("❌ Input file does not exist. Please place 'sample.csv' in the same folder.")
    else:
        clean_csv(input_file, output_file, fill_value="NULL")
