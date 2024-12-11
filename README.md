# Hola Odoo

Examples for Odoo

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

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Odoo Community Association (OCA)
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit
organization whose mission is to support the collaborative development of Odoo features
and promote its widespread use.
