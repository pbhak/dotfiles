from libqtile.config import Key, Group
from libqtile import layout
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = 'mod4'

terminal = guess_terminal() # or kitty
app_launcher = 'rofi -show drun'
file_manager = ''
web_browser = ''

# keybindings
keys = [
  # move window focus
  Key([mod], 'h', lazy.layout.left(), desc = 'move window focus to left'),
  Key([mod], 'j', lazy.layout.down(), desc = 'move window focus down'),
  Key([mod], 'k', lazy.layout.up(), desc = 'move window focus to right'),  
  Key([mod], 'l', lazy.layout.right(), desc = 'move window focus up'),
  Key([mod, 'shift'], 'Return', lazy.layout.toggle_split(), desc = 'toggle between split/unsplit sides of stack'),
  # launch applications
  Key([mod], 'Return', lazy.spawn(terminal), desc = 'launch terminal'),
  Key([mod], 't', lazy.spawn(file_manager), desc = 'launch file manager'),
  Key([mod], 'f', lazy.spawn(web_browser), desc = 'launch web browser'),
  Key([mod], 'space', lazy.spawn(app_launcher), desc = 'launch app launcher')
  # layout, window manipulation and qtile specific commands
  Key([mod], 'Tab', lazy.next_layout(), desc = 'toggle between layouts'),
  Key([mod], 'w', lazy.window.kill(), desc = 'kill focused window'),
  Key([mod, 'shift'], 'r', lazy.restart(), desc = 'restart qtile'),
  Key([mod, 'shift'], 'q', lazy.shutdown(), desc = 'shutdown qtile')
]

