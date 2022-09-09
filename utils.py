from quanlyphongmach import app, db
from flask import session
from quanlyphongmach.models import Patient, Medicine, HealthCertification, Prescription, \
    PrescriptionDetail, Receipt, ReceiptDetail, User, UserRole, Regulations
from quanlyphongmach.models import Patient, User, UserRole
from sqlalchemy.sql import extract
from flask_login import current_user
import hashlib
from sqlalchemy import func


def load_medicines(id_medicines=None):
    md = Medicine.query
    if id_medicines:
        md = Medicine.query.filter(Medicine.id.__eq__(id_medicines))
    return md


def load_patients(pat_id=None, name=None, id_card=None):
    patient = Patient.query.filter()
    if pat_id:
        patient = Patient.query.filter(Patient.id.__eq__(pat_id))
    if name:
        patient = Patient.query.filter(Patient.name.lower().__eq__(name.lower()))
    if id_card:
        patient = Patient.query.filter(Patient.idcard.__eq__(id_card))
    return patient.all()


def check_slot(date_register):
    patient = db.session.query(extract('day', Patient.date_of_registration), func.count(Patient.id))\
                        .filter(extract('month', Patient.date_of_registration) == int(date_register.split("-")[1])) \
                        .filter(extract('year', Patient.date_of_registration) == int(date_register.split("-")[0])) \
                        .filter(extract('day', Patient.date_of_registration) == int(date_register.split("-")[2])) \
                        .group_by(extract('day', Patient.date_of_registration)).all()
    regulations = Regulations.query.filter(Regulations.active.__eq__(True))
    if len(patient) == 0:
        return True
    if int(patient[0][1]) >= int(regulations[0].quantity_patient):
        return False
    return True


def add_db(obj):
    db.session.add(obj)
    db.session.commit()


def add_prescription_detail(prescription, prescription_session):
    if prescription and prescription_session:
        for p in prescription_session.values():
            c = PrescriptionDetail(prescription=prescription,
                                   medicine_id=int(p['id']),
                                   quantity=p['quantity'],
                                   using=p['using']
                                   )
            db.session.add(c)
        db.session.commit()
        del session['prescription_session']


def load_prescriptions():
    return Prescription.query.all()


def load_receipt_details(id_receipt=None):
    receiptDetail = ReceiptDetail.query
    if id_receipt:
        receiptDetail = ReceiptDetail.query.filter(ReceiptDetail.receipt_id.__eq__(id_receipt))
    return receiptDetail.all()


def load_receipts(id_receipt=None):
    receipt = Receipt.query
    if id_receipt:
        receipt = Receipt.query.filter(Receipt.id.__eq__(id_receipt))
    return receipt.all()


def load_healthcertifications(id_patient=None, created_date=None):
    hc = HealthCertification.query
    if created_date:
        hc = hc.filter(extract('month', HealthCertification.created_date) == 12) \
            .filter(extract('year', HealthCertification.created_date) == int(created_date.split("-")[0])) \
            .filter(extract('day', HealthCertification.created_date) == int(created_date.split("-")[2]))
    if id_patient:
        hc = hc.filter(HealthCertification.patient_id.__eq__(id_patient))
    return hc.all()


def load_regulations():
    return Regulations.query.all()


def load_users():
    return User.query.all()


def load_patients_date_register(date_of_registration=None):
    patients = Patient.query.filter(Patient.date_of_registration.__eq__(date_of_registration))
    return patients.all()


def load_prescriptions(id_pre=None):
    prescription = Prescription.query
    if id_pre:
        prescription = Prescription.query.filter(Prescription.id.__eq__(id_pre))
    return prescription.all()


def load_prescription_details(id_prescription=None):
    prescription_detail = PrescriptionDetail.query
    if id_prescription:
        prescription_detail = PrescriptionDetail.query.filter(PrescriptionDetail.prescription_id.__eq__(id_prescription))
    return prescription_detail


def get_user_by_id(user_id):
    return User.query.get(user_id)


def check_login(username, password, role=UserRole.NURSE):
    if username and password:
        # password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password),
                                 User.user_role.__eq__(role)).first()


def check_loginuser(username, password, role=UserRole.ADMIN):
    if username and password:
        # password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password),
                                 User.user_role.__eq__(role)).first()


def revenue_months_stats(year):
    return db.session.query(extract('month', Receipt.created_id),
                           Regulations.patient_price + func.sum(ReceiptDetail.quantity * ReceiptDetail.price)) \
        .join(ReceiptDetail, ReceiptDetail.receipt_id.__eq__(Receipt.id)) \
        .join(Regulations, Regulations.id.__eq__(Receipt.regulation_id)) \
        .filter(extract('year', Receipt.created_id) == year) \
        .group_by(extract('month', Receipt.created_id)) \
        .order_by(extract('month', Receipt.created_id)).all()


def patient_stats(year):
    return db.session.query(extract('month', HealthCertification.created_date),
                            func.count(HealthCertification.id), extract('year', HealthCertification.created_date))\
                .filter(extract('year', HealthCertification.created_date) == year) \
                .group_by(extract('month', HealthCertification.created_date)) \
                .order_by(extract('month', HealthCertification.created_date)).all()


def prescription_stats(month):
    return db.session.query(Medicine.name, extract('month', Receipt.created_id), func.sum(ReceiptDetail.quantity)) \
        .join(Medicine, Medicine.id.__eq__(ReceiptDetail.medicine_id), isouter=True) \
        .join(Receipt, Receipt.id.__eq__(ReceiptDetail.receipt_id), isouter=True) \
        .filter(extract('month', Receipt.created_id) == month) \
        .group_by(Medicine.name, extract('month', Receipt.created_id))\
        .order_by(extract('month', Receipt.created_id)).all()