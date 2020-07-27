COBRA
===========================

<img align="right" src="static/images/cobra-icon.png">

> A **CO**mbination of systems **B**iology and experimental high-throughput approaches to develop sustainable **R**esistance against pl**A**nt
viruses in crops.

---

> **COBRA** plant virus interaction database is developed in coordination with other plant genomics and bioinformatics groups via the consortium. The Plant KBBE project is funded by the European Commission within its 7th Framework Programme, under the thematic area. 
<br/>




<!-- ![cobra-logo](images/cobra-icon.png) -->
<br/>



# Contact
A COBRA instance is available [here](https://services.cbib.u-bordeaux.fr/cobra/login.php).

# About
(PLANT-KBBE) 2013 Projet COBRA.
<br/>Project ID: [ANR-13-KBBE-0006](http://www.agence-nationale-recherche.fr/Project-ANR-13-KBBE-0006).
<br/>This application was first initiated by CBiB. You can have a look at the inital project [here](https://github.com/marieBvr/COBRA).

# Documentation

## Installation
```bash
sudo apt-get update
sudo apt install apache2
sudo apt-get install libapache2-mod-wsgi-py3 python-dev
sudo apt install python3.6-pip
curl https://bootstrap.pypa.io/get-pip.py | sudo python3.6
sudo pip3.6 install flask
```
In you /home/user
```bash
git clone https://github.com/marieBvr/COBRAsuite.git
cd COBRAsuite/
```
Check path to your app
```bash
nano cobrasuite.wsgi
```
For apache
```bash
sudo nano /etc/apache2/sites-available/cobrasuite.conf
```
Paste
```
<VirtualHost *:80>
     # Add machine's IP address (use ifconfig command)
     ServerName your.IP.or.ServerName
     # Give an alias to to start your website url with
     WSGIScriptAlias / /home/username/COBRAsuite/cobrasuite.wsgi
     <Directory /home/username/COBRAsuite/>
     		# set permissions as per apache2.conf file
            Options FollowSymLinks
            AllowOverride None
            Require all granted
     </Directory>
     ErrorLog ${APACHE_LOG_DIR}/error.log
     LogLevel warn
     CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
Enable cobrasuite conf
```bash
sudo a2ensite cobrasuite
```

## Mongodb
```bash
sudo python3.6 -m pip install Flask-PyMongo
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
sudo echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install mongodb-org
sudo systemctl start mongod
sudo systemctl enable mongod
sudo systemctl restart apache2
```
Try to connect to http://yourIPorServerName/

If problem, try
```bash
sudo apt-get purge mongodb mongodb-server mongodb-server-core mongodb-clients
sudo apt-get purge mongodb-org
sudo apt-get autoremove
sudo apt-get update
sudo apt-get install mongodb-org
```

## COBRA scripts
```bash
sudo python3.6 -m pip install prettytable 
sudo python3.6 -m pip install configobj
```
Create dabatade template
```bash
cd COBRAsuite/script/loader
python3.6 1_species.py
```

