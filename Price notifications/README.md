# Product Price Notifier

Python script to notify specified users through mail, if the price of the product is less than or equal price
specified by the user.

Following packages are to be installed using pip.
    * beautifulsoup4
    * requests

# Note :
The sender (sender mail id) should make sure that the following services are on, so as to provide the
permissions to script to send mail.
    * Less secure apps - On
    * Sender Mail address & Password are required

Alternative:
    * Enable 2-Step verification to the Sender's Google Account so the user can setup App passwords
    * Select 'MAIL' as type of application and 'Windows Computer' as type of device.
    * Above steps will generate an alternative password which would give permission to script only to
      access mail id of the user.

These steps(Mail ID's and Password) are required only if the user wants to send a notification through mail.
