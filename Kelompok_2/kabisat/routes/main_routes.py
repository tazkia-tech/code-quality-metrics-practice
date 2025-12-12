# kabisat/routes.py

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .services.leap_year_logic import is_leap

# Definisikan Blueprint
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    tahun = None
    is_kabisat = None
    error_msg = None

    if request.method == 'POST':
        tahun_input = request.form.get('year_input')
        
        try:
            tahun = int(tahun_input)
            
            if tahun <= 0:
                error_msg = "Tahun harus berupa angka positif."
            else:
                is_kabisat = is_leap(tahun)
                
        except ValueError:
            error_msg = f"Input '{tahun_input}' bukan angka tahun yang valid."
        
    return render_template(
        'index.html', 
        tahun=tahun, 
        is_kabisat=is_kabisat, 
        error_msg=error_msg
    )