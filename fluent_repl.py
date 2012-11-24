import sublime, sublime_plugin, os, re

class FluentReplTypeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        replView = get_ghci_view(self.view.window().views())
        if replView is None:
            return

        sels = self.view.sel()
        for sel in sels:
            word = self.view.substr(self.view.word(sel))
            if not re.match(r"^\w+$", word) and not re.match(r"^\(.*\)$", word):
                word = "(" + word + ")"

            put_ghci_command(replView, "t", word)

class FluentReplAutoLoadEventListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        filename = view.file_name()
        path, ext = os.path.splitext(filename)

        if ext != ".hs" and ext != ".lhs":
            return

        replView = get_ghci_view(view.window().views())
        if replView is None:
            return

        put_ghci_command(replView, "l", filename)

def get_ghci_view(views):
    for view in views:
        if view.name() == "*REPL* [haskell]":
            return view
    return None

def put_ghci_command(view, command, param):
    edit = view.begin_edit()
    view.insert(edit, view.size(), ":" + command + " " + param)
    view.run_command("repl_enter")
    view.end_edit(edit)