import sys
import prompt_toolkit as pt
import pathlib as p
from prompt_toolkit import completion as cmp
from prompt_toolkit import history as hst
from prompt_toolkit import auto_suggest
from svtter_template_creator import lib


cmd_list = ["help", "create"]


class SimpleCompleter(cmp.Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor()
        for command in cmd_list:
            if command.startswith(word_before_cursor):
                yield cmp.Completion(command, -len(word_before_cursor))


def repl():
    session = pt.PromptSession(
        history=hst.FileHistory(str(p.Path.home() / ".config" / "tt" / "history.txt")),
        completer=SimpleCompleter(),
        auto_suggest=auto_suggest.AutoSuggestFromHistory(),
    )

    while True:
        try:
            cmd_str = session.prompt("tt> ")
            if cmd_str.strip() == "exit":
                break
            else:
                cmd, args = cmd_str.split(" ")
                if cmd not in cmd_list:
                    print(f"error cmd: {cmd}")
                else:
                    lib.create(args)
        except EOFError:
            return
        except KeyboardInterrupt:
            continue
        except Exception as e:
            print(e, file=sys.stderr)
