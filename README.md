# Pune District Court Case Search

A Flask-based web application for searching case statuses in the Pune District Court. This application allows users to search for court cases by selecting a court complex, court establishment, case type, case number, and year, and retrieves detailed case information, including links to associated court orders or judgments in PDF format.

## Features

- **Case Search**: Users can search for cases by providing court complex, establishment, case type, case number, and year.
- **Dynamic Case Types**: Fetches and displays available case types dynamically.
- **CAPTCHA Integration**: Retrieves and displays CAPTCHA images for secure form submissions.
- **Case Details**: Retrieves detailed case information, including links to PDF orders/judgments.
- **Database Logging**: Logs all search queries and responses in a SQLite database for record-keeping.
- **Responsive Design**: Built with Bootstrap for a user-friendly and responsive interface.

## Prerequisites

- Python 3.8+
- SQLite (included with Python)
- A modern web browser

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/pune-court-case-search.git
   cd pune-court-case-search
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**:
   ```bash
   python init_db.py
   ```

   This creates a SQLite database (`queries.db`) with a `queries` table to store search data.

## Usage

1. **Run the Application**:
   ```bash
   python app.py
   ```

   The application will start in debug mode and be accessible at `http://localhost:5000`.

2. **Access the Web Interface**:
   - Open a web browser and navigate to `http://localhost:5000`.
   - Select the court complex, court establishment, case type, enter the case number, year, and CAPTCHA code.
   - Submit the form to view case details, including links to any available PDF orders or judgments.

3. **Check Database Contents**:
   ```bash
   python check_db.py
   ```

   This script displays all stored queries and their responses from the `queries.db` database.

4. **Example Inputs**:
   Below are real examples from the Civil Court, Pimpri, listed on 02-08-2025. You can use these to test the form, or replace with your own case details (court complex, establishment, case type, case number, and year):

   | Serial Number | Case Type/Case Number/Case Year | Party Name                          | Advocate                |
   |---------------|---------------------------------|-------------------------------------|-------------------------|
   | 1             | Reg.Sum.Suit/80/2024            | Uco Bank Through Its Authorized Officer Shamik Acharee vs Narayan Jibeba Aru | Shah Ronak              |
   | 2             | Reg.Dkst/13/2024                | Lata Vithal Sonawane Vs Kisan Maruti alias Malhari | Rawade Ramkrishna Balasaheb |
   | 3             | Civil M.A./37/2024              | Rahul Ratnakar Kastu Vs No Anyone    | Gawade Shashikant Shobha|
   | 4             | Reg.Sum.Suit/99/2024            | Shweta Sudam Ghodechor Vs Sudam Ramesh Ghodechor | Gundawade Vaishali Bhauso Vs null |
   | 5             | R.C.S./24/2024                  | Dhananjay Balkrushna Pogam Alias Pungam Vs Maruti Baburao Taras | Joshi Pramod Vynkatesh  |
   | 6             | R.C.S./19/2025                  | Ramchandra Khandagale Vs Shriram Finance Ltd | Parchure Pramod Vishwas |
   | 7             | R.C.S./36/2025                  | Mr Santosh Keshavrao Mane Vs Yogesh Mangalsen Bahal | Sawant Manali Pandurang |
   | 8             | Civil M.A./21/2025              | Usha Mahendra Damle Vs Ratna Nilin Marthe | ADV SANJAY ASHOK JADHAV |

   - **How to Use**: Select "Pimpri, Civil Court" as the court complex and establishment, choose the appropriate case type (e.g., "Reg.Sum.Suit" for serial number 1), enter the case number (e.g., "80" for serial number 1), and year (e.g., "2024" for serial number 1). Add your own CAPTCHA code and submit.
   - **Try Your Own**: Replace the above with your case number, year, and relevant court complex/establishment from the form options.

## Project Structure

```
pune-court-case-search/
├── app.py                # Main Flask application
├── check_db.py           # Script to check contents of the SQLite database
├── init_db.py            # Script to initialize the SQLite database
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # HTML template for the case search form
└── queries.db            # SQLite database (created after running init_db.py)
```

## Dependencies

Listed in `requirements.txt`:
- Flask: Web framework for the application
- Playwright: For browser automation (if used)
- BeautifulSoup4: For HTML parsing
- python-dotenv: For environment variable management
- Requests: For making HTTP requests to the court server

## Database Schema

The `queries` table in `queries.db` has the following schema:

| Column         | Type     | Description                              |
|----------------|----------|------------------------------------------|
| `id`           | INTEGER  | Primary key, auto-incremented            |
| `timestamp`    | DATETIME | Timestamp of the query (auto-generated)  |
| `court_complex`| TEXT     | Court complex code                       |
| `case_type`    | TEXT     | Case type code                           |
| `case_number`  | TEXT     | Case number                              |
| `case_year`    | TEXT     | Case year                                |
| `raw_response` | TEXT     | Raw HTML/JSON response from the server   |

## Routes

- **GET/POST `/`**: Renders the main case search form (GET) and handles form submissions (POST).
- **GET `/get_case_types`**: Returns a JSON list of available case types.
- **GET `/get_captcha`**: Fetches CAPTCHA image and associated form tokens.
- **POST `/get_details`**: Retrieves detailed case information, including PDF links, based on a case identifier (CINO).

## Notes

- The application interacts with the Pune District Court's AJAX endpoints to fetch case data.
- Ensure a stable internet connection, as the application relies on external server responses.
- CAPTCHA validation is required for form submissions, as per the court's website requirements.
- The application logs all queries to the SQLite database for auditing and debugging purposes.
- PDF links for orders/judgments are extracted and appended to the case details response for easy access.

## Troubleshooting

- **Database Errors**: If `check_db.py` reports that the database or table does not exist, run `python init_db.py` to initialize it.
- **CAPTCHA Issues**: If the CAPTCHA fails to load, refresh the page or check your internet connection.
- **Server Errors**: If the court server returns errors, verify the form inputs or try again later, as the external server may be temporarily unavailable.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This application is for educational and personal use only. It interacts with the Pune District Court's public website and does not store or process sensitive personal data beyond what is necessary for case searches. Ensure compliance with all applicable laws and regulations when using this tool.
