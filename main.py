from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

# Flask is class
# flask is module

app = Flask(__name__)  # make an object from Flask class


# __name__ = __main

# now we have created flask application


# now we need to build route


@app.route('/')  # after the domain name, when the / url access, show Hello world
def home_page():
    JOBS = load_jobs_from_db()
    return render_template('home.html', jobs=JOBS, company_name='Nsr')


@app.route('/api/jobs')
def list_jobs():
    JOBS = load_jobs_from_db()
    return jsonify(JOBS)


@app.route('/job/<id>')
def show_job(id):
    job = load_job_from_db(id)
    if job is None:
        # Handle the case where the job was not found in the database
        return "error not found", 404
    else:
        # Convert the Row object to a dictionary and return as JSON
        job_dict = job._asdict()
        return render_template('job_page.html', job_dict=job_dict)


@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id):
    data = request.form
    add_application_to_db(id, data)
    return render_template('application_submitted.html', application=data)


if __name__ == '__main__':  # this is the case to run the website
    app.run(host='0.0.0.0', debug=True)  # to run the website locally
