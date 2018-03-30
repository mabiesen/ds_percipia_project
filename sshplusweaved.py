import requests
import subprocess
import sys
import getopt

# if this is windows, use putty
if (sys.platform == 'win32'):
    puttyPath = 'D:\\Program Files (x86)\\PuTTY\\putty.exe'

# otherwise it will use the ssh command
else:
    puttyPath = ''

# values can be set here, passed as arguments or with user input
weavedUser = ''  # weaved username
weavedPwd = ''  # weaved password
deviceAddr = '' # if deviceAddr is blank it will query a list of devices to choose from


# login to weaved account and attempt to connect to a device
def getSSHInfo(weavedUser, weavedPwd, deviceAddr):
    try:

        # login to weaved so we can get an auth token
        url = 'https://api.weaved.com/v22/api/user/login/{}/{}'.format(weavedUser, weavedPwd)
        headers = {'apikey': 'WeavedDeveloperToolsWy98ayxR'}
        r = requests.get(url, headers=headers)

        # if we were successful...
        if (r.status_code == 200):
            print('Logged into Weaved account!')

            token = r.json()['auth_token']

            if (deviceAddr == ''):
                print('No Weaved Device specified, retrieving device list...')

                url = 'https://api.weaved.com/v22/api/device/list/all'
                headers = {'apikey': 'WeavedDeveloperToolsWy98ayxR','token': token}
                r = requests.get(url, headers=headers)

                devices = r.json()['devices']

                # print out each device name and state
                print('Choose device:')
                i = 1
                for device in devices:
                    print ('{}. {} - {}'.format(i, device['devicealias'], device['devicestate']))
                    i = i + 1

                # let the user pick the device
                choiceNum = int(input('Select device, by number: '))

                # go back through the device dict and find the one the user selected
                #  and pull the device address, making sure it is active
                i = 1
                for device in devices:
                    if (i == choiceNum):
                        if (device['devicestate'] == 'active'):
                            deviceAddr = device['deviceaddress']
                        else:
                            print('Device not active!')
                    i = i + 1

            # by now we should have a deviceAddr
            if (deviceAddr != ''):
                print('Connecting to device(may take several seconds)')

                # request ssh info for the specified weaved device
                url = 'https://api.weaved.com/v22/api/device/connect'
                headers = {'apikey': 'WeavedDeveloperToolsWy98ayxR', 'token': token, 'content-type': 'application/json'}
                r = requests.post(url, json={'deviceaddress': deviceAddr, 'wait': 'true'}, headers=headers)

                if (r.status_code == 200):
                    print('Connected to Weaved device!')

                    # address is returned as full url, so need to break it apart
                    sshIP, sshPort = r.json()['connection']['proxy'].replace('http://', '').split(':')
                    print ('Weaved ip:port {}:{}'.format(sshIP, sshPort))

                    return sshIP, sshPort

                else:
                    print (r.text)
                    print('Connection to Weaved device failed!')

            else:
                print('Missing device address, unable to connect...')

        else:
            print (r.text)
            print('Weaved login failed!  Username/password wrong or maybe no internet connection')

        # if we get to here something went wrong so return empty string
        return '', ''

    except Exception as e:
        print(e)
        print('Failed to get SSH info...')


# parse arguements as options
opts, args = getopt.getopt(sys.argv[1:],"hu:p:a:")

# overwrite the default values with any supplied by user
for opt, arg in opts:
    if (opt == '-u'):    weavedUser = arg
    if (opt == '-p'):    weavedPwd = arg
    if (opt == '-a'):    deviceAddr = arg
    if (opt == '-h'):
        print('Options: -u weavedUsername -p weavedPassword -a deviceAddress')
        sys.exit(2)

# check the login vars to see if we need to prompt the user for more info
if (weavedUser == ''):    weavedUser = raw_input('Enter Weaved username: ')
if (weavedPwd == ''):     weavedPwd = raw_input('Enter Weaved password: ')

# login to weaved account and attempt to connect to a device
sshIP, sshPort = getSSHInfo(weavedUser, weavedPwd, deviceAddr)

if (sshIP != ''):
    try:
        if (puttyPath == ''):
            print('Opening SSH connection...')
            subprocess.call(['ssh', sshIP, '-p', sshPort])

        else:
            print('Opening SSH connection with putty...')
            subprocess.call([puttyPath, '-ssh', sshIP, sshPort])

    except Exception as e:
        print(e)
        print('Failed opening terminal...')

else:
    print('Something didnt work, script ending...')
