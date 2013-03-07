import sys
sys.path.insert(1, "./")

from tools import TestUtils
from apps import DOM, app_calendar
from gaiatest import GaiaTestCase
from datetime import datetime

class test_34(GaiaTestCase):
    _Description = "Add calendar event."
 
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = TestUtils(self, 34)
        self.calendar   = app_calendar.main(self)
        self.titleStr   = "Test event " + str(datetime.now().time())
        self.locatStr   = "Right here"
        
        #
        # Set the timeout for element searches.
        #
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
        
    def tearDown(self):
        self.UTILS.reportResults()

    def test_run(self):
        #
        # Launch contacts app.
        #
        self.calendar.launch()
        
        #
        # Create new event 1 hour from now for 1 hour.
        #        
        t = datetime.now().time()
        t_h1 = str(t.hour  + 1).zfill(2)
        t_h2 = str(t.hour  + 2).zfill(2)
        t_m1 = str(t.minute   ).zfill(2) 
        t_m2 = str(t.minute   ).zfill(2) 
        t_s  = str(t.second   ).zfill(2)
        
        # I can't figure out how to make the app accept a different time when it's passed in as a string
        # like this, so just set it to default for now.
        t_m1 = "00"
        t_m2 = "00"
        t_s  = "00"
        
        startTime = t_h1 + ":" + t_m1 + ":" + t_s
        endTime   = t_h2 + ":" + t_m2 + ":" + t_s        
        self.calendar.createEvent(self.titleStr, self.locatStr, False, False, startTime, False, endTime, "Some test notes")
                
        #
        # Check the event is listed as expected in MONTH view.
        #
        x = self.calendar.getEventPreview("month", t_h1, self.titleStr, self.locatStr)
        self.UTILS.TEST(x, "Created calendar event not found in month view.")
        
        #
        # Check the event is listed as expected in WEEK view.
        #
        x = self.calendar.getEventPreview("week", t_h1, self.titleStr, self.locatStr)
        self.UTILS.TEST(x, "Created calendar event not found in week view.")
        
        #
        # Check the event is listed as expected in DAY view.
        #
        x = self.calendar.getEventPreview("day", t_h1, self.titleStr, self.locatStr)
        self.UTILS.TEST(x, "Created calendar event not found in day view.")
        
