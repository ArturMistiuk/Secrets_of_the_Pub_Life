init -1 python:
    def neutral_talking_callback(name):
        def callback(event, interact=True, **kwargs):
            if not renpy.store.use_talking_neutral_callback:
                return
            if event == "begin":
                renpy.show(name + " talking")
            elif event == "end":
                renpy.show(name + " neutral")
        return callback

init python:
    def show_subtitles(subtitles: str, sec: float) -> None:
        global subtitle_text
        subtitle_text = subtitles
        renpy.restart_interaction()
        renpy.pause(sec, hard=True)

