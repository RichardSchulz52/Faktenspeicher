# This file will be run by docker to use environment variables for configuration and streamlit start

import yaml
import os
import subprocess

user_yaml = 'user.yaml'
with open(user_yaml, 'a+') as f:
    doc = dict()

    admin_name = os.environ.get('admin_login', 'admin')
    admin_password = os.environ.get('admin_password', 'pass')
    doc['credentials'] = {'usernames': {admin_name: {'password':  admin_password, 'logged_in': False, 'name': admin_name}}}
    doc['cookie'] = {'expiry_days': 30, 'key': 'bambussoft_de_login', 'name': 'bambussoft_de_login_keks'}

    yaml.dump(doc, f)

subprocess.run(["streamlit", "run", "./Search.py"])
