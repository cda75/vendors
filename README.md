# vendors
Project for small automation that helps me to work with some IT vendors web sites.
You should use a geckodriver and have a Mozilla Firefox installed on yor system.
Download geckodriver from https://github.com/mozilla/geckodriver/releases.
In order to use it you have to create a file named "user.conf" which contains an auth credentials.
This file should have the next format: 
[HPE]
user = <username>
password = <user password>

[CISCO]
user = <username>
password = <user password>

[IBM]
user = <username>
password = <user password>

[DELL]
user = <username>
password = <user password>

[APC]
user = <username>
password = <user password>

[PANDUIT]
user = <username>
password = <user password>

[NETAPP]
user = <username>
password = <user password>

[HUAWEI]
user = <username>
password = <user password>

In order to add a new vendors you must add a specific definitions into "vendor.conf" file.
