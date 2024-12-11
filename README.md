# Hola Odoo

Examples for Odoo

## Create python virtual environment
```
virtualenv venv
```
or
```
virtualenv -p python3.12 venv
```
or
```
python3.12 -m venv venv
```
## Activate python virtual environment
```
source venv/bin/activate
```
## Update pip and tools
```
pip install -U pip
pip install --upgrade wheel
pip install --upgrade setuptools
```
## Install requirements
```
pip install -r requirements.txt
```
```
pip install -e ./
```

## Commands and Applications
### Create odoo module
```
odoo scaffold my_module ./custom_addons/HolaOdoo
```
### Install odoo module
```
odoo -c odoo.conf -i my_module --stop-after-init
```
### Hot Reload
```
pip install watchdog
```
Run
```
odoo -c odoo.conf --dev=all -u my_module
```
or
```
odoo -c odoo.conf --dev=reload -u my_module 
```
### Pre-commit
Run in folder where contains module or modules
```
pip install pre-commit
```
Run
```
pre-commit run -a
```