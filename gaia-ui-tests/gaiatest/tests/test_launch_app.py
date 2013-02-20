from gaiatest import GaiaTestCase

MANIFEST = 'http://mozqa.com/data/webapps/mozqa.com/manifest.webapp'
APP_NAME = 'Mozilla QA WebRT Tester'
TITLE = 'Index of /data'


class TestLaunchApp(GaiaTestCase):
    _yes_button_locator = ('id', 'app-install-install-button')
    # locator for li.icon, because click on label doesn't work.
    _icon_locator = ('css selector', 'li.icon[aria-label="%s"]' % APP_NAME)
    _app_locator = ('css selector', 'iframe[src="http://mozqa.com/data"]')
    _header_locator = ('css selector', 'h1')

    def setUp(self):
        GaiaTestCase.setUp(self)

        if self.wifi:
            self.data_layer.enable_wifi()
            self.data_layer.connect_to_wifi(self.testvars['wifi'])

        self.homescreen = self.apps.launch('Homescreen')

        # install app
        self.marionette.switch_to_frame()
        self.marionette.execute_script(
            'navigator.mozApps.install("%s")' % MANIFEST)

        # click yes on the installation dialog and wait for icon displayed
        self.wait_for_element_displayed(*self._yes_button_locator)
        yes = self.marionette.find_element(*self._yes_button_locator)
        yes.click()

        self.marionette.switch_to_frame(self.homescreen.frame)

        # We don't need to check it's displayed, only present(installed)
        # We'll find the icon in the test instead
        self.wait_for_element_present(*self._icon_locator)

    def test_launch_app(self):
        # click icon and wait for h1 element displayed
        icon = self.marionette.find_element(*self._icon_locator)

        # We iterate through the homescreen pages until we find the icon
        # It can be on different screens depending on what is packaged with the build
        while self._homescreen_has_more_pages():
            self._go_to_next_page()
            if icon.is_displayed():
                break

        self.marionette.tap(icon)
        self.marionette.switch_to_frame()
        iframe = self.marionette.find_element(*self._app_locator)
        self.marionette.switch_to_frame(iframe)
        self.wait_for_element_displayed(*self._header_locator, timeout=20)
        self.assertEqual(self.marionette.find_element(*self._header_locator).text, TITLE)

    def _go_to_next_page(self):
        self.marionette.execute_script('window.wrappedJSObject.GridManager.goToNextPage()')

    def _homescreen_has_more_pages(self):
        # the naming of this could be more concise when it's in an app object!
        return self.marionette.execute_script("""
            var pageHelper = window.wrappedJSObject.GridManager.pageHelper;
            return pageHelper.getCurrentPageNumber() < (pageHelper.getTotalPagesNumber() - 1);""")

    def tearDown(self):
        self.apps.uninstall(APP_NAME)
        if self.wifi:
            self.data_layer.disable_wifi()
        GaiaTestCase.tearDown(self)
