Copy `web_monitoring.py` to `/usr/lib/zabbix/externalscripts`

Install requirement software:
- `apt install chromium chromium-common chromium-driver`
- `pip3 install -r requirements.txt`

Change the owner of a file: `chown zabbix:zabbix /usr/lib/zabbix/externalscripts/web_monitoring.py`

Create new Zabbix item:
- Type: External check
- Key: web_monitoring.py[-a https://example.com/]
- Type of information: Numeric (float)
- Units: seconds

