default player_name = "Никто"
default use_talking_neutral_callback = False


define player = DynamicCharacter("player_name", color="#4709d8", what_slow_cps=35)
define silver_boss = Character(name="Седой Босс", color="#787171", what_slow_cps=35)
define viktor = Character("Виктор", color="#7804bbff", what_slow_cps=35, callback=neutral_talking_callback("viktor"))
define scarlet = Character("Скарлет", color="#2e356dff", what_slow_cps=35, callback=neutral_talking_callback("scarlet"))


image car_inside_video_bg = Movie(play="video/car_windows_bg.webm", loop=True)

image viktor neutral = "characters/viktor/viktor_neutral.png"
image viktor talking = "characters/viktor/viktor_talking.png"

image scarlet neutral = "characters/scarlet/scarlet_neutral.png"
image scarlet talking = "characters/scarlet/scarlet_talking.png"
