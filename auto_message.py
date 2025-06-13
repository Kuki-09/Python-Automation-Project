import pandas as pd
import os
import json

df = pd.read_csv("data/cleaned_output.csv")

os.makedirs("outputs/messages_txt", exist_ok=True)
os.makedirs("outputs/messages_json", exist_ok=True)

all_messages = []


for i, row in df.iterrows():
    name = row["first_name"]
    email = row["email"]
    job_title = row["Job Title"]
    has_joined = row["has_joined_event"]

    if row["Job_Title_missing"]:
        job_title = "Professional"

    if has_joined:
        msg = f"Hey {name}, thanks for joining our session! As a {job_title}, we think you’ll love our upcoming AI workflow tools. Want early access?"
    else:
        msg = f"Hi {name}, sorry we missed you at the last event! We’re preparing another session that might better suit your interests as a {job_title}."

    all_messages.append({"email": email, "message": msg})

    with open(f"outputs/messages_txt/{name}_{i}.txt", "w") as f:
        f.write(msg)

    with open(f"outputs/messages_json/{name}_{i}.json", "w") as f:
        json.dump({"email": email, "message": msg}, f)


pd.DataFrame(all_messages).to_csv("outputs/messages.csv", index=False)
print("Messages saved to messages.csv and individual .txt/.json files.")


def send_dummy_email(to_email, subject, body):
    print(f"Simulating sending email to {to_email}...\nSubject: {subject}\nMessage: {body[:60]}...\n")


for msg in all_messages:
    send_dummy_email(msg["email"], "Follow-up on Event", msg["message"])
