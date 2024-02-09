import csv
import json

# Load the Context from a text file
with open('C:\\Users\\SamSpacey\\OneDrive - Woodhurst Consulting Limited\\AI RFP\\Python\\Context.txt', 'r') as file:
    context_input = file.read()

# Load the prompt template from a text file
with open('C:\\Users\\SamSpacey\\OneDrive - Woodhurst Consulting Limited\\AI RFP\\Python\\prompt_template.txt', 'r') as file:
    prompt_template = file.read()

# Load the sample data and the JSONL
with open('C:\\Users\\SamSpacey\\OneDrive - Woodhurst Consulting Limited\\AI RFP\\Python\\AI_Training_Data_2_Sample.csv') as csvfile, open("C:\\Users\\SamSpacey\\OneDrive - Woodhurst Consulting Limited\\AI RFP\\Python\\target.jsonl", "a") as jsonfile:
    r = csv.DictReader(csvfile)

    for row in r:
        model = {
            "messages": [
                {
                    "role": "system",
                    "content": context_input
                },
                {
                    "role": "user",
                    "content": prompt_template.format(
                        user_story=row['User Story'], 
                        conditions_of_satisfaction=row['Conditions of satisfaction'], 
                        vendor_response=row['Vendor Response']
                    )
                },
                {
                    "role": "assistant",
                    "content": row['Score'] # Response row
                },
                {
                    "role": "user",
                    "content": "Please explain the rationale for providing this score."
                    
                },
                {
                    "role": "assistant",
                    "content": row['Rationale'] # Response row
                }                
            ]
        }
        jsonl = json.dumps(model)
        jsonfile.write(f"{jsonl}\n")