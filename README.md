command line utility to list session power inhibitors for Linux Gnome users.

Inspired by https://askubuntu.com/a/1239194/152287 from Alexis Wilke (https://www.m2osw.com/)

# Install Tips
The pip install adds an executable to your path (see usage).

This script assumes you are using Gnome.

## Prerequisite packages
The python package PyGObject is a prerequisite.
Installation is automatic, but certain system packages must be installed, according to the requirements of PyGObject

For Ubuntu 20.10 and 21.04 (perhaps others):

``sudo apt install python3-pip libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0``

for other distributions, see https://pygobject.readthedocs.io/en/latest/getting_started.html

You may get a warning that ~/.local/bin is not on your path. 

When you next login, this will be fixed.


# Usage

``inhibitors list``

## Example
With the Gnome Shell plugin Caffeine activate, and a Google Meet running in Firefox:

    $ inhibitors list
    Listing inhibitors reported by dbus:
    Inhibitor: firefox audio-playing
    Inhibitor: user Inhibit by Caffeine


# Comparison with systemd

we can do
``$ systemd-inhibit --list``

which on my desktop gives:

    WHO                            UID  USER PID  COMM            WHAT                                                     WHY                                                       MODE 
    ModemManager                   0    root 2222 ModemManager    sleep                                                    ModemManager needs to reset devices                       delay
    NetworkManager                 0    root 1912 NetworkManager  sleep                                                    NetworkManager needs to turn off networks                 delay
    UPower                         0    root 2654 upowerd         sleep                                                    Pause device polling                                      delay
    Unattended Upgrades Shutdown   0    root 2449 unattended-upgr shutdown                                                 Stop ongoing upgrades or perform upgrades before shutdown delay
    GNOME Shell                    1000 tim  5039 gnome-shell     sleep                                                    GNOME needs to lock the screen                            delay
    Telepathy                      1000 tim  5156 mission-control shutdown:sleep                                           Disconnecting IM accounts before suspend/shutdown...      delay
    gnome-tweak-tool-lid-inhibitor 1000 tim  5325 python3         handle-lid-switch                                        user preference                                           block
    tim                            1000 tim  5255 gsd-media-keys  handle-power-key:handle-suspend-key:handle-hibernate-key GNOME handling keypresses                                 block
    tim                            1000 tim  5020 gnome-session-b shutdown:sleep                                           user session inhibited                                    block
    tim                            1000 tim  5255 gsd-media-keys  sleep                                                    GNOME handling keypresses                                 delay
    tim                            1000 tim  5257 gsd-power       sleep                                                    GNOME needs to lock the screen                            delay
    
        
  The Caffeine plugin inhibit is the third line from the bottom. However, it is not obvious. I am sure in this case, because when I deactivate caffeine, the third line disappears.
  
The Google Meet inhibitor is not even listed at all. However, it is definitely an inhibitor.


### Building and uploading
    python3 -m build
    python3 -m twine upload --skip-existing dist/* 