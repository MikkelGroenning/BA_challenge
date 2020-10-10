#%% Package import
import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import sklearn

from sklearn import linear_model

df = pd.read_csv(os.path.abspath('../../data/Processed/Cities.csv'), index_col=0)

#%% Split the data such that the first 75 % percent of the data is training data and the 
# reamaing 25 % is test data

def train_test_split(data, test_size, target, drop_cols = [], shuffle = True):
    X = df.drop(drop_cols+[target], axis = 1)
    y = df[target]

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
        X, y, test_size = test_size, shuffle = shuffle)

    return X_train, X_test, y_train.values, y_test.values

# %%
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.metrics import make_scorer

def negeate_MSE(y_true, y_pred):
    mse = -mean_squared_error(y_true, y_pred)
    return mse

def cv(pipe, parameters, X_train, y_train, cf = 10):    
    # perform cross validaiton over the input parameters
    cv_select = GridSearchCV(
        estimator=pipe, 
        param_grid=parameters, 
        scoring=make_scorer(negeate_MSE),
        n_jobs=-1,
        return_train_score=True,
        verbose=10, 
        cv=cf
    )
    cv_select.fit(X_train, y_train)
    
    return(cv_select)

def getPipe(model, numerical_columns, categorical_columns):

    # Pipeline to handle continous parameters. Here the parameters are scaled 
    numeric_transformer = Pipeline([
        ('scale', StandardScaler())
    ])
    
    # Pipeline to handle categorical parameters. Here the categorical variables
    # which are missing is imputed by using the most frequent value
    # afterwards they are one-hot encoded.
    categorical_transformer = Pipeline([
        ('imputer', SimpleImputer(
            missing_values = ' NaN',
            strategy = 'most_frequent')),
        ('hot', OneHotEncoder())
    ])
    
    # Split the data into continous and caterigorical using ColumnTransformer
    # and apply numeric_transformer and categorical_transformer 
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numerical_columns),
            ('cat', categorical_transformer, categorical_columns)
        ],
        remainder='drop'
    )
    
    # Build the final pipeline for model fitting
    pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('model', model)
    ])

    return pipe


# %%
X_train, X_test, y_train, y_test  = train_test_split(
    data = df, 
    test_size = 0.25, 
    target = 'CO2_Emissions_per_Capita_(metric_tonnes)',
    drop_cols = ['Pollution_Index_'],
    shuffle = False
)

#%%
colum_names = X_train.columns

no_info_column = [
    'City', 'cityID', 'clusterID', 'Country', 'Latitude', 'Longitude'
]

columsn_with_nan = ['Bicycle_Modeshare_(%)', 'Congestion_(%)', 'Congestion_AM_Peak_(%)',
       'Congestion_PM_Peak_(%)', 'Traffic_Index', 'Travel_Time_Index',
       'Inefficiency_Index', 'Unemployment_Rate_(%)', 'Cost_of_Living_Index',
       'Rent_Index', 'Grocery_Index', 'Restaurant_Price_Index',
       'Local_Purchasing_Power_Index', 'Poverty_Rate_(%)', 'Safety_Index',
       'Pollution_Index_']

remove_columns = no_info_column + columsn_with_nan

categorical_columns = ['Typology', 'Continent']

numerical_columns = [ column for column in colum_names if column not in remove_columns+categorical_columns ]

#%% Apply elastic net
elastic_net_model = linear_model.ElasticNet(fit_intercept = True)

n1 = 50
n2 = 50
parameters = {
    'model__alpha': np.logspace(-3, 1, n1),
    'model__l1_ratio': np.linspace(0, 1, n2)
}

elastic_net_pibe = getPipe(
    model = elastic_net_model,
    numerical_columns = numerical_columns,
    categorical_columns = categorical_columns
)


elastic_net_cv = cv(elastic_net_pibe, parameters, X_train, y_train, cf = 3)

#%%
from sklearn.metrics import r2_score
y_pred = elastic_net_cv.predict(X_test)
print('Elastic 1 RMSE: ', r2_score(y_test, y_pred))

# %%
