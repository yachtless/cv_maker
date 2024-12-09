from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate_cv', methods=['POST'])
def generate_cv():
    # Personal Information
    personal_info = {
        'full_name': request.form['full_name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'location': request.form['location']
    }
    
    # Work Experience (multiple entries)
    work_experiences = []
    for i in range(len(request.form.getlist('company[]'))):
        experience = {
            'company': request.form.getlist('company[]')[i],
            'position': request.form.getlist('position[]')[i],
            'start_date': request.form.getlist('work_start_date[]')[i],
            'end_date': request.form.getlist('work_end_date[]')[i],
            'description': request.form.getlist('work_description[]')[i]
        }
        work_experiences.append(experience)
    
    # Education (multiple entries)
    education = []
    for i in range(len(request.form.getlist('institution[]'))):
        edu = {
            'institution': request.form.getlist('institution[]')[i],
            'degree': request.form.getlist('degree[]')[i],
            'start_date': request.form.getlist('edu_start_date[]')[i],
            'end_date': request.form.getlist('edu_end_date[]')[i],
            'description': request.form.getlist('edu_description[]')[i]
        }
        education.append(edu)
    
    # Skills (as a list)
    skills = request.form['skills'].split(',')

    # About Me section
    about_me = request.form['about_me']

    # Languages (multiple entries)
    languages = []
    for i in range(len(request.form.getlist('language[]'))):
        lang = {
            'name': request.form.getlist('language[]')[i],
            'proficiency': request.form.getlist('proficiency[]')[i]
        }
        languages.append(lang)

    # References (multiple entries)
    references = []
    for i in range(len(request.form.getlist('ref_name[]'))):
        reference = {
            'name': request.form.getlist('ref_name[]')[i],
            'position': request.form.getlist('ref_position[]')[i],
            'company': request.form.getlist('ref_company[]')[i],
            'email': request.form.getlist('ref_email[]')[i],
            'phone': request.form.getlist('ref_phone[]')[i]
        }
        references.append(reference)

    return render_template('cv_template.html',
                           personal_info=personal_info,
                           about_me=about_me,
                           work_experiences=work_experiences,
                           education=education,
                           skills=skills,
                           languages=languages,
                           references=references)

if __name__ == '__main__':
    app.run(debug=True)