Introduction
============

This addon is an integration of galleriffic in Plone using gallery. 
It provides a Galleriffic view for Folder, Collection and Link content types.

Dependencies
============

* collective.gallery
* collective.js.galleriffic
* collective.configviews

How to install
==============

This addon is a Plone add on so please follow the official documentation at 
http://plone.org/documentation/kb/add-ons/installing

Exposed configuration
=====================

The Galleriffic view expose some of the configuration of Galleriffic using the 
configure view link provided by collective.configviews addon. 
Options are translated.

* Delay in milliseconds
* Number of thubnails to show per page
* Preload
* Enable top pager
* Enable bottom pager
* Max pages to show
* Render SS controls (Play & Pause)
* Render navigation controls (Previous & Next)
* Enable history (you will need to install collective.jqhistory for this option)
* Enable Keyboard navigation
* Autostart
* Sync transitions
* default transition duration
