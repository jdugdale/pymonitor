import gi, time, math, datetime, threading
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

Gdk.threads_init()


# class MainWindow(Gtk.Window):

#     def __init__(self):

#         Gtk.Window.__init__(self, title="Hello Wolrd")
#         grid = Gtk.Grid()
#         self.add(grid)

#         lbl1 = Gtk.Label('Label 1')
#         lbl2 = Gtk.Label('Label 2')
#         lbl3 = Gtk.Label('Label 3')

#         grid.attach(lbl1, 0,0,1,1)
#         grid.attach(lbl2,0,1,1,1)
#         grid.attach(lbl3,1,1,1,1)


#         # vbox = Gtk.Box(spacing=10,orientation=Gtk.Orientation.VERTICAL)
#         # self.add(vbox)

#         # self.entries = [ Gtk.Entry() for i in range(3) ]
#         # for e in self.entries:
#         #     vbox.pack_start(e, True, True, 0)
#         #     e.connect("changed", self.on_entry_changed)
#         #     e.set_text('123')

#         # button=Gtk.Button('ok',name='ok-button')
#         # vbox.pack_end(button,True,True,0)


#     def on_entry_changed(self,entry):
#         ctx = entry.get_style_context()
#         if not entry.get_text().isnumeric():
#             ctx.add_class('invalid')
#         else:
#             ctx.remove_class('invalid')

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
            label.set_text(time.asctime(time.localtime()))
            Gdk.threads_leave()
            time.sleep(1)

    def stop(self):
        self.stopthread.set()

def main_quit(obj, other):
    global t
    t.stop()
    Gtk.main_quit


print time.localtime(time.time())

builder = Gtk.Builder()
builder.add_from_file("glade1.glade")
builder.connect_signals(Handler())

cssProvider = Gtk.CssProvider()
cssProvider.load_from_path('style.css')
screen = Gdk.Screen.get_default()
styleContext = Gtk.StyleContext()
styleContext.add_provider_for_screen(screen, cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

label = builder.get_object("label1")

window = builder.get_object("window1")
window.connect("delete-event", main_quit)
window.show_all()

today = time.localtime()
next = time.mktime((today[0], today[1], today[2], 23, 0, 0, today[6], today[7], today[8]))
diff = next - time.time()
secs = int(math.floor(diff % 60))
mins = int(math.floor(diff / 60 % 60))
hrs = int(math.floor(diff / 3600))
# countdown = time.mktime((today[0], today[1], today[2], hrs, mins, secs, today[6], today[7], today[8]))
# dddff = datetime.datetime()
# then = datetime.datetime.now()
# then.hour = 23
# then.minute = 15
# then.second = 0
# ddff = then - datetime.datetime.now()
# ddff.seconds

#print '{:%H:%M:%S}'.format(datetime.timedelta.

print time.asctime(time.localtime())

t = Threader()
t.start()

Gtk.main()
#print 'in yer code'
