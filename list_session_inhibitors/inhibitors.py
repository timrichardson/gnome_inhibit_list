#!/usr/bin/python3
# requires python >= 3.5
# pyGObject requires for Ubuntu:
# sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0

from typing import *
from pydbus import SessionBus


def get_inhibitors_pydbus()->List[Dict[str,Any]]:
    session_bus = SessionBus()
    proxy = session_bus.get("org.gnome.SessionManager","/org/gnome/SessionManager")
    results = []
    #print(proxy)
    r = proxy.GetInhibitors()
    for inhibitor in r:
        p_i = session_bus.get("org.gnome.SessionManager",inhibitor)
        app_id = p_i.GetAppId()
        reason = p_i.GetReason()
        results.append({"app_id":app_id,"reason":reason})
    return results








