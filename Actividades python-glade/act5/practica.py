import PyGObjet
import gtk


class HelloWorld:
    def onClick(self, widget, data=None):
        self.child.show()

    def delete_event(self, widget, event, data=None):
        print ("delete event occurred")
        return False

    def child_delete_event(self, widget, event, data=None):
        self.child.hide()
        return True

    def destroy(self, widget, data=None):
        print ("destroy signal occurred")
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.child = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.connect("delete_event", self.delete_event)
        self.child.connect("delete_event", self.child_delete_event)

        self.window.connect("destroy", self.destroy)
        self.child.connect("destroy", self.destroy)

        self.window.set_border_width(10)

        self.button = gtk.Button("Mostrar ventana")
        self.cbutton = gtk.Button("Boton de prueba")

        self.button.connect("clicked", self.onClick, None)

        self.window.add(self.button)
        self.child.add(self.cbutton)

        self.button.show()
        self.cbutton.show()
        self.window.show()
        self.child.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()
