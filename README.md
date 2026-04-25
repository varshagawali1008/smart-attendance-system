<img width="1919" height="1067" alt="Screenshot 2026-04-21 193252" src="https://github.com/user-attachments/assets/cab1b767-1998-451e-bc03-127623e3229e" />
👩‍💻 Smart Face Attendance System
🚀 Project Overview

The Smart Face Attendance System is an intelligent attendance management system built using Django and OpenCV. It uses facial recognition technology to automatically mark attendance without any manual intervention.

The system captures faces through a webcam, recognizes the user, and records attendance in the database with date and time. This helps in reducing manual effort, saving time, and improving accuracy.

🎯 Objectives
Replace manual attendance system with automation
Improve accuracy in attendance tracking
Reduce human errors
Provide a fast and secure attendance solution
✨ Features
👤 Real-time face detection and recognition
🧠 Automatic attendance marking
📊 Attendance storage in database
🕒 Date and time tracking
🔒 Secure and reliable system
⚡ Fast processing using OpenCV
🛠️ Technologies Used
Python 🐍
Django 🌐
OpenCV (Face Detection & Recognition)
NumPy
Face Recognition Library
SQLite (Default Django Database)
HTML/CSS (Frontend templates)
🗄️ Database (SQLite)

This project uses SQLite, the default database of Django.

Key Points:
Stores user/student information
Stores attendance records with timestamp
Lightweight and easy to manage
Suitable for development projects
Can be upgraded to MySQL/PostgreSQL for production
⚙️ How It Works
User/student face images are registered
Dataset is created
Model is trained using face data
Webcam is activated
System detects and recognizes the face
If match is found, attendance is marked automatically
Data is stored in SQLite database
📂 Project Structure
Smart-Face-Attendance-System/
│
├── dataset/              # Face images dataset
├── db.sqlite3           # Database file
├── app/                  # Django application
├── templates/           # HTML templates
├── static/              # CSS/JS files
├── models.py            # Database models
├── views.py             # Backend logic
├── urls.py              # URL routing
├── train.py             # Model training script
├── recognize.py         # Face recognition script
├── manage.py            # Django project file
└── requirements.txt     # Project dependencies
📸 Screenshots
Face Recognition Output

🔧 Installation Steps
git clone https://github.com/your-username/Smart-Face-Attendance-System.git
cd Smart-Face-Attendance-System
pip install -r requirements.txt
▶️ Run Project
python manage.py runserver

Then open in browser:

http://127.0.0.1:8000/
📌 Applications
Schools 🏫
Colleges 🎓
Offices 🏢
Training institutes 👩‍🏫
🚀 Future Enhancements
AWS cloud deployment ☁️
Mobile application integration 📱
Anti-spoofing detection system
Advanced admin dashboard
Email/SMS notifications
👩‍🎓 Author

Varsha Gawali
AWS Trainee Project
Pune, Maharashtra

⭐ Conclusion

The Smart Face Attendance System provides an efficient, automated, and accurate solution for attendance management using facial recognition technology. It eliminates manual work and improves reliability.<img width="1919" height="1067" alt="Screenshot 2026-04-21 193252" src="https://github.com/user-attachments/assets/f28b157d-8b99-4ee8-9ff1-771d6beff35c" />
