import gi, time, math, datetime, threading
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

Gdk.threads_init()

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
    def onButtonPressed(self, button):
        print('Button pressed')

class Threader(threading.Thread):
    stopthread = threading.Event()
    def run(self):
        global label
        while not self.stopthread.isSet():
            Gdk.threads_enter()
            today = datetime.datetime.today()
            next = today.replace(hour=15, minute=54, second=0)
            diff = next - today
            lblTime.set_text(str(diff))
            lblNext.set_text('Next thing')
            Gdk.threads_leave()
            time.sleep(1)

    def stop(self):
        self.stopthread.set()

class Config:
    weekdays = 'NMTWRFS'

    def load():
        with open('times.txt') as f:
            read_data = f.read()
        for cmd in read_data.splitlines():
            sp = cmd.split('|')
            print sp[0], sp[1], sp[2]

    def get_today_code():
        return weekdays[datetime.date.today().weekday()]

    def next_time(sched_days, sched_time):
        weekday = get_today_code()
        print weekday

        


def main_quit(obj, other):
    global t
    t.stop()
    Gtk.main_quit


builder = Gtk.Builder()
builder.add_from_file("glade1.glade")
builder.connect_signals(Handler())

cssProvider = Gtk.CssProvider()
cssProvider.load_from_path('style.css')
screen = Gdk.Screen.get_default()
styleContext = Gtk.StyleContext()
styleContext.add_provider_for_screen(screen, cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

lblTime = builder.get_object("lblTime")
lblNext = builder.get_object("lblNext")

window = builder.get_object("window1")
window.connect("delete-event", main_quit)
window.maximize()
window.show_all()

t = Threader()
t.start()

Gtk.main()
