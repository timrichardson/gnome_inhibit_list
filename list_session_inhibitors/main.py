import click
from signal import signal, SIGINT, SIG_DFL
from list_session_inhibitors.inhibitors import get_inhibitors_pydbus


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def inhibitor_loop(tray_handler):
    """Checks for inhibitors in Widget mode"""
    try:
        inhibitors = get_inhibitors_pydbus()
    except KeyError as e:
        print(f"Caught exception {e}")
        inhibitors = []

    if len(inhibitors) == 0:
        tray_handler.set_icon("uninhibited.png")
        tray_handler.set_inhibitors([])
    else:
        tray_handler.set_icon("inhibited.png")

        inhib_tip = []
        for i in inhibitors:
            inhib_tip.append(f"{i['app_id']}: {i['reason']}")

        tray_handler.set_inhibitors(inhib_tip)


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
        print(f"Inhibitor: {i['app_id']} {i['reason']}")


@main.command()
def widget():
    from list_session_inhibitors.tray_handler import TrayHandler
    handler = TrayHandler()

    from threading import Timer

    class RepeatTimer(Timer):
        def run(self):
            while not self.finished.wait(self.interval):
                self.function(*self.args, **self.kwargs)

    t = RepeatTimer(2, inhibitor_loop, args=[handler])

    # catch ctrl-c
    signal(SIGINT, SIG_DFL)

    # Begin timer thread and pyqt thread
    t.start()
    handler.run()

    # Application is quitting normally via UI
    print("Exiting")
    t.join(timeout=0.1)
    t.cancel()


# put this at the end of the file to make sure all functions defs are parsed and available
if __name__ == "__main__":
    main()
