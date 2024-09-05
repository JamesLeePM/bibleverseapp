# Bible Verse Lookup App

This application allows users to look up Bible verses and provides links to external resources like Bible Gateway and The Bible Says.

## **Features**

- **Search for Bible Verses**: Use the King James Version to find specific verses.
- **Auto-Suggestions**: Get real-time suggestions for book names as you type.
- **Additional Resources**: View related content on Bible Gateway and The Bible Says.
- **Responsive Design**: Fully responsive and mobile-friendly interface.
- **Loading Indicator**: Displays a spinner while fetching results.
- **Error Handling**: Provides feedback if no results are found.

## **Setup Instructions**

### **Prerequisites**

- Python 3.x
- Flask
- Requests library
- dotenv library

### **Installation**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jamesakanoa/bibleverseapp.git
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

   Open web browser as referenced by IDE or server integration results

## Usage ##

- Enter a Bible verse in the format "John 3:16" and click "Lookup."
- Use the auto-suggestions to find book names quickly.
- View the verse result and additional resources.

## Code Overview ##
app.py: Contains the main Flask application logic, including routes and API calls.
templates/: Contains HTML templates (index.html and result.html).
static/: Contains CSS files for styling and JavaScript for auto-suggestions.

## Troubleshooting ##
No Results Found: Ensure the API key is valid and the verse is in the correct format.
API Errors: Check the console for error messages and ensure rate limits are not exceeded.

## Contributing ##
Feel free to submit issues or pull requests. 
Contributions are welcome!
