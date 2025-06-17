from libqtile.config import Key, Group, Screen
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
  Key([mod], 'space', lazy.spawn(app_launcher), desc = 'launch app launcher'),
  # layout, window manipulation and qtile specific commands
  Key([mod], 'Tab', lazy.next_layout(), desc = 'toggle between layouts'),
  Key([mod], 'w', lazy.window.kill(), desc = 'kill focused window'),
  Key([mod, 'shift'], 'r', lazy.restart(), desc = 'restart qtile'),
  Key([mod, 'shift'], 'q', lazy.shutdown(), desc = 'shutdown qtile')
]

# workspaces
group_names = [
  'home',
  'net',
  'msg',
  'mus',
  'git',
  'etc'
]

groups = [Group(name, {}) for name in group_names]

# mod + [group number] = switch to group
# mod + shift + [group number] = move currently focused window to group
for i, name in enumerate(group_names, 1):
  keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
  keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))
  
# themes!
gruvbox = [
  '282828', # background   [0]
  '504945', # current line [1] 
  'fbf1c7', # foreground   [2] 
  '665c54', # comment      [3]
  'cc241d', # red          [4]
  '98971a', # green        [5]
  '458588', # blue         [6]
  '689d6a', # aqua         [7] 
  'b16286', # purple       [8]
  'fe8019', # orange       [9]
  'ebdbb2', # alt fg       [10]
]

# layouts
layout_settings = {
  'border_width': 2,
  'margin': 3,
  'border_focus': gruvbox[5]
}

layouts = {
  layout.MonadTall(**layout_settings),
  layout.Max(),
  layout.Floating(**layout_settings)
}

# screens
screens = [
    Screen()
]

wmname = 'LG3D'