#Preparation
sudo apt-get install mysql # mysql db
sudo pip install mysql-python  #mysql connector for python
sudo pip install python-mysqldb #

#Initialization 
python manage.py syncdb   #create tables


#Superuser
Username (leave blank to use 'guojingyu'): guojingyu
Email address: guojy8993@163.com
Password: 
Password (again): 
Superuser created successfully.

#And starting
python manage.py runserver # start server


#mysql测试数据
insert into jobs_location (city,state,country) values('Zheng zhou','Henan','China');
insert into jobs_job (pub_date,job_title,job_description,location_id) values(CURRENT_TIMESTAMP,'Cloud Computing Engineer','Skills Required: 1.java or python 2.openstack,AWS,Hadoop 3...',1);

insert into jobs_location (city,state,country) values('Hang zhou','JiangSu','China');
insert into jobs_job (pub_date,job_title,job_description,location_id) values(CURRENT_TIMESTAMP,'C++/Java Engineer','Skills Required: 1.java or python 2.openstack,AWS,Hadoop 3...',2);

insert into jobs_location (city,state,country) values('Zhu zhou','Hunan','China');
insert into jobs_job (pub_date,job_title,job_description,location_id) values(CURRENT_TIMESTAMP,'UI Designer','Skills Required: 1.PS or FLASH ...',3);

