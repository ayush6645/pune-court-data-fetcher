# Pune Court Case Data Fetcher

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://github.com/YourGitHubUsername/pune_court_data_fetcher">
    <!-- Add a logo here if you have one -->
    <!-- <img src="path/to/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

  <h3 align="center">Pune Court Case Data Fetcher</h3>

  <p align="center">
    A web application to easily search for and retrieve case data from the Pune District Court e-courts portal.
    <br />
    <a href="https://github.com/YourGitHubUsername/pune_court_data_fetcher"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="#">View Demo</a>
    · -->
    <a href="https://github.com/YourGitHubUsername/pune_court_data_fetcher/issues">Report Bug</a>
    ·
    <a href="https://github.com/YourGitHubUsername/pune_court_data_fetcher/issues">Request Feature</a>
  </p>
</div>

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

---

## About The Project

This project provides a simple and efficient web interface to search for case information from the Pune District Court's public portal. It streamlines the process of accessing case data by offering a clean form that interacts with the e-courts backend services.

Users can quickly find case summaries and dive into detailed views, including case history and orders, without needing to navigate the complexities of the official website directly.

### Features

*   **Flexible Search**: Search by either **Court Complex** or **Court Establishment**.
*   **Dynamic Case Types**: The "Case Type" dropdown is automatically populated with the correct options based on your court selection.
*   **Specific Queries**: Find cases using their unique **Case Number** and **Registration Year**.
*   **CAPTCHA Handling**: Integrates with the e-courts CAPTCHA system, including a refresh button for new challenges.
*   **Detailed Modal View**: Click on any case in the search results to view comprehensive details in a clean pop-up, including:
    *   Case Status and Filing Information
    *   Petitioner and Respondent details
    *   Associated Acts and FIR information
    *   Complete Case History and Orders
    *   Direct links to downloadable order PDFs (when available).

### Built With

This project is built with a combination of a Python backend and a vanilla JavaScript frontend.

*   **Backend**: Python (likely with a web framework like Flask or FastAPI)
*   **Frontend**: HTML, CSS, JavaScript

---

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

You will need Python 3 and `pip` installed on your system.

*   Python 3
    ```sh
    # Check if python is installed
    python --version
    ```

### Installation

1.  Clone the repo
    ```sh
    git clone https://github.com/YourGitHubUsername/pune_court_data_fetcher.git
    ```
2.  Navigate to the project directory
    ```sh
    cd pune_court_data_fetcher
    ```
3.  Create and activate a virtual environment (recommended)
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  Install Python packages (assuming a `requirements.txt` file exists)
    ```sh
    pip install -r requirements.txt
    ```
5.  Run the application (assuming the main file is `app.py`)
    ```sh
    python app.py
    ```
6.  Open your browser and navigate to `http://127.0.0.1:5000` (or the port specified in your app).

---

## Usage

1.  Open the web page in your browser.
2.  Select whether you want to search by "Court Complex" or "Court Establishment".
3.  Choose the specific court from the dropdown menu.
4.  Select the appropriate "Case Type" that loads dynamically.
5.  Enter the "Case Number" and "Year".
6.  Enter the characters you see in the CAPTCHA image. Use the "Refresh CAPTCHA" button if it's unclear.
7.  Click "Search".
8.  The results will appear below the form. Click the "View" link on any case to see its full details in a pop-up window.

---

## Roadmap

See the open issues for a full list of proposed features (and known issues).

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

---

## Contact

Your Name - @YourTwitter - email@example.com

Project Link: https://github.com/YourGitHubUsername/pune_court_data_fetcher

---

## Acknowledgments

*   Data is sourced from the official e-Courts Services portal.
*   Shields.io for the badges.

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/YourGitHubUsername/pune_court_data_fetcher.svg?style=for-the-badge
[contributors-url]: https://github.com/YourGitHubUsername/pune_court_data_fetcher/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/YourGitHubUsername/pune_court_data_fetcher.svg?style=for-the-badge
[forks-url]: https://github.com/YourGitHubUsername/pune_court_data_fetcher/network/members
[stars-shield]: https://img.shields.io/github/stars/YourGitHubUsername/pune_court_data_fetcher.svg?style=for-the-badge
[stars-url]: https://github.com/YourGitHubUsername/pune_court_data_fetcher/stargazers
[issues-shield]: https://img.shields.io/github/issues/YourGitHubUsername/pune_court_data_fetcher.svg?style=for-the-badge
[issues-url]: https://github.com/YourGitHubUsername/pune_court_data_fetcher/issues
[license-shield]: https://img.shields.io/github/license/YourGitHubUsername/pune_court_data_fetcher.svg?style=for-the-badge
[license-url]: https://github.com/YourGitHubUsername/pune_court_data_fetcher/blob/main/LICENSE.txt
