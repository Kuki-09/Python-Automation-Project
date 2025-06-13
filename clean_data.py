import pandas as pd

df = pd.read_csv("data/Data.csv")

print(df.head(5))
print("\nTotal rows and columns are:", df.shape)
print("\nColumn names:",df.columns)

print("\nNumber of duplicated rows before: ",df.duplicated().sum())
df = df.drop_duplicates()
print("Number of duplicated rows after: ",df.duplicated().sum())

df["has_joined_event"] = df["has_joined_event"].str.lower().map({"yes":True , "no":False})

df["LinkedIn_profile_missing"] = df["What is your LinkedIn profile?"].isna() | (df["What is your LinkedIn profile?"].str.strip() == "")
print("\nNumber of rows with missing LinkedIn profile: ",df["LinkedIn_profile_missing"].sum())

df["Job_Title_missing"] = df["Job Title"].isna() | (df["Job Title"].str.strip() == "")
print("Number of rows with missing job title: ",df["Job_Title_missing"].sum())

df.to_csv("data/cleaned_output.csv",index = False)
print("\nCleaned data saved to cleaned_output.csv")





