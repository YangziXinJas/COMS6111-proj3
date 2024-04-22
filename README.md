# Association Rule Mining of NYC 311 Service Requests
COMS-E6111 Project 3

## How to run

### Install program requirements
In the directory of the repository, run:

  ```bash
  pip install -r requirements.txt
  ```

### Run 

In the directory of the repository, run:

  ```bash
  python3 main.py <INTEGRATED_DATASET.csv> <min_sup> <min_conf>
  ```
   
where:
- `<INTEGRATED_DATASET.csv>` is the file name
    (in this case, use `INTEGRATED_DATASET.csv`)

- `<min_sup>` is the minimum support 
        (a value between 0 and 1)

- `<min_conf>` is the minimum confidence 
    (a value between 0 and 1)

## Program description

### Overall structure
The project implements a variant of the Apriori algorithm for frequent itemset generation and association rule mining. The goal is to extract meaningful patterns from transaction data provided in CSV format. The program will accept a dataset provided in CSV and 2 values for support and confidence to help generate associations. After converting the CSV into dataframe, we apply the variant of Apriori algorithm to focus on frequent itemsets only. Details for this algorithm is provided below.
### Details
Unlike the original Apriori algorithm which evaluates all possible item combinations explicitly, this implementation progressively builds candidate itemsets only from previously identified frequent itemsets. This reduces the computational overhead significantly.
The variation aim to optimize the computational efficiency of the Apriori algorithm, particularly in handling large datasets and reducing the execution time by minimizing unnecessary computations. The approach of building upon only frequent itemsets reduces the size of the search space dramatically compared to traditional methods that consider all possible item combinations.

Association rules are generated only from the identified frequent itemsets, which simplifies the rule generation phase. This focuses the computational effort only on viable candidate rules.

#### Specific Functions
* get_frequent_itemsets(): This function leverages iterative candidate generation where only the sets from the previous iteration that met the minimum support threshold are combined to form new candidate sets.
* get_association_rules(): For each frequent itemset with more than one item, all non-empty proper subsets are generated. The support and confidence of potential rules are calculated to filter out those that do not meet the minimum criteria.
* powerset(): Generates all possible subsets of a given itemset, utilized in rule generation to explore potential antecedents in association rules.

## About the dataset

1. which NYC Open Data data set(s) you used to generate the INTEGRATED-DATASET file
2. what (high-level) procedure you used to map the original NYC Open Data data set(s) into your INTEGRATED-DATASET file
3. what makes your choice of INTEGRATED-DATASET file compelling (in other words, justify your choice of NYC Open Data data set(s)). The explanation should be detailed enough to allow us to recreate your INTEGRATED-DATASET file exactly from scratch from the NYC Open Data site.

### Sample run
  ```bash
  python3 main.py INTEGRATED_DATASET.csv <min_sup> <min_conf>
  ```

  Results: Briefly explain why the results are indeed compelling.


## About the repository
Authors: 

- Aryana Mohammadi (am5723)

- Jasmine Shin (yx2810)

Files included:

- `main.py`

- `README.md`

- `requirements.txt`

References:

Notes:
