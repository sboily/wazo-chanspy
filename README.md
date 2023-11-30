# wazo-chanspy

To install

    apt install wazo-plugind-cli
    wazo-plugind-cli -c "install git https://github.com/sboily/wazo-chanspy --ref main"

Please edit interfaces.py in /etc/asterisk/extensions_extra.d/ to fill the username and password of the API. Need to have confd acl to get interface from extension.

To spy an extension, the channel need to be up and you can use the extension *556 or *556\<EXTENSION\>.
To change the spy mode

    4 - spy mode
    5 - whisper mode
    6 - barge mode

To make the extension available you need to include spy-call in the dialplan.
Add in /etc/asterisk/extensions_extra.d/xivo-extrafeatures.conf in the context xivo-extrafeatures

    include => spy-call

To remove

    wazo-plugind-cli -c "uninstall quintana/wazo-chanspy"
