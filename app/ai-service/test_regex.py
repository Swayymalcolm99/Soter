import re

PATTERNS = {
    "name": [
        r"(?:Full\s+)?[Nn]ame[:\s]+\n?([A-Z][a-z]+(?:[ \t]+(?!(?:Date|DOB|Birth|ID|Passport))[A-Z][a-z]+)+)",
        r"(?:Full\s+)?[Nn]ame[:\s]+\n?([A-Z]+(?:[ \t]+(?!(?:DATE|DOB|BIRTH|ID|PASSPORT))[A-Z]+)+)",
    ],
}

def test_pattern(text):
    print(f"Testing text: {text}")
    for pattern in PATTERNS["name"]:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            print(f"Matched: '{match.group(1)}'")
            return
    print("No match found")

texts = [
    "Name: John Doe Date of Birth: 15 Jan 1990",
    "Full Name: JANE SMITH DOB: 01/01/1980",
    "name: Robert Paulson ID: 12345",
    "Name: John Doe",
]

for text in texts:
    test_pattern(text)
