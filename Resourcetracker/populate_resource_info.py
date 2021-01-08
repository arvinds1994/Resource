import os
import faker
import django
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Resourcetracker.settings')
django.setup()


from datetime import datetime
from resource.models import Resource
from faker import Faker
fake = Faker()

def populate(n):
    id = 1244865
    for i in range(n):
        name = fake.name().split()
        fname = name[0]
        lname = name[1]
        email = fake.email()
        add_date = fake.date()
        emp_id = id

        project_list = ['Cisco','Equifax','Ultimatix','Wells Fargo']
        project_name = random.choice(project_list)

        team_list = ['Citi','Anav','BDO']
        team_name = random.choice(team_list)

        id=id+3

        customer_record = Resource.objects.get_or_create(first_name=fname, last_name=lname, employee_id= emp_id, email_id=email,
                                                         added_on = add_date, project_name= project_name, team_name= team_name)


if __name__ =='__main__':
    print("Populating Script")
    populate(20)
    print("Populating Complete")