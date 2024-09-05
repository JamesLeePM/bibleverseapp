from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv('API_KEY')
API_BASE_URL = 'https://api.scripture.api.bible/v1'

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
    parts = verse_input.lower().strip().split()
    book = ' '.join(parts[:-1])
    book = corrections.get(book, book)
    return f"{book.title()} {parts[-1]}"

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

@app.route('/', methods=['GET', 'POST'])
def index():
    kjv_bible_id = "de4e12af7f28f599-02"
    if request.method == 'POST':
        verse_input = request.form['verse']
        corrected_verse = correct_spelling(verse_input)
        osis_verse = convert_to_osis(corrected_verse)
        if osis_verse:
            result = lookup_verse(osis_verse, kjv_bible_id)
            return render_template('result.html', result=result, corrected_verse=corrected_verse, bible_id=kjv_bible_id)
        else:
            return render_template('result.html', result=None, corrected_verse=corrected_verse, bible_id=kjv_bible_id)
    return render_template('index.html')

def lookup_verse(verse, bible_id):
    headers = {'api-key': API_KEY}
    url = f"{API_BASE_URL}/bibles/{bible_id}/passages/{verse}"
    response = requests.get(url, headers=headers, params={
        'content-type': 'text',
        'include-notes': 'false',
        'include-titles': 'true',
        'include-chapter-numbers': 'false',
        'include-verse-numbers': 'true',
        'include-verse-spans': 'false'
    })
    app.logger.info(f"API Response: {response.json()}")
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)