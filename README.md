Viewer for Android SMS backup app, for ex [SMSBackupRestore](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore)

The server-side is using [Flask](http://flask.pocoo.org/) and client-side [AngularJS](http://angularjs.org/)

First you need to install all the PIP requirement

    pip install -r requirements.txt
    
After you can run the server
    
    python server.py {sms_file_to_read}

You can then visualize your sms on `http://127.0.0.1:5000/static/index.html`

    
