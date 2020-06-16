from flask import Flask, jsonify, render_template
from flask_login import login_required
from .models import setup_db
from .views.user import setup_lm, user


app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config')
setup_db(app)
setup_lm(app)


# Register routes
app.register_blueprint(user)


@app.route('/')
def index():
    welcome = 'Welcome to this page!'
    return render_template('pages/home.html', welcome=welcome)


@app.route('/dashboard')
@login_required
def dashboard():
    welcome = 'Welcome to the Dashboard!'
    return render_template('pages/dashboard.html', welcome=welcome)


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'success': False,
        'error': 400,
        'message': 'Bad Request'
    }), 400


@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        'success': False,
        'error': 403,
        'message': 'Forbidden'
    }), 403


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'Not Found'
    }), 404


@app.errorhandler(422)
def unprocessable_entity(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': 'Unprocessable Entity'
    }), 422


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'Internal Server Error'
    }), 500


if __name__ == '__main__':
    app.run()
