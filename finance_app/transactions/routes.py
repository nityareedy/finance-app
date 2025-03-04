from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import bp
from ..models import Transaction
from .. import db

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_transaction():
    if request.method == 'POST':
        transaction = Transaction(
            amount=float(request.form['amount']),
            description=request.form['description'],
            category=request.form['category'],
            type=request.form['type'],
            user_id=current_user.id
        )
        db.session.add(transaction)
        db.session.commit()
        flash('Transaction added successfully!')
        return redirect(url_for('main.index'))
    return render_template('transactions/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    if transaction.user_id != current_user.id:
        flash('You cannot edit this transaction.')
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        transaction.amount = float(request.form['amount'])
        transaction.description = request.form['description']
        transaction.category = request.form['category']
        transaction.type = request.form['type']
        db.session.commit()
        flash('Transaction updated successfully!')
        return redirect(url_for('main.index'))
    return render_template('transactions/edit.html', transaction=transaction)

@bp.route('/delete/<int:id>')
@login_required
def delete_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    if transaction.user_id != current_user.id:
        flash('You cannot delete this transaction.')
        return redirect(url_for('main.index'))
    
    db.session.delete(transaction)
    db.session.commit()
    flash('Transaction deleted successfully!')
    return redirect(url_for('main.index')) 