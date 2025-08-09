from flask import Flask, render_template, request
from scraper import fetch_case_data
from models import init_db, log_query

app = Flask(__name__)
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']
        try:
            result = fetch_case_data(case_type, case_number, filing_year)
            log_query(case_type, case_number, filing_year, result['raw_html'])
        except Exception as e:
            error = str(e)
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
