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
A clear description of the internal design of your project; 
### Details
in particular, if you decided to implement variations of the original a-priori algorithm (see above), you must explain precisely what variations you have implemented and why.

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