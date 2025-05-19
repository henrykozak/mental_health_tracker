from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/mental_health.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class DailyLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    
    # Mental Health Metrics (1-10 scale)
    overall_feeling = db.Column(db.Integer, nullable=False)  # 10 is excellent
    self_confidence = db.Column(db.Integer, nullable=False)  # 10 is excellent
    self_worth = db.Column(db.Integer, nullable=False)  # 10 is excellent
    energy_levels = db.Column(db.Integer, nullable=False)  # 10 is high energy
    physical_wellness = db.Column(db.Integer, nullable=False)  # 10 is no aches/pains
    
    # Daily Actions (Boolean checkboxes)
    slept_well = db.Column(db.Boolean, default=False)
    ate_well = db.Column(db.Boolean, default=False)
    cold_water = db.Column(db.Boolean, default=False)
    meditated = db.Column(db.Boolean, default=False)
    breathwork = db.Column(db.Boolean, default=False)
    exercised = db.Column(db.Boolean, default=False)
    hydrated = db.Column(db.Boolean, default=False)
    bgl_control = db.Column(db.Boolean, default=False)
    low_stress_event = db.Column(db.Boolean, default=False)
    medium_stress_event = db.Column(db.Boolean, default=False)
    high_stress_event = db.Column(db.Boolean, default=False)
    physical_anxiety = db.Column(db.Boolean, default=False)
    anxious_moment = db.Column(db.Boolean, default=False)
    displayed_courage = db.Column(db.Boolean, default=False)
    comfort_zone = db.Column(db.Boolean, default=False)
    
    notes = db.Column(db.Text)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trends')
def trends():
    return render_template('trends.html')

@app.route('/log_entry', methods=['POST'])
def log_entry():
    data = request.form
    
    new_entry = DailyLog(
        date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
        
        # Mental Health Metrics
        overall_feeling=int(data['overall_feeling']),
        self_confidence=int(data['self_confidence']),
        self_worth=int(data['self_worth']),
        energy_levels=int(data['energy_levels']),
        physical_wellness=int(data['physical_wellness']),
        
        # Daily Actions
        slept_well=bool(data.get('slept_well')),
        ate_well=bool(data.get('ate_well')),
        cold_water=bool(data.get('cold_water')),
        meditated=bool(data.get('meditated')),
        breathwork=bool(data.get('breathwork')),
        exercised=bool(data.get('exercised')),
        hydrated=bool(data.get('hydrated')),
        bgl_control=bool(data.get('bgl_control')),
        low_stress_event=bool(data.get('low_stress_event')),
        medium_stress_event=bool(data.get('medium_stress_event')),
        high_stress_event=bool(data.get('high_stress_event')),
        physical_anxiety=bool(data.get('physical_anxiety')),
        anxious_moment=bool(data.get('anxious_moment')),
        displayed_courage=bool(data.get('displayed_courage')),
        comfort_zone=bool(data.get('comfort_zone')),
        
        notes=data.get('notes', '')
    )
    
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/get_logs')
def get_logs():
    logs = DailyLog.query.order_by(DailyLog.date).all()
    log_list = []
    for log in logs:
        log_list.append({
            'date': log.date.strftime('%Y-%m-%d'),
            
            # Mental Health Metrics
            'overall_feeling': log.overall_feeling,
            'self_confidence': log.self_confidence,
            'self_worth': log.self_worth,
            'energy_levels': log.energy_levels,
            'physical_wellness': log.physical_wellness,
            
            # Daily Actions
            'slept_well': log.slept_well,
            'ate_well': log.ate_well,
            'cold_water': log.cold_water,
            'meditated': log.meditated,
            'breathwork': log.breathwork,
            'exercised': log.exercised,
            'hydrated': log.hydrated,
            'bgl_control': log.bgl_control,
            'low_stress_event': log.low_stress_event,
            'medium_stress_event': log.medium_stress_event,
            'high_stress_event': log.high_stress_event,
            'physical_anxiety': log.physical_anxiety,
            'anxious_moment': log.anxious_moment,
            'displayed_courage': log.displayed_courage,
            'comfort_zone': log.comfort_zone,
            
            'notes': log.notes
        })
    return jsonify(log_list)

if __name__ == '__main__':
    app.run(debug=True) 