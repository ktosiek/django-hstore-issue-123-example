#!/usr/bin/env nix-shell
#!nix-shell -i bash --pure -p python33Packages.virtualenv postgresql

virtualenv _env
_env/bin/pip install -r requirements.txt

echo "source _env/bin/activate"
