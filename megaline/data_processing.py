import time
import warnings
from contextlib import contextmanager

import numpy as np
import pandas as pd
from IPython.display import display, Markdown
from pandas_dq import dq_report
from scipy import stats as st


def show_df_info(df, name):
    display(Markdown(f'### {name}'))
    display(df.info(), df.describe(), df.head())
    time.sleep(1)  # to slow down the output


def downcast_dtypes(df):
    fcols = df.select_dtypes('float').columns
    icols = df.select_dtypes('integer').columns

    df[fcols] = df[fcols].apply(pd.to_numeric, downcast='float')
    df[icols] = df[icols].apply(pd.to_numeric, downcast='integer')
    return df


@contextmanager
def suppress_dq_warnings():
    # Suppress specific warnings
    warnings.filterwarnings("ignore",
                            message="The argument 'infer_datetime_format' is deprecated and will be removed in a "
                                    "future version.")
    warnings.filterwarnings("ignore", message="DataFrame.applymap has been deprecated. Use DataFrame.map instead.")
    try:
        yield
    finally:
        # Reset warnings to default state after the block
        warnings.resetwarnings()


def check_data_quality(df):
    """
    Check data quality of the dataframe for the most common issues:
    - Missing values
    - Duplicate rows
    - Constant columns
    - Categorical columns with high cardinality
    - Numerical columns with high cardinality
    - Outliers
    - Correlated columns
    - Generates a dq_report

    Parameters:
    df: pandas.DataFrame
        The dataframe to check

    Returns:
        None
    """
    display(Markdown('### Data Quality Report'))

    # Missing values
    display(Markdown('#### Missing Values'))
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if missing.empty:
        display(Markdown('<span style="color:green">No missing values found</span>'))
    else:
        display(Markdown('<span style="color:orange">Missing values found:</span>'))
        display(missing)

    # Duplicate rows
    display(Markdown('#### Duplicate Rows'))
    duplicates = df.duplicated().sum()
    if duplicates == 0:
        display(Markdown('<span style="color:green">No duplicate rows found</span>'))
    else:
        display(Markdown(f'<span style="color:orange">{duplicates} duplicate rows found</span>'))

    # Constant columns
    display(Markdown('#### Constant Columns'))
    constant = df.columns[df.nunique() == 1]
    if constant.empty:
        display(Markdown('<span style="color:green">No constant columns found</span>'))
    else:
        display(Markdown('<span style="color:orange">Constant columns found:</span>'))
        display(constant)

    # Categorical columns with high cardinality
    display(Markdown('#### Categorical Columns with High Cardinality'))
    cat_cols = df.select_dtypes('object').columns
    high_cardinality = df[cat_cols].nunique()
    high_cardinality = high_cardinality[high_cardinality > 10]
    if high_cardinality.empty:
        display(Markdown('<span style="color:green">No categorical columns with high cardinality found</span>'))
    else:
        display(Markdown('<span style="color:orange">Categorical columns with high cardinality found:</span>'))
        display(high_cardinality)

    # Numerical columns with high cardinality
    display(Markdown('#### Numerical Columns with High Cardinality'))
    num_cols = df.select_dtypes(['int', 'float']).columns
    high_cardinality = df[num_cols].nunique()
    high_cardinality = high_cardinality[high_cardinality > 10]
    if high_cardinality.empty:
        display(Markdown('<span style="color:green">No numerical columns with high cardinality found</span>'))
    else:
        display(Markdown('<span style="color:orange">Numerical columns with high cardinality found:</span>'))
        display(high_cardinality)

    # Outliers
    display(Markdown('#### Outliers'))
    outliers = {}
    for col in num_cols:
        z_scores = np.abs(st.zscore(df[col].dropna()))
        outliers[col] = np.sum(z_scores > 3)
    outliers = {k: v for k, v in outliers.items() if v > 0}
    if not outliers:
        display(Markdown('<span style="color:green">No outliers found</span>'))
    else:
        display(Markdown('<span style="color:orange">Outliers found:</span>'))
        display(outliers)

    # Correlated columns
    display(Markdown('#### Correlated Columns'))
    corr_matrix = df.select_dtypes(['int', 'float']).corr().abs()
    upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    highly_correlated = [column for column in upper_tri.columns if any(upper_tri[column] > 0.9)]
    if not highly_correlated:
        display(Markdown('<span style="color:green">No highly correlated columns found</span>'))
    else:
        display(Markdown('<span style="color:orange">Highly correlated columns found:</span>'))
        display(highly_correlated)

    # DQ Report
    display(Markdown('#### Data Quality Report'))
    with suppress_dq_warnings():
        return dq_report(df)
