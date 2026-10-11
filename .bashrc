export PATH="$HOME/.local/bin:$HOME/bin:$PREFIX/bin:$PATH"
export GEMINI_API_KEY=""

export LS_COLORS="di=01;36:ln=01;35:ex=01;32:*.py=01;33"
alias ls='ls --color=auto'
alias ll='ls -la --color=auto'
alias agi-web='~/bin/start-agi'
alias robot-web='agi-web'
alias agi='josie'
alias robot='josie'

# Auto-start sshd & web_app.py if not already running
pgrep -x sshd >/dev/null 2>&1 || sshd 2>/dev/null
pgrep -f web_app.py >/dev/null 2>&1 || (nohup python3 ~/web_app.py > ~/web_app.log 2>&1 &)

echo -e "\033[1;36m⚡ [TERMUX READY]\033[0m | Commands: \033[1;32mjosie\033[0m, \033[1;32mhummie\033[0m, \033[1;32mcomet\033[0m, \033[1;32magi\033[0m, \033[1;32magi-web\033[0m"
export PS1='\[\033[01;32m\]termux\[\033[00m\]:\[\033[01;36m\]\w\[\033[01;33m\] \$ \[\033[01;37m\]'
