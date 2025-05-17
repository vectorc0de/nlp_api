# 🧾 Invoice Extractor Flask App 🧾

A simple Flask application to extract information from invoice PDFs. It can currently identify the total amount and the description of the items.

## ✨ Features ✨

* **PDF Parsing:** Reads and extracts text from PDF invoice files.
* **Total Amount Extraction:** Identifies and extracts the total amount from the invoice.
* **Description Extraction:** Captures the description of the items listed in the invoice.
* **Simple Flask API:** Provides an easy-to-use API endpoint to upload and process invoices.

## 🚀 Getting Started 🚀

### Prerequisites

* Python 3.x
* pip (Python package installer)

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/vectorc0de/nlp_api
    cd nlp_api
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  Set the Flask environment (if needed):
    ```bash
    export FLASK_APP=your_app_file.py  # Replace your_app_file.py
    # export FLASK_ENV=development      # Optional: for development mode
    ```

2.  Run the Flask development server:
    ```bash
    flask run
    ```

    Or, if you have `app.py` as your main file:
    ```bash
    python app.py
    ```

3.  The application will be accessible at `http://127.0.0.1:5000/` (or the port specified by Flask).

## 🛠️ Usage 🛠️

You can interact with the application by sending a POST request to the `/extract_info` endpoint with a PDF file.

**Example using `curl`:**

```bash
curl -X POST -F "pdf_file=@/path/to/your/invoice.pdf" [http://127.0.0.1:5000/extract_info](http://127.0.0.1:5000/extract_info)