from sqlalchemy import Column, Integer, Float, Boolean, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from quanlyphongmach import db
from datetime import datetime
from enum import Enum as UserEnum
from flask_login import UserMixin


class UserRole(UserEnum):
    ADMIN = 1
    DOCTOR = 2
    NURSE = 3


class Sex(UserEnum):
    Nam = 1
    Nữ = 2

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


# Nhân Viên
class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    date_of_birth = Column(DateTime, default=datetime.now(), nullable=False)
    sex = Column(Enum(Sex), default=Sex.Nam)
    address = Column(String(100), nullable=False)
    certificate = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    avatar = Column(String(100))
    user_role = Column(Enum(UserRole), default=UserRole.DOCTOR)
    receipt = relationship('Receipt', backref='user', lazy=True)
    prescription = relationship('Prescription', backref='user', lazy=True)

    def __str__(self):
        return self.name


class Patient(BaseModel):
    name = Column(String(50), nullable=False)
    dateofbirth = Column(DateTime, default=datetime.now(), nullable=False)
    sex = Column(String(3), nullable=False)
    idcard = Column(String(12), nullable=False)
    date_of_registration = Column(DateTime, default=datetime.now())
    address = Column(String(255), nullable=False)
    phone_number = Column(String(11), nullable=False)
    email = Column(String(100))
    health_certification = relationship('HealthCertification', backref='patient', lazy=True)
    receipt = relationship('Receipt', backref='patient', lazy=True)

    def __str__(self):
        return self.name


class HealthCertification(BaseModel):
    __tablename__ = 'healthcertification'

    created_date = Column(DateTime, default=datetime.now(), nullable=False)
    symptoms = Column(String(100), nullable=False)
    disease_prediction = Column(String(100), nullable=False)
    prescription = relationship('Prescription', backref='healthcertification', uselist=False, lazy=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), nullable=False)

    def __str__(self):
        return str(self.id)


class Prescription(BaseModel):
    __tablename__ = 'prescription'

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_date = Column(DateTime, default=datetime.now(), nullable=False)
    healthCertification_id = Column(Integer, ForeignKey('healthcertification.id'), nullable=False)
    medicine = relationship('PrescriptionDetail', backref='prescription',lazy=True)
    receipt = relationship('Receipt', backref='prescription', lazy=True)

    def __str__(self):
        return str(self.id)


class PrescriptionDetail(BaseModel):
    __tablename__ = 'prescriptiondetail'

    prescription_id = Column(ForeignKey('prescription.id'), primary_key=True)
    medicine_id = Column(ForeignKey('medicine.id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    using = Column(String(50), nullable=False)


class Medicine(BaseModel):
    __tablename__ = 'medicine'

    name = Column(String(50), nullable=False)
    composition = Column(String(500), nullable=False)
    content = Column(String(500), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit = Column(String(10), nullable=False)
    howtopack = Column(String(20), nullable=False)
    price = Column(Float, nullable=False)
    active = Column(Boolean, default=True, nullable=False)
    prescription = relationship('PrescriptionDetail', backref='medicine', lazy=True)
    receipt = relationship('ReceiptDetail', backref='medicine', lazy=True)

    def __str__(self):
        return self.name


class Receipt(BaseModel):
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_id = Column(DateTime, default=datetime.now())
    patient_id = Column(Integer, ForeignKey('patient.id'), nullable=False)
    prescription_id = Column(Integer, ForeignKey('prescription.id'), nullable=False)
    regulation_id = Column(Integer, ForeignKey('regulations.id'), nullable=False)
    receipt_detail = relationship('ReceiptDetail', backref='receipt', lazy=True)

    def __str__(self):
        return str(self.id)


class ReceiptDetail(BaseModel):
    medicine_id = Column(Integer, ForeignKey('medicine.id'), primary_key=True)
    receipt_id = Column(Integer, ForeignKey('receipt.id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)


class Regulations(BaseModel):
    create_date = Column(DateTime, default=datetime.now())
    quantity_patient = Column(Integer, nullable=False)
    patient_price = Column(Float, nullable=False)
    active = Column(Boolean, default=True)
    receipts = relationship('Receipt', backref="regulations", lazy=True)

    def __str__(self):
        return str(self.id)


if __name__ == '__main__':
    pass
    # db.drop_all()

    # db.create_all()

    # a = [{
    #     "name": "Paracetamol 500mg",
    #     "composition": "500mg Paracetamol cùng với một số tá dược khác như ethanol, magie stearate, gelatin,…",
    #     "content": "Dùng 1 viên/liều, mỗi liều cách nhau 6 giờ, tối đa 4 viên/ngày.",
    #     "quantity": 48,
    #     "unit": "Viên",
    #     "howtopack": "Hộp 4 vỉ x 16 viên",
    #     "price": 45000,
    #     "active": 1
    # },{
    #     "name": "Panadol Extra With Optizorb",
    #     "composition": "Paracetamol, caffeine",
    #     "content": "500 mg Paracetamol, 65 mg Caffeine",
    #     "quantity": 20,
    #     "unit": "Viên",
    #     "howtopack": "Hộp 12 vỉ x 10 viên",
    #     "price": 5000,
    #     "active": 1
    # },{
    #     "name": "Thuốc ho Bổ phế Nam Hà",
    #     "composition": "Dextromethorphan HBr, chlorpheniramine maleate, natri citrate, ammonium, glyceryl guaiacolate.",
    #     "content": "Dextromethorphane bromhydrate 5 mg, Chlorphéniramine maléate 1,33 mg,Phénylpropanolamine chlorhydrate 8,3 mg, Sodium citrate 133 mg, Ammonium chlorure 50 mg, Glycéryl guaiacolate 50 mg.",
    #     "quantity": 50,
    #     "unit": "Viên",
    #     "howtopack": "Hộp 25 vỉ x 4 viên",
    #     "price": 2000,
    #     "active": 1
    # },{
    #     "name": "Panadol Extra With Optizorb",
    #     "composition": "Cefuroxim (dạng Cefuroxim axetil) 500mg",
    #     "content": "500 mg Paracetamol, 65 mg Caffeine",
    #     "quantity": 50,
    #     "unit": "Viên",
    #     "howtopack": "Chai 50 viên",
    #     "price": 1600,
    #     "active": 1
    # },{
    #     "name": "Thuốc dạ dày chữ P – Phosphalugel",
    #     "composition": "Aluminum phosphate dạng keo.",
    #     "content": "Thuốc kháng axit dạ dày. Có tác dụng nhanh trong việc giảm đau, tạo lớp màng bảo vệ và làm lành những tổn thương của cơ quan tiêu hóa.",
    #     "quantity": 52,
    #     "unit": "Gói",
    #     "howtopack": "Hộp 26 gói",
    #     "price": 3800,
    #     "active": 1
    # }]
    #
    # b = [{
    #   "name": "Nguyễn Trùm",
    #   "dateofbirth": "2001-11-07 00:00:00",
    #   "sex": "Nam",
    #   "idcard": "123456789199",
    #   "date_of_registration": "2021-09-11 00:00:00" ,
    #   "address": "66 Âu Cơ, phường 15, quận Tân BÌnh",
    #   "phone_number": "0986356666",
    #   "email": "boss@gmail.com"
    # },{
    #   "name": "Bùi Thị",
    #   "dateofbirth": "2005-11-07 00:00:00",
    #   "sex": "Nữ",
    #   "idcard": "123456789098",
    #   "date_of_registration": "2021-10-11 00:00:00" ,
    #   "address": "Trần Hải, phường 15, quận Bình Tân",
    #   "phone_number": "0777356666",
    #   "email": "btthi@gmail.com"
    # },{
    #   "name": "Trần Mỹ",
    #   "dateofbirth": "2007-10-08 00:00:00",
    #   "sex": "Nữ",
    #   "idcard": "233356789098",
    #   "date_of_registration": "2021-07-11 00:00:00" ,
    #   "address": "Lạc Long Quân, phường 15, quận Bình Tân",
    #   "phone_number": "0978356666",
    #   "email": "myy@gmail.com"
    # },{
    #   "name": "Triệu Lệ Dĩnh",
    #   "dateofbirth": "2002-10-08 00:00:00",
    #   "sex": "Nữ",
    #   "idcard": "100056789098",
    #   "date_of_registration": "2021-07-29 00:00:00" ,
    #   "address": "Nguyễn Tâm, phường 15, quận Bình Tân",
    #   "phone_number": "0794356666",
    #   "email": "ledinh@gmail.com"
    # },{
    #   "name": "Địch Lệ Nhiệt Ba",
    #   "dateofbirth": "2013-03-08 00:00:00",
    #   "sex": "Nữ",
    #   "idcard": "100056747893",
    #   "date_of_registration": "2021-03-29 00:00:00" ,
    #   "address": "Quốc lộ, phường 15, quận Bình Chánh",
    #   "phone_number": "0222356666",
    #   "email": "nhietba@gmail.com"
    # }]
    #
    # c = [{
    #   "create_date": "2021-12-19 11:14:50",
    #   "quantity_patient": 30,
    #   "patient_price": 100000,
    #   "active": 1
    # }]
    #
    # d = [{
    #     "name": "Lê Phát Đạt",
    #     "date_of_birth": "2001-04-27 00:00:00",
    #     "sex": "Nam",
    #     "address": "422A/17 Bờ Đắp Mới, An Phú Tây, Bình Chánh",
    #     "certificate": "Có chứng chỉ hành nghề",
    #     "username": "admin",
    #     "password": "admin",
    #     "active": 1,
    #     "joined_date": "2021-12-19 09:30:00",
    #     "avatar": "",
    #     "user_role": "ADMIN"
    # },{
    #     "name": "Nguyễn Thị Tâm",
    #     "date_of_birth": "2001-10-23 00:00:00",
    #     "sex": "Nữ",
    #     "address": "363 Chiến Lược, Bình Trị Đông A, Bình Tân",
    #     "certificate": "Có chứng chỉ hành nghề",
    #     "username": "ntam231001",
    #     "password": "ntam231001",
    #     "active": 1,
    #     "joined_date": "2021-12-19 11:30:00",
    #     "avatar": "",
    #     "user_role": "NURSE"
    # },{
    #     "name": "Nguyễn Thành Hưng",
    #     "date_of_birth": "2001-03-04 00:00:00",
    #     "sex": "Nam",
    #     "address": "65 Xô Viết Nghệ Tỉnh, phường 11, Tân Bình",
    #     "certificate": "Có chứng chỉ hành nghề",
    #     "username": "dhung040301",
    #     "password": "dhung040301",
    #     "active": 1,
    #     "joined_date": "2021-12-19 13:30:00",
    #     "avatar": "",
    #     "user_role": "DOCTOR"
    # }]
    #
    # e = [{
    #   "created_date": "2021-05-17 10:30:00",
    #   "symptoms": "Đau bụng và ợ chua",
    #   "disease_prediction": "Viêm loét dạ dày",
    #   "patient_id": 1
    # },{
    #   "created_date": "2021-05-18 10:30:00",
    #   "symptoms": "Xây xẫm khi đứng lên",
    #   "disease_prediction": "Tuột huyết áp",
    #   "patient_id": 2
    # },{
    #   "created_date": "2021-06-18 10:30:00",
    #   "symptoms": "Sưng mắt cá chân",
    #   "disease_prediction": "Lệch sơmi",
    #   "patient_id": 3
    # },{
    #   "created_date": "2021-12-18 10:30:00",
    #   "symptoms": "Ho nhiều và đau họng",
    #   "disease_prediction": "Viêm họng",
    #   "patient_id": 4
    # },{
    #   "created_date": "2021-12-19 10:30:00",
    #   "symptoms": "Sốt",
    #   "disease_prediction": "Sốt",
    #   "patient_id": 5
    # }]
    #
    # f = [{
    #   "user_id": 3,
    #   "created_date": "2021-05-17 11:30:00",
    #   "healthCertification_id": 1
    # },{
    #   "user_id": 3,
    #   "created_date": "2021-05-18 11:30:00",
    #   "healthCertification_id": 2
    # },{
    #   "user_id": 3,
    #   "created_date": "2021-06-18 11:30:00",
    #   "healthCertification_id": 3
    # },{
    #   "user_id": 3,
    #   "created_date": "2021-12-18 11:30:00",
    #   "healthCertification_id": 4
    # },{
    #   "user_id": 3,
    #   "created_date": "2021-12-19 11:30:00",
    #   "healthCertification_id": 5
    # }]
    #
    # g = [{
    #   "prescription_id":1,
    #   "medicine_id": 5,
    #   "quantity": 9,
    #   "using": "Uống 2 lần(Sáng, chiều) trước khi ăn 30p."
    # },{
    #   "prescription_id":2,
    #   "medicine_id": 4,
    #   "quantity": 6,
    #   "using": "Uống 3 lần 1 ngày sáng, trưa, chiều sau khi ăn."
    # },{
    #   "prescription_id":3,
    #   "medicine_id": 1,
    #   "quantity": 4,
    #   "using": "Uống 2 lần(Sáng, chiều) sau khi ăn."
    # },{
    #   "prescription_id":4,
    #   "medicine_id": 3,
    #   "quantity": 3,
    #   "using": "Uống 3 lần(Sáng, trưa, chiều) sau khi ăn."
    # },{
    #   "prescription_id":5,
    #   "medicine_id": 1,
    #   "quantity": 4,
    #   "using": "Uống 2 lần(Sáng, Tối) sau khi ăn."
    # }]
    #
    # h = [{
    #   "user_id": 2,
    #   "created_id": "2021-05-17 12:30:00",
    #   "patient_id": 1,
    #   "prescription_id": 1,
    #   "regulation_id": 1
    # },{
    #   "user_id": 2,
    #   "created_id": "2021-05-18 12:30:00",
    #   "patient_id": 2,
    #   "prescription_id": 2,
    #   "regulation_id": 1
    # },{
    #   "user_id": 2,
    #   "created_id": "2021-06-18 12:30:00",
    #   "patient_id": 3,
    #   "prescription_id": 3,
    #   "regulation_id": 1
    # },{
    #   "user_id": 2,
    #   "created_id": "2021-12-18 12:30:00",
    #   "patient_id": 4,
    #   "prescription_id": 4,
    #   "regulation_id": 1
    # },{
    #   "user_id": 2,
    #   "created_id": "2021-12-19 12:30:00",
    #   "patient_id": 5,
    #   "prescription_id": 5,
    #   "regulation_id": 1
    # }]
    #
    # i = [{
    #   "medicine_id": 5,
    #   "receipt_id": 1,
    #   "quantity": 9,
    #   "price": 3800
    # },{
    #   "medicine_id": 4,
    #   "receipt_id": 2,
    #   "quantity": 6,
    #   "price": 1600
    # },{
    #   "medicine_id": 1,
    #   "receipt_id": 3,
    #   "quantity": 4,
    #   "price": 45000
    # },{
    #   "medicine_id": 3,
    #   "receipt_id": 4,
    #   "quantity": 3,
    #   "price": 2000
    # },{
    #   "medicine_id": 1,
    #   "receipt_id": 5,
    #   "quantity": 4,
    #   "price": 45000
    # }]
    # a = [{
    #     "name": "Paracetamol 500mg",
    #     "composition": "500mg Paracetamol cùng với một số tá dược khác như ethanol, magie stearate, gelatin,…",
    #     "content": "Dùng 1 viên/liều, mỗi liều cách nhau 6 giờ, tối đa 4 viên/ngày.",
    #     "quantity": 48,
    #     "unit": "Viên",
    #     "howtopack": "Hộp 4 vỉ x 16 viên",
    #     "price": 45000,
    #     "active": 1
    # },{
    #     "name": "Panadol Extra With Optizorb",
    #     "composition": "Paracetamol, caffeine",
    #     "content": "500 mg Paracetamol, 65 mg Caffeine",
    #     "quantity": 20,
    #     "unit": "Viên",
    #     "howtopack": "Hộp 12 vỉ x 10 viên",
    #     "price": 5000,
    #     "active": 1
    # },{
    #     "name": "Thuốc ho Bổ phế Nam Hà",
    #     "composition": "Dextromethorphan HBr, chlorpheniramine maleate, natri citrate, ammonium, glyceryl guaiacolate.",
    #     "content": "Dextromethorphane bromhydrate 5 mg, Chlorphéniramine maléate 1,33 mg,Phénylpropanolamine chlorhydrate 8,3 mg, Sodium citrate 133 mg, Ammonium chlorure 50 mg, Glycéryl guaiacolate 50 mg.",
    #     "quantity": 50,
    #     "unit": "Viên",
    #     "howtopack": "Hộp 25 vỉ x 4 viên",
    #     "price": 2000,
    #     "active": 1
    # },{
    #     "name": "Panadol Extra With Optizorb",
    #     "composition": "Cefuroxim (dạng Cefuroxim axetil) 500mg",
    #     "content": "500 mg Paracetamol, 65 mg Caffeine",
    #     "quantity": 50,
    #     "unit": "Viên",
    #     "howtopack": "Chai 50 viên",
    #     "price": 1600,
    #     "active": 1
    # },{
    #     "name": "Thuốc dạ dày chữ P – Phosphalugel",
    #     "composition": "Aluminum phosphate dạng keo.",
    #     "content": "Thuốc kháng axit dạ dày. Có tác dụng nhanh trong việc giảm đau, tạo lớp màng bảo vệ và làm lành những tổn thương của cơ quan tiêu hóa.",
    #     "quantity": 52,
    #     "unit": "Gói",
    #     "howtopack": "Hộp 26 gói",
    #     "price": 3800,
    #     "active": 1
    # }]
    #
    # b = [{
    #   "name": "Nguyễn Trùm",
    #   "dateofbirth": "2001-11-07 00:00:00",
    #   "sex": "Nam",
    #   "idcard": "123456789199",
    #   "date_of_registration": "2021-09-11 00:00:00" ,
    #   "address": "66 Âu Cơ, phường 15, quận Tân BÌnh",
    #   "phone_number": "0986356666",
    #   "email": "boss@gmail.com"
    # },{
    #   "name": "Bùi Thị",
    #   "dateofbirth": "2005-11-07 00:00:00",
    #   "sex": "Nữ",
    #   "idcard": "123456789098",
    #   "date_of_registration": "2021-10-11 00:00:00" ,
    #   "address": "Trần Hải, phường 15, quận Bình Tân",
    #   "phone_number": "0777356666",
    #   "email": "btthi@gmail.com"
    # },{
    #   "name": "Trần Mỹ",
    #   "dateofbirth": "2007-10-08 00:00:00",
    #   "sex": "Nữ",
    #   "idcard": "233356789098",
    #   "date_of_registration": "2021-07-11 00:00:00" ,
    #   "address": "Lạc Long Quân, phường 15, quận Bình Tân",
    #   "phone_number": "0978356666",
    #   "email": "myy@gmail.com"
    # },{
    #   "name": "Triệu Lệ Dĩnh",
    #   "dateofbirth": "2002-10-08 00:00:00",
    #   "sex": "Nữ",
    #   "idcard": "100056789098",
    #   "date_of_registration": "2021-07-29 00:00:00" ,
    #   "address": "Nguyễn Tâm, phường 15, quận Bình Tân",
    #   "phone_number": "0794356666",
    #   "email": "ledinh@gmail.com"
    # },{
    #   "name": "Địch Lệ Nhiệt Ba",
    #   "dateofbirth": "2013-03-08 00:00:00",
    #   "sex": "Nữ",
    #   "idcard": "100056747893",
    #   "date_of_registration": "2021-03-29 00:00:00" ,
    #   "address": "Quốc lộ, phường 15, quận Bình Chánh",
    #   "phone_number": "0222356666",
    #   "email": "nhietba@gmail.com"
    # }]
    #
    # c = [{
    #   "create_date": "2021-12-19 11:14:50",
    #   "quantity_patient": 30,
    #   "patient_price": 100000,
    #   "active": 1
    # }]
    #
    # d = [{
    #     "name": "Lê Phát Đạt",
    #     "date_of_birth": "2001-04-27 00:00:00",
    #     "sex": "Nam",
    #     "address": "422A/17 Bờ Đắp Mới, An Phú Tây, Bình Chánh",
    #     "certificate": "Có chứng chỉ hành nghề",
    #     "username": "admin00998",
    #     "password": "admin00998",
    #     "active": 1,
    #     "joined_date": "2021-12-19 09:30:00",
    #     "avatar": "",
    #     "user_role": "ADMIN"
    # },{
    #     "name": "Nguyễn Thị Tâm",
    #     "date_of_birth": "2001-10-23 00:00:00",
    #     "sex": "Nữ",
    #     "address": "363 Chiến Lược, Bình Trị Đông A, Bình Tân",
    #     "certificate": "Có chứng chỉ hành nghề",
    #     "username": "ntam231001",
    #     "password": "ntam231001",
    #     "active": 1,
    #     "joined_date": "2021-12-19 11:30:00",
    #     "avatar": "",
    #     "user_role": "NURSE"
    # },{
    #     "name": "Nguyễn Thành Hưng",
    #     "date_of_birth": "2001-03-04 00:00:00",
    #     "sex": "Nam",
    #     "address": "65 Xô Viết Nghệ Tỉnh, phường 11, Tân Bình",
    #     "certificate": "Có chứng chỉ hành nghề",
    #     "username": "dhung040301",
    #     "password": "dhung040301",
    #     "active": 1,
    #     "joined_date": "2021-12-19 13:30:00",
    #     "avatar": "",
    #     "user_role": "DOCTOR"
    # }]
    #
    # e = [{
    #   "created_date": "2021-05-17 10:30:00",
    #   "symptoms": "Đau bụng và ợ chua",
    #   "disease_prediction": "Viêm loét dạ dày",
    #   "patient_id": 1
    # },{
    #   "created_date": "2021-05-18 10:30:00",
    #   "symptoms": "Xây xẫm khi đứng lên",
    #   "disease_prediction": "Tuột huyết áp",
    #   "patient_id": 2
    # },{
    #   "created_date": "2021-06-18 10:30:00",
    #   "symptoms": "Sưng mắt cá chân",
    #   "disease_prediction": "Lệch sơmi",
    #   "patient_id": 3
    # },{
    #   "created_date": "2021-12-18 10:30:00",
    #   "symptoms": "Ho nhiều và đau họng",
    #   "disease_prediction": "Viêm họng",
    #   "patient_id": 4
    # },{
    #   "created_date": "2021-12-19 10:30:00",
    #   "symptoms": "Sốt",
    #   "disease_prediction": "Sốt",
    #   "patient_id": 5
    # }]
    #
    # f = [{
    #   "user_id": 3,
    #   "created_date": "2021-05-17 11:30:00",
    #   "healthCertification_id": 1
    # },{
    #   "user_id": 3,
    #   "created_date": "2021-05-18 11:30:00",
    #   "healthCertification_id": 2
    # },{
    #   "user_id": 3,
    #   "created_date": "2021-06-18 11:30:00",
    #   "healthCertification_id": 3
    # },{
    #   "user_id": 3,
    #   "created_date": "2021-12-18 11:30:00",
    #   "healthCertification_id": 4
    # },{
    #   "user_id": 3,
    #   "created_date": "2021-12-19 11:30:00",
    #   "healthCertification_id": 5
    # }]
    #
    # g = [{
    #   "prescription_id":1,
    #   "medicine_id": 5,
    #   "quantity": 9,
    #   "using": "Uống 2 lần(Sáng, chiều) trước khi ăn 30p."
    # },{
    #   "prescription_id":2,
    #   "medicine_id": 4,
    #   "quantity": 6,
    #   "using": "Uống 3 lần 1 ngày sáng, trưa, chiều sau khi ăn."
    # },{
    #   "prescription_id":3,
    #   "medicine_id": 1,
    #   "quantity": 4,
    #   "using": "Uống 2 lần(Sáng, chiều) sau khi ăn."
    # },{
    #   "prescription_id":4,
    #   "medicine_id": 3,
    #   "quantity": 3,
    #   "using": "Uống 3 lần(Sáng, trưa, chiều) sau khi ăn."
    # },{
    #   "prescription_id":5,
    #   "medicine_id": 1,
    #   "quantity": 4,
    #   "using": "Uống 2 lần(Sáng, Tối) sau khi ăn."
    # }]
    #
    # h = [{
    #   "user_id": 2,
    #   "created_id": "2021-05-17 12:30:00",
    #   "patient_id": 1,
    #   "prescription_id": 1,
    #   "regulation_id": 1
    # },{
    #   "user_id": 2,
    #   "created_id": "2021-05-18 12:30:00",
    #   "patient_id": 2,
    #   "prescription_id": 2,
    #   "regulation_id": 1
    # },{
    #   "user_id": 2,
    #   "created_id": "2021-06-18 12:30:00",
    #   "patient_id": 3,
    #   "prescription_id": 3,
    #   "regulation_id": 1
    # },{
    #   "user_id": 2,
    #   "created_id": "2021-12-18 12:30:00",
    #   "patient_id": 4,
    #   "prescription_id": 4,
    #   "regulation_id": 1
    # },{
    #   "user_id": 2,
    #   "created_id": "2021-12-19 12:30:00",
    #   "patient_id": 5,
    #   "prescription_id": 5,
    #   "regulation_id": 1
    # }]
    #
    # i = [{
    #   "medicine_id": 5,
    #   "receipt_id": 1,
    #   "quantity": 9,
    #   "price": 3800
    # },{
    #   "medicine_id": 4,
    #   "receipt_id": 2,
    #   "quantity": 6,
    #   "price": 1600
    # },{
    #   "medicine_id": 1,
    #   "receipt_id": 3,
    #   "quantity": 4,
    #   "price": 45000
    # },{
    #   "medicine_id": 3,
    #   "receipt_id": 4,
    #   "quantity": 3,
    #   "price": 2000
    # },{
    #   "medicine_id": 1,
    #   "receipt_id": 5,
    #   "quantity": 4,
    #   "price": 45000
    # }]

    # for x in a:
    #     m = Medicine(name=x['name'], composition=x['composition'], content=x['content'], quantity=x['quantity'], unit=x['unit'], howtopack=x['howtopack'], price=x['price'], active=x['active'])
    #     db.session.add(m)
    #
    # for x in b:
    #     p = Patient(name=x['name'], dateofbirth=x['dateofbirth'], sex=x['sex'], idcard=x['idcard'], date_of_registration=x['date_of_registration'], address=x['address'], phone_number=x['phone_number'], email=x['email'])
    #     db.session.add(p)
    #
    # for x in c:
    #     r = Regulations(create_date=x['create_date'], quantity_patient=x['quantity_patient'], patient_price=x['patient_price'], active=x['active'])
    #     db.session.add(r)
    #
    # for x in d:
    #     u = User(name=x['name'], date_of_birth=x['date_of_birth'], sex=x['sex'], address=x['address'], certificate=x['certificate'], username=x['username'], password=x['password'], active=x['active'], joined_date=x['joined_date'], avatar=x['avatar'], user_role=x['user_role'])
    #     db.session.add(u)
    #
    # for x in e:
    #     hc = HealthCertification(created_date=x['created_date'], symptoms=x['symptoms'], disease_prediction=x['disease_prediction'], patient_id=x['patient_id'])
    #     db.session.add(hc)
    #
    # for x in f:
    #     pre = Prescription(user_id=x['user_id'], created_date=x['created_date'], healthCertification_id=x['healthCertification_id'])
    #     db.session.add(pre)
    #
    # for x in g:
    #     predetail = PrescriptionDetail(prescription_id=x['prescription_id'], medicine_id=x['medicine_id'], quantity=x['quantity'], using=x['using'])
    #     db.session.add(predetail)
    #
    # for x in h:
    #     re = Receipt(user_id=x['user_id'], created_id=x['created_id'], patient_id=x['patient_id'], prescription_id=x['prescription_id'], regulation_id=x['regulation_id'])
    #     db.session.add(re)
    #
    # for x in i:
    #     redetail = ReceiptDetail(medicine_id=x['medicine_id'], receipt_id=x['receipt_id'], quantity=x['quantity'], price=x['price'])
    #     db.session.add(redetail)
    #
    # db.session.commit()