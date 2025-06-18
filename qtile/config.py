import os, subprocess
from libqtile.config import Key, Group, Screen
from libqtile import layout, hook, bar, widget
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
  'fb4934', # red          [4]
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
  'border_focus': gruvbox[6]
}

layouts = {
  layout.MonadTall(**layout_settings),
  layout.Max()
}

# bar
widget_defaults = dict(
  font = 'Source Code Pro',
  fontsize = 12,
  padding = 2,
  background = gruvbox[0],
  foreground = gruvbox[2]
)

## widgets
widgets = [
  widget.Sep(
    linewidth = 0,
    padding = 6
  ),
  widget.GroupBox(
    active = gruvbox[2],
    inactive = gruvbox[2],
    highlight_method = 'block',
    rounded = False
  ),
  widget.Sep(
    linewidth = 0,
    padding = 925,
  ),
  widget.CurrentLayout(
    fmt = 'Layout: {}',
    foreground = gruvbox[6]
  ),
  widget.TextBox(text = '|'),
  widget.CheckUpdates(
    display_format = '{updates}',
    fmt = 'Updates: {}',
    colour_have_updates = gruvbox[4],
    colour_no_updates = gruvbox[4],
    no_update_string = '0',
    custom_command = 'checkupdates'
  ),
  widget.TextBox(text='|'),
  widget.Clock(
    format = '%b %d %I:%M:%S %p',
    foreground = gruvbox[5]
  ),
  widget.Spacer(
    length = 35
  )
]

# screens
screens = [
    Screen(top=bar.Bar(widgets = widgets, opacity = 1, size = 30))
]

@hook.subscribe.startup_once
def autostart():
  file = os.path.expanduser('~/.config/qtile/autostart.sh')
  subprocess.call(file)

wmname = 'LG3D'