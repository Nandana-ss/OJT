# Rule-based text classification
def classify_request(text):
    text = text.lower()
   
    if any(keyword in text for keyword in ["billing", "invoice", "charge"]):
        return "Billing Issue"
   
    elif any(keyword in text for keyword in ["password", "access", "login", "account"]):
        return "Technical Support"
   
    elif any(keyword in text for keyword in ["hours", "time", "location", "general"]):
        return "General Support"
   
    else:
        return "Other Support"

# Test sample
requests = [
    "my account is blocked",
    "I need my last billing details",
    "I need to know the timing of my order"
]

for request in requests:
    category = classify_request(request)
    print(f"Request: {request}\nCategory: {category}\n")
