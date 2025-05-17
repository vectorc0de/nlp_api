from flask import *  
from invoice import extract_invoice_info
from flask_cors import CORS
import os

app = Flask(__name__)   
CORS(app)

@app.route('/')   
def main():   
    return render_template("index.html")   

@app.route('/upload_invoice', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)
        
        invoice_info = extract_invoice_info(f.filename)

        # delete file
        os.remove(f.filename)

        print(invoice_info)
        
        return invoice_info

if __name__ == '__main__':   
    app.run(debug=True, port=6969)