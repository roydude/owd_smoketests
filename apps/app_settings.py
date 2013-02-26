from apps import DOM
import time

class main():
    
    #
    # When you create your instance of this class, include the
    # "self" object so we can access the calling class' objects.
    #
    def __init__(self, p_parentSelf, p_testUtils):
        self.testUtils  = p_testUtils
        self.marionette = p_parentSelf.marionette
        self.parent     = p_parentSelf

    def launch(self):
        self.app = self.parent.apps.launch('Settings')
        self.parent.wait_for_element_not_displayed(*DOM.GLOBAL.loading_overlay)

    #
    # Open wifi settings.
    #
    def wifi(self):
        x = self.testUtils.get_element(*DOM.Settings.wifi)
        self.marionette.tap(x)
        self.parent.wait_for_element_displayed(*DOM.Settings.wifi_header)

    #
    # Open cellular and data settings.
    #
    def cellular_and_data(self):
        x = self.testUtils.get_element(*DOM.Settings.cellData)
        self.marionette.tap(x)
        self.parent.wait_for_element_displayed(*DOM.Settings.celldata_header)

    #
    # Click slider to turn data connection on.
    #
    def turn_dataConn_on(self, p_wifiOFF=False):
        if p_wifiOFF:
            if self.parent.data_layer.get_setting("wifi.enabled"):
                self.parent.data_layer.disable_wifi()
            
        if not self.parent.data_layer.get_setting("ril.data.enabled"):
            x = self.testUtils.get_element(*DOM.Settings.celldata_DataConn)
            self.marionette.tap(x)
            
            #
            # If we get prompted for action, say 'Turn ON'.
            #
            time.sleep(1)
            x = self.marionette.find_element(*DOM.Settings.celldata_DataConn_ON)
            if x.is_displayed():
                self.marionette.tap(x)
                
        #
        # Give the statusbar icon time to appear, then check for it.
        #
        time.sleep(3)
        x = self.testUtils.check_statusbar_for_icon(DOM.Statusbar.dataConn, DOM.Settings.frame_locator)
        self.testUtils.TEST(x, "Data connection icon not detected in status bar.")

    #
    # Click slider to turn wifi on.
    #
    def turn_wifi_on(self):
        if not self.parent.data_layer.get_setting("wifi.enabled"):
            x = self.testUtils.get_element(*DOM.Settings.wifi_enabled)
            self.marionette.tap(x)
        
        #
        # Give the statusbar icon time to appear, then check for it.
        #
        time.sleep(3)
        x = self.testUtils.check_statusbar_for_icon(DOM.Statusbar.wifi, DOM.Settings.frame_locator)
        self.testUtils.TEST(x, "Wifi icon not detected in status bar.")
        
    #
    # Verify the expected network is listed as connected in 'available networks'.
    #
    def checkWifiLisetedAsConnected(self, p_name):
        # 
        # Wait a little time to be sure the networks are all listed.
        #
        time.sleep(5)
        
        #
        # Compare the available networks - if one's connected then check it's the
        # one we expect (starts at array 3).
        #
        x = self.marionette.find_elements(*DOM.Settings.wifi_available_networks)
        for i in range(3, len(x)):
            connStatus = self.marionette.find_element('xpath', DOM.Settings.wifi_available_status % i)
            connName   = self.marionette.find_element('xpath', DOM.Settings.wifi_available_name   % i)
            
            if ("Connected" in connStatus.text) and (p_name == connName.text):
                return True
            else:
                return False
        #
        # If we get to here, we didn't find the network we were looking for.
        #
        return False
        

    #
    # Select a network.
    #
    def tap_wifi_network_name(self, p_wifi_name, p_user, p_pass):
        wifi_name_element = DOM.Settings.wifi_name_xpath % p_wifi_name
        x= self.testUtils.get_element('xpath', wifi_name_element)
        self.marionette.tap(x)
        
        #
        # In case we are asked for a username and password ...
        #
        time.sleep(2)
        wifi_login_user = self.marionette.find_element(*DOM.Settings.wifi_login_user)
        wifi_login_pass = self.marionette.find_element(*DOM.Settings.wifi_login_pass)
        wifi_login_ok   = self.marionette.find_element(*DOM.Settings.wifi_login_ok)
        if wifi_login_user.is_displayed():
            wifi_login_user.send_keys(p_user)
            wifi_login_pass.send_keys(p_pass)
            self.testUtils.clickNTap(wifi_login_ok)
            
        
        #
        # Wait for 'anything' to be Connected.
        #
        try: 
            self.parent.wait_for_element_displayed(*DOM.Settings.wifi_connected)

        except:
            self.testUtils.reportError("Connected to '" + p_wifi_name + "' not established before timeout.")
            self.testUtils.quitTest()       

