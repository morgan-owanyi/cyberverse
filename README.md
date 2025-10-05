Cyberverse 🚀

Cyberverse is an interactive cybersecurity learning platform designed for students to learn, practice, and test their cybersecurity skills. It combines educational resources, quizzes, and real-time URL safety scanning into one cohesive platform.

🌟 Features

1.Home Page

Brief overview of the Cyberverse project.

URL scanning functionality using VirusTotal API to detect potential malicious links.

2.Modules Page

Curated external links for students to learn about cybersecurity concepts and practices.

3.Quizzes Page

Interactive quizzes with automatic scoring to test users’ knowledge.

4.Resources Page

Links to additional cybersecurity tools, tutorials, and guides.

5.Feedback Page

Users can submit feedback or suggestions; submissions are stored in the database.

6.About the Developer

Developer bio, journey in cybersecurity, technologies used, and contact information.

💻 Technologies Used

1.Python & Django – backend framework

2.Bootstrap – responsive front-end styling

3.HTML5 & CSS3 – web structure and design

4.SQLite / MySQL – database for storing feedback and quiz results

5.VirusTotal API – URL scanning functionality

6.Git & GitHub – version control and project repository

⚡ Installation & Setup

Clone the repository

git clone https://github.com/yourusername/cyberverse.git
cd cyberverse


Create a virtual environment

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux


Install dependencies

pip install -r requirements.txt


Set up environment variables

In settings.py or .env file, add:

VIRUSTOTAL_API_KEY = "YOUR_API_KEY_HERE"


Apply migrations

python manage.py makemigrations
python manage.py migrate


Create a superuser (to access Django Admin):

python manage.py createsuperuser


Run the server

python manage.py runserver


Visit http://127.0.0.1:8000/
 to see Cyberverse in action.

📂 Project Structure
cyberverse/
│
├── awareness/       # Main app
│   ├── templates/   # HTML templates
│   ├── static/      # CSS, images
│   ├── models.py    # Database models
│   ├── views.py     # View functions
│   ├── forms.py     # Forms
│   └── urls.py      # App URL routing
│
├── cyberverse/      # Project settings
│   ├── settings.py
│   └── urls.py
│
├── manage.py
└── README.md

🎯 Future Improvements

Enhanced URL scanning – detailed reports for each URL scanned.

Quiz analytics – track user progress and performance.

Admin dashboard – visualize feedback and user activity.

AI Recommendations – suggest modules and quizzes based on user performance.

📧 Contact

Morgan Owanyi
Email: owanyimorgan@gmail.com

GitHub: https://github.com/morgan-owanyi
