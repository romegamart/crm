from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_page),
    path('admin-dashboard/',views.admin_dashboard),
    path('admin-telesales-employee/',views.admin_telesales_employee),
    path('admin-digital-employee/',views.admin_digital_employee),
    path('admin-add-employee/',views.admin_add_employee),
    path('admin-add-client/',views.admin_add_client),
    path('admin-update-employee/<int:id>/',views.admin_update_employee),
    path('admin-delete-employee/<int:id>/',views.admin_delete_employee),
    path('admin-update-employee-status/<int:id>/<str:ops>/',views.admin_update_employee_status),
    path('admin-client/<str:ops>/',views.admin_client),
    path('admin-upload-excel/',views.admin_upload_excel),
    path('admin-update-client/<int:id>/',views.admin_update_client),
    path('admin-delete-client/<int:id>/<int:pn>/',views.admin_delete_client),
    path('admin-exchange-data/',views.admin_exchange_data),
    path('admin-employee-by-type/<str:ops>/',views.admin_client_by_type),
    path('assign_type/',views.assign_type),
    path('admin-search/',views.admin_search),
    path('admin-logout/',views.admin_logout),
    path('admin-download-employee-report/',views.admin_download_employee_report),
    path('admin-distribute-data/',views.admin_distribute_data),
    path('admin-download-data/',views.admin_download_data),
    path('admin-download-employee-data/',views.admin_download_employee_data),
    path('filter/',views.admin_filter),
    path('admin-report-filter/',views.admin_employee_filter),
 

    #Empployee Report
    path('employee-report/<str:phone>/<ops>/',views.employee_report_by_status),

    #Digital Empployee Report
    path('digital-employee-report/<str:phone>/<ops>/',views.employee_report_by_status),

    #Employee Operation Digital Marketing
    path('employee-login/',views.employee_login),
    path('employee-dashboard/',views.employee_dashboard),
    path('employee-add-data/',views.employee_add_data),
    path('employee-update-data/<int:id>/',views.employee_update_data),
    path('employee-delete-data/<int:id>/<int:pn>/',views.employee_delete_data),
    path('employee-logout/',views.employee_logout),
    path('add-image/',views.add_image),
    path('employee-delete-image/<int:id>/',views.delete_image),
    path('employee-data/<str:ops>/',views.employee_client),
    path('employee-search/',views.employee_search),
    path('employee-add-single-client/',views.employee_add_single_client),
    path('employee-email/',views.employee_email),
    path('employee-add-email/',views.employee_add_email),
    
    #API
    path('app-employee-login/',views.app_employee_login),
    path('app-get-client/',views.app_get_client),
    path('app-get-client-details/',views.app_get_client_details),
    path('app-update-client/',views.app_update_client),
    path('assign-employees/',views.assign_employees),


    path('remove-data/',views.remove_date),
    path('remove-data-from-date/',views.admin_filter_delete),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
