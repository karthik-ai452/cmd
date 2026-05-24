"""
CmdRunner Website — Main Server
Operated by BotifyQA Solutions Private Limited
"""

import os
import logging
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

logging.basicConfig(level=logging.INFO)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json(silent=True) or {}
    name = (data.get('name') or '').strip()
    email = (data.get('email') or '').strip()
    role = (data.get('role') or '').strip()
    usecase = (data.get('usecase') or '').strip()

    errors = {}
    if not name:
        errors['name'] = 'Name is required.'
    if not email or '@' not in email:
        errors['email'] = 'A valid work email is required.'
    if not role:
        errors['role'] = 'Please select your role.'
    if not usecase:
        errors['usecase'] = 'Please describe what CmdRunner should test.'

    if errors:
        return jsonify({'ok': False, 'errors': errors}), 400

    app.logger.info('Beta registration: name=%s email=%s role=%s usecase=%s', name, email, role, usecase[:80])

    return jsonify({'ok': True, 'message': "Thanks! We'll be in touch soon."})


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/privacy')
def privacy():
    return redirect('/terms#privacy-policy', code=301)


@app.route('/refund')
def refund():
    return redirect('/terms#refund', code=301)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))