#!/usr/bin/python3
# requires python >= 3.5
# pyGObject requires for Ubuntu:
# sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0

from typing import *
from pydbus import SessionBus
import click



CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """ List session inhibitor information """
    return

@main.command()
@click.pass_context
def help(ctx):
    print(ctx.parent.get_help())

@main.command()
def list():
    click.echo("Listing inhibitors reported by dbus:")
    inhibitors = get_inhibitors_pydbus()
    if len(inhibitors) == 0:
        print("There are no inhibitors active.")
    for i in inhibitors:
        print (f"Inhibitor: {i['app_id']} {i['reason']}")



# def get_inhibitors()->str:
#
#     shell_command = "dbus-send --print-reply --dest=org.gnome.SessionManager /org/gnome/SessionManager org.gnome.SessionManager.GetInhibitors"
#     output = subprocess.run(shell_command,shell=True,
#                                stdout=subprocess.PIPE,
#                                stderr=subprocess.PIPE)
#     print (output.stdout.decode())
#     stdout_str = output.stdout.decode()
#     stdout_str_list = stdout_str.split("\n")
#     #
#     return output.stdout.decode()
#


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




#put this at the end of the file to make sure all functions defs are parsed and available
if __name__ == "__main__":
    main()







