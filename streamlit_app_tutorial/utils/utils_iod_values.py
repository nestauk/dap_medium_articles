# Creating dictionaries for the IoD.
# Cleaned names of the IoD deciles for data manipulation.
iod_indices = [
    "index_of_multiple_deprivation",
    "income_deprivation",
    "employment_deprivation",
    "education_skills_and_training",
    "health_deprivation_and_disability",
    "crime",
    "barriers_to_housing_and_services",
    "living_environment_deprivation",
    "income_deprivation_affecting_children",
    "income_deprivation_affecting_older_people",
]

# Name of IoD deciles to use in figures
iod_names = [
    "Index of Multiple Deprivation (IMD)",
    "Income Deprivation",
    "Employment Deprivation",
    "Education, Skills and Training",
    "Health Deprivation and Disability",
    "Crime",
    "Barriers to Housing and Services",
    "Living Environment Deprivation",
    "Income Deprivation Affecting Children Index (IDACI)",
    "Income Deprivation Affecting Older People Index (IDAOPI)",
]

# Shortened name of IoD deciles to use in the tooltips
iod_tooltip = [
    "IMD",
    "Income",
    "Employment",
    "Education",
    "Health and Disability",
    "Crime",
    "Barriers to Housing",
    "Living Environment",
    "IDACI",
    "IDAOPI",
]

# Creating Dictionaries to link the two indices,
iod_dict = dict(zip(iod_names, iod_indices))
iod_dict_inv = dict(zip(iod_indices, iod_names))