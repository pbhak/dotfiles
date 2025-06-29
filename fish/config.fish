# Variable declarations
set fish_greeting # Disables initial Fish greeting message
set -x STARSHIP_CONFIG ~/.config/starship/config.toml

# Initialize Starship (starship.rs)
starship init fish | source
