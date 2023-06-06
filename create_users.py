import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manager.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()


def create_users():

    aram_admin = User.objects.create_superuser(username = 'aram', password= 'aram')
    aram_admin.save()

    # Create an admin user
    admin_user = User.objects.create_user(username='Vardges', password='adminpassword')
    admin_user.is_admin = True
    admin_user.save()

    # Create a customer user
    customer_user = User.objects.create_user(username='Onik', password='onikpassword')
    customer_user.is_customer = True
    customer_user.save()    

    customer_user = User.objects.create_user(username='Arman', password='armanpassword')
    customer_user.is_customer = True
    customer_user.save()

    customer_user = User.objects.create_user(username='148', password='148npassword')
    customer_user.is_customer = True
    customer_user.save()

    # Create an employee user
    employee_user = User.objects.create_user(username='Karen', password='karenpassword')
    employee_user.is_employee = True
    employee_user.save()

    # Create a supplier user
    supplier_user = User.objects.create_user(username='Nune', password='nunepassword')
    supplier_user.is_supplier = True
    supplier_user.save()

    supplier_user = User.objects.create_user(username='Valod', password='valodpassword')
    supplier_user.is_supplier = True
    supplier_user.save()

    supplier_user = User.objects.create_user(username='Hermine', password='herminepassword')
    supplier_user.is_supplier = True
    supplier_user.save()
    
create_users()
