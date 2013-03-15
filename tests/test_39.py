#
# Imports which are standard for all test cases.
#
import sys
sys.path.insert(1, "./")
from tools      import TestUtils
from gaiatest   import GaiaTestCase
import DOM

#
# Imports particular to this test case.
#
from apps.app_settings import *
from apps.app_everythingMe import *

class test_39(GaiaTestCase):
    _Description = "Install an app via 'everything.me'."
    
    _GROUP_NAME  = "Games"
    _APP_NAME    = "Tetris"
    _APP_FRAME   = ("src", "https://aduros.com/block-dream")
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        
        self.UTILS      = TestUtils(self, 0)
        self.Settings   = AppSettings(self)
        self.EME        = AppEverythingMe(self)
        
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
        
        #
        # Make sure 'things' are as we expect them to be first.
        #
        self.data_layer.disable_wifi()
        self.Settings.turn_dataConn_on_if_required()
        
        #
        # Make sure our app isn't installed already.
        #
        self.UTILS.uninstallApp(self._APP_NAME)
            
        #
        # Don't prompt me for geolocation (this was broken recently in Gaia, so 'try' it).
        #
        try:
            self.apps.set_permission('Homescreen', 'geolocation', 'deny')
        except:
            self.UTILS.reportComment("(Just FYI) Unable to automatically set Homescreen geolocation permission.")

    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Launch the 'everything.me' app.
        #
        self.UTILS.TEST(self.EME.launch(), "No application icons found.", True)
        
        #
        # Pick a group.
        #
        self.UTILS.TEST(self.EME.pickGroup(self._GROUP_NAME),
                        "Cannot find group '" + self._GROUP_NAME + "' in EverythingME.",
                        True)

        #
        # Add the app to the homescreen.
        #
        self.UTILS.TEST(self.EME.addAppToHomescreen(self._APP_NAME),
                        "Unable to add application '" + self._APP_NAME + "' to the homescreen.",
                        True)
        
        #
        # Go back to the homescreen and check it's installed.
        #
        self.UTILS.TEST(self.UTILS.launchAppViaHomescreen(self._APP_NAME), 
                        self._APP_NAME + " not installed.", True)
        
        #
        # Give it 10 seconds to start up, switch to the frame for it and grab a screenshot.
        #
        time.sleep(10)
        self.marionette.switch_to_frame()
        self.UTILS.switchToFrame(*self._APP_FRAME)
        x = self.UTILS.screenShot("_" + self._APP_NAME)
        self.UTILS.reportComment("NOTE: Please check the game screenshot in " + x)
