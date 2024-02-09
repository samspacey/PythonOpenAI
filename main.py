import pandas as pd
import openai
import os

# Ensure the OpenAI API key is set as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load your dataset
df = pd.read_csv('C:\\Users\\SamSpacey\\OneDrive - Woodhurst Consulting Limited\\AI RFP\\Python\\AI_Training_Data_2_Sample.csv')

# Load the Context from a text file
with open('C:\\Users\\SamSpacey\\OneDrive - Woodhurst Consulting Limited\\AI RFP\\Python\\Context.txt', 'r') as file:
    context_input = file.read()

# Load the prompt template from a text file
with open('C:\\Users\\SamSpacey\\OneDrive - Woodhurst Consulting Limited\\AI RFP\\Python\\prompt_template.txt', 'r') as file:
    prompt_template = file.read()

def score_vendor_response(row, model="gpt-3.5-turbo", max_tokens=50):
    # Assuming prompt_template structures the conversation context
    messages = [
        {"role": "system", "content": context_input},
        {"role": "user", "content": prompt_template.format(
            user_story=row['User Story'], 
            conditions_of_satisfaction=row['Conditions of satisfaction'], 
            vendor_response=row['Vendor Response']
        )}
    ]

    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=0,
        n=2
    )

    # Extract the completion text from the API's response
    if response.choices:
        completion_text = response.choices[0].message.content.strip()
    else:
        completion_text = None

    return completion_text



# Score each row and add it to a new column
df['AI Score'] = df.apply(score_vendor_response, axis=1)

# Save the updated dataset to a new CSV file
df.to_csv('updated_dataset_with_scores.csv', index=False)

print("Dataset updated and saved successfully.")
