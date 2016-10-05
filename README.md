[![Stories in Ready](https://badge.waffle.io/changer/cmsplugin-fbgallery.png?label=ready&title=Ready)](https://waffle.io/changer/cmsplugin-fbgallery)
cmsplugin-fbgallery
===================

[![Build Status](https://travis-ci.org/changer/cmsplugin-fbgallery.png?branch=master)](https://travis-ci.org/changer/cmsplugin-fbgallery)

Django CMS plugin for facebook album gallery

This projects helps integrate Facebook album into your Django CMS based website. The plugin provide superb performance compared to the Ajax based alternatives and works even on IE > 6 without any issues. Also, with caching enabled it loads fast without any lag.


## Installation:

Add the following line into your `requirements.txt` file:

```bash
https://github.com/changer/cmsplugin-fbgallery/archive/v1.0.2.zip
```
And add the Facebook App ID and Secret in your settings file:

```py
INSTALLED_APPS = (
                  `cmsplugin_fbgallery`,
                  )
                  
FB_APP_ID = os.environ.get('FB_APP_ID')
FB_APP_SECRET = os.environ.get('FB_APP_SECRET')

```

Since this is secret information, we encourage to keep the secret out of source control. This also allows easy configuration on platforms like heroku. You can obtain the Facebook App ID and Secret by creating an app at [facebook for developers](developers.facebook.com)


Once done, add a block into the django template where you want to use the plugin to work, preferably in
base.html:

```html
{% placeholder facebook-gallery %}
```

## Usage:

In order to use, add the plugin into the intended placeholder and add facebook album Id in the admin and save the plugin and page. Once done, you will have the gallery up and running for you. 

### Finding Album ID:

A facebook Album URL contains the information about the Album ID, here is how you get the Album ID:

If URL is: https://www.facebook.com/pagename/photos/?tab=album&album_id=1234567890

Your Album ID is: 1234567890 .

## Scope:

The future versions with bring in more cleanup and fixes to the plugin.

## Bugs/Issues:

Create an issue here with proper detail: https://github.com/changer/cmsplugin-fbgallery/issues 


## Inspirations/Credits:

This projects seeks some inspirations from the work of [@dantium](https://github.com/dantium) and [@driesdesmet](https://github.com/driesdesmet) on django-fbgallery but adapts it to more CMS plugin way.
