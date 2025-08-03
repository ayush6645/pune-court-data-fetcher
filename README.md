# 🏛️ Court Data Fetcher

A user-friendly web interface for retrieving court case details from Pune District Court. This tool allows users to search for case information using various parameters such as court type, case number, year, and more. It also includes CAPTCHA verification and dynamic UI components for an improved user experience.

---

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- Select between **Court Complex** or **Court Establishment**
- Dynamically load court and case types
- CAPTCHA image loading and refresh
- Responsive form with validation
- Modal for displaying detailed case information
- Stylish and modern UI with CSS enhancements
- Fully client-side interactive form behavior

---

## 🛠️ Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/court-data-fetcher.git
    cd court-data-fetcher
    ```

2. Place the `index.html` in your web server directory (e.g., `public_html/` or any backend-integrated server route).

3. Ensure you have backend endpoints for:
   - `/get_case_types`
   - `/get_captcha`
   - `/get_details`
   - `/` (to receive POST form data)

---

## 🚀 Usage

1. Open the `index.html` in a browser or deploy it on a server.
2. Choose between **Court Complex** or **Court Establishment**.
3. Select the appropriate options from the dropdown menus.
4. Fill in the case number and year.
5. Enter the CAPTCHA and click **Search**.
6. Case results will appear below the form. Click on a case to view more details in a modal.

---

## ⚙️ Configuration

- The CAPTCHA and dynamic dropdowns depend on backend APIs (`/get_captcha`, `/get_case_types`, etc.)
- Ensure CORS is enabled if the frontend and backend are on different domains.
- Tokens and hidden fields (`scid`, `tok_`) are handled dynamically via JavaScript.

---

## 📦 Dependencies

- Pure HTML, CSS, and Vanilla JavaScript
- Requires server-side endpoints for dynamic functionalities

---

## 🧪 Examples

- **Court Complex**: Select *Pune, Civil and Criminal Court*
- **Case Number**: `1234`
- **Year**: `2023`
- CAPTCHA will be dynamically fetched and validated.

---

## 🛠️ Troubleshooting

| Problem                             | Solution                                                       |
|-------------------------------------|----------------------------------------------------------------|
| CAPTCHA not loading                 | Ensure backend `/get_captcha` endpoint is functioning.         |
| Dropdowns not populating case types| Backend `/get_case_types` should return a valid JSON array.    |
| Modal not showing case details     | Confirm `/get_details` returns proper HTML content.            |

---

## 👨‍💻 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or additional features.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

