use std::fs;

fn main() {
    let zshrc_content = r#"# Josie Core Immutable CLI Lock
export TERM="xterm-256color"
export LANG="en_US.UTF-8"
cd "$HOME/josie_core"

HISTFILE="$HOME/.zsh_history"
HISTSIZE=30000
SAVEHIST=30000
setopt appendhistory
setopt sharehistory
setopt hist_ignore_all_dups

PROMPT=$'\n%F{39}josie@termux%f %F{220}%~%f %F{120}❯%f '

alias json='cd $HOME/josie_core && zsh json && source ~/.zshrc'
alias jsi='cd $HOME/josie_core'
alias gs='git status'
alias gp='git push'
alias usefish='fish'
alias usebash='bash'

zsh "$HOME/josie_core/json"
"#;

    let _ = fs::write("/data/data/com.termux/files/home/.zshrc", zshrc_content);
}
