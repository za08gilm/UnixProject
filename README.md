# UnixProject
Programs used for the Unix project:

  For this project, the main program used was pyOBD-II, by Pbartek https://github.com/Pbartek/pyOBD-pi, 
  which is an "improved" version of a version of pyOBD-II by peterh, as explained in the README for the
  program. 

Packages needed to run pyOBD-II:
  python-wxgtk2.8 python-wxtools wx2.8-i18n libwxgtk2.8-dev: Packages needed to run the wx import on
  pyOBD-II
  python-serial: Package used to communicate with USB input devices via the /dev/ttyUSB0 directory
  ( used for the ELM-327 to USB input)


Packages needed to run Spotify:

  libwidevinecdm0: This package is a digital rights management (DRM) program that allows for the use
  of streaming copyrighted content on computers. While DRMs are typically installed on Windows machines
  and Macs by default, on the Raspberry Pi running Raspbian, this is not the case, making this package
  a necessity to run Spotify.
  
Necessities for the Neo 6M:
  In order to get the Neo 6M module running, I had to modify the /boot/config.txt and /boot/cmdline.txt
  files in order for the raspberry pi to display coordinate information from the module at specified intervals.
  In order to back up my information in case of crashing, I also created a backup file containing the 
  contents of the original cmdline.txt file.
