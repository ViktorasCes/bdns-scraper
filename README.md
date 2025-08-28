# BDNS Asset Name Scraper

A simple command-line Python utility to scrape BDNS (Broad-spectrum Digital Naming System) compliant asset names from PDF documents. It finds matching names, extracts them, and saves the unique, sorted list to a text file.

---

## Features

-   **PDF Scraping**: Extracts text from any page of a given PDF file.
-   **Regex Matching**: Uses a pattern to identify BDNS-compliant asset names.
-   **Unique & Sorted Output**: Gathers all found asset names, removes duplicates, sorts them, and saves them to a `.txt` file.
-   **CLI Interface**: It's easy to use from the terminal with simple arguments for input and output files.

---

## Requirements

-   **Python 3.x**
-   **PyMuPDF**

---

## Installation & Setup

Follow these steps to get the scraper running in a virtual environment.

1.  **Set up a Virtual Environment**

    It's highly recommended to use a virtual environment to manage dependencies.

    ```bash
    # Create the virtual environment
    python3 -m venv venv

    # Activate it
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    # venv\Scripts\activate
    ```

2.  **Install Dependencies**

    With the virtual environment activated, install the required packages.

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

You run the script from the command line. You **must** provide the path to the input PDF file. You can also specify an optional output file path.

### Basic Usage

This command will scrape the specified PDF and save the results to the default `bdns_assets.txt` file.

```bash
python3 scraper.py /path/to/your/document.pdf -o /path/to/custom_output.txt

