Take a snapshot of web pages
============================

This very simple utility will take a screenshot of a web site, or web sites, at a moment in time.

It's designed to be most useful when it's run automagically, such as once an hour.

Initial setup
=============

Install Python from Python.org.

Put SeleniumJS somewhere. You can find the main file in a "bin" folder instead of the ZIP you download.

Use "pip install Pillow selenium" to install the other two things needed.

Edit screengrabs.py to customize the location of where it saves ("c:\screengrabs" or whatever you want).

Also edit your SeleniumJS location.

Continue editing to fix the mysites thing the way you want. The first entry is the URL in quotes (e.g., "http://www.google.com"). The second is a filename prefix -- perhaps you want "goog" or "google" or "maingoogle".

Scheduling setup
================

If you're on Windows and you want to schedule this thing, try this:

Start: Programs: Accessories: System Tools: Task Scheduler.

Let's say you want to run this twice an hour.

On the right, Create  Task. Name can be something like screengrabs.

Pick Run Whether User is logged on or not. Then probably turn on Do not store password.

Click the Triggers tab at the top, then New. Start it Daily at, whatever, 12:12 a.m.

Turn on Repeat task, pick 30 minutes. Hit OK.

Click the Actions tab, then hit New.

Start a program, browse, find the script, e.g., C:\git\screengrabs\screengrabs.py

Hit OK.
