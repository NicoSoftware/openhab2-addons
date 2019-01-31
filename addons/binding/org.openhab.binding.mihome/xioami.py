Xiaomi.py:
```
@rule("Mijia & Aqara Wireless Switch")
@when("Channel "mihome:sensor_switch:<GwID>:<ID>:button" triggered")
def switchRule(event):
	event = event.event
	if "SHORT_PRESSED" in str(event):
		<ACTION>
	elif "DOUBLE_PRESSED" in str(event):
		<ACTION>
	elif "DOUBLE_PRESSED" in str(event):
		<ACTION>
	elif "DOUBLE_PRESSED" in str(event):
		<ACTION>


@rule("Mijia & Aqara Cube Controller")
@when("Channel "mihome:sensor_switch:<GwID>:<ID>:button" triggered")
def cubeControllerRule(event):
event = event.event
    if "MOVE" in str(event):
	<ACTION>
    elif "ROTATE_RIGHT" in str(event):
	<ACTION>
    elif "ROTATE_LEFT" in str(event):
	<ACTION>
    elif "FLIP90" in str(event2):
        <ACTION>
    elif "FLIP180" in str(event2):
        <ACTION>
    elif "TAP_TWICE" in str(event):
        <ACTION>
    elif "SHAKE_AIR" in str(event):
        <ACTION>
    elif "FREE_FALL" in str(event):
        <ACTION>
    elif "ALERT" in str(event):
        <ACTION>



@rule("Aqara Smart Motion Sensor")
@when("Channel 'mihome:sensor_vibration:<GwID>:<ID>:action' triggered")
def vibrationRule(event):
	event = event.event
	if "VIBRATE" in str(event):
		<ACTION>
    	elif "TILT" in str(event):
		<ACTION>
    	elif "FREE_FALL" in str(event):
		<ACTION>


@rule("Mijia & Aqara Motion Sensor")
@when("Item MotionSensor_MotionStatus changed")
def motionSensorRule(event):
	if items["MotionSensor_MotionStatus"].State == OnOffType.ON:
		<ACTION>
	else:
		<ACTION>


@rule("Mijia & Aqara Door/Window Sensor")
@when("Item WindowSwitch_Status changed")
def windowSensorRule(event):
	if items["WindowSwitch_Status"].State == OpenClosedType.OPEN:
		<ACTION>
	else:
		<ACTION>


@rule("Mijia & Aqara Door/Window Sensor - Window is open for longer than WindowSwitch_AlarmTimer")
@when("Channel "mihome:sensor_magnet:<GwID>:<ID>:isOpenAlarm" triggered ALARM")
def windowSensorAlarmRule(event):
	<ACTION>

@rule("Aqara Wirelss Light Control (1 Button)")
@when("Channel "mihome:86sw1:<GwID>:<ID>:ch1" triggered SHORT_PRESSED")
def wirelessSwitchRule(event):	
	<ACTION>


@rule("Aqara Wirelss Light Control (2 Button)")
@when("Channel "mihome:86sw2:<GwID>:<ID>:ch1" triggered SHORT_PRESSED")
def wirelessSwitch2Rule(event):	
	<ACTION>


@rule("Aqara Wirelss Light Control (2 Button)")
@when("Channel "mihome:86sw2:<GwID>:<ID>:ch2" triggered SHORT_PRESSED")
def wirelessSwitch3Rule(event):	
	<ACTION>


@rule("Aqara Wirelss Light Control (2 Button)")
@when("Channel "mihome:86sw2:<GwID>:<ID>:dual_ch" triggered SHORT_PRESSED")
def wirelessSwitch4Rule(event):	
	<ACTION>


@rule("Xiaomi Motion Sensor Low Battery")
@when("Item MotionSensor_BatteryLow changed to ON")
def sensorBLRule(event):	
	<ACTION>
  ```
