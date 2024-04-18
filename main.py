import sys
import pandas as pd

# Input variables
DATASET = None
MIN_SUP = None
MIN_CONF = None



###########################
#       MAIN RUNNER       #
###########################

def main():
    
    # Read in file
    try:
        df = pd.read_csv(DATASET)
    except FileNotFoundError:
        print("ERROR: File not found.")
        exit(1)
    except Exception as e:
        print("ERROR: Could not read CSV file. ", e)
        exit(1)
        
    # Compute frequent itemsets
    frequent_itemsets = get_frequent_itemsets(df)
    
    # Build all association rules
    all_association_rules = get_association_rules(frequent_itemsets)
    
    # Print high confidence association rules
    high_conf_rules = get_high_conf_rules(all_association_rules)

    # Print output to output.txt
    with open("output.txt", "w") as f:
        # Redirect stdout to the file
        sys.stdout = f
        
        # Print
        print_frequent_itemsets(frequent_itemsets)
        print_high_conf_rules(high_conf_rules)
        
        # Reset stdout back to the console
        sys.stdout = sys.__stdout__


    print("Done.")

###########################
#   ALGORITHM FUNCTIONS   #
###########################

def get_frequent_itemsets(df):
    '''Compute all frequent itemsets with the a-priori algorithm.'''
    
    
    return "" #returns frequent itemsets



def get_association_rules(frequent_itemsets):
    '''Build all possible association rules for each of the frequent itemsets'''
    
    return "" #returns frequent itemsets



def get_high_conf_rules(all_association_rules):
    '''Identify association rules with a confidence of at least MIN_CONF and print them.'''
    
    
    return "" # returns high confidence rules
    
    
    
###########################
#     PRINT FUNCTIONS     #
###########################

def print_frequent_itemsets(frequent_itemsets):
    '''Print frequent itemsets'''
    
    print("------------")
    print(f"Frequent itemsets (min_sup={int(float(MIN_SUP)*100)}%)")
    

    print("------------")



def print_high_conf_rules(high_conf_rules):
    '''Print high-confidence association rules'''
    
    print("------------")
    print(f"High-confidence association rules (min_conf={int(float(MIN_CONF)*100)}%)")
    
    print("------------")
    
    
    
###########################
#          SETUP          #
###########################

if __name__ == "__main__":
    
    try:
        DATASET = str(sys.argv[1])
        MIN_SUP= str(sys.argv[2])
        MIN_CONF = str(sys.argv[3])
    except:
        print("Usage: python3 main.py <INTEGRATED-DATASET.csv> <min_sup> <min_conf>")
        exit(1)

    print("------------")
    print(f"Dataset file       = {DATASET}")
    print(f"Minimum support    = {MIN_SUP}")
    print(f"Minimum confidence = {MIN_CONF}")
    print("------------\n")
    
    main()