@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404