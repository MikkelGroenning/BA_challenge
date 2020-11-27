Project Introduction
--------------------
This project contains the solution to the challenge to the 42577 Introduction to Business Analytics course at the Technical University of Denmark. The solution can be read in Jupyter Notebooks located in the notebook folder (see directory structure below). 

To read the project as a full report go into the notebook-folder and read the notebooks in the following order. 
- 0_Introduction (Short introduction to the project and scope)
- 1_Preprocess (Preprocessing of the original cities data)
- 2_Descriptive (Descriptive analysis of the original cities data)
- 3_Modelling_part1 (Machine learning models on the original cities data prediction CO2 emission)
- 4_External_data (Gathering and process of external geographical and meteorological data)
- 5_External_Desciptive (Descriptive analysis of the newly acquired data)
- 6_Modelling_part2 (Machine learning models predicting the CO2 emission using the additional data)
- 7_Conclusion (Conclusion on the project and key takeaways)

Please note the the part 1 and part 2 (based on the train/test-split) is provided both in 03_modelling_part1 and 06_modelling_part2 - just with more data in 06_modelling_part2.



How to run the code
--------------------
An environment has been created to ensure the reproducibility of the data. Please note that this requires a conda-distribution to be installed on the computer. From the top folder run the current command in the terminal:

`conda env create -f environment.yml`

Activate the environment by the following command

`conda activate environment.yml`

Verify that the correct environment is activated by running

`conda info --envs`

All code should now run as intended.

Authored by Toke Bøgelund Andersen (s164202) and Mikkel Grønning (s144968).

Directory Structure
--------------------
    .
    ├── README.md
    ├── data
    │   ├── processed 	<- data after all preprocessing has been done
    │   ├── interim		<- data saved but not to be used for final analysis
    │   └── raw 		<- original unmodified data acting as source of truth and provenance
    │
    ├── docs 			<- usage documentation or reference papers
    ├── notebooks 		<- jupyter notebooks for  analysis and explanation 
    │   └── figures
    │
    ├── models 			<- compiled model .pkl or HDFS or .pb format  
    ├── environment.yml <- file with libraries and library versions for recreating the analysis
