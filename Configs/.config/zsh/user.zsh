#  Startup 
# Commands to execute on startup (before the prompt is shown)
# Check if the interactive shell option is set

#  Plugins 
# manually add your oh-my-zsh plugins here
plugins=(
    "sudo"
    "zsh-256color"
    "zsh-autosuggestions"
    "zsh-syntax-highlighting"
    "zsh-completions"
    "zsh-history-substring-search"
    "fzf-tab"
)

#   Overrides 
# unset HYDE_ZSH_DEFER # Uncomment to disable deferred loading of zsh and let you load you plugin YOURSELF example using zinit
# HYDE_ZSH_OMZ_DEFER=1 # Set to 1 to defer loading of oh-my-zsh plugins ONLY if prompt is already loaded
unset HYDE_ZSH_PROMPT # Uncomment to unset/disable loading of prompts from HyDE and let you load your own prompts
HYDE_ZSH_COMPINIT_CHECK=24 # Set 24 (hours) per compinit security check // lessens startup time
ZSH_THEME=""
DISABLE_AUTO_TITLE="true"
