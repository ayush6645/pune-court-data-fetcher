from flask import Flask, request, render_template, jsonify
import requests
import os
from bs4 import BeautifulSoup
import json
import sqlite3

app = Flask(__name__)

# Pune district court AJAX URL for fetching cases
AJAX_URL = "https://pune.dcourts.gov.in/wp-admin/admin-ajax.php"

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles the main page display (GET) and the case search submission (POST).
    This function also logs the query and response to the SQLite database.
    """
    if request.method == 'POST':
        # --- 1. GATHER FORM DATA ---
        data = request.form
        est_code = data.get('est_code')
        case_type = data.get('case_type')
        reg_no = data.get('reg_no')
        reg_year = data.get('reg_year')

        # --- 2. PREPARE AND SEND REQUEST TO COURT SERVER ---
        try:
            # Prepare the data payload for the court's server
            token_key = next((key for key in data if key.startswith("tok_")), None)
            post_data = {
                "service_type": data.get('service_type'),
                "est_code": est_code,
                "case_type": case_type,
                "reg_no": reg_no,
                "reg_year": reg_year,
                "siwp_captcha_value": data.get('siwp_captcha_value'),
                "scid": data.get('scid'),
                "es_ajax_request": "1",
                "submit": "Search",
                "action": "get_cases",
                token_key: data.get(token_key)
            }
            headers = {
                "User-Agent": "Mozilla/5.0 (compatible; CourtDataFetcher/1.0)",
                "Referer": "https://pune.dcourts.gov.in/case-status-search-by-case-number/"
            }

            # Make the request
            resp = requests.post(AJAX_URL, data=post_data, headers=headers)
            resp.raise_for_status()

            # --- 3. LOG THE QUERY AND RESPONSE TO THE DATABASE ---
            try:
                conn = sqlite3.connect('queries.db')
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO queries (court_complex, case_type, case_number, case_year, raw_response) VALUES (?, ?, ?, ?, ?)",
                    (est_code, case_type, reg_no, reg_year, resp.text)
                )
                conn.commit()
                conn.close()
            except Exception as db_error:
                # If logging fails, print the error to the console but don't crash the app
                print(f"Database logging failed: {db_error}")

            # --- 4. PROCESS AND RETURN THE RESPONSE TO THE BROWSER ---
            response_json = resp.json()
            if response_json.get('success') and response_json.get('data'):
                return response_json['data']
            else:
                # Return the error message provided by the court's site
                return response_json.get('data', '<div class="alert alert-warning">No records found.</div>')

        except requests.RequestException as e:
            return f'<div class="alert alert-danger">Failed to connect to court server: {e}</div>'
        except json.JSONDecodeError:
            return '<div class="alert alert-danger">Received an invalid response from the court server.</div>'

    # For a GET request, just render the main page
    return render_template('index.html')

@app.route('/get_case_types')
def get_case_types():
    case_types = [
        {"code": "46", "name": "AC Cri.M.A."}, {"code": "35", "name": "Arbitration Case"},
        {"code": "73", "name": "Arbitration R.D"}, {"code": "24", "name": "Atro.Spl.Case"},
        {"code": "72", "name": "B.G.P.E.Act Case"}, {"code": "11", "name": "C.Appln."},
        {"code": "32", "name": "Chapter Case"}, {"code": "86", "name": "Civil Appeal PPE"},
        {"code": "3", "name": "Civil M.A."}, {"code": "4", "name": "Civil Revn."},
        {"code": "5", "name": "Civil Suit"}, {"code": "102", "name": "Commercial Appeal"},
        {"code": "101", "name": "Commercial Suit"}, {"code": "69", "name": "Contempt Proceeding"},
        {"code": "17", "name": "Cri.Appeal"}, {"code": "36", "name": "Cri.Bail Appln."},
        {"code": "31", "name": "Cri.Case"}, {"code": "19", "name": "Cri.M.A."},
        {"code": "92", "name": "Cri.Municipal Appeal"}, {"code": "18", "name": "Cri.Rev.App."},
        {"code": "8", "name": "Darkhast"}, {"code": "58", "name": "Distress Warrant"},
        {"code": "25", "name": "E.C.Act.Spl.Case"}, {"code": "10", "name": "Elec.Petn."},
        {"code": "85", "name": "Election Appeal"}, {"code": "77", "name": "E.S.I.Act Case"},
        {"code": "63", "name": "Final Decree"}, {"code": "68", "name": "Guardian  Wards Case"},
        {"code": "26", "name": "I.C.M.A."}, {"code": "65", "name": "Insolvency"},
        {"code": "67", "name": "Juvenile"}, {"code": "90", "name": "Juvenile Cri.MA"},
        {"code": "7", "name": "L.A.R."}, {"code": "9", "name": "L.R.DKST."},
        {"code": "33", "name": "L.R.M.A."}, {"code": "12", "name": "M.A.C.P."},
        {"code": "41", "name": "MACP C Appln."}, {"code": "14", "name": "MACP. Dkst."},
        {"code": "13", "name": "MACP. M.A."}, {"code": "88", "name": "MACP M.A.N.R.J.I."},
        {"code": "49", "name": "MACP Spl."}, {"code": "42", "name": "MAHA P.I.D. 1999."},
        {"code": "52", "name": "M.A.N.R.J.I."}, {"code": "6", "name": "Marriage Petn."},
        {"code": "2", "name": "M.C.A."}, {"code": "39", "name": "MCOCO1999"},
        {"code": "40", "name": "MCOCO.Revn."}, {"code": "61", "name": "Mesne Profit"},
        {"code": "60", "name": "M.J.Cases"}, {"code": "44", "name": "MOCCA M.A."},
        {"code": "38", "name": "MPID M.A."}, {"code": "50", "name": "MPID M.A. Others"},
        {"code": "89", "name": "MSEB MA"}, {"code": "28", "name": "Munci. Appeal"},
        {"code": "45", "name": "NDPS Cri.Revn."}, {"code": "43", "name": "NDPS M.A.."},
        {"code": "22", "name": "NDPS. S. Case"}, {"code": "84", "name": "Other Misc.Appln."},
        {"code": "81", "name": "Other Misc.Cri.Appln"}, {"code": "71", "name": "Pauper Appln."},
        {"code": "80", "name": "P.C.M.Appln."}, {"code": "66", "name": "Probate"},
        {"code": "95", "name": "PWDVA Appeal"}, {"code": "97", "name": "PWDVA Appln."},
        {"code": "98", "name": "PWDVA Execution"}, {"code": "96", "name": "PWDVA Revi."},
        {"code": "1", "name": "R.C.A."}, {"code": "30", "name": "R.C.C."},
        {"code": "27", "name": "R.C.S."}, {"code": "47", "name": "Reg Dkst"},
        {"code": "83", "name": "Reg.Sum.Suit"}, {"code": "51", "name": "Rent Appeal"},
        {"code": "55", "name": "Rent Suit"}, {"code": "70", "name": "Review Appln."},
        {"code": "34", "name": "S.C.C."}, {"code": "15", "name": "Sessions Case"},
        {"code": "64", "name": "Small Cause Dkst"}, {"code": "54", "name": "Small Cause Suit"},
        {"code": "16", "name": "Spl.Case"}, {"code": "23", "name": "Spl.Case ACB"},
        {"code": "99", "name": "Spl.Case ATS"}, {"code": "93", "name": "Spl.Case Child Prot."},
        {"code": "100", "name": "Spl. Case Drug Cosm."}, {"code": "53", "name": "Spl Case MSEB"},
        {"code": "37", "name": "Spl.Cri.M.A."}, {"code": "29", "name": "Spl.C.S."},
        {"code": "48", "name": "Spl .Dkst"}, {"code": "94", "name": "Spl.M.A. Child Prot."},
        {"code": "74", "name": "Spl. Marriage Petn."}, {"code": "82", "name": "Spl.Sum.Suit"},
        {"code": "87", "name": "Std. Rent Appln."}, {"code": "62", "name": "Succession"},
        {"code": "79", "name": "Suit Indian Divorce Act"}, {"code": "78", "name": "Suit Trade Mark Act"},
        {"code": "59", "name": "Sum.Civ.Suit"}, {"code": "91", "name": "Sum. Darkhast"},
        {"code": "20", "name": "TADA S. C."}, {"code": "21", "name": "T.Cri.M.A."},
        {"code": "56", "name": "Trust Appeal"}, {"code": "57", "name": "Trust Suit"},
        {"code": "75", "name": "W.C.F.A.Case"}, {"code": "76", "name": "W.C.N.F.A. Case"}
    ]
    return jsonify({"case_types": case_types})

@app.route('/get_captcha')
def get_captcha():
    try:
        url = "https://pune.dcourts.gov.in/case-status-search-by-case-number/"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch CAPTCHA page"}), 500

        soup = BeautifulSoup(response.text, 'html.parser')

        captcha_img = soup.find('img', {'id': 'siwp_captcha_image_0'})
        captcha_url = captcha_img['src'] if captcha_img else ''
        if captcha_url.startswith("/"):
            captcha_url = f"https://pune.dcourts.gov.in{captcha_url}"

        scid_input = soup.find('input', {'name': 'scid'})
        scid = scid_input['value'] if scid_input else ''

        token_name, token_value = '', ''
        token_input = soup.find('input', {'name': lambda x: x and x.startswith('tok_')})
        if token_input:
            token_name = token_input['name']
            token_value = token_input['value']

        if not all([captcha_url, scid, token_name, token_value]):
            return jsonify({"error": "Failed to extract CAPTCHA fields"}), 500

        return jsonify({
            "captcha_url": captcha_url,
            "scid": scid,
            "token_name": token_name,
            "token_value": token_value
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- THIS IS THE NEW ROUTE ---
@app.route('/get_details', methods=['POST'])
def get_details():
    cino = request.form.get('cino')
    if not cino:
        return "<h3>Error: CINO identifier was not provided.</h3>", 400

    details_ajax_url = "https://pune.dcourts.gov.in/wp-admin/admin-ajax.php"
    post_data = { 'action': 'get_cnr_details', 'cino': cino, 'es_ajax_request': '1' }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://pune.dcourts.gov.in/case-status-search-by-case-number/",
        "X-Requested-With": "XMLHttpRequest"
    }

    try:
        resp = requests.post(details_ajax_url, data=post_data, headers=headers)
        resp.raise_for_status()
        response_json = resp.json()

        if response_json.get('success') and response_json.get('data'):
            html_content = response_json['data']
            
            # --- NEW PDF PARSING LOGIC ---
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find all anchor tags that link to a PDF
            pdf_links = soup.find_all('a', href=lambda href: href and '.pdf' in href)
            
            if pdf_links:
                # Create a new section for the PDF links
                orders_html = "<h3>Orders / Judgments</h3><ul>"
                for link in pdf_links:
                    # Get the link URL and the text
                    url = link['href']
                    text = link.get_text(strip=True) or "Download PDF"
                    orders_html += f'<li><a href="{url}" target="_blank">{text}</a></li>'
                orders_html += "</ul>"
                
                # Append the new section to the original HTML
                html_content += orders_html

            return html_content
        else:
            return "<div>Could not find case details in the server response.</div>"
            
    except requests.RequestException as e:
        return f"<h3>Error</h3><p>Failed to fetch case details: {e}</p>", 502
    except json.JSONDecodeError:
        return "<h3>Error</h3><p>Received an invalid response from the court server.</p>", 500

if __name__ == "__main__":
    app.run(debug=True)