from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Campus

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/')
def index():
    return render_template('base.html')

@main_bp.route('/campus', methods=['GET', 'POST'])
def manage_campus():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        estado = request.form['estado']
        new_campus = Campus(descripcion=descripcion, estado=estado)
        db.session.add(new_campus)
        db.session.commit()
        return redirect(url_for('main.manage_campus'))
    campus_list = Campus.query.all()
    return render_template('manage_campus.html', campus_list=campus_list)



