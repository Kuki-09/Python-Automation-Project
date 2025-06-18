# Python Automation Project

This project showcases automation skills through cleaning real event participant data, generating personalized follow-up messages, and simulating email workflows using Python.


## Dataset Description

The dataset (`Data.csv`) contains over 600 rows with the following participant information:

- **Basic Info:** `name`, `first_name`, `last_name`, `email`, `created_at`
- **Event Details:** `approval_status`, `has_joined_event`
- **Transaction Info:** `amount`, `amount_tax`, `amount_discount`, `currency`, `ticket_name`
- **Professional Info:** `Job Title`, `What is your LinkedIn profile?`

## Step 1: Data Cleaning

**Script: `clean_data.py`**

Performs the following actions:
- Removes duplicate rows based on all columns.
- Normalizes `has_joined_event` values to `True/False`.
- Flags rows with:
  - Missing or blank **LinkedIn profiles**
  - Missing or blank **Job Titles**

Outputs:
  - `cleaned_output.csv` – cleaned and processed dataset with two new flag columns:
  - `LinkedIn_profile_missing`
  - `Job_Title_missing`


## Step 2: Auto-Personalized Messaging

**Script: `auto_message.py`**

This script:
- Reads the cleaned data from `cleaned_output.csv`
- Creates a personalized message for each user based on:
  - Their **name**
  - Whether they **joined the event**
  - Their **job title** (uses "Professional" if missing)

#### Example Messages:
- If **joined**:
  > "Hey Venkatesh, thanks for joining our session! As a freelance developer, we think you’ll love our upcoming AI workflow tools. Want early access?"

- If **not joined**:
  > "Hi Arushi, sorry we missed you at the last event! We’re preparing another session that might better suit your interests as a Product Manager."

#### Outputs:
- `messages.csv`: Contains columns `email`, `message`
- `messages_txt/`: Individual `.txt` files for each user
- `messages_json/`: Individual `.json` files for each user


## Step 3: Email Automation (Simulated)

- A simulated function `send_dummy_email()` prints out a mock email dispatch for each user using their email and message content.



