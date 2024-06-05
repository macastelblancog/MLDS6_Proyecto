import sys
sys.path.append("../../..")
from src.bazinga.preprocessing import text_preprocess, BERT_embeddings
import requests
import json
import pandas as pd
import torch
from transformers import BertTokenizer, BertModel
import numpy as np


def get_bert_embeddings(text, max_length=512):
    # Preprocess the text
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased').to(device)
    text = text_preprocess(text)
    
    # Tokenize the text
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=max_length).to(device)
    
    # Get BERT embeddings
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Use [CLS] token and move back to CPU
    embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy()
    
    return embeddings.tolist() 

def predict(text, port):
    preprocessed_text = get_bert_embeddings(text)
    preprocessed_text_np = np.array(preprocessed_text)  # Convert to numpy array
    preprocessed_text_reshaped = preprocessed_text_np.reshape(1, -1)  # Reshape to (1, 768)
    
    url = f"http://127.0.0.1:{port}/invocations"
    headers = {"Content-Type": "application/json"}
    data = {"inputs": preprocessed_text_reshaped.tolist()}  # Convert to list for JSON serialization
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    
    if response.status_code == 200:
        predictions = response.json().get('predictions', [])
        
        # Ensure the predictions are lists of floats
        formatted_predictions = []
        for pred_list in predictions:
            formatted_pred_list = []
            for pred in pred_list:
                try:
                    formatted_pred_list.append(round(float(pred), 2))
                except (ValueError, TypeError):
                    print(f"Skipping invalid prediction value: {pred}")  # Debugging print for invalid values
                    continue
            formatted_predictions.append(formatted_pred_list)
        
        if formatted_predictions:
            first_prediction = formatted_predictions[0][0]
            if first_prediction >= 0.5:
                print("The headline is not sarcastic.")
            else:
                print("The headline is sarcastic.")
        
        return formatted_predictions
        
        return formatted_predictions
    else:
        return f"Failed to make prediction. Status code: {response.status_code}. Reason: {response.text}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python predict.py 'Your headline here' port_number")
        sys.exit(1)

    headline = sys.argv[1]
    port = int(sys.argv[2])  # Convert port number to integer
    result = predict(headline, port)
    print(f"Prediction: {result}")
