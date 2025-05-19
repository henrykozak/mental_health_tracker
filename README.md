# Mental Health Tracker

A simple web application to track your mental health and the activities that contribute to it. This application helps you monitor your daily mental well-being and identify patterns between your activities and mental health metrics.

## Features

- Daily logging of mental health metrics (1-10 scale):
  - Overall feeling
  - Self confidence
  - Self worth
  - Energy levels
  - Physical wellness

- Track daily activities and events:
  - Sleep quality
  - Nutrition
  - Cold water exposure
  - Meditation
  - Breathwork
  - Exercise
  - Hydration
  - Blood glucose control
  - Stress events
  - Anxiety moments
  - Moments of courage
  - Comfort zone challenges

- Visualization of trends:
  - Mental health metrics over time
  - Activity impact analysis
  - Weekly activity summary

## Setup Instructions

1. Make sure you have Python 3.7 or newer installed on your computer.

2. Clone this repository or download the files to your computer.

3. Open a terminal/command prompt and navigate to the project directory:
   ```
   cd path/to/mental_health_tracker
   ```

4. Create a virtual environment (recommended):
   ```
   python -m venv venv
   ```

5. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

6. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

7. Run the application:
   ```
   python app.py
   ```

8. Open your web browser and go to:
   ```
   http://localhost:5000
   ```

## How to Use

1. **Daily Logging**
   - Visit the home page every day to log your mental health metrics
   - Use the sliders to rate your feelings from 1-10
   - Check the boxes for activities you completed
   - Add any notes about your day
   - Click "Save Daily Log" to record your entry

2. **Viewing Trends**
   - Click on "Trends" in the navigation bar
   - View your mental health metrics over time
   - See how different activities impact your mental health
   - Track your weekly activity completion

## Data Storage

Your data is stored locally in a SQLite database in the `database` folder. To back up your data, copy the `database/mental_health.db` file to a safe location.

## Privacy

All your data is stored locally on your computer. This application does not send any data to external servers or third parties. 

web: gunicorn app:app 