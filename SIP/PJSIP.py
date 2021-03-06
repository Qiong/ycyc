##PJSIP

import sys
import pjsau as pj

#Logging callback

def log_cb(level, str, len):
	print str

#Callback to receieve events from Call

class MyCallCallback(pj.CallCallback):
	def __init__(self, call = None):
		pj.CallCallback.__init__(self,call)

	#Notification when call state has changed
	def on_state(self):
		print "Call is ", self.call.info().state_text
		print "last code = ", self.call.info().last_code
		print "(" + self.call.info().last_reason + ")"

	#Notification when call's media stat has changed.
	def on_media_state(self):
		global lib
		if self.call.info().media_state == pj.MediaState.ACTIVE:
			#Connect the call to sound device
			call_slot = self.call.info().conf_slot
			lib.conf_connect(call_slot,0)
			lib.conf_connect(0,call_slot)
			print "Hello world, I can talk!"

#check command lian argument
if len(sys.argv) != 2:
	print "Usage: pjsip.py <dst-URI>"
	sys.exit(1)

try:
	#Create library instance
	lib = pj.Lib()

	#Init library with default config
	lib.init(log_cfg = pj.LogConfig(level =3, callback = log_cb))

	#Create UDP transport which listens to any available port
	transport = lib.create_transport(pj.TransportType.UDP)

	#Start the library
	lib.start()

	#Create local/user-less account
	acc = lib.create_account_for_transport(transport)

	#Make call
	call = acc.make_call(sys.argv[1], MyCallCallback())

	# Wait for ENTER before quitting
    print "Press <ENTER> to quit"
    input = sys.stdin.readline().rstrip("\r\n")

    # We're done, shutdown the library
    lib.destroy()
    lib = None

except pj.Error, e:
    print "Exception: " + str(e)
    lib.destroy()
    lib = None
    sys.exit(1)

