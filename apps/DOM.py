class GLOBAL():
    loading_overlay  = ('id', 'loading-overlay')
    app_head_specific= "//h1[text()='%s']"
    app_head         = ('xpath', "//h1")
    status_bar       = ('id', 'statusbar')
    status_bar_new   = ('xpath', "//*[@id='statusbar-notification'][@data-unread='true']")
    status_bar_count = ('xpath', "//*[@id='desktop-notifications-container']/div")

class Browser():
    frame_locator          = ('css selector', 'iframe[src="app://browser.gaiamobile.org/index.html"]')

class Contacts():
    frame_locator          = ('css selector', 'iframe[src="app://communications.gaiamobile.org/index.html"]')
    view_all_header        = ('xpath', GLOBAL.app_head_specific % 'Contacts')
    add_contact_header     = ('xpath', GLOBAL.app_head_specific % 'Add contact')
    edit_contact_header    = ('xpath', GLOBAL.app_head_specific % 'Edit contact')
    view_details_title     = ('id', 'contact-form-title')
    add_contact_button     = ('id', 'add-contact-button')
    edit_details_button    = ('id', 'edit-contact-button')
    done_button            = ('id', 'save-button')
    edit_update_button     = ('id', 'save-button')
    details_back_button    = ('id', 'details-back')
    given_name_field       = ('id', 'givenName')
    family_name_field      = ('id', 'familyName')
    email_field            = ('id', "email_0")
    phone_field            = ('id', "number_0")
    street_field           = ('id', "streetAddress_0")
    zip_code_field         = ('id', "postalCode_0")
    city_field             = ('id', 'locality_0')
    country_field          = ('id', 'countryName_0')
    comment_field          = ('id', 'note_0')
    sms_button             = ('id', 'send-sms-button-0')

class Messages():
    frame_locator          = ('css selector', 'iframe[src="app://sms.gaiamobile.org/index.html"]')
    statusbar_new_sms      = ('xpath', '//div[@class="notification"]/div[text()="%s"]')
    statusbar_all_notifs   = ".//*[@id='desktop-notifications-container']/div[%s]"
    create_new_message_btn = ('id', 'icon-add')
    target_number          = ('id', 'receiver-input')
    input_message_area     = ('id', 'message-to-send')
    send_message_button    = ('id', 'send-message')
    header_back_button     = ('xpath', '//header/a[1]')
    unread_message         = ('css selector', 'li > a.unread')
    unread_messages        = ('class name', 'unread')
    message_sending_spinner= ('css selector', "img[src='style/images/spinningwheel_small_animation.gif']")
    received_messages      = ('xpath', "//li[@class='bubble'][a[@class='received']]")

class Camera():
    capture_button           = ('id', 'capture-button')
    thumbnail                = ('class name', 'thumbnail')
    thumbnail_preview_marker = ('id', 'preview')
    switch_source_btn        = ('id', 'switch-button')
    capture_button_enabled   = ('css selector', '#capture-button:not([disabled])')
    video_timer              = ('id', 'video-timer')
    video_play_button        = ('xpath', "//button[@class='videoPlayerPlayButton']")
    video_pause_button       = ('xpath', "//button[@class='videoPlayerPauseButton']")
    
class Gallery():
    thumbnail_items         = ('css selector', 'li.thumbnail')
    thumbnail_list_section  = ('id', 'thumbnail-list-view')
    current_image_pic       = ('css selector', '#frame2 > img')
    current_image_vid       = ('xpath', "//*[@id='frame2']/div")
    video_play_button       = ('xpath', "//*[@id='frame2']/div/button")
    video_pause_button      = ('xpath', "//*[@id='frame2']/div/div/button")
    fullscreen_back_button  = ('id', 'fullscreen-back-button')

class Video():
    items                   = ('xpath', "//*[@id='thumbnails']/li/div/div[3]")
    #thumbnails              = ('id', 'thumbnails')
    thumb_durations         = ('xpath', "//*[@id='thumbnails']/li/div/div[3]/span[13]/span")
    video_frame             = ('id', 'videoFrame')
    video_loaded            = ('css selector', 'video[style]')

class Phone():
    frame_locator          = ('css selector', 'iframe[src="app://communications.gaiamobile.org/index.html"]')
    
