import re

def clean_text_utility(text):
    # Convert to lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    # Remove special characters and digits (keeping alphabets and spaces)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Sample messy text data for testing
messy_comments = [
    "   CHECK OUT this awesome link: https://example.com !!! It's 100% amazing...   ",
    "DONT buy this product@@@ 1234 useless service...",
    "Hello World!   This is a clean test case...    "
]

print("=== Data Cleaning & Regex Utility Demo ===")
for i, comment in enumerate(messy_comments, 1):
    cleaned = clean_text_utility(comment)
    print(f"\nOriginal {i}: '{comment}'")
    print(f"Cleaned  {i}: '{cleaned}'")

print("\nUtility script executed successfully on mobile!")
