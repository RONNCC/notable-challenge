"""
	Generic front end app where we use an in-memory non persistent
	SQLite backend that forgets data on server restart.
"""
import datetime
from flask import Flask, render_template, url_for, redirect, request, flash
from db.dbutils import delete_old_db, get_db, close_connection, query_db,exec_db


app = Flask(__name__)
app.secret_key = b'1j19iaindosidan902h09dhw09dh1209br1902b09b1f029]/'


"""
	Init the db before we process the first request to make
	it easier to run this app.
"""
@app.before_first_request
def init_db():
    with app.app_context():
        delete_old_db()
        db = get_db()

        with app.open_resource('db/db_w_data.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        app.teardown_appcontext(close_connection)

"""
    Our home/index page
"""
@app.route('/')
def home():
    return render_template('index.html')

"""
    Route to delete an appt
"""
@app.route('/appts/delete/<int:doctorid>/<int:apptid>')
def appt_delete(doctorid, apptid):
    delete_appt = exec_db("DELETE FROM appointments WHERE rowid = {}".format(apptid))
    return redirect(url_for('doctor_profile',id=doctorid))

"""
    Route to create an appt
"""
@app.route('/appts/create/<int:doctorid>', methods = ['POST'] )
def appt_create(doctorid):
    #check if valid
    apptTime = request.form['apptTime']
    apptKind = request.form['apptKind']
    patientID = request.form['apptPatientID']
    dateTimeFMT = '%Y-%m-%d %H:%M:%S'
    dateTimeNoSecsFMT = '%Y-%m-%d %H:%M:00'
    apptDT = datetime.datetime.strptime(apptTime, dateTimeFMT)

    if apptDT.minute % 15 != 0:
        flash('Time interval not on a 15m boundary')
        return redirect(url_for('doctor_profile',id=doctorid))

    appt_time_groups = query_db(("SELECT COUNT(*) as count, strftime('%Y-%m-%d %H:%M:00', appt_time) as time"
                                " FROM appointments"
                                " WHERE doctor_id={}"
                                " GROUP by strftime('%Y-%m-%dT%H:00:00.000', appt_time)").format(doctorid))
    print (appt_time_groups)
    print (apptDT.strftime(dateTimeNoSecsFMT))
    numApptsInSameSlot = list(filter(lambda x: x['time'] == apptDT.strftime(dateTimeNoSecsFMT), appt_time_groups))
    print (numApptsInSameSlot)
    if len(numApptsInSameSlot) > 0:
        assert(len(numApptsInSameSlot) == 1)
        if numApptsInSameSlot[0]['count'] == 3:
            flash('Too many appts (already 3!) at that time, please choose another time')
            return redirect(url_for('doctor_profile',id=doctorid))

    exec_db("INSERT INTO `appointments` (`appt_time`, `kind`, `patient_id`,`doctor_id`) "+
            ' VALUES ("{}", "{}", {},{});'.format(
              apptTime, apptKind, patientID, doctorid ))
    return redirect(url_for('doctor_profile',id=doctorid))


"""
    Route to list doctors
"""
@app.route('/doctors/list')
def doctors_list():
    doctors = query_db('select rowid,firstname, lastname, phone from doctors')
    return render_template('doctors/list.html',doctors_list=doctors)

"""
    Route to look at at a specific doctor
"""
@app.route('/doctors/profile/<int:id>')
def doctor_profile(id):
    doctors = query_db('select rowid, firstname, lastname, phone from doctors where rowid={}'.format(id))
    assert(len(doctors) == 1)
    patientappts = query_db(' select a.rowid, p.firstname, p.lastname, p.phone, a.appt_time, a.kind' +
                     ' from appointments a, doctors d, patients p ' +
                     ' where d.rowid={} and a.doctor_id=d.rowid and a.patient_id=p.rowid'.format(id))
    patientList = query_db(' select rowid, firstname, lastname from patients ')
    return render_template('doctors/profile.html',doctor=doctors[0],
        appts=patientappts, patients=patientList, apptKinds=['Follow-up', 'New Patient'])
