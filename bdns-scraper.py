import argparse
import fitz  # PyMuPDF
import re
import os
import sys

def scrape_bdns_assets(pdf_path):
    """
    Scrapes a PDF file for BDNS-compliant asset names.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        list: A list of unique BDNS-compliant asset names found in the PDF.
    """
    # A general regex pattern for BDNS names. This can be refined based on specific BDNS rules.
    # It looks for a sequence like: <uppercase_letters>-<alphanumeric_chars>-<digits>-<alphanumeric_chars>
    bdns_pattern = r'\b[A-Z]{2,}-\w+-\d{2,}-\w{2,}\b'
    
    found_assets = set()
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text = page.get_text()
                # Find all matches in the page text
                matches = re.findall(bdns_pattern, text)
                for match in matches:
                    found_assets.add(match)
    except FileNotFoundError:
        print(f"Error: The file '{pdf_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while processing the PDF: {e}")
        sys.exit(1)

    return sorted(list(found_assets))

def main():
    """
    Main function to handle command-line arguments and run the scraper.
    """
    parser = argparse.ArgumentParser(
        description="Scrape a PDF for BDNS-compliant asset names."
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="The path to the input PDF file."
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="bdns_assets.txt",
        help="The path to the output text file. Defaults to bdns_assets.txt."
    )

    args = parser.parse_args()
    input_pdf = args.input_file
    output_file = args.output

    # Check if the input file exists
    if not os.path.exists(input_pdf):
        print(f"Error: The input file '{input_pdf}' does not exist.")
        sys.exit(1)

    print(f"Scraping BDNS asset names from '{input_pdf}'...")
    assets = scrape_bdns_assets(input_pdf)
    
    if not assets:
        print("No BDNS-compliant assets were found.")
        sys.exit(0)

    print(f"Found {len(assets)} unique BDNS-compliant assets. Writing to '{output_file}'...")
    try:
        with open(output_file, "w") as f:
            for asset in assets:
                f.write(f"{asset}\n")
        print("Done!")
    except Exception as e:
        print(f"Error writing to output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
