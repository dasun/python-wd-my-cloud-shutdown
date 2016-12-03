# Sachindra Dasun <sachindradasun@gmail.com>
#
# WD My Cloud Device Shutdown
#
# This python script connect to the WD My Cloud device via SSH and
# execute a SSH command to shutdown the device.
# SSH feature should be enabled in WD My Cloud before running the script.

import paramiko

# If mycredentialstore module not was found, default values will be used
# Following are default values of WD My Cloud Device
WD_MYCLOUD_HOST = 'wdmycloud'  # WD My Cloud hostname. Usually wdmycloud
WD_MYCLOUD_PORT = 22  # WD My Cloud SSH Port. Usually 22
WD_MYCLOUD_USERNAME = 'root'  # WD My Cloud SSH login username. Usually root
WD_MYCLOUD_PASSWORD = 'welc0me'  # WD My Cloud SSH login password. Usually welc0me

# Credentials are stored in a private local module.
try:
    import mycredentialstore
    WD_MYCLOUD_HOST = mycredentialstore.WD_MYCLOUD_HOST
    WD_MYCLOUD_PORT = mycredentialstore.WD_MYCLOUD_PORT
    WD_MYCLOUD_USERNAME = mycredentialstore.WD_MYCLOUD_USERNAME
    WD_MYCLOUD_PASSWORD = mycredentialstore.WD_MYCLOUD_PASSWORD
except ImportError as e:
    if e.message != 'No module named mycredentialstore':
        raise

# WD My Cloud shutdown commands.
CMD_SHUTDOWN_ONLY = '/sbin/shutdown -r now'
CMD_POWER_OFF_ONLY = '/sbin/poweroff'
CMD_SHUTDOWN_AND_POWER_OFF = '/sbin/shutdown -h -P now'
CMD_REBOOT = '/sbin/reboot'

CMD = CMD_SHUTDOWN_AND_POWER_OFF

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=WD_MYCLOUD_HOST, port=WD_MYCLOUD_PORT, username=WD_MYCLOUD_USERNAME,
               password=WD_MYCLOUD_PASSWORD)

print('$ ' + CMD);

stdin, stdout, stderr = client.exec_command(CMD)
for line in stdout:
    print('> ' + line.strip('\n'))

client.close()
print('Finished')
