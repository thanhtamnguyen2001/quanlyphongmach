from quanlyphongmach import app, login
from flask import render_template, Flask, request, redirect, url_for, session, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from quanlyphongmach.models import UserRole, Patient


@app.route("/")
def home():
    p = utils.load_patients()
    return render_template('index.html', p=p)


@app.route("/test")
def test():
    return render_template('test.html')


@app.route('/admin-login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = utils.check_login(username=username, password=password, role=UserRole.ADMIN)
    if user:
        login_user(user=user)

    return redirect('/admin')


#Y tá
@app.route("/nurse/dangky", methods=['get', 'post'])
def y_ta_dang_ky():
    err_msg = ''
    res_msg = ''
    patients = utils.load_patients()
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        dob = request.form.get('DOB')
        id_card = request.form.get('idCard')
        sex = request.form.get('sex')
        address = request.form.get('address')
        phone_number = request.form.get('numberPhone')
        email = request.form.get('email')
        date_register = request.form.get('date_register')
        if date_register:
            if utils.check_slot(date_register=date_register):
                p = Patient(name=name, dateofbirth=dob, sex=sex, idcard=id_card,
                            date_of_registration=date_register, address=address,
                            phone_number=phone_number, email=email)
                utils.add_db(obj=p)
                res_msg = 'đăng ký thành công'
                return render_template('index.html', res_msg=res_msg)
            else:
                err_msg = "Ngày khám đã đăng ký hết, vui lòng đăng ký ngày khác!"
                return render_template('register.html', err_msg=err_msg)
    return render_template('nurse/register.html', patients=patients)


@app.route("/nurse/thanhtoan", methods=['post', 'get'])
def y_ta_thanh_toan():
    res_receipt = ''
    receipt = []
    patient = []
    receipt_detail = []
    regulation = []
    receipts = utils.load_receipts()
    receipt_details = utils.load_receipt_details()
    if request.method.__eq__('POST'):
        receipt_id = request.form.get('id')
        receipt_id = int(receipt_id)

        receipt = utils.load_receipts(id_receipt=receipt_id)
        receipt_detail = utils.load_receipt_details(id_receipt=receipt_id)
        patient = utils.load_patients(pat_id=receipt[0].patient_id)
        regulation = utils.load_regulations()
        if len(receipt) != 0:
            res_receipt = '1111'
    return render_template('nurse/payment.html',
                           receipt=receipt, patient=patient, res_receipt=res_receipt,
                           receipt_detail=receipt_detail, regulation=regulation, receipts=receipts,
                           receipt_details=receipt_details)


@app.route("/nurse/laphoadon", methods=['get', 'post'])
def lap_hoa_don():
    get_id = ''
    msg_res = ''
    health = utils.load_healthcertifications()
    prescription = utils.load_prescriptions()
    prescription_detail = utils.load_prescription_details()
    medicine = utils.load_medicines()
    patient = utils.load_patients()
    receipt = utils.load_receipts()
    receipt_detail = utils.load_receipt_details()
    pre = []
    pd = []
    md = []

    if request.method.__eq__('POST'):
        id_nurse = request.form.get('id_nurse')
        id_nurse = int(id_nurse)
        prescription_id = request.form.get('id')
        prescription_id = int(prescription_id)
        id_patient = request.form.get('id_patient')
        id_patient = int(id_patient)

        pre = utils.load_prescriptions(id_pre=prescription_id)
        hc = utils.load_healthcertifications(id_patient=pre[0].healthCertification_id)

        r = Receipt(prescription_id=prescription_id, user_id=id_nurse,
                    patient_id=id_patient, regulation_id=1)
        utils.add_db(obj=r)

        pd = utils.load_prescription_details(id_prescription=prescription_id)
        md = utils.load_medicines(id_medicines=pd[0].medicine_id)
        rd = ReceiptDetail(medicine_id=pd[0].medicine_id, quantity=pd[0].quantity,
                           price=md[0].price, receipt_id=r.id)
        utils.add_db(obj=rd)
        msg_res = 'Lập hoá đơn thành công!'
    return render_template('nurse/create_payment.html', health=health, prescription=prescription,
                           prescription_detail=prescription_detail, medicine=medicine, patient=patient,
                           receipt=receipt, receipt_detail=receipt_detail, msg_res=msg_res)


@app.route("/danhsachkham")
def medical_examination_list():
    msg_res = ''
    date_of_registration = request.args.get("date_of_registration")
    patients = utils.load_patients_date_register(date_of_registration=date_of_registration)
    return render_template('nurse/medical_examination_list.html',
                            patients=patients, msg_res=msg_res)


# Benh nhan
@app.route("/dangky", methods=['get', 'post'])
def dang_ky():
    err_msg = ''
    res_msg = ''
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        dob = request.form.get('DOB')
        id_card = request.form.get('idCard')
        sex = request.form.get('sex')
        address = request.form.get('address')
        phone_number = request.form.get('numberPhone')
        email = request.form.get('email')
        date_register = request.form.get('date_register')
        if date_register:
            if utils.check_slot(date_register=date_register):
                p = Patient(name=name, dateofbirth=dob, sex=sex, idcard=id_card,
                            date_of_registration=date_register, address=address,
                            phone_number=phone_number, email=email)
                utils.add_db(obj=p)
                res_msg = 'đăng ký thành công'
            else:
                err_msg = "Ngày khám đã đăng ký hết, vui lòng đăng ký ngày khác!"
            return render_template('register.html', res_msg=res_msg, err_msg=err_msg)
    return render_template('register.html')


@app.route('/PhieuKhamBenh', methods=['post', 'get'])
def phieu_kham():
    err_msg = ''
    res_msg = ''
    res_patient = ''
    patient = []
    medicines = utils.load_medicines()
    if request.method.__eq__('POST'):
        patient_id = request.form.get('id')
        patient_id = int(patient_id)
        patient = utils.load_patients(pat_id=patient_id)
        if len(patient) != 0:
            res_patient = '1'
    return render_template('created_health_certification.html',
                           patient=patient, res_patient=res_patient, medicines=medicines)


@app.route('/user-login', methods=['get', 'post'])
def user_signin():
    err_msg = ""
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = utils.check_loginuser(username=username, password=password, role=UserRole.ADMIN)
        user1 = utils.check_loginuser(username=username, password=password, role=UserRole.NURSE)
        user2 = utils.check_loginuser(username=username, password=password, role=UserRole.DOCTOR)
        if user:
            login_user(user=user)
            next = request.args.get('next', 'home')
            return redirect(url_for(next))
        if user1:
            login_user(user=user1)
            next1 = request.args.get('next1', 'home')
            return redirect(url_for(next1))
        if user2:
            login_user(user=user2)
            next2 = request.args.get('next2', 'home')
            return redirect(url_for(next2))
        else:
            err_msg = "Tài khoản hoặc Mật khẩu không chính xác"

    return render_template('login.html', err_msg=err_msg)


@app.route('/api/add-prescription', methods=['post'])
def add_prescription():
    data = request.json
    name = data.get('name')
    id = str(data.get('id'))
    unit = data.get('unit')
    quantity = data.get('quantity')
    using = data.get('using')
    prescription = session.get('prescription_session')
    if not prescription:
        prescription = {}
    if id in prescription:
        prescription[id]['name'] = name
        prescription[id]['id'] = id
        prescription[id]['unit'] = unit
        prescription[id]['quantity'] = quantity
        prescription[id]['using'] = using
    else:
        prescription[id] = {
            'name': name,
            'id': id,
            'unit': unit,
            'quantity': quantity,
            'using': using
        }
    session['prescription_session'] = prescription
    return jsonify(prescription)


@app.route('/api/update-prescription', methods=['put'])
def update_prescription():
    data = request.json
    id = str(data.get('id'))
    quantity = data.get('quantity')
    prescription = session.get('prescription_session')
    if prescription and id in prescription:
        prescription[id]['quantity'] = quantity
        session['prescription_session'] = prescription
    return jsonify(prescription)


@app.route('/api/delete-prescription/<prescription_id>', methods=['delete'])
def delete_prescription(prescription_id):
    prescription = session.get('prescription_session')
    if prescription and prescription_id in prescription:
        del prescription[prescription_id]
        session['prescription_session'] = prescription
    return jsonify(prescription)


@app.route('/hoantatkham', methods=['post'])
def hoan_tat_kham():
    err_msg = ''
    s = request.form.get('symptoms')
    dp = request.form.get('disease_prediction')
    created_date = request.form.get('date_registration')
    patient_id = request.form.get('pid')
    patient = utils.load_patients(pat_id=patient_id)
    hc = HealthCertification(created_date=created_date, symptoms=s,
                             disease_prediction=dp, patient_id=patient_id)
    prescription = Prescription(user=current_user, created_date=datetime.now(),
                                healthcertification=hc)
    prescription_detail = session['prescription_session']
    if session.get('prescription_session'):
        utils.add_db(hc)
        utils.add_db(hc)
        utils.add_prescription_detail(prescription=prescription, prescription_session=session['prescription_session'])
    else:
        err_msg = 'Chưa kê toa!'
        return render_template('created_health_certification.html', err_msg=err_msg)
    i = 1
    for p in prescription_detail.values():
        p['id'] = utils.load_medicines(id_medicines=int(p['id']))[0].name
        p.update({'stt': i})
        i += 1

    return render_template('health_certification.html', patient=patient, hc=hc,
                           prescription_detail=prescription_detail)


@login.user_loader
def load_user(user_id):
    return utils.get_user_by_id(user_id=user_id)


@app.route('/user-logout')
def user_signout():
    logout_user()
    return redirect(url_for('user_signin'))


@app.route('/change-password', methods=['get', 'post'])
@login_required
def account_change():
    msg_err = ''
    msg_res = ''
    if current_user.is_authenticated:
        user_details = current_user.id
        user = User.query.filter_by(id=current_user.id).first()
        if request.method == 'POST':
            pass2 = request.form.get('pass2')
            pass3 = request.form.get('pass3')
            if pass2 == pass3:
                updated_values_dict = request.form.to_dict()
                for k, v in updated_values_dict.items():
                    if k == 'pass2':
                        user.password = v.rstrip()
                db.session.commit()
                msg_res = 'Đổi mật khẩu thành công'
            else:
                msg_err = 'Hai mật khẩu không chính xác'
    return render_template('change_password.html', user_details=user_details, msg_res=msg_res, msg_err=msg_err)


if __name__ == '__main__':
    from quanlyphongmach.admin import *
    app.run(debug=True)

