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

This project is developed with the [311 Service Requests 2010 to Present Dataset](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/about_data) from NYC OpenData.

In order to map this dataset into our project, we first removed all rows not between the years of 2022 and 2024. This cut the data down from 30+ million rows to 3+ million rows. This choice was simply to bring the runtime down.

Next, we dropped all columns that were either non-categorical, mostly empty cells, or seemed unlikely to yield useful results. We kept the following columns: Complaint Type, Location Type, Incident Zip, Street Name, City, Status, Community Board, Borough, Police Precinct.

We also cleaned up some columns to make them better fit categorical data. For example, the "Location Type" column had both "Residential Building/Home" and "RESIDENTIAL BUILDING" as options (depending on what department logged the claim). We combined this data to all say "Residential Building/Home."

We chose this dataset to see the relations among complaints accross boroughs. We also wanted to see if different complaints are treated similarly (i.e speed of completion).

### Sample run
  ```bash
  python3 main.py INTEGRATED_DATASET.csv 0.2 0.85
  ```

 The results of this run can be found in `example_run.txt`. For this run, we extracted high association rules from this dataset and discovered that when a complain is open, it is likely to be from a residential building. Illegal parking, on the other hand, is a large portion of the complaints, but they (and other street complaints) are mostly resolved. Additionally, from the frequent itemsets and their supports, we can see that the amount of complaints coming from each borough is relatively similar; however, the Bronx seemed to have the least closed complaints in relation to the amount total. 


## About the repository
Authors: 

- Aryana Mohammadi (am5723)

- Jasmine Shin (yx2810)

Files included:

- `main.py`

- `README.md`

- `requirements.txt`

References:
- Recommended course readings.
