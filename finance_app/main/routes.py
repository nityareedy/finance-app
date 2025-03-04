from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from . import bp
from ..models import Transaction
from sqlalchemy import func

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    # Get summary statistics
    total_income = Transaction.query.filter_by(
        user_id=current_user.id, 
        type='income'
    ).with_entities(func.sum(Transaction.amount)).scalar() or 0

    total_expenses = Transaction.query.filter_by(
        user_id=current_user.id, 
        type='expense'
    ).with_entities(func.sum(Transaction.amount)).scalar() or 0

    recent_transactions = Transaction.query.filter_by(
        user_id=current_user.id
    ).order_by(Transaction.date.desc()).limit(5).all()

    return render_template('main/index.html',
                         total_income=total_income,
                         total_expenses=total_expenses,
                         recent_transactions=recent_transactions) 