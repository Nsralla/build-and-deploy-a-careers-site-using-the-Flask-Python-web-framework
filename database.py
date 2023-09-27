from sqlalchemy import create_engine
from sqlalchemy import text

# we need to connect to the database

# we need to create engine to connect with database

# Replace these placeholders with your MySQL database credentials
username = 'root'
password = 'jj137157177jj'
hostname = '127.0.0.1'
port = '3306'  # Default MySQL port is 3306
database_name = 'careers'

# Create the SQLAlchemy engine
db_url = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database_name}"
engine = create_engine(db_url)


def load_jobs_from_db():  # load jobs from database
    # get info out of the database
    with engine.connect() as conn:
        result = conn.execute(text(" select * from jobs "))
        # print data got from the database
    load_jobs = []
    for row in result:
        job_data = {
            'id': row.id,
            'title': row.title,
            'location': row.location,
            'salary': row.salary,
            'currency': row.currency,
            'responsibilities': row.responsibilities,
            'requirements': row.requirements
        }
        load_jobs.append(job_data)
    return load_jobs


def load_job_from_db(job_id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM JOBS WHERE id = :job_id"), [{"job_id": job_id}])
    rows = result.all()
    if len(rows) == 0:
        return None
    else:
        return rows[0]


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, "
                     "resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, "
                     ":resume_url)")
        conn.execute(query, {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],
            'resume_url': data['resume_url']
        })
        conn.commit()

