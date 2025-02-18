# Bible Verse App

This application allows users to look up Bible verses and provides links to external resources like Bible Gateway and The Bible Says. It is designed to be user-friendly, offering real-time suggestions and a responsive design.

Video demo: https://youtu.be/FQdmBKtsQcY

## **Features**

bible_verse_app/
│
├── app.py
├── .env
├── templates/
│   ├── index.html
│   └── result.html
└── static/
    ├── css/
        ├── main.css
        └── scripture.css

- **Search for Bible Verses**: Users can search for specific verses using the King James Version. The app corrects common misspellings and handles case sensitivity through correct_spelling function.

def correct_spelling(verse_input):
    corrections = {
        'mrak': 'mark',
        'colosians': 'colossians',
        'philippine': 'philippians',
        'genisis': 'genesis',
        'numer': 'numbers',
        'deuternomy': 'deuteronomy',
        'joshau': 'joshua',
        '1samuel': '1 samuel',
        '2samuel': '2 samuel',
        '1king': '1 kings',
        '2king': '2 kings',
        '1chronicles': '1 chronicles',
        '2chronicles': '2 chronicles',
        'matew': 'matthew',
    }

- **Auto-Suggestions**: As users type, the app provides real-time suggestions for book names, enhancing the search experience and converts format to OSIS format for the API to recognize it correctly

def convert_to_osis(verse_input):
    book_map = {
        "genesis": "GEN", "exodus": "EXO", "leviticus": "LEV", "numbers": "NUM", "deuteronomy": "DEU",
        "joshua": "JOS", "judges": "JDG", "ruth": "RUT", "1 samuel": "1SA", "2 samuel": "2SA",
        "1 kings": "1KI", "2 kings": "2KI", "1 chronicles": "1CH", "2 chronicles": "2CH",
        "ezra": "EZR", "nehemiah": "NEH", "esther": "EST", "job": "JOB", "psalms": "PSA",
        "proverbs": "PRO", "ecclesiastes": "ECC", "song of solomon": "SNG", "isaiah": "ISA",
        "jeremiah": "JER", "lamentations": "LAM", "ezekiel": "EZK", "daniel": "DAN",
        "hosea": "HOS", "joel": "JOE", "amos": "AMO", "obadiah": "OBA", "jonah": "JON",
        "micah": "MIC", "nahum": "NAH", "habakkuk": "HAB", "zephaniah": "ZEP",
        "haggai": "HAG", "zechariah": "ZEC", "malachi": "MAL",
        "matthew": "MAT", "mark": "MRK", "luke": "LUK", "john": "JHN",
        "acts": "ACT", "romans": "ROM", "1 corinthians": "1CO", "2 corinthians": "2CO",
        "galatians": "GAL", "ephesians": "EPH", "philippians": "PHP", "colossians": "COL",
        "1 thessalonians": "1TH", "2 thessalonians": "2TH", "1 timothy": "1TI", "2 timothy": "2TI",
        "titus": "TIT", "philemon": "PHM", "hebrews": "HEB", "james": "JAS",
        "1 peter": "1PE", "2 peter": "2PE", "1 john": "1JN", "2 john": "2JN",
        "3 john": "3JN", "jude": "JUD", "revelation": "REV"
    }
    try:
        parts = verse_input.lower().strip().split()
        book = ' '.join(parts[:-1])
        chapter, verse = parts[-1].split(':')
        osis_book = book_map.get(book)
        return f'{osis_book}.{chapter}.{verse}' if osis_book else None
    except (IndexError, ValueError):
        return None

- **Additional Resources**: After finding a verse, users can view related content on Bible Gateway and The Bible Says for further study and commentary.
- **Responsive Design**: The app is fully responsive, ensuring a seamless experience across all devices, including desktops, tablets, and smartphones.
- **Loading Indicator**: A spinner is displayed while fetching results, providing feedback that the app is processing the request.
- **Error Handling**: If no results are found, the app provides feedback and suggests checking the spelling or trying a different version.

## **Setup Instructions**

### **Prerequisites**

- Python 3.x
- Flask: A micro web framework for Python.
- Requests library: Used for making HTTP requests.
- dotenv library: For loading environment variables from a `.env` file.

### **Installation**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jamesleepm/bibleverseapp.git
   cd bibleverseapp

2. **Create a Virtual Environment**

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**

   pip install -r requirements.txt

4. **Set Up Environment Variables**

   Create a `.env` file in the project root:

   API_KEY=your_api_key_here*
   * => Replace your_api_key_here with your actual API key from api.bible.

## Running the Application ##

1. **Start the Flask Server**

   flask run

2. **Access the application**

   Open web browser and navigate to local server as referenced by IDE or based on your own server integration

## Usage ##

- Search for Verses: Enter a Bible verse in the format "John 3:16" and click "Lookup."
- Use Auto-Suggestions: Start typing a book name to see suggestions and select the correct one.
- View Additional Resources: After finding a verse, click on the links to view related content on Bible Gateway and The Bible Says.

## Code Overview ##
app.py: Contains the main Flask application logic, including routes, API calls, and input handling.
templates/: Contains HTML templates (index.html and result.html) for rendering the web pages.
static/: Contains CSS files for styling and JavaScript for implementing auto-suggestions.

## Troubleshooting ##
No Results Found: Ensure the API key is valid and the verse is in the correct format with lookup_verse function.

def lookup_verse(verse, bible_id):
    headers = {'api-key': API_KEY}
    url = f"{API_BASE_URL}/bibles/{bible_id}/passages/{verse}"
    response = requests.get(url, headers=headers, params={'content-type': 'text', 'include-notes': 'false', 'include-titles': 'true', 'include-chapter-numbers': 'false', 'include-verse-numbers': 'true', 'include-verse-spans': 'false'})
    app.logger.info(f"API Response: {response.text}")
    return response.json()

API Errors: Check the console for error messages and ensure rate limits are not exceeded.

## Contributing ##
Feel free to submit issues or pull requests.
Contributions are welcome!
