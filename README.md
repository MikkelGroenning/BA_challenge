Project Introduction
--------------------
This project contains the solution to the challenge to the 42577 Introduction to Business Analytics course at the Technical University of Denmark. The solution can be read in Jupyter Notebooks located in the notebook folder (see directory structure below). 

As of this moment project contains the "Part 0: Preliminary data wrangling, cleaning, descriptive statistics and "Part 2: Exploratory component" part of the challenge. The two first notebooks `01_Preprocess.ipynb` and `02_Descriptive.ipynb` contain the anvers to part 0. The reamining two notebookes `03_External_data.ipynb` and `04_External_Descriptive.ipynb`contain the answer to Part 2.


Authored by Toke Bøgelund Andersen and Mikkel Grønning.

Directory Structure
--------------------
    .
    ├── README.md
    ├── data
    │   ├── processed 	<- data after all preprocessing has been done
    │   └── raw 		<- original unmodified data acting as source of truth and provenance
    │
    ├── docs 			<- usage documentation or reference papers
    ├── notebooks 		<- jupyter notebooks for exploratory analysis and explanation 
    │   └── figures
    │
    ├── models 			<- compiled model .pkl or HDFS or .pb format  
    ├── environment.yml <- file with libraries and library versions for recreating the analysis environment
