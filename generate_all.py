import os
import json
import time
import urllib.request
import re

# Your API Key
API_KEY = "AIzaSyBfSobNUOkVA2KacporlwoizToeJarYoY4"
BASE_DIR = r"d:\DESKTOP\Java"

# Step 1: Get all valid topic directories that start with 3 digits
topics = []
for item in os.listdir(BASE_DIR):
    item_path = os.path.join(BASE_DIR, item)
    if os.path.isdir(item_path) and re.match(r"^\d{3}-", item):
        topics.append(item)

# Sort them alphabetically
topics.sort()

# Step 2: We skip "001" because we already manually perfected it
topics = [t for t in topics if not t.startswith("001")]

print(f"Found {len(topics)} topics to generate.")

def generate_content(topic_name):
    # We use gemini-flash-latest to avoid quota issues with newer models
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"
    
    prompt = f"""You are an expert Java instructor. Write a comprehensive, exam-focused Markdown guide for the following Java topic: "{topic_name}".
The topic is part of a 112-topic syllabus.
Format the output as a clean Markdown file. Include:
1. A clear definition and explanation of the concept.
2. Code examples.
3. Common mistakes or pitfalls.
4. Important exam tips and key takeaways.
Make it highly detailed, beginner ready,not overkill,can be covered all in 6 hours, similar to a high-quality study guide. 
Do not output anything outside of the markdown content (no wrapper text, just the markdown itself).
"""
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "temperature": 0.4,
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    max_retries = 20
    retry_delay = 60
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode('utf-8'))
                text = result['candidates'][0]['content']['parts'][0]['text']
                # Clean up markdown codeblocks if it wrapped everything in ```markdown
                if text.startswith("```markdown"):
                    text = text[11:]
                if text.startswith("```"):
                    text = text[3:]
                if text.endswith("```"):
                    text = text[:-3]
                return text.strip()
        except urllib.error.HTTPError as e:
            error_msg = e.read().decode('utf-8')
            if e.code == 429:
                print(f"  -> Rate limited (429). Waiting {retry_delay}s before retrying (Attempt {attempt+1}/{max_retries})...")
                time.sleep(retry_delay)
                retry_delay += 5 # slightly increase delay to be safe
            else:
                print(f"Error generating {topic_name}: {e.code} - {e.reason}\nDetails: {error_msg}")
                return None
        except Exception as e:
            print(f"Error generating {topic_name}: {e}")
            return None
            
    print(f"  -> Failed after {max_retries} attempts.")
    return None

# Step 3: Loop through topics, call the API, and save the content
for index, topic in enumerate(topics):
    print(f"[{index+1}/{len(topics)}] Generating content for {topic}...")
    readme_path = os.path.join(BASE_DIR, topic, "README.md")
    
    # We are forcing a re-write to make them more detailed.
    content = generate_content(topic)
    
    if content:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  -> Successfully saved.")
    else:
        print(f"  -> Failed to generate.")
    
    # Rate Limit Protection: Free tier limits requests to 15 RPM (1 per 4 seconds)
    # We sleep for 4.5 seconds to be safe.
    time.sleep(4.5) 

print("Finished generating all files!")
