import sys
import pandas as pd
from itertools import combinations, chain
from collections import defaultdict

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
        df = pd.read_csv(DATASET, nrows=100000)
        print("Number of rows:", df.shape[0])
    except FileNotFoundError:
        print("ERROR: File not found.")
        exit(1)
    except Exception as e:
        print("ERROR: Could not read CSV file. ", e)
        exit(1)
        
    # Compute frequent itemsets
    frequent_itemsets = get_frequent_itemsets(df)
    
    # Build all association rules
    all_association_rules = get_association_rules(frequent_itemsets.copy(), df)
    
    # Print high confidence association rules
    high_conf_rules = get_high_conf_rules(all_association_rules)

    # Print output to output.txt
    with open("output.txt", "w") as f:
        # Redirect stdout to the file
        sys.stdout = f
        
        # Print
        print_frequent_itemsets(frequent_itemsets, len(df))
        print_high_conf_rules(high_conf_rules)
        
        # Reset stdout back to the console
        sys.stdout = sys.__stdout__


    print("Done.")

###########################
#   ALGORITHM FUNCTIONS   #
###########################

def get_frequent_itemsets(df):
    '''Compute all frequent itemsets with the a-priori algorithm.''' 
    
    # Iterate through all the rows and get a dictionary of unique items and their count
    item_counts = dict()
    for _, row in df.iterrows():
        for item in row:
            if pd.isna(item):
                continue
            
            if item not in item_counts.keys():
                item_counts[item] = 1
            else:
                item_counts[item] += 1
    
    frequent_items = set(item for item, count in item_counts.items() if count/len(df) >= MIN_SUP)
    
    frequent_itemsets = [frozenset([item]) for item in frequent_items]
    result = {frozenset([item]): item_counts[item] for item in frequent_items}
    
    k = 2
    while True:
        # Generate candidate itemsets
        candidate_itemsets = set()
        for set1, set2 in combinations(frequent_itemsets, 2):
            candidate_itemset = set1.union(set2)
            if len(candidate_itemset) == k:
                candidate_itemsets.add(candidate_itemset)
        
        # Calculate support for each candidate itemset
        candidate_count = defaultdict(int)
        for _, row in df.iterrows():
            for candidate in candidate_itemsets:
                if candidate.issubset(row):
                    candidate_count[candidate] += 1
        
        frequent_itemsets = set(itemset for itemset, count in candidate_count.items() if count/len(df) >= MIN_SUP)
        result.update({itemset: candidate_count[itemset] for itemset in frequent_itemsets})
        
        if not frequent_itemsets:
            break

        k += 1
        
    # Return frequent itemsets candidate_count
    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True)) 



def get_association_rules(frequent_itemsets, df):
    '''Build all possible association rules for each of the frequent itemsets'''
    rules = []

    # iterate through all frequent itemsets
    for itemset in frequent_itemsets:
        if len(itemset) == 1:
            continue
        

        subsets = [frozenset(subset) for subset in powerset(itemset)]
        for subset in subsets:
            # skip empty set or the itemset itself
            if not subset or not itemset.difference(subset):
                continue

            # calculate support and confidence of the rule
            support = frequent_itemsets[itemset] / len(df)
            confidence = frequent_itemsets[itemset] / frequent_itemsets[subset]

            if confidence >= MIN_CONF and support >= MIN_SUP:
                rule = (f"{list(subset)} => {list(itemset.difference(subset))} (support={support:.2f}, confidence={confidence:.2f})")
                rules.append((rule, confidence))
    
    return sorted(rules, key=lambda x: x[1], reverse=True)

def powerset(s):
    '''Generate all possible subsets of a set'''
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def get_high_conf_rules(all_association_rules):
    '''Identify association rules with a confidence of at least MIN_CONF and print them.'''
    
    
    return all_association_rules # returns high confidence rules
    
    
    
###########################
#     PRINT FUNCTIONS     #
###########################

def print_frequent_itemsets(frequent_itemsets, df_size):
    '''Print frequent itemsets'''
    
    print("==============")
    print(f"--------------Frequent itemsets (min_sup={int(float(MIN_SUP)*100)}%)")
    
    for key in frequent_itemsets.keys():
        print(f"{list(key)} ({round(((frequent_itemsets[key]/df_size)*100), 2)}%)")
        
    print("==============")



def print_high_conf_rules(high_conf_rules):
    '''Print high-confidence association rules'''
    
    print("==============")
    print(f"--------------High-confidence association rules (min_conf={int(float(MIN_CONF)*100)}%)")
    
    for item in high_conf_rules:
        print(item[0])
    print("==============")
    
    
    
###########################
#          SETUP          #
###########################

if __name__ == "__main__":
    
    try:
        DATASET = str(sys.argv[1])
        MIN_SUP= float(sys.argv[2])
        MIN_CONF = float(sys.argv[3])
    except:
        print("Usage: python3 main.py <INTEGRATED-DATASET.csv> <min_sup> <min_conf>")
        exit(1)

    print("------------")
    print(f"Dataset file       = {DATASET}")
    print(f"Minimum support    = {MIN_SUP}")
    print(f"Minimum confidence = {MIN_CONF}")
    print("------------\n")
    
    main()