import sys
import pandas as pd

DATASET = None

def main():
    
    # Read dataset
    try:
        na_values_list = ["N/A", "", "Unspecified", "UNKNOWN", " "]
        df = pd.read_csv(DATASET, na_values=na_values_list)
    except FileNotFoundError:
        print("ERROR: File not found.")
        exit(1)
    except Exception as e:
        print("ERROR: Could not read CSV file. ", e)
        exit(1) 
    
    print("begin")
    
    # Create duration column
    df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce') 
    df['resolution_action_updated_date'] = pd.to_datetime(df['resolution_action_updated_date'], errors='coerce') 
    df['duration'] = df['resolution_action_updated_date'] - df['created_date']
    df.loc[df['created_date'].isna() | df['resolution_action_updated_date'].isna(), 'duration'] = pd.NaT
    
    # Categorize duration
    less_than_day_threshold = pd.Timedelta(days=1)
    less_than_week_threshold = pd.Timedelta(weeks=1)
    less_than_month_threshold = pd.Timedelta(days=30)  
    less_than_year_threshold = pd.Timedelta(days=365)
    df['progress_duration'] = pd.cut(df['duration'], 
                                 bins=[pd.Timedelta(days=-99999), 
                                       less_than_day_threshold, 
                                       less_than_week_threshold, 
                                       less_than_month_threshold,
                                       less_than_year_threshold,
                                       pd.Timedelta(days=99999)],
                                 labels=['Less than a day', 
                                         'Less than a week', 
                                         'Less than a month', 
                                         'Less than a year', 
                                         'Greater than a year'])
    categories = ['Less than a day', 'Less than a week', 'Less than a month', 'Less than a year', 'Greater than a year', 'Ongoing']
    df['progress_duration'] = df['progress_duration'].astype(pd.CategoricalDtype(categories=categories))
    df.loc[df['duration'].isna(), 'progress_duration'] = 'Ongoing'
    
    # Categorize dates
    df['created_year'] = df['created_date'].dt.year.astype('Int64')
    df['resolution_action_updated_year'] = df['resolution_action_updated_date'].dt.year.astype('Int64')
    df['incident_zip'] = df['incident_zip'].astype('Int64')
    df['bbl'] = df['incident_zip'].astype('Int64')
    
    # Drop unneeded columns
    columns_to_drop = ['unique_key', 'created_date', 'closed_date', 'agency', 'due_date', 'incident_address', 'resolution_action_updated_date', 'x_coordinate_state_plane',
       'y_coordinate_state_plane', 'latitude', 'longitude', 'location', 'duration'] 
    df.drop(columns=columns_to_drop, inplace=True) 

      
    print(df.head())
    print(df.columns)
            
    # Save new dataset
    df.to_csv("INTEGRATED_DATASET.csv", index=False)
    

if __name__ == "__main__":
    
    try:
        DATASET = str(sys.argv[1])
    except:
        print("ERROR")
        exit(1)
        
    main()