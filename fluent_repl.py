import sublime, sublime_plugin, os, re

class FluentReplTypeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        lang = Haskell()
        replView = _get_repl_view(self.view.window().views(), lang)
        if replView is None:
            return

        sels = self.view.sel()
        for sel in sels:
            word = self.view.substr(self.view.word(sel))
            if not re.match(r"^\w+$", word) and not re.match(r"^\(.*\)$", word):
                word = "(" + word + ")"

            _put_repl_command(replView, lang, "t", word)

class FluentReplAutoLoadEventListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        filename = view.file_name()
        path, ext = os.path.splitext(filename)

        lang = _get_lang(ext)
        if lang is None:
            return

        replView = _get_repl_view(view.window().views(), lang)
        if replView is None:
            return

        _put_repl_command(replView, lang, lang.load_command, "\"" + filename.translate({ord(u"\\"): u"/"}) + "\"")


def _get_lang(extension):
    if extension in [".hs", ".lhs"]:
        return Haskell()
    if extension in [".fs", ".fsx"]:
        return FSharp()
    return None

def _get_repl_view(views, lang):
    name = lang.name
    for view in views:
        if view.name() == "*REPL* [%(name)s]" % locals():
            return view
    return None

def _put_repl_command(view, lang, command, param):
    external_id = view.scope_name(0).split(" ")[0].split(".", 1)[1]
    text = lang.createCommandValue(command, param)
    view.run_command("repl_send", {"external_id": external_id, "text": text})


class Haskell:
    name = "haskell"
    load_command = "l"

    def createCommandValue(self, command, param):
        return ":" + command + " " + param

class FSharp:
    name = "fsharp"
    load_command = "load"

    def createCommandValue(self, command, param):
        return "#" + command + " @" + param + ";;"
