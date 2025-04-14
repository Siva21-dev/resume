import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            # Get form data safely
            name = request.form.get('name', '')
            title = request.form.get('title', '')
            email = request.form.get('email', '')
            phone = request.form.get('phone', '')
            address = request.form.get('address', '')
            description = request.form.get('description', '')
            skills = request.form.get('skills', '')
            education = request.form.get('education', '')
            experience = request.form.get('experience', '')

            # Handle file upload
            photo = request.files.get('photo')
            photo_filename = ''
            if photo and photo.filename != '':
                photo_filename = secure_filename(photo.filename)
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))

            # Render final portfolio
            return render_template('portfolio.html',
                name=name, title=title, email=email, phone=phone, address=address,
                description=description, skills=skills, education=education,
                experience=experience, photo_filename=photo_filename
            )

        except Exception as e:
            return f"Something went wrong: {e}"

    return render_template('form.html')

if __name__ == '__main__':
    app.run()
