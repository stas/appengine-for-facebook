# Welcome to the appengine-for-facebook wiki!

## About
I wrote a couple of facebook apps, most of them were written just for fun and using Google AppEngine.
Facebook has a Python library to work with their API, but so far, the initial work of [[sciyoshi|https://github.com/sciyoshi/pyfacebook]] (and now the [[tubaman|https://github.com/tubaman/pyfacebook]]) on the Old REST Facebook API library is the best I could find and use.

This repo is intended to help beginners write facebook apps and learn how to use pyfacebook lib.

## How to deploy

`git clone git://github.com/stas/appengine-for-facebook.git`
`cd appengine-for-facebook`

Now modify `app-sample.yaml` and `facebook-sample.yaml`
Once you're done, rename the files into `app.yaml` and `facebook.yaml`
And update your Google App!
```
appcfg.py update .
```
