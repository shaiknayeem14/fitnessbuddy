# 🏋️ Fitness Buddy

## AI-Powered Personal Fitness Coach using IBM Granite

### Project Overview

Fitness Buddy is an AI-powered virtual fitness coach designed to help users maintain a healthy lifestyle through personalized workout recommendations, nutrition guidance, motivational support, and habit-building assistance.

The application uses IBM Granite Models to generate intelligent fitness suggestions based on user goals and preferences. It provides an easy-to-use web interface where users can track their fitness journey and receive personalized recommendations.

---

## Problem Statement

Many individuals struggle to maintain a healthy lifestyle due to:

* Lack of personalized fitness guidance
* Busy schedules and time constraints
* Inconsistent motivation
* Limited access to professional trainers
* Difficulty maintaining healthy habits

Fitness Buddy addresses these challenges by providing an accessible AI-powered fitness assistant available anytime.

---

## Objectives

The system aims to:

* Recommend personalized home workout routines
* Provide healthy meal suggestions
* Deliver motivational fitness guidance
* Encourage positive lifestyle habits
* Calculate and monitor BMI
* Track fitness progress
* Offer goal-based fitness recommendations

---

## Features

### User Authentication

* User Registration
* Secure Login
* Session Management

### Fitness Dashboard

* User Profile Information
* Goal Tracking
* Health Overview

### BMI Calculator

* Calculate Body Mass Index
* Instant BMI Results

### Workout Recommendation System

* Weight Loss Plans
* Muscle Gain Plans
* General Fitness Plans

### Nutrition Guidance

* Healthy Meal Suggestions
* Balanced Diet Recommendations

### Motivation Engine

* Daily Fitness Quotes
* Consistency Reminders

### Responsive UI

* Modern Glassmorphism Design
* Animated Dashboard
* Mobile-Friendly Interface

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask Framework

### Database

* SQLite

### AI Integration

* IBM Granite Models
* IBM watsonx.ai

### Deployment

* IBM Cloud Lite

---

## Project Structure

```text
FitnessBuddy/
│
├── app.py
├── config.py
├── database.db
├── requirements.txt
│
├── models/
│   └── user.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│
└── README.md
```

---

## Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/FitnessBuddy.git
```

### Step 2: Navigate to Project

```bash
cd FitnessBuddy
```

### Step 3: Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run Application

```bash
python app.py
```

### Step 6: Open Browser

```text
http://127.0.0.1:5000
```

---

## IBM Granite Integration

Fitness Buddy uses IBM Granite Models through IBM watsonx.ai to generate:

* Personalized workout plans
* Healthy meal suggestions
* Motivational fitness advice
* Lifestyle improvement recommendations

### Required Configuration

Update the following values in `config.py`:

```python
IBM_API_KEY = "YOUR_API_KEY"
IBM_PROJECT_ID = "YOUR_PROJECT_ID"
IBM_URL = "https://us-south.ml.cloud.ibm.com"
```

---

## Future Enhancements

* Water Intake Tracker
* Step Counter Integration
* Smartwatch Connectivity
* Voice-Based Fitness Assistant
* AI Meal Image Recognition
* Personalized Fitness Analytics
* Exercise Demonstration Videos
* Multi-Language Support

---

## Role of Agentic AI

Fitness Buddy leverages Agentic AI principles to act as an intelligent virtual fitness coach.

The AI can:

* Understand user goals
* Generate personalized fitness plans
* Adapt recommendations based on user needs
* Provide proactive guidance
* Encourage long-term healthy habits

This creates a more interactive and personalized fitness experience than traditional static fitness applications.

---

## Expected Outcomes

* Improved user fitness awareness
* Better workout consistency
* Healthier eating habits
* Increased motivation
* Personalized fitness guidance
* Enhanced overall well-being

---

## Author

Project Title: Fitness Buddy

Domain: Healthcare & Fitness

Developed using IBM Granite Models and Flask.

---

## License

This project is developed for educational and academic purposes under the IBM University Engagement Program.
