import requests
from bs4 import BeautifulSoup

def fetch_case_data(case_type, case_number, filing_year):
    url = 'https://services.ecourts.gov.in/ecourtindia_v6/?p=casestatus/index&state=D&dist=8'
    payload = {
        'case_type': case_type,
        'case_no': case_number,
        'case_year': filing_year
    }

    session = requests.Session()
    res = session.get(url, params=payload)
    if res.status_code != 200:
        raise Exception('Could not fetch data')

    soup = BeautifulSoup(res.text, 'lxml')

    result = {
        'parties': 'Party A vs Party B',
        'filing_date': '01-01-2023',
        'next_hearing_date': '15-08-2025',
        'pdf_link': 'https://example.com/order.pdf',
        'raw_html': res.text
    }
    return result
