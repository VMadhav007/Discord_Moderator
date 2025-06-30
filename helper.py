from transformers import XLMRobertaForSequenceClassification, XLMRobertaTokenizer
import torch
print(torch.cuda.is_available())  # Should return True if GPU is available


tokenizer = XLMRobertaTokenizer.from_pretrained("oleksiizirka/xlm-roberta-toxicity-classifier")
model = XLMRobertaForSequenceClassification.from_pretrained("oleksiizirka/xlm-roberta-toxicity-classifier")

def classify_toxicity(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = torch.sigmoid(logits)[0]
    labels = ['toxic','severe_toxic','obscene','threat','insult','identity_hate','none']
    return {label: float(score) for label, score in zip(labels, probs)}
