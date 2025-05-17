# transform.py

import pandas as pd
from datetime import datetime

def clean_job_title(title):
    title = title.lower()
    if 'data scientist' in title:
        if 'senior' in title or 'sr' in title:
            return 'Senior Data Scientist'
        elif 'lead' in title or 'principal' in title or 'staff' in title:
            return 'Lead Data Scientist'
        elif 'machine learning' in title or 'ml' in title:
            return 'ML/Data Scientist'
        elif 'intern' in title:
            return 'Data Science Intern'
        else:
            return 'Data Scientist'
    elif 'analyst' in title:
        return 'Data Analyst'
    elif 'engineer' in title:
        return 'Data Engineer'
    elif 'scientist' in title:
        return 'Other Scientist'
    else:
        return 'Other'

def get_seniority(title):
    title = title.lower()
    if 'senior' in title or 'sr' in title:
        return 'Senior'
    elif 'lead' in title or 'principal' in title or 'staff' in title:
        return 'Lead'
    elif 'intern' in title:
        return 'Intern'
    else:
        return 'Junior-Mid'

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms and cleans the raw DataFrame.
    
    Parameters:
        df (pd.DataFrame): Raw data.
    
    Returns:
        pd.DataFrame: Cleaned data.
    """

    # Drop redundant index
    df = df.drop(columns=['index'])

    # Clean company name
    df['Company Name'] = df['Company Name'].str.split('\n').str[0].str.strip()

    # Normalize job title
    df['Job Title Cleaned'] = df['Job Title'].apply(clean_job_title)

    # Clean salary estimate
    df['Salary Estimate Cleaned'] = (
        df['Salary Estimate']
        .str.replace(r'\(.*?\)', '', regex=True)
        .str.replace('K', '', regex=False)
        .str.replace('$', '', regex=False)
        .str.strip()
    )

    df[['min_salary', 'max_salary']] = df['Salary Estimate Cleaned'].str.split('-', expand=True)
    df['min_salary'] = pd.to_numeric(df['min_salary'], errors='coerce')
    df['max_salary'] = pd.to_numeric(df['max_salary'], errors='coerce')
    df['avg_salary'] = (df['min_salary'] + df['max_salary']) / 2

    # Split location
    df[['job_city', 'job_state']] = df['Location'].str.split(',', expand=True)
    df['job_city'] = df['job_city'].str.strip()
    df['job_state'] = df['job_state'].str.strip()

    # Clean categorical columns
    df['Size'] = df['Size'].replace('-1', 'Unknown').str.strip()
    df['Revenue'] = df['Revenue'].replace(['-1', 'Unknown / Non-Applicable'], 'Unknown').str.strip()

    for col in ['Type of ownership', 'Industry', 'Sector']:
        df[col] = df[col].replace('-1', 'Unknown').fillna('Unknown').str.strip().str.title()

    # Standardize missing values
    missing_values = ['-1', 'Unknown / Non-Applicable', 'None', '']
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].replace(missing_values, 'Unknown').fillna('Unknown')

    # Clean competitors
    df['Competitors'] = df['Competitors'].replace('Unknown', 'No Competitor Info')
    df['Competitor_List'] = df['Competitors'].apply(
        lambda x: [comp.strip() for comp in x.split(',')] if x != 'No Competitor Info' else []
    )

    # Derived columns
    current_year = datetime.now().year
    df['company_age'] = df['Founded'].apply(lambda x: current_year - x if x > 0 else None)
    df['seniority_level'] = df['Job Title'].apply(get_seniority)
    df['remote_flag'] = df['Job Description'].apply(
        lambda x: 1 if 'remote' in x.lower() or 'work from home' in x.lower() else 0
    )

    return df
