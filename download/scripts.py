# import os
# import pandas as pd

# def list_csv_files_and_columns(folder_path):
#     try:
#         # Get all files in the folder
#         files = os.listdir(folder_path)
        
#         # Filter only .csv files
#         csv_files = [file for file in files if file.endswith('.csv')]
        
#         if csv_files:
#             print("CSV files and their column names:")
#             for csv_file in csv_files:
#                 file_path = os.path.join(folder_path, csv_file)
#                 try:
#                     # Read the CSV file and get column names
#                     df = pd.read_csv(file_path)
#                     print(f"\nFile: {csv_file}")
#                     print("Columns:", list(df.columns))
#                 except Exception as e:
#                     print(f"Could not read {csv_file}: {str(e)}")
#         else:
#             print("No CSV files found in the folder.")
        
#         return csv_files
#     except FileNotFoundError:
#         print(f"The folder '{folder_path}' does not exist.")
#         return []
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
#         return []

# # Example usage
# folder_path = "/Users/konkimk/Desktop/cap_dataset/download"  # Replace with the path to your folder
# list_csv_files_and_columns(folder_path)

import pandas as pd
import os

# # Define the directory where the CSV files are stored
# DATA_DIR = "/Users/konkimk/Desktop/cap_dataset/download"  # Update this to your actual path

# # Define the relevant features for PD detection
# relevant_features = {
#     "MDS-UPDRS_Part_I_30Mar2025.csv": ["PATNO", "EVENT_ID", "NP1COG", "NP1HALL", "NP1DPRS", "NP1ANXS", "NP1APAT"],
#     "MDS_UPDRS_Part_II__Patient_Questionnaire_30Mar2025.csv": ["PATNO", "EVENT_ID", "NP2SPCH", "NP2SALV", "NP2SWAL", "NP2EAT", "NP2DRES"],
#     "MDS-UPDRS_Part_III_30Mar2025.csv": ["PATNO", "EVENT_ID", "NP3SPCH", "NP3GAIT", "NP3FRZGT", "NP3PSTBL", "NP3TOT"],
#     "FS7_APARC_SA_30Mar2025.csv": ["PATNO", "EVENT_ID", "lh_bankssts", "lh_caudalanteriorcingulate", "rh_bankssts", "rh_caudalanteriorcingulate"],
#     "FS7_ASEG_VOL_30Mar2025.csv": ["PATNO", "EVENT_ID", "BrainSegVol", "lhCortexVol", "rhCortexVol", "EstimatedTotalIntraCranialVol"],
#     "Clinical_Diagnosis_30Mar2025.csv": ["PATNO", "EVENT_ID", "NEWDIAG"],
#     "Age_at_visit_30Mar2025.csv": ["PATNO", "EVENT_ID", "AGE_AT_VISIT"],
#     "Family_History_30Mar2025.csv": ["PATNO", "EVENT_ID", "ANYFAMPD", "BIOMOMPD", "BIODADPD", "FULSIBPD", "DISFAMPD"],
#     "Subject_Cohort_History_30Mar2025.csv": ["PATNO", "APPRDX", "COHORT"],  # No EVENT_ID
#     "Symbol_Digit_Modalities_Test_30Mar2025.csv": ["PATNO", "EVENT_ID", "SDMTOTAL"],
#     "Hopkins_Verbal_Learning_Test_-_Revised_30Mar2025.csv": ["PATNO", "EVENT_ID", "HVLTRT1", "HVLTRT2", "HVLTRT3", "HVLTRDLY", "HVLTREC"],
#     "Montreal_Cognitive_Assessment__MoCA__30Mar2025.csv": ["PATNO", "EVENT_ID", "MCATOT"]
# }

# # Initialize an empty DataFrame for the merged data
# merged_df = None

# # Load and merge datasets
# for file_name, columns in relevant_features.items():
#     file_path = os.path.join(DATA_DIR, file_name)
#     if os.path.exists(file_path):
#         print(f"Processing file: {file_name}")
#         df = pd.read_csv(file_path, usecols=columns)
        
#         # Drop columns that are completely empty
#         df = df.dropna(axis=1, how="all")
        
#         # Check if EVENT_ID exists in the file
#         if "EVENT_ID" in df.columns:
#             # Filter rows where EVENT_ID is 'BL'
#             df = df[df["EVENT_ID"] == "BL"]
#             # Merge on PATNO and EVENT_ID
#             if merged_df is None:
#                 merged_df = df
#             else:
#                 merged_df = pd.merge(merged_df, df, on=["PATNO", "EVENT_ID"], how="outer")
#         else:
#             # Merge on PATNO only
#             if merged_df is None:
#                 merged_df = df
#             else:
#                 merged_df = pd.merge(merged_df, df, on="PATNO", how="outer")
#     else:
#         print(f"Warning: {file_name} not found in {DATA_DIR}")

# # Drop duplicate columns (keep the first occurrence)
# merged_df = merged_df.loc[:, ~merged_df.columns.duplicated()]

# # Fill missing values with 'NA'
# merged_df.fillna("NA", inplace=True)

# # Save the final preprocessed dataset
# output_file = os.path.join(DATA_DIR, "preprocessed_pd_features.csv")
# merged_df.to_csv(output_file, index=False)
# print(f"Preprocessed dataset saved to {output_file}")

df = pd.read_csv('/Users/konkimk/Desktop/cap_dataset/download/preprocessed_pd_features.csv')
# print(df.head())
# print(df.info())

import pandas as pd

# Load your dataset
# df = pd.read_csv('/path/to/your/file.csv')  # Replace with the path to your CSV file

# Calculate the threshold for dropping columns (50% missing values)
threshold = len(df) * 0.5

# Drop columns with more than 50% missing values
df_cleaned = df.dropna(axis=1, thresh=threshold)

# Save the cleaned dataframe to a new CSV
df_cleaned.to_csv('/Users/konkimk/Desktop/cap_dataset/download/cleaned.csv', index=False)  # Replace with your desired save path

# Print the shape of the cleaned data
print(f"Original DataFrame shape: {df.shape}")
print(f"Cleaned DataFrame shape: {df_cleaned.shape}")
