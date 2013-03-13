add_event_btn           = ('xpath', ".//a[@href='/event/add/']")

event_title             = ('xpath', ".//input[@name='title']")
event_location          = ('xpath', ".//input[@name='location']")
event_allDay            = ('xpath', ".//input[@name='allday']")
event_start_date        = ('xpath', ".//input[@name='startDate']")
event_start_time        = ('xpath', ".//input[@name='startTime']")
event_end_date          = ('xpath', ".//input[@name='endDate']")
event_end_time          = ('xpath', ".//input[@name='endTime']")
event_notes             = ('xpath', ".//textarea[@name='description']")
event_delete            = ('xpath', ".//*[@data-l10n-id='event-delete']")
event_save_btn          = ('class name', "save")

view_type               = ('xpath', ".//*[@id='view-selector']//li[@class='%s']")
view_month              = ('xpath', ".//*[@id='view-selector']//li[@class='month']")
view_week               = ('xpath', ".//*[@id='view-selector']//li[@class='week']")
view_day                = ('xpath', ".//*[@id='view-selector']//li[@class='day']")

# WARNING: there is a space character after the hour in the DOM!
view_events_str1         = "section[@class='hour hour-%s  calendar-display calendar-id-local-first']"
view_events_block_m      = "//section[@id='months-day-view']//" + view_events_str1
view_events_block_d      = "//section[@id='day-view']//"        + view_events_str1
view_events_block_w      = "//section[@id='week-view']//ol[@class='hour-%s events calendar-id-local-first']//li"
view_events_title_month  = ".//h5[text()='%s']"
view_events_title_day    = ".//h5[text()='%s']"
view_events_title_week   = ".//div[text()='%s']"
view_events_locat        = "//*[@class='location' and text()='%s']"
