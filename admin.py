from quanlyphongmach import app, db
from flask_admin import Admin
from quanlyphongmach.models import Patient, Medicine, HealthCertification, Prescription, \
    PrescriptionDetail, Receipt, ReceiptDetail, User, UserRole, Regulations
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from flask_admin import BaseView, expose, AdminIndexView
from flask import redirect, request
from datetime import datetime
import utils


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)


class PatientView(AuthenticatedModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    column_filters = ['dateofbirth', 'sex']
    column_searchable_list = ['name', 'phone_number']
    column_labels = {
        'id': 'Mã bệnh nhân',
        'name': 'Họ tên',
        'dateofbirth': 'Năm sinh',
        'idcard': 'CMND/CCCD',
        'date_of_registration': 'Ngày khám đăng ký',
        'sex': 'Giới tính',
        'address': 'Địa chỉ',
        'phone_number': 'Số điện thoại',
        'prescription': 'Hóa đơn',
        'health_certification': 'Phiếu khám bệnh',
        'receipt': 'Hóa đơn'
    }
    form_excluded_columns = ['receipt', 'health_certification']


class MedicineView(AuthenticatedModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True
    column_filters = ['name', 'unit']
    column_searchable_list = ['name', 'composition', 'content']
    column_labels = {
        'id': 'Mã thuốc',
        'name': 'Tên thuốc',
        'unit': 'Đơn vị',
        'composition': 'Thành phần',
        'content': 'Liều lượng',
        'howtopack': 'Quy cách đóng gói',
        'quantity': 'Số lượng',
        'price': 'Giá thuốc',
        'receipt': 'Hóa đơn',
        'prescription': 'Toa thuốc',
        'active': 'Còn sử dụng'
    }
    form_excluded_columns = ['receipt', 'prescription']


class HealthCertificationView(AuthenticatedModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True
    column_labels = {
        'id': 'Mã phiếu khám',
        'created_date': 'Ngày khám',
        'symptoms': 'Triệu chứng',
        'disease_prediction': 'Chuẩn đoán bệnh',
        'patient': 'Tên bệnh nhân',
        'prescription': 'Mã hóa đơn'
    }
    form_excluded_columns = ['id', 'prescription']


class PrescriptionView(AuthenticatedModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True
    column_labels = {
        'id': 'Mã toa thuốc',
        'created_date': 'Ngày tạo',
        'healthcertification': 'Mã phiếu khám',
        'patient': 'Tên bệnh nhân',
        'user': 'Bác sĩ lập toa',
        'receipt': 'Hóa đơn',
        'medicine': 'Tên thuốc'
    }
    form_excluded_columns = ['medicine', 'receipt']


class PrescriptionDetailView(AuthenticatedModelView):
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True
    column_labels = {
        'quantity': 'Số lượng',
        'prescription': 'Mã toa thuốc',
        'medicine': 'Tên thuốc',
        'using': 'Cách sử dụng'
    }


class ReceiptView(AuthenticatedModelView):
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True
    column_labels = {
        'receipt_detail': 'Chi tiết hóa đơn',
        'created_id': 'Ngày tạo',
        'patient': 'Bệnh nhân',
        'prescription': 'Mã toa thuốc',
        'user': 'Y tá lập hóa đơn',
        'regulations': 'Quy định'
    }
    form_excluded_columns = ['receipt_detail']


class ReceiptDetailView(AuthenticatedModelView):
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True
    column_labels = {
        'quantity': 'Số lượng',
        'price': 'Đơn giá',
        'medicine': 'Tên thuốc',
        'receipt': 'Hóa đơn',
        'patient_price': 'Tiền khám'
    }


class UserView(AuthenticatedModelView):
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True
    column_labels = {
        'name': 'Họ và Tên',
        'date_of_birth': 'Ngày sinh',
        'username': 'Tên đăng nhập',
        'joined_date': 'Ngày vào làm',
        'avatar': 'Hình ảnh',
        'user_role': 'Chức vụ',
        'sex': 'Giới tính',
        'address': 'Địa chỉ',
        'certificate': 'Chứng chỉ',
        'password': 'Mật khẩu',
        'active': 'Trạng thái',
        'health_certification': 'Phiếu khám bệnh',
        'receipt': 'Hóa đơn'
    }
    form_excluded_columns = ['receipt', 'health_certification', 'prescription']


class RegulationView(AuthenticatedModelView):
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True
    column_labels = {
        'create_date': 'Ngày tạo',
        'quantity_patient': 'Số lượng bệnh nhân',
        'patient_price': 'Tiền khám',
        'active': 'Còn sử dụng'
    }
    form_excluded_columns = {'receipts'}


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated


class StatsView(BaseView):
    @expose('/')

    def index(self):
        year = request.args.get('year', datetime.now().year)
        month = request.args.get('month', datetime.now().month)
        return self.render('admin/stats.html', revenue_month_stats=utils.revenue_months_stats(year=year),
                           patient_stats=utils.patient_stats(year=year),
                           prescription_stats=utils.prescription_stats(month=month))

    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


admin = Admin(app=app, name='Phòng mạch ', template_mode='bootstrap4')
admin.add_view(PatientView(Patient, db.session, name='Danh sách bệnh nhân'))
admin.add_view((MedicineView(Medicine, db.session,  name='Danh sách thuốc')))
admin.add_view((HealthCertificationView(HealthCertification, db.session,  name='Phiếu khám bệnh')))
admin.add_view((PrescriptionView(Prescription, db.session,  name='Toa thuốc')))
admin.add_view((PrescriptionDetailView(PrescriptionDetail, db.session,  name='Chi tiết toa thuốc')))
admin.add_view(ReceiptView(Receipt, db.session, name='Hóa đơn'))
admin.add_view(ReceiptDetailView(ReceiptDetail, db.session, name='Chi tiết hóa đơn'))
admin.add_view(UserView(User, db.session, name='Danh sách người dùng'))
admin.add_view(RegulationView(Regulations, db.session, name='Quy định'))
admin.add_view(StatsView(name='Thống kê'))
admin.add_view(LogoutView(name='Đăng xuất'))