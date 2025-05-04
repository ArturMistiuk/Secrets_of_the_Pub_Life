init python:
    def show_subtitles(subtitles: str, sec: float) -> None:
        global subtitle_text
        subtitle_text = subtitles
        renpy.restart_interaction()
        renpy.pause(sec, hard=True)
        