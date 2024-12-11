# Hola Odoo

Examples for Odoo

## Applications
### Hot Reload
```
pip install watchdog
```
Run
```
odoo -c odoo.conf --dev=all -u l10n_ec_account_edi
```
or
```
odoo -c odoo.conf --dev=reload -u om_hospital 
```
### Pre-commit
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
