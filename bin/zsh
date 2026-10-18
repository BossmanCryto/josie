Time (μs)   Sum (μs)  Command
       136      37138 > __fish_on_interactive
        35         35 -> functions -e __fish_on_interactive
       669      36967 -> __fish_config_interactive
        46         46 --> function __fish_config_interactive -d "Initializations that should be performed when entering interactive mode"...
        27         27 --> functions -e __fish_config_interactive
        16         16 --> set -g __fish_active_key_bindings
       227        249 --> functions -q __fish_webconfig_update_color_hook
        22         22 ---> function __fish_webconfig_update_color_hook --on-variable __fish_webconfig_theme_notification...
        10       1777 --> if not set -q FISH_UNIT_TESTS_RUNNING...
        17         17 ---> not set -q FISH_UNIT_TESTS_RUNNING
        34       1750 ---> if not test -d $__fish_cache_dir/generated_completions...
      1716       1716 ----> not test -d $__fish_cache_dir/generated_completions
        21       1876 --> if not status is-interactive-read...
        24         24 ---> not status is-interactive-read
       289        309 ---> functions -q fish_greeting
        20         20 ----> function fish_greeting...
        39       1522 ---> fish_greeting
        32       1385 ----> if not set -q fish_greeting...
        14         14 -----> not set -q fish_greeting
       251        291 -----> set -l line1 (_ 'Welcome to fish, the friendly interactive shell')
        40         40 ------> _ 'Welcome to fish, the friendly interactive shell'
       220       1023 -----> set -l line2 \n(printf (_ 'Type %shelp%s for instructions on how to use fish') (set_color green) (set_color --reset))
       556        803 ------> printf (_ 'Type %shelp%s for instructions on how to use fish') (set_color green) (set_color --reset)
        29         29 -------> _ 'Type %shelp%s for instructions on how to use fish'
       181        181 -------> set_color green
        37         37 -------> set_color --reset
        25         25 -----> set -g fish_greeting "$line1$line2"
         5         10 ----> if set -q fish_private_mode...
         5          5 -----> set -q fish_private_mode
        13         13 ----> test -n "$fish_greeting"
        75         75 ----> echo $fish_greeting
         6         30 --> if not status is-interactive-read...
        13         13 ---> not status is-interactive-read
        11         11 ---> set -q SHELL_WELCOME[1]
         7         49 --> if test -d /etc/init.d...
        42         42 ---> test -d /etc/init.d
       427        732 --> complete -c(builtin -n | string match -rv '(\.|:|source|cd|contains|count|echo|exec|fish_indent|printf|random|realpath|set|\\[|test|for)') --no-files
       305        305 ---> builtin -n | string match -rv '(\.|:|source|cd|contains|count|echo|exec|fish_indent|printf|random|realpath|set|\\[|test|for)'
        43         43 --> function __fish_reload_key_bindings -d "Reload key bindings when binding variable change" --on-variable fish_key_bindings...
        42      18827 --> __fish_reload_key_bindings
        45      18785 ---> if not set --query fish_key_bindings...
        13         13 ----> not set --query fish_key_bindings
       147      18675 ----> set --global fish_key_bindings fish_default_key_bindings
       132      18528 -----> __fish_reload_key_bindings VARIABLE SET fish_key_bindings
         9         22 ------> if not set --query fish_key_bindings...
        13         13 -------> not set --query fish_key_bindings
         4         39 ------> if test "$fish_key_bindings" = "$__fish_active_key_bindings" -a -n "$fish_key_bindings"...
        35         35 -------> test "$fish_key_bindings" = "$__fish_active_key_bindings" -a -n "$fish_key_bindings"
        19        465 ------> if not functions -q "$fish_key_bindings"...
       415        446 -------> not functions -q "$fish_key_bindings"
        31         31 --------> function fish_default_key_bindings -d "emacs-like key binds"...
        95         95 ------> set -g __fish_active_key_bindings "$fish_key_bindings"
        16         16 ------> set -g fish_bind_mode default
       375      15550 ------> $fish_key_bindings
         8         23 -------> if contains -- -h $argv...
        10         10 --------> contains -- -h $argv
         5          5 --------> contains -- --help $argv
        11        184 -------> if not set -q argv[1]...
         5          5 --------> not set -q argv[1]
       142        142 --------> bind --erase --all --preset
         5         26 --------> if test "$fish_key_bindings" != fish_default_key_bindings...
        21         21 ---------> test "$fish_key_bindings" != fish_default_key_bindings
       798      13492 -------> eval "$(__fish_shared_key_bindings)" $argv
       261        534 --------> __fish_shared_key_bindings
        24         24 ---------> function __fish_shared_key_bindings -d "Prints function body for bindings shared between emacs and vi mode"...
       249        249 ---------> printf %s '
                                 if contains -- -h $argv
                                     or contains -- --help $argv
                                     echo "Sorry but this function doesn\'t support -h or --help" >&2
                                     return 1
                                 end
                                 bind --preset $argv ctrl-y yank
                                 or return # protect against invalid $argv
                                 bind --preset $argv alt-y yank-pop
                                 
                                  # Left/Right arrow
                                 bind --preset $argv right forward-char
                                 bind --preset $argv left backward-char
                                 
                                  # Ctrl-left/right - these also work in vim.
                                 bind --preset $argv ctrl-right forward-token
                                 bind --preset $argv ctrl-left backward-token
                                 
                                 bind --preset $argv pageup beginning-of-history
                                 bind --preset $argv pagedown end-of-history
                                 
                                  # Interaction with the system clipboard.
                                 bind --preset $argv ctrl-x fish_clipboard_copy
                                 bind --preset $argv ctrl-v fish_clipboard_paste
                                 
                                 bind --preset $argv escape cancel
                                 bind --preset $argv ctrl-\[ cancel
                                 bind --preset $argv tab complete
                                 bind --preset $argv ctrl-i complete
                                 bind --preset $argv ctrl-s pager-toggle-search
                                  # shift-tab does a tab complete followed by a search.
                                 bind --preset $argv shift-tab complete-and-search
                                 bind --preset $argv shift-delete history-delete or backward-delete-char
                                 
                                 bind --preset $argv down down-or-search
                                 bind --preset $argv up up-or-search
                                 
                                 bind --preset $argv shift-right forward-bigword
                                 bind --preset $argv shift-left backward-bigword
                                 
                                 bind --preset $argv alt-b prevd-or-backward-word
                                 bind --preset $argv alt-f nextd-or-forward-word
                                 
                                 for alt_right in alt-right \e\[1\;9C  # TODO(terminal-workaround) iTerm2 < 3.5.12
                                     bind --preset $argv $alt_right nextd-or-forward-word
                                 end
                                 for alt_left in alt-left \e\[1\;9D  # TODO(terminal-workaround) iTerm2 < 3.5.12
                                     bind --preset $argv $alt_left prevd-or-backward-word
                                 end
                                 
                                 bind --preset $argv alt-up history-token-search-backward
                                 bind --preset $argv alt-down history-token-search-forward
                                  # TODO(terminal-workaround)
                                 bind --preset $argv \e\[1\;9A history-token-search-backward  # iTerm2 < 3.5.12
                                 bind --preset $argv \e\[1\;9B history-token-search-forward  # iTerm2 < 3.5.12
                                  # Bash compatibility
                                  # https://github.com/fish-shell/fish-shell/issues/89
                                 bind --preset $argv alt-. history-token-search-backward
                                 
                                 bind --preset $argv alt-l __fish_list_current_token
                                 bind --preset $argv alt-o __fish_preview_current_file
                                 bind --preset $argv alt-w __fish_whatis_current_token
                                 bind --preset $argv ctrl-l \
                                     "status test-terminal-feature scroll-content-up && commandline -f scrollback-push" \
                                     clear-screen
                                 bind --preset $argv ctrl-c clear-commandline
                                 bind --preset $argv ctrl-u backward-kill-line
                                 bind --preset $argv ctrl-k kill-line
                                 bind --preset $argv ctrl-w backward-kill-path-component
                                 bind --preset $argv end end-of-line
                                 bind --preset $argv home beginning-of-line
                                 
                                 bind --preset $argv alt-d \'if test "$(commandline; printf .)" = \n.; __fish_echo dirh; else; commandline -f kill-word; end\'
                                 bind --preset $argv ctrl-d delete-or-exit
                                 
                                 bind --preset $argv alt-s \'for cmd in sudo doas please run0; if command -q $cmd; fish_commandline_prepend $cmd; break; end; end\'
                                 
                                  # Allow reading manpages by pressing f1 (many GUI applications) or Alt+h (like in zsh).
                                 bind --preset $argv f1 __fish_man_page
                                 bind --preset $argv alt-h __fish_man_page
                                 
                                  # This will make sure the output of the current command is paged using the default pager when
                                  # you press Meta-p.
                                  # If none is set, less will be used.
                                 bind --preset $argv alt-p __fish_paginate
                                 
                                  # Make it easy to turn an unexecuted command into a comment in the shell history. Also,
                                  # remove the commenting chars so the command can be further edited then executed.
                                 bind --preset $argv alt-# __fish_toggle_comment_commandline
                                 
                                  # These keystrokes invoke an external editor on the command buffer.
                                 bind --preset $argv alt-e edit_command_buffer
                                 bind --preset $argv alt-v edit_command_buffer
                                 
                                  # Bindings that are shared in text-insertion modes.
                                 if not set -l index (contains --index -- -M $argv)
                                     or test $argv[(math $index + 1)] = insert
                                 
                                      # This is the default binding, i.e. the one used if no other binding matches
                                     bind --preset $argv "" self-insert
                                     or exit # protect against invalid $argv
                                 
                                      # Space and other command terminators expands abbrs _and_ inserts itself.
                                     bind --preset $argv space self-insert expand-abbr
                                     bind --preset $argv ";" self-insert expand-abbr
                                     bind --preset $argv "|" self-insert expand-abbr
                                     bind --preset $argv "&" self-insert expand-abbr
                                     bind --preset $argv ">" self-insert expand-abbr
                                     bind --preset $argv "<" self-insert expand-abbr
                                     set -l maybe_search_field "(commandline --search-field >/dev/null && echo --search-field)"
                                     bind --preset $argv shift-enter "commandline -i \n $maybe_search_field"  expand-abbr
                                     bind --preset $argv alt-enter "commandline -i \n $maybe_search_field"  expand-abbr
                                     bind --preset $argv ")" self-insert expand-abbr  # Closing a command substitution.
                                     bind --preset $argv ctrl-space \'test -n "$(commandline)" && commandline -i " " \'$maybe_search_field
                                      # Shift-space behaves like space because it\'s easy to mistype.
                                     bind --preset $argv shift-space \'commandline -i " " \'$maybe_search_field expand-abbr
                                 
                                     bind --preset $argv enter execute
                                     bind --preset $argv ctrl-j execute
                                     bind --preset $argv ctrl-m execute
                                      # Make Control+Return behave like Return because it\'s easy to mistype after accepting an autosuggestion.
                                     bind --preset $argv ctrl-enter execute
                                 end'
        16         61 --------> if contains -- -h $argv...
        38         38 ---------> contains -- -h $argv
         7          7 ---------> contains -- --help $argv
        15         15 --------> bind --preset $argv ctrl-y yank
         7          7 --------> bind --preset $argv alt-y yank-pop
         5          5 --------> bind --preset $argv right forward-char
         5          5 --------> bind --preset $argv left backward-char
         5          5 --------> bind --preset $argv ctrl-right forward-token
         5          5 --------> bind --preset $argv ctrl-left backward-token
         6          6 --------> bind --preset $argv pageup beginning-of-history
         6          6 --------> bind --preset $argv pagedown end-of-history
         4          4 --------> bind --preset $argv ctrl-x fish_clipboard_copy
         5          5 --------> bind --preset $argv ctrl-v fish_clipboard_paste
         4          4 --------> bind --preset $argv escape cancel
        10         10 --------> bind --preset $argv ctrl-\[ cancel
         6          6 --------> bind --preset $argv tab complete
         4          4 --------> bind --preset $argv ctrl-i complete
         4          4 --------> bind --preset $argv ctrl-s pager-toggle-search
         5          5 --------> bind --preset $argv shift-tab complete-and-search
         6          6 --------> bind --preset $argv shift-delete history-delete or backward-delete-char
         4          4 --------> bind --preset $argv down down-or-search
         5          5 --------> bind --preset $argv up up-or-search
         5          5 --------> bind --preset $argv shift-right forward-bigword
         5          5 --------> bind --preset $argv shift-left backward-bigword
         6          6 --------> bind --preset $argv alt-b prevd-or-backward-word
         6          6 --------> bind --preset $argv alt-f nextd-or-forward-word
        27         60 --------> for alt_right in alt-right \e\[1\;9C  # TODO(terminal-workaround) iTerm2 < 3.5.12...
        21         21 ---------> bind --preset $argv $alt_right nextd-or-forward-word
        12         12 ---------> bind --preset $argv $alt_right nextd-or-forward-word
        13         36 --------> for alt_left in alt-left \e\[1\;9D  # TODO(terminal-workaround) iTerm2 < 3.5.12...
        14         14 ---------> bind --preset $argv $alt_left prevd-or-backward-word
         9          9 ---------> bind --preset $argv $alt_left prevd-or-backward-word
         6          6 --------> bind --preset $argv alt-up history-token-search-backward
         7          7 --------> bind --preset $argv alt-down history-token-search-forward
         6          6 --------> bind --preset $argv \e\[1\;9A history-token-search-backward
         7          7 --------> bind --preset $argv \e\[1\;9B history-token-search-forward
         5          5 --------> bind --preset $argv alt-. history-token-search-backward
        18         18 --------> bind --preset $argv alt-l __fish_list_current_token
         9          9 --------> bind --preset $argv alt-o __fish_preview_current_file
         5          5 --------> bind --preset $argv alt-w __fish_whatis_current_token
        12         12 --------> bind --preset $argv ctrl-l \
                                    "status test-terminal-feature scroll-content-up && commandline -f scrollback-push" \
                                    clear-screen
         6          6 --------> bind --preset $argv ctrl-c clear-commandline
         6          6 --------> bind --preset $argv ctrl-u backward-kill-line
         4          4 --------> bind --preset $argv ctrl-k kill-line
         5          5 --------> bind --preset $argv ctrl-w backward-kill-path-component
         5          5 --------> bind --preset $argv end end-of-line
         5          5 --------> bind --preset $argv home beginning-of-line
         8          8 --------> bind --preset $argv alt-d 'if test "$(commandline; printf .)" = \n.; __fish_echo dirh; else; commandline -f kill-word; end'
         5          5 --------> bind --preset $argv ctrl-d delete-or-exit
         7          7 --------> bind --preset $argv alt-s 'for cmd in sudo doas please run0; if command -q $cmd; fish_commandline_prepend $cmd; break; end; end'
         6          6 --------> bind --preset $argv f1 __fish_man_page
         5          5 --------> bind --preset $argv alt-h __fish_man_page
         5          5 --------> bind --preset $argv alt-p __fish_paginate
         8          8 --------> bind --preset $argv alt-# __fish_toggle_comment_commandline
         5          5 --------> bind --preset $argv alt-e edit_command_buffer
         5          5 --------> bind --preset $argv alt-v edit_command_buffer
       415      11710 --------> if not set -l index (contains --index -- -M $argv)...
      1549       1676 ---------> not set -l index (contains --index -- -M $argv)
       127        127 ----------> contains --index -- -M $argv
       180        180 ---------> bind --preset $argv "" self-insert
      2729       2729 ---------> bind --preset $argv space self-insert expand-abbr
       124        124 ---------> bind --preset $argv ";" self-insert expand-abbr
        97         97 ---------> bind --preset $argv "|" self-insert expand-abbr
        74         74 ---------> bind --preset $argv "&" self-insert expand-abbr
       636        636 ---------> bind --preset $argv ">" self-insert expand-abbr
       107        107 ---------> bind --preset $argv "<" self-insert expand-abbr
        79         79 ---------> set -l maybe_search_field "(commandline --search-field >/dev/null && echo --search-field)"
      4844       4844 ---------> bind --preset $argv shift-enter "commandline -i \n $maybe_search_field"  expand-abbr
       178        178 ---------> bind --preset $argv alt-enter "commandline -i \n $maybe_search_field"  expand-abbr
       110        110 ---------> bind --preset $argv ")" self-insert expand-abbr
       110        110 ---------> bind --preset $argv ctrl-space 'test -n "$(commandline)" && commandline -i " " '$maybe_search_field
        87         87 ---------> bind --preset $argv shift-space 'commandline -i " " '$maybe_search_field expand-abbr
        51         51 ---------> bind --preset $argv enter execute
       119        119 ---------> bind --preset $argv ctrl-j execute
        59         59 ---------> bind --preset $argv ctrl-m execute
        35         35 ---------> bind --preset $argv ctrl-enter execute
        47         47 -------> bind --preset $argv right forward-char
        29         29 -------> bind --preset $argv left backward-char
        33         33 -------> bind --preset $argv delete delete-char
        34         34 -------> bind --preset $argv backspace backward-delete-char
        28         28 -------> bind --preset $argv shift-backspace backward-delete-char
        27         27 -------> bind --preset $argv home beginning-of-line
        25         25 -------> bind --preset $argv end end-of-line
        25         25 -------> bind --preset $argv ctrl-a beginning-of-line
        23         23 -------> bind --preset $argv ctrl-e end-of-line
        27         27 -------> bind --preset $argv ctrl-h backward-delete-char
        53         53 -------> bind --preset $argv ctrl-p up-or-search
        37         37 -------> bind --preset $argv ctrl-n down-or-search
        28         28 -------> bind --preset $argv ctrl-f forward-char
        27         27 -------> bind --preset $argv ctrl-b backward-char
        26         26 -------> bind --preset $argv ctrl-t transpose-chars
        25         25 -------> bind --preset $argv ctrl-g cancel
        26         26 -------> bind --preset $argv ctrl-/ undo
       256        256 -------> bind --preset $argv ctrl-_ undo
        83         83 -------> bind --preset $argv ctrl-z undo
        33         33 -------> bind --preset $argv ctrl-shift-z redo
        86         86 -------> bind --preset $argv alt-/ redo
        30         30 -------> bind --preset $argv alt-t transpose-words
        35         35 -------> bind --preset $argv alt-u upcase-word
        43         43 -------> bind --preset $argv alt-c capitalize-word
        29         29 -------> bind --preset $argv alt-backspace backward-kill-word
        27         27 -------> bind --preset $argv ctrl-alt-h backward-kill-word
        80         80 -------> bind --preset $argv ctrl-backspace backward-kill-token
        35         35 -------> bind --preset $argv alt-delete kill-word
        26         26 -------> bind --preset $argv ctrl-delete kill-token
        41         41 -------> bind --preset $argv alt-\< beginning-of-buffer
        32         32 -------> bind --preset $argv alt-\> end-of-buffer
        29         29 -------> bind --preset $argv ctrl-r history-pager
        49         91 -------> switch "$TERM"...
        42         42 --------> bind --preset $argv \e\x20ep fish_clipboard_paste
        67       2209 ------> if functions --query fish_user_key_bindings >/dev/null...
      2142       2142 -------> functions --query fish_user_key_bindings >/dev/null
        52         52 ----> return
        32       1258 --> if not set -q fish_handle_reflow...
        48         48 ---> not set -q fish_handle_reflow
        70       1178 ---> if string match -rq -- '^(?:VTE\b|Konsole |WezTerm )' (status terminal)...
       714        781 ----> string match -rq -- '^(?:VTE\b|Konsole |WezTerm )' (status terminal)
        67         67 -----> status terminal
        45        192 ----> ...
       147        147 -----> set -q KONSOLE_VERSION
        87         87 ----> string match -q -- 'alacritty*' $TERM
        48         48 ----> set -g fish_handle_reflow 1
        71         71 --> function __fish_winch_handler --on-signal WINCH -d "Repaint screen when window changes size"...
       305        822 --> if not functions --query __fish_update_cwd_osc...
       401        401 ---> not functions --query __fish_update_cwd_osc
       116        116 ---> function __fish_update_cwd_osc --description 'Notify terminals when $PWD might have changed' \
                                       --on-variable=PWD --on-event=fish_prompt...
       137      10475 --> __fish_update_cwd_osc
       162        162 ---> set -l host $hostname
        19         58 ---> if set -q KONSOLE_VERSION...
        39         39 ----> set -q KONSOLE_VERSION
        32        187 ---> if [ -n "$MSYSTEM" ]...
       155        155 ----> [ -n "$MSYSTEM" ]
        22        187 ---> if [ "$TERM" = dumb ]...
       165        165 ----> [ "$TERM" = dumb ]
      9653       9744 ---> printf \e\]7\;file://%s%s\a (string escape --style=url -- $host $PWD)
        91         91 ----> string escape --style=url -- $host $PWD
        56         56 > function fish_mode_prompt --description "Displays the current mode"...
       113       1222 > fish_mode_prompt
       854       1109 -> fish_default_mode_prompt
        77         77 --> function fish_default_mode_prompt --description "Display vi prompt mode"...
        46        178 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
       105        105 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
        27         27 ---> return
        85         85 > function fish_prompt --description 'Write out the prompt'...
       320     127215 > fish_prompt
       112        112 -> set -l last_pipestatus $pipestatus
        66         66 -> set -lx __fish_last_status $status
       758        920 -> set -l normal (set_color --reset)
       162        162 --> set_color --reset
       344        344 -> set -l color_cwd $fish_color_cwd
       122        122 -> set -l suffix '>'
        45       1491 -> if functions -q fish_is_root_user...
       762        858 --> functions -q fish_is_root_user
        96         96 ---> function fish_is_root_user --description "Check if the user is root"...
       128        588 --> fish_is_root_user
        46        286 ---> if test "$EUID" = 0 2>/dev/null...
       240        240 ----> test "$EUID" = 0 2>/dev/null
        26        146 ---> if contains -- $USER root toor Administrator...
       120        120 ----> contains -- $USER root toor Administrator
        28         28 ---> return 1
        59         59 -> set -l bold_flag --bold
        41         41 -> set -q __fish_prompt_status_generation
       225        225 -> set -g __fish_prompt_status_generation $status_generation
        44        161 -> if test $__fish_prompt_status_generation = $status_generation...
        75         75 --> test $__fish_prompt_status_generation = $status_generation
        42         42 --> set bold_flag
        71         71 -> set __fish_prompt_status_generation $status_generation
      1939       2077 -> set -l status_color (set_color $fish_color_status)
       138        138 --> set_color $fish_color_status
      1258       1424 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
       166        166 --> set_color $bold_flag $fish_color_status
       227        744 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
       372        517 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        31         31 ---> function __fish_print_pipestatus --description "Print pipestatus for prompt"...
        25         25 ---> set -l last_status
         6         23 ---> if set -q __fish_last_status...
         7          7 ----> set -q __fish_last_status
        10         10 ----> set last_status $__fish_last_status
         9          9 ---> set -l left_brace $argv[1]
         7          7 ---> set -l right_brace $argv[2]
         6          6 ---> set -l separator $argv[3]
         7          7 ---> set -l brace_sep_color $argv[4]
         7          7 ---> set -l status_color $argv[5]
         7          7 ---> set -e argv[1 2 3 4 5]
         3          6 ---> if not set -q argv[1]...
         3          3 ----> not set -q argv[1]
         3         17 ---> if not contains $last_status 0 141...
        14         14 ----> not contains $last_status 0 141
       604     119038 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
      1553       6429 --> prompt_login
        38         38 ---> function prompt_login --description "display user name for the prompt"...
        17        163 ---> if not set -q __fish_machine...
        21         21 ----> not set -q __fish_machine
         9          9 ----> set -g __fish_machine
         9          9 ----> set -l debian_chroot $debian_chroot
        12         91 ----> if test -r /etc/debian_chroot...
        79         79 -----> test -r /etc/debian_chroot
         4         16 ----> if set -q debian_chroot[1]...
        12         12 -----> set -q debian_chroot[1]
         2          6 ---> if set -q __fish_machine[1]...
         4          4 ----> set -q __fish_machine[1]
        18         18 ---> set -l color_host $fish_color_host
         2          6 ---> if set -q SSH_TTY...
         4          4 ----> set -q SSH_TTY
      3948       4645 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        91         91 ----> set_color $fish_color_user
        72         72 ----> set_color --reset
        48         48 ----> set_color $color_host
       296        426 ----> prompt_hostname
        33         33 -----> function prompt_hostname --description 'short hostname for the prompt'...
        97         97 -----> string replace -r -- "\..*" "" $hostname
        60         60 ----> set_color --reset
        62         62 --> set_color $color_cwd
       383       7689 --> prompt_pwd
        50         50 ---> function prompt_pwd --description 'short CWD for the prompt'...
        32         32 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        31         31 ---> argparse -n prompt_pwd $options -- $argv
         6         44 ---> if set -q _flag_help...
        38         38 ----> set -q _flag_help
         7          7 ---> set -q argv[1]
        15         15 ---> set argv $PWD
        27         27 ---> set -ql _flag_d
         6          6 ---> set -q fish_prompt_pwd_dir_length
         7          7 ---> set -l fish_prompt_pwd_dir_length 1
         4          4 ---> set -l fulldirs 0
         3          3 ---> set -ql _flag_D
         3          3 ---> set -q fish_prompt_pwd_full_dirs
         5          5 ---> set -l fish_prompt_pwd_full_dirs 1
        27       7072 ---> for path in $argv...
       278       1475 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       546       1197 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
        22         22 ------> function __fish_unexpand_tilde --description 'Replace $HOME with "~"'...
       216        497 ------> set -l realhome (string escape --style=regex -- ~)
       281        281 -------> string escape --style=regex -- ~
       132        132 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        26       5570 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        28         28 -----> test "$fish_prompt_pwd_dir_length" -eq 0
         7          7 -----> set -l full
        22       5206 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        58         58 ------> test $fish_prompt_pwd_full_dirs -gt 0
       608       5095 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
      2135       4487 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
      2352       2352 --------> math $fish_prompt_pwd_full_dirs - 1
        24         24 ------> set tmp $all[1]
         7          7 ------> set full $all[2..]
       221        303 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        82         82 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
       205     104254 --> fish_vcs_prompt
        18         18 ---> function fish_vcs_prompt --description "Print all vcs prompts"...
       523       1921 ---> fish_jj_prompt $argv
        23         23 ----> function fish_jj_prompt...
        29       1375 ----> if not command -sq jj...
      1315       1315 -----> not command -sq jj
        31         31 -----> return 1
      2265     102110 ---> fish_git_prompt $argv
        47         47 ----> function __fish_git_prompt_show_upstream --description "Helper function for fish_git_prompt"...
        25      16505 ----> if string match -q Darwin -- (__fish_uname)...
       293      16480 -----> string match -q Darwin -- (__fish_uname)
       202      16187 ------> __fish_uname
        12         12 -------> function __fish_uname...
        27      15937 -------> if not set -q __fish_uname...
        18         18 --------> not set -q __fish_uname
       358      15892 --------> set -g __fish_uname (uname)
     15534      15534 ---------> uname
        36         36 -------> echo -- $__fish_uname
        57         57 ----> function fish_git_prompt --description "Prompt function for Git"...
         5          5 ----> function __fish_git_prompt_status_porcelain_modulo_rename_source...
        10         10 ----> function __fish_git_prompt_informative_status...
        23         23 ----> function __fish_git_prompt_operation_branch_bare --description "fish_git_prompt helper, returns the current Git operation and branch"...
         5          5 ----> function __fish_git_prompt_set_char...
         9          9 ----> function __fish_git_prompt_validate_chars --description "fish_git_prompt helper, checks char variables"...
         5          5 ----> function __fish_git_prompt_set_color...
         6          6 ----> function __fish_git_prompt_validate_colors --description "fish_git_prompt helper, checks color variables"...
        29         29 ----> function __fish_git_prompt_reset -a type -a op -a var --description "Event handler, resets prompt when functionality changes" \
                                --on-variable=__fish_git_prompt_{show_informative_status,use_informative_chars}...
        68         68 ----> function __fish_git_prompt_reset_color -a type -a op -a var --description "Event handler, resets prompt when any color changes" \
                                --on-variable=__fish_git_prompt_color{'',_prefix,_suffix,_bare,_merging,_cleanstate,_invalidstate,_upstream,_flags,_branch,_dirtystate,_stagedstate,_branch_detached,_stashstate,_untrackedfiles} --on-variable=__fish_git_prompt_showcolorhints...
        42         42 ----> function __fish_git_prompt_reset_char -a type -a op -a var --description "Event handler, resets prompt when any char changes" \
                                --on-variable=__fish_git_prompt_char_{cleanstate,dirtystate,invalidstate,stagedstate,stashstate,stateseparator,untrackedfiles,upstream_ahead,upstream_behind,upstream_diverged,upstream_equal,upstream_prefix}...
        33       1698 ----> if not command -sq git...
      1665       1665 -----> not command -sq git
        17        174 ----> if functions -q __fish_git_prompt_ready...
       157        157 -----> functions -q __fish_git_prompt_ready
       373      31942 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     31569      31569 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        33         33 ----> test -n "$repo_info"
        18         18 ----> set -l git_dir $repo_info[1]
         8          8 ----> set -l git_common_dir $repo_info[2]
         6          6 ----> set -l inside_gitdir $repo_info[3]
         6          6 ----> set -l bare_repo $repo_info[4]
        10         10 ----> set -l inside_worktree $repo_info[5]
         4          4 ----> set -q repo_info[6]
         9          9 ----> set -l sha $repo_info[6]
       287      15783 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
        85      15496 -----> __fish_git_prompt_operation_branch_bare $repo_info
        19         19 ------> set -l git_dir $argv[1]
         7          7 ------> set -l inside_gitdir $argv[3]
         7          7 ------> set -l bare_repo $argv[4]
         4          4 ------> set -q argv[6]
         7          7 ------> set -l sha $argv[6]
         4          4 ------> set -l branch
         6          6 ------> set -l operation
         5          5 ------> set -l detached no
         4          4 ------> set -l bare
         4          4 ------> set -l step
         3          3 ------> set -l total
        14        172 ------> if test -d $git_dir/rebase-merge...
        58         58 -------> test -d $git_dir/rebase-merge
        20        100 -------> if test -d $git_dir/rebase-apply...
        28         28 --------> test -d $git_dir/rebase-apply
        17         17 --------> test -f $git_dir/MERGE_HEAD
        13         13 --------> test -f $git_dir/CHERRY_PICK_HEAD
        11         11 --------> test -f $git_dir/REVERT_HEAD
        11         11 --------> test -f $git_dir/BISECT_LOG
         3         18 ------> if test -n "$step" -a -n "$total"...
        15         15 -------> test -n "$step" -a -n "$total"
         6      14983 ------> if test -z "$branch"...
         5          5 -------> test -z "$branch"
        25      14972 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       350      14947 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     14597      14597 ---------> command git symbolic-ref HEAD 2>/dev/null
         6         39 ------> if test true = $inside_gitdir...
        33         33 -------> test true = $inside_gitdir
        24         24 ------> echo $operation
        91         91 ------> echo $branch
         9          9 ------> echo $detached
         5          5 ------> echo $bare
        21         21 ----> set -l operation $branch_state[1]
         8          8 ----> set -l branch $branch_state[2]
         6          6 ----> set -l detached $branch_state[3]
         4          4 ----> set -l dirtystate
        14         14 ----> set -l stagedstate
         4          4 ----> set -l invalidstate
         3          3 ----> set -l stashstate
         4          4 ----> set -l untrackedfiles
         6          6 ----> set -l bare_prefix $branch_state[4]
         4          4 ----> set -l upstream
         4          4 ----> set -l informative_status
         5          5 ----> set -q __fish_git_prompt_status_order
        18         18 ----> set -g __fish_git_prompt_status_order stagedstate invalidstate dirtystate untrackedfiles stashstate
        22      17644 ----> if not set -q ___fish_git_prompt_init...
         5          5 -----> not set -q ___fish_git_prompt_init
        41       4102 -----> __fish_git_prompt_validate_chars
        17         17 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        44        361 ------> __fish_git_prompt_set_char __fish_git_prompt_char_cleanstate ''
        13         13 -------> set -l user_variable_name "$argv[1]"
         7          7 -------> set -l char $argv[2]
         8         12 -------> if set -q argv[3]...
         4          4 --------> set -q argv[3]
         8          8 -------> set -l variable _$user_variable_name
        10         10 -------> set -l variable_done "$variable"_done
        12        267 -------> if not set -q $variable...
         6          6 --------> not set -q $variable
       217        249 --------> set -g $variable (set -q $user_variable_name; and echo $$user_variable_name; or echo $char)
        20         20 ---------> set -q $user_variable_name
        12         12 ---------> echo $char
        28        359 ------> __fish_git_prompt_set_char __fish_git_prompt_char_dirtystate '*' '✚'
        14         14 -------> set -l user_variable_name "$argv[1]"
        35         35 -------> set -l char $argv[2]
         4         42 -------> if set -q argv[3]...
         6          6 --------> set -q argv[3]
        10         32 --------> ...
        15         15 ---------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
         7          7 ---------> contains -- "$__fish_git_prompt_use_informative_chars" yes true 1
         9          9 -------> set -l variable _$user_variable_name
        15         15 -------> set -l variable_done "$variable"_done
         7        216 -------> if not set -q $variable...
         7          7 --------> not set -q $variable
       177        202 --------> set -g $variable (set -q $user_variable_name; and echo $$user_variable_name; or echo $char)
        15         15 ---------> set -q $user_variable_name
        10         10 ---------> echo $char
        24        292 ------> __fish_git_prompt_set_char __fish_git_prompt_char_invalidstate '#' '✖'
        12         12 -------> set -l user_variable_name "$argv[1]"
         7          7 -------> set -l char $argv[2]
         3         30 -------> if set -q argv[3]...
         4          4 --------> set -q argv[3]
         6         23 --------> ...
        11         11 ---------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
         6          6 ---------> contains -- "$__fish_git_prompt_use_informative_chars" yes true 1
         7          7 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         7        205 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
       170        193 --------> set -g $variable (set -q $user_variable_name; and echo $$user_variable_name; or echo $char)
        14         14 ---------> set -q $user_variable_name
         9          9 ---------> echo $char
        27        272 ------> __fish_git_prompt_set_char __fish_git_prompt_char_stagedstate '+' '●'
        11         11 -------> set -l user_variable_name "$argv[1]"
         7          7 -------> set -l char $argv[2]
         4         30 -------> if set -q argv[3]...
         4          4 --------> set -q argv[3]
         6         22 --------> ...
        10         10 ---------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
         6          6 ---------> contains -- "$__fish_git_prompt_use_informative_chars" yes true 1
         8          8 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         6        182 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
       152        171 --------> set -g $variable (set -q $user_variable_name; and echo $$user_variable_name; or echo $char)
        11         11 ---------> set -q $user_variable_name
         8          8 ---------> echo $char
        24        282 ------> __fish_git_prompt_set_char __fish_git_prompt_char_stashstate '$' '⚑'
        11         11 -------> set -l user_variable_name "$argv[1]"
         7          7 -------> set -l char $argv[2]
         4         29 -------> if set -q argv[3]...
         3          3 --------> set -q argv[3]
         5         22 --------> ...
        10         10 ---------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
         7          7 ---------> contains -- "$__fish_git_prompt_use_informative_chars" yes true 1
         8          8 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         6        196 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
       139        185 --------> set -g $variable (set -q $user_variable_name; and echo $$user_variable_name; or echo $char)
        36         36 ---------> set -q $user_variable_name
        10         10 ---------> echo $char
        46        323 ------> __fish_git_prompt_set_char __fish_git_prompt_char_stateseparator ' ' '|'
        34         34 -------> set -l user_variable_name "$argv[1]"
         8          8 -------> set -l char $argv[2]
         6         36 -------> if set -q argv[3]...
         3          3 --------> set -q argv[3]
         6         27 --------> ...
        10         10 ---------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        11         11 ---------> contains -- "$__fish_git_prompt_use_informative_chars" yes true 1
        10         10 -------> set -l variable _$user_variable_name
         8          8 -------> set -l variable_done "$variable"_done
         7        181 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
       148        169 --------> set -g $variable (set -q $user_variable_name; and echo $$user_variable_name; or echo $char)
        12         12 ---------> set -q $user_variable_name
         9          9 ---------> echo $char
        60        327 ------> __fish_git_prompt_set_char __fish_git_prompt_char_untrackedfiles '%' '…'
        18         18 -------> set -l user_variable_name "$argv[1]"
         8          8 -------> set -l char $argv[2]
         4         30 -------> if set -q argv[3]...
         4          4 --------> set -q argv[3]
         6         22 --------> ...
        10         10 ---------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
         6          6 ---------> contains -- "$__fish_git_prompt_use_informative_chars" yes true 1
         8          8 -------> set -l variable _$user_variable_name
        14         14 -------> set -l variable_done "$variable"_done
         8        189 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
       154        176 --------> set -g $variable (set -q $user_variable_name; and echo $$user_variable_name; or echo $char)
        13         13 ---------> set -q $user_variable_name
         9          9 ---------> echo $char
        59        394 ------> __fish_git_prompt_set_char __fish_git_prompt_char_upstream_ahead '>' '↑'
        11         11 -------> set -l user_variable_name "$argv[1]"
         6          6 -------> set -l char $argv[2]
         6         59 -------> if set -q argv[3]...
         5          5 --------> set -q argv[3]
         8         48 --------> ...
        33         33 ---------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
         7          7 ---------> contains -- "$__fish_git_prompt_use_informative_chars" yes true 1
        10         10 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         8        242 -------> if not set -q $variable...
         6          6 --------> not set -q $variable
       193        228 --------> set -g $variable (set -q $user_variable_name; and echo $$user_variable_name; or echo $char)
        14         14 ---------> set -q $user_variable_name
        21         21 ---------> echo $char
        26        318 ------> __fish_git_prompt_set_char __fish_git_prompt_char_upstream_behind '<' '↓'
        11         11 -------> set -l user_variable_name "$argv[1]"
         7          7 -------> set -l char $argv[2]
         5         60 -------> if set -q argv[3]...
         3          3 --------> set -q argv[3]
         7         52 --------> ...
        36         36 ---------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
         9          9 ---------> contains -- "$__fish_git_prompt_use_informative_chars" yes true 1
         8          8 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         8        199 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
       160        186 --------> set -g $variable (set -q $user_variable_name; and echo $$user_variable_name; or echo $char)
        16         16 ---------> set -q $user_variable_name
        10         10 ---------> echo $char
        23        267 ------> __fish_git_prompt_set_char __fish_git_prompt_char_upstream_diverged '<>' '↓↑'
        11         11 -------> set -l user_variable_name "$argv[1]"
         9          9 -------> set -l char $argv[2]
         4         29 -------> if set -q argv[3]...
         4          4 --------> set -q argv[3]
         6         21 --------> ...
         9          9 ---------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
         6          6 ---------> contains -- "$__fish_git_prompt_use_informative_chars" yes true 1
         7          7 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         6        181 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
       147        170 --------> set -g $variable (set -q $user_variable_name; and echo $$user_variable_name; or echo $char)
        13         13 ---------> set -q $user_variable_name
        10         10 ---------> echo $char
        20        216 ------> __fish_git_prompt_set_char __fish_git_prompt_char_upstream_equal '='
        13         13 -------> set -l user_variable_name "$argv[1]"
         6          6 -------> set -l char $argv[2]
         4          7 -------> if set -q argv[3]...
         3          3 --------> set -q argv[3]
         7          7 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         6        156 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
       127        145 --------> set -g $variable (set -q $user_variable_name; and echo $$user_variable_name; or echo $char)
        10         10 ---------> set -q $user_variable_name
         8          8 ---------> echo $char
       280        633 ------> __fish_git_prompt_set_char __fish_git_prompt_char_upstream_prefix ''
        10         10 -------> set -l user_variable_name "$argv[1]"
         7          7 -------> set -l char $argv[2]
         4          7 -------> if set -q argv[3]...
         3          3 --------> set -q argv[3]
         7          7 -------> set -l variable _$user_variable_name
        26         26 -------> set -l variable_done "$variable"_done
        16        296 -------> if not set -q $variable...
        38         38 --------> not set -q $variable
       202        242 --------> set -g $variable (set -q $user_variable_name; and echo $$user_variable_name; or echo $char)
        26         26 ---------> set -q $user_variable_name
        14         14 ---------> echo $char
        42      13506 -----> __fish_git_prompt_validate_colors
        44        352 ------> __fish_git_prompt_set_color __fish_git_prompt_color '' ''
        14         14 -------> set -l user_variable_name "$argv[1]"
         4          4 -------> set -l default
         4          4 -------> set -l default_done
       152        200 -------> switch (count $argv)...
        21         21 --------> count $argv
        19         19 --------> set default "$argv[2]"
         8          8 --------> set default_done "$argv[3]"
        10         10 -------> set -l variable _$user_variable_name
        22         22 -------> set -l variable_done "$variable"_done
         6         54 -------> if not set -q $variable...
        10         10 --------> not set -q $variable
         8         38 --------> if test -n "$$user_variable_name"...
        11         11 ---------> test -n "$$user_variable_name"
        10         10 ---------> set -g $variable $default
         9          9 ---------> set -g $variable_done $default_done
        34        318 ------> __fish_git_prompt_set_color __fish_git_prompt_color_prefix
        10         10 -------> set -l user_variable_name "$argv[1]"
         5          5 -------> set -l default
         3          3 -------> set -l default_done
       141        181 -------> switch (count $argv)...
        18         18 --------> count $argv
        14         14 --------> set default $___fish_git_prompt_color
         8          8 --------> set default_done $___fish_git_prompt_color_done
         8          8 -------> set -l variable _$user_variable_name
        22         22 -------> set -l variable_done "$variable"_done
         5         55 -------> if not set -q $variable...
         7          7 --------> not set -q $variable
         9         43 --------> if test -n "$$user_variable_name"...
        10         10 ---------> test -n "$$user_variable_name"
        14         14 ---------> set -g $variable $default
        10         10 ---------> set -g $variable_done $default_done
        19        291 ------> __fish_git_prompt_set_color __fish_git_prompt_color_suffix
        18         18 -------> set -l user_variable_name "$argv[1]"
         6          6 -------> set -l default
         4          4 -------> set -l default_done
       134        176 -------> switch (count $argv)...
        21         21 --------> count $argv
        13         13 --------> set default $___fish_git_prompt_color
         8          8 --------> set default_done $___fish_git_prompt_color_done
         8          8 -------> set -l variable _$user_variable_name
         8          8 -------> set -l variable_done "$variable"_done
         5         52 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
         7         42 --------> if test -n "$$user_variable_name"...
        18         18 ---------> test -n "$$user_variable_name"
         9          9 ---------> set -g $variable $default
         8          8 ---------> set -g $variable_done $default_done
        20        266 ------> __fish_git_prompt_set_color __fish_git_prompt_color_bare
        27         27 -------> set -l user_variable_name "$argv[1]"
         5          5 -------> set -l default
         3          3 -------> set -l default_done
       115        147 -------> switch (count $argv)...
        14         14 --------> count $argv
        11         11 --------> set default $___fish_git_prompt_color
         7          7 --------> set default_done $___fish_git_prompt_color_done
         7          7 -------> set -l variable _$user_variable_name
         8          8 -------> set -l variable_done "$variable"_done
         4         49 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
         6         40 --------> if test -n "$$user_variable_name"...
         8          8 ---------> test -n "$$user_variable_name"
         8          8 ---------> set -g $variable $default
        18         18 ---------> set -g $variable_done $default_done
        24        260 ------> __fish_git_prompt_set_color __fish_git_prompt_color_merging
        10         10 -------> set -l user_variable_name "$argv[1]"
         4          4 -------> set -l default
         4          4 -------> set -l default_done
       109        139 -------> switch (count $argv)...
        12         12 --------> count $argv
        11         11 --------> set default $___fish_git_prompt_color
         7          7 --------> set default_done $___fish_git_prompt_color_done
         7          7 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         4         65 -------> if not set -q $variable...
        28         28 --------> not set -q $variable
         7         33 --------> if test -n "$$user_variable_name"...
         9          9 ---------> test -n "$$user_variable_name"
         9          9 ---------> set -g $variable $default
         8          8 ---------> set -g $variable_done $default_done
        18        231 ------> __fish_git_prompt_set_color __fish_git_prompt_color_cleanstate
         9          9 -------> set -l user_variable_name "$argv[1]"
         4          4 -------> set -l default
         4          4 -------> set -l default_done
       109        141 -------> switch (count $argv)...
        13         13 --------> count $argv
        11         11 --------> set default $___fish_git_prompt_color
         8          8 --------> set default_done $___fish_git_prompt_color_done
         8          8 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         5         40 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
         6         30 --------> if test -n "$$user_variable_name"...
         7          7 ---------> test -n "$$user_variable_name"
         9          9 ---------> set -g $variable $default
         8          8 ---------> set -g $variable_done $default_done
        16        224 ------> __fish_git_prompt_set_color __fish_git_prompt_color_invalidstate
         9          9 -------> set -l user_variable_name "$argv[1]"
         4          4 -------> set -l default
         4          4 -------> set -l default_done
        96        130 -------> switch (count $argv)...
        14         14 --------> count $argv
        12         12 --------> set default $___fish_git_prompt_color
         8          8 --------> set default_done $___fish_git_prompt_color_done
         8          8 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         4         46 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
         6         37 --------> if test -n "$$user_variable_name"...
         7          7 ---------> test -n "$$user_variable_name"
        14         14 ---------> set -g $variable $default
        10         10 ---------> set -g $variable_done $default_done
        26       9169 ------> __fish_git_prompt_set_color __fish_git_prompt_color_upstream
        10         10 -------> set -l user_variable_name "$argv[1]"
         4          4 -------> set -l default
         3          3 -------> set -l default_done
       118       9033 -------> switch (count $argv)...
        13         13 --------> count $argv
        12         12 --------> set default $___fish_git_prompt_color
      8890       8890 --------> set default_done $___fish_git_prompt_color_done
        24         24 -------> set -l variable _$user_variable_name
        10         10 -------> set -l variable_done "$variable"_done
         8         59 -------> if not set -q $variable...
         8          8 --------> not set -q $variable
         9         43 --------> if test -n "$$user_variable_name"...
        14         14 ---------> test -n "$$user_variable_name"
        11         11 ---------> set -g $variable $default
         9          9 ---------> set -g $variable_done $default_done
        12       1405 ------> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        20         20 -------> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
        22        532 -------> __fish_git_prompt_set_color __fish_git_prompt_color_flags
        13         13 --------> set -l user_variable_name "$argv[1]"
         5          5 --------> set -l default
         4          4 --------> set -l default_done
       345        420 --------> switch (count $argv)...
        24         24 ---------> count $argv
        41         41 ---------> set default $___fish_git_prompt_color
        10         10 ---------> set default_done $___fish_git_prompt_color_done
        10         10 --------> set -l variable _$user_variable_name
        10         10 --------> set -l variable_done "$variable"_done
         5         48 --------> if not set -q $variable...
         7          7 ---------> not set -q $variable
         7         36 ---------> if test -n "$$user_variable_name"...
        11         11 ----------> test -n "$$user_variable_name"
         9          9 ----------> set -g $variable $default
         9          9 ----------> set -g $variable_done $default_done
        23        285 -------> __fish_git_prompt_set_color __fish_git_prompt_color_branch
        12         12 --------> set -l user_variable_name "$argv[1]"
         5          5 --------> set -l default
         4          4 --------> set -l default_done
       140        184 --------> switch (count $argv)...
        17         17 ---------> count $argv
        18         18 ---------> set default $___fish_git_prompt_color
         9          9 ---------> set default_done $___fish_git_prompt_color_done
         8          8 --------> set -l variable _$user_variable_name
         8          8 --------> set -l variable_done "$variable"_done
         4         41 --------> if not set -q $variable...
         5          5 ---------> not set -q $variable
         7         32 ---------> if test -n "$$user_variable_name"...
         9          9 ----------> test -n "$$user_variable_name"
         8          8 ----------> set -g $variable $default
         8          8 ----------> set -g $variable_done $default_done
        43        287 -------> __fish_git_prompt_set_color __fish_git_prompt_color_dirtystate $___fish_git_prompt_color_flags $___fish_git_prompt_color_flags_done
        11         11 --------> set -l user_variable_name "$argv[1]"
         4          4 --------> set -l default
         4          4 --------> set -l default_done
       123        161 --------> switch (count $argv)...
        16         16 ---------> count $argv
        16         16 ---------> set default "$argv[2]"
         6          6 ---------> set default_done "$argv[3]"
        11         11 --------> set -l variable _$user_variable_name
        10         10 --------> set -l variable_done "$variable"_done
         5         43 --------> if not set -q $variable...
         6          6 ---------> not set -q $variable
         7         32 ---------> if test -n "$$user_variable_name"...
         8          8 ----------> test -n "$$user_variable_name"
         9          9 ----------> set -g $variable $default
         8          8 ----------> set -g $variable_done $default_done
        24        269 -------> __fish_git_prompt_set_color __fish_git_prompt_color_stagedstate $___fish_git_prompt_color_flags $___fish_git_prompt_color_flags_done
        20         20 --------> set -l user_variable_name "$argv[1]"
         4          4 --------> set -l default
         4          4 --------> set -l default_done
       125        162 --------> switch (count $argv)...
        17         17 ---------> count $argv
        13         13 ---------> set default "$argv[2]"
         7          7 ---------> set default_done "$argv[3]"
         8          8 --------> set -l variable _$user_variable_name
         7          7 --------> set -l variable_done "$variable"_done
         4         40 --------> if not set -q $variable...
         6          6 ---------> not set -q $variable
         5         30 ---------> if test -n "$$user_variable_name"...
         8          8 ----------> test -n "$$user_variable_name"
         9          9 ----------> set -g $variable $default
         8          8 ----------> set -g $variable_done $default_done
       124        483 ------> __fish_git_prompt_set_color __fish_git_prompt_color_branch_detached (set_color red)
        21         21 -------> set_color red
        15         15 -------> set -l user_variable_name "$argv[1]"
         4          4 -------> set -l default
         4          4 -------> set -l default_done
       105        241 -------> switch (count $argv)...
        15         15 --------> count $argv
        13         13 --------> set default "$argv[2]"
        93        108 --------> set default_done (set_color --reset)
        15         15 ---------> set_color --reset
        10         10 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         6         57 -------> if not set -q $variable...
         6          6 --------> not set -q $variable
        17         45 --------> if test -n "$$user_variable_name"...
         9          9 ---------> test -n "$$user_variable_name"
        10         10 ---------> set -g $variable $default
         9          9 ---------> set -g $variable_done $default_done
        28        240 ------> __fish_git_prompt_set_color __fish_git_prompt_color_stashstate $___fish_git_prompt_color_flags $___fish_git_prompt_color_flags_done
        10         10 -------> set -l user_variable_name "$argv[1]"
         4          4 -------> set -l default
         3          3 -------> set -l default_done
       100        134 -------> switch (count $argv)...
        14         14 --------> count $argv
        13         13 --------> set default "$argv[2]"
         7          7 --------> set default_done "$argv[3]"
         7          7 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         4         47 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
         7         38 --------> if test -n "$$user_variable_name"...
         8          8 ---------> test -n "$$user_variable_name"
         8          8 ---------> set -g $variable $default
        15         15 ---------> set -g $variable_done $default_done
        22        225 ------> __fish_git_prompt_set_color __fish_git_prompt_color_untrackedfiles $___fish_git_prompt_color_flags $___fish_git_prompt_color_flags_done
         8          8 -------> set -l user_variable_name "$argv[1]"
         4          4 -------> set -l default
         4          4 -------> set -l default_done
        97        128 -------> switch (count $argv)...
        13         13 --------> count $argv
        11         11 --------> set default "$argv[2]"
         7          7 --------> set default_done "$argv[3]"
         8          8 -------> set -l variable _$user_variable_name
         7          7 -------> set -l variable_done "$variable"_done
         4         44 -------> if not set -q $variable...
         5          5 --------> not set -q $variable
         6         35 --------> if test -n "$$user_variable_name"...
         7          7 ---------> test -n "$$user_variable_name"
         8          8 ---------> set -g $variable $default
        14         14 ---------> set -g $variable_done $default_done
         9          9 -----> set -g ___fish_git_prompt_init
        24         24 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         6          6 ----> set -l informative
         3          3 ----> set -l dirty
         4          4 ----> set -l untracked
      1515      14440 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     12925      12925 -----> read -lz key value
        20         92 ----> if not set -q dirty[1]...
        34         34 -----> not set -q dirty[1]
        38         38 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        23         23 ----> contains dirtystate $__fish_git_prompt_status_order
         6         21 ----> if not set -q untracked[1]...
         6          6 -----> not set -q untracked[1]
         9          9 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
         9          9 ----> contains untrackedfiles $__fish_git_prompt_status_order
         9        104 ----> if test true = $inside_worktree...
        15         15 -----> test true = $inside_worktree
         9         66 -----> if test "$informative" = true...
         7          7 ------> test "$informative" = true
         3         11 ------> ...
         8          8 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        10         25 ------> if not test "$dirty" = true...
         6          6 -------> not test "$dirty" = true
         4          4 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         7         14 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         7          7 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         4         14 -----> if set -q __fish_git_prompt_showupstream...
         4          4 ------> set -q __fish_git_prompt_showupstream
         6          6 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        14         14 ----> set -l branch_color $___fish_git_prompt_color_branch
        16         16 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         9         32 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        23         23 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         7          7 ----> set -l flags ""
        21         63 ----> for i in $__fish_git_prompt_status_order...
         5         12 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
         2          8 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          7 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
         4          8 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
         3          7 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
       208        239 ----> set branch (string replace refs/heads/ '' -- $branch)
        31         31 -----> string replace refs/heads/ '' -- $branch
       124        186 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        62         62 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       102        131 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        29         29 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        11         41 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        30         30 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         5         45 ----> if test -n "$branch"...
        11         11 -----> test -n "$branch"
        10         10 -----> set branch "$branch_color$branch$branch_done"
         6         19 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
         5          5 ------> test -n "$___fish_git_prompt_char_cleanstate"
         2          6 ----> if test -n "$bare_prefix"...
         4          4 -----> test -n "$bare_prefix"
         1          5 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         3          7 ----> if test -n "$upstream"...
         4          4 -----> test -n "$upstream"
         2          8 ----> if test -n "$flags$bare_prefix$upstream"...
         6          6 -----> test -n "$flags$bare_prefix$upstream"
         8          8 ----> set -l format $argv[1]
         5         13 ----> if test -z "$format"...
         3          3 -----> test -z "$format"
         5          5 -----> set format " (%s)"
        51         51 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        12         12 > function fish_title...
        23       1661 > fish_title
        18         18 -> set -l ssh
         5          5 -> set -q SSH_TTY
        14       1615 -> if set -q argv[1]...
         4          4 --> set -q argv[1]
       117        126 --> set -l command (status current-command)
         9          9 ---> status current-command
         6         25 --> if test "$command" = fish...
        13         13 ---> test "$command" = fish
         6          6 ---> set command
       179       1446 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        13         13 ---> string sub -l 20 -- $command
        44       1254 ---> prompt_pwd -d 1 -D 1
        11         11 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        40         40 ----> argparse -n prompt_pwd $options -- $argv
         5          9 ----> if set -q _flag_help...
         4          4 -----> set -q _flag_help
         4          4 ----> set -q argv[1]
         8          8 ----> set argv $PWD
         3          3 ----> set -ql _flag_d
        13         13 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         3          3 ----> set -q fish_prompt_pwd_dir_length
         5          5 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         6          6 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        19       1102 ----> for path in $argv...
       146        570 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       215        424 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       115        153 -------> set -l realhome (string escape --style=regex -- ~)
        38         38 --------> string escape --style=regex -- ~
        56         56 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        17        513 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        19         19 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         6          6 ------> set -l full
        14        299 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 -------> test $fish_prompt_pwd_full_dirs -gt 0
       120        258 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       107        138 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        31         31 ---------> math $fish_prompt_pwd_full_dirs - 1
        12         12 -------> set tmp $all[1]
         7          7 -------> set full $all[2..]
       120        172 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        52         52 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
       899       6148 > __fish_winch_handler SIGWINCH
       415       5249 -> if test "$fish_handle_reflow" = 1 2>/dev/null...
      1559       1559 --> test "$fish_handle_reflow" = 1 2>/dev/null
      3275       3275 --> commandline -f repaint >/dev/null 2>/dev/null
       113        480 > fish_mode_prompt
        49        367 -> fish_default_mode_prompt
        51        318 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
       259        259 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         8          8 ---> return
       121     167511 > fish_prompt
       123        123 -> set -l last_pipestatus $pipestatus
        24         24 -> set -lx __fish_last_status $status
       250        455 -> set -l normal (set_color --reset)
       205        205 --> set_color --reset
        25         25 -> set -l color_cwd $fish_color_cwd
        37         37 -> set -l suffix '>'
        32        449 -> if functions -q fish_is_root_user...
       177        177 --> functions -q fish_is_root_user
        69        240 --> fish_is_root_user
        22        139 ---> if test "$EUID" = 0 2>/dev/null...
       117        117 ----> test "$EUID" = 0 2>/dev/null
         3         25 ---> if contains -- $USER root toor Administrator...
        22         22 ----> contains -- $USER root toor Administrator
         7          7 ---> return 1
        16         16 -> set -l bold_flag --bold
       218        218 -> set -q __fish_prompt_status_generation
        10         59 -> if test $__fish_prompt_status_generation = $status_generation...
        22         22 --> test $__fish_prompt_status_generation = $status_generation
        27         27 --> set bold_flag
        22         22 -> set __fish_prompt_status_generation $status_generation
       363        412 -> set -l status_color (set_color $fish_color_status)
        49         49 --> set_color $fish_color_status
       250        456 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
       206        206 --> set_color $bold_flag $fish_color_status
       160        436 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
       114        276 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        14         14 ---> set -l last_status
        12         26 ---> if set -q __fish_last_status...
         5          5 ----> set -q __fish_last_status
         9          9 ----> set last_status $__fish_last_status
        10         10 ---> set -l left_brace $argv[1]
         6          6 ---> set -l right_brace $argv[2]
         6          6 ---> set -l separator $argv[3]
         6          6 ---> set -l brace_sep_color $argv[4]
        35         35 ---> set -l status_color $argv[5]
         9          9 ---> set -e argv[1 2 3 4 5]
         4          9 ---> if not set -q argv[1]...
         5          5 ----> not set -q argv[1]
        28         41 ---> if not contains $last_status 0 141...
        13         13 ----> not contains $last_status 0 141
       708     164658 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        59        804 --> prompt_login
        21         50 ---> if not set -q __fish_machine...
        29         29 ----> not set -q __fish_machine
         4          8 ---> if set -q __fish_machine[1]...
         4          4 ----> set -q __fish_machine[1]
        14         14 ---> set -l color_host $fish_color_host
         3          7 ---> if set -q SSH_TTY...
         4          4 ----> set -q SSH_TTY
       457        666 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        40         40 ----> set_color $fish_color_user
        14         14 ----> set_color --reset
        15         15 ----> set_color $color_host
        40        128 ----> prompt_hostname
        88         88 -----> string replace -r -- "\..*" "" $hostname
        12         12 ----> set_color --reset
        18         18 --> set_color $color_cwd
       100       9023 --> prompt_pwd
        16         16 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        24         24 ---> argparse -n prompt_pwd $options -- $argv
         7         12 ---> if set -q _flag_help...
         5          5 ----> set -q _flag_help
        20         20 ---> set -q argv[1]
        10         10 ---> set argv $PWD
         4          4 ---> set -ql _flag_d
         8          8 ---> set -q fish_prompt_pwd_dir_length
         6          6 ---> set -l fish_prompt_pwd_dir_length 1
         4          4 ---> set -l fulldirs 0
         3          3 ---> set -ql _flag_D
        18         18 ---> set -q fish_prompt_pwd_full_dirs
         7          7 ---> set -l fish_prompt_pwd_full_dirs 1
        62       8791 ---> for path in $argv...
       416       7574 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
      6810       7158 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       203        231 ------> set -l realhome (string escape --style=regex -- ~)
        28         28 -------> string escape --style=regex -- ~
       117        117 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        28       1155 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        44         44 -----> test "$fish_prompt_pwd_dir_length" -eq 0
        11         11 -----> set -l full
        39        824 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        12         12 ------> test $fish_prompt_pwd_full_dirs -gt 0
       196        716 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       206        520 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
       314        314 --------> math $fish_prompt_pwd_full_dirs - 1
        49         49 ------> set tmp $all[1]
         8          8 ------> set full $all[2..]
       163        248 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        85         85 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        48     154105 --> fish_vcs_prompt
        71       2051 ---> fish_jj_prompt $argv
        37       1980 ----> if not command -sq jj...
      1918       1918 -----> not command -sq jj
        25         25 -----> return 1
       550     152006 ---> fish_git_prompt $argv
        56        243 ----> if not command -sq git...
       187        187 -----> not command -sq git
        14        197 ----> if functions -q __fish_git_prompt_ready...
       183        183 -----> functions -q __fish_git_prompt_ready
      1480      52423 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     50943      50943 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        46         46 ----> test -n "$repo_info"
        26         26 ----> set -l git_dir $repo_info[1]
         8          8 ----> set -l git_common_dir $repo_info[2]
         7          7 ----> set -l inside_gitdir $repo_info[3]
        11         11 ----> set -l bare_repo $repo_info[4]
        12         12 ----> set -l inside_worktree $repo_info[5]
         4          4 ----> set -q repo_info[6]
        10         10 ----> set -l sha $repo_info[6]
       652      43412 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
       278      42760 -----> __fish_git_prompt_operation_branch_bare $repo_info
        30         30 ------> set -l git_dir $argv[1]
        12         12 ------> set -l inside_gitdir $argv[3]
         7          7 ------> set -l bare_repo $argv[4]
         5          5 ------> set -q argv[6]
         8          8 ------> set -l sha $argv[6]
         5          5 ------> set -l branch
         6          6 ------> set -l operation
         6          6 ------> set -l detached no
         5          5 ------> set -l bare
         4          4 ------> set -l step
         4          4 ------> set -l total
        42        276 ------> if test -d $git_dir/rebase-merge...
        85         85 -------> test -d $git_dir/rebase-merge
        39        149 -------> if test -d $git_dir/rebase-apply...
        41         41 --------> test -d $git_dir/rebase-apply
        13         13 --------> test -f $git_dir/MERGE_HEAD
        15         15 --------> test -f $git_dir/CHERRY_PICK_HEAD
        13         13 --------> test -f $git_dir/REVERT_HEAD
        28         28 --------> test -f $git_dir/BISECT_LOG
         4         22 ------> if test -n "$step" -a -n "$total"...
        18         18 -------> test -n "$step" -a -n "$total"
        16      41397 ------> if test -z "$branch"...
         7          7 -------> test -z "$branch"
        51      41374 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
      5809      41323 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     35514      35514 ---------> command git symbolic-ref HEAD 2>/dev/null
        41        609 ------> if test true = $inside_gitdir...
       568        568 -------> test true = $inside_gitdir
        59         59 ------> echo $operation
        13         13 ------> echo $branch
         8          8 ------> echo $detached
         6          6 ------> echo $bare
        76         76 ----> set -l operation $branch_state[1]
        11         11 ----> set -l branch $branch_state[2]
         6          6 ----> set -l detached $branch_state[3]
         8          8 ----> set -l dirtystate
        18         18 ----> set -l stagedstate
         6          6 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         5          5 ----> set -l untrackedfiles
         7          7 ----> set -l bare_prefix $branch_state[4]
         6          6 ----> set -l upstream
         9          9 ----> set -l informative_status
        17         17 ----> set -q __fish_git_prompt_status_order
        44         55 ----> if not set -q ___fish_git_prompt_init...
        11         11 -----> not set -q ___fish_git_prompt_init
        42         42 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
        23         23 ----> set -l informative
         4          4 ----> set -l dirty
         6          6 ----> set -l untracked
      2257      52269 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     50012      50012 -----> read -lz key value
        24        121 ----> if not set -q dirty[1]...
        52         52 -----> not set -q dirty[1]
        45         45 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        37         37 ----> contains dirtystate $__fish_git_prompt_status_order
        46         87 ----> if not set -q untracked[1]...
        10         10 -----> not set -q untracked[1]
        31         31 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        11         11 ----> contains untrackedfiles $__fish_git_prompt_status_order
        37        194 ----> if test true = $inside_worktree...
        17         17 -----> test true = $inside_worktree
        10        111 -----> if test "$informative" = true...
         8          8 ------> test "$informative" = true
         6         15 ------> ...
         9          9 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        15         46 ------> if not test "$dirty" = true...
         6          6 -------> not test "$dirty" = true
         4          4 -------> test "$untracked" = true
        21         21 -------> test "$dirty" = true
         9         32 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
        23         23 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         4         29 -----> if set -q __fish_git_prompt_showupstream...
        17         17 ------> set -q __fish_git_prompt_showupstream
         8          8 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        23         23 ----> set -l branch_color $___fish_git_prompt_color_branch
        27         27 ----> set -l branch_done $___fish_git_prompt_color_branch_done
        10         18 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
         8          8 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
        27         27 ----> set -l flags ""
        27         81 ----> for i in $__fish_git_prompt_status_order...
         5         16 -----> if test -n "$$i"...
        11         11 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         4          8 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
         3         13 -----> if test -n "$$i"...
        10         10 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
       311        350 ----> set branch (string replace refs/heads/ '' -- $branch)
        39         39 -----> string replace refs/heads/ '' -- $branch
       168        242 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        74         74 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       173        217 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        44         44 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        26        381 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
       355        355 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
        11         86 ----> if test -n "$branch"...
        28         28 -----> test -n "$branch"
        19         19 -----> set branch "$branch_color$branch$branch_done"
        10         28 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         9          9 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
         9          9 ------> test -n "$___fish_git_prompt_char_cleanstate"
        41         85 ----> if test -n "$bare_prefix"...
        44         44 -----> test -n "$bare_prefix"
         3          8 ----> if test -n "$operation"...
         5          5 -----> test -n "$operation"
         4         28 ----> if test -n "$upstream"...
        24         24 -----> test -n "$upstream"
         2         18 ----> if test -n "$flags$bare_prefix$upstream"...
        16         16 -----> test -n "$flags$bare_prefix$upstream"
        16         16 ----> set -l format $argv[1]
         6         18 ----> if test -z "$format"...
         5          5 -----> test -z "$format"
         7          7 -----> set format " (%s)"
       410        410 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
       101       2628 > fish_title
        29         29 -> set -l ssh
         6          6 -> set -q SSH_TTY
        28       2492 -> if set -q argv[1]...
         4          4 --> set -q argv[1]
       423        439 --> set -l command (status current-command)
        16         16 ---> status current-command
        13         47 --> if test "$command" = fish...
        24         24 ---> test "$command" = fish
        10         10 ---> set command
       385       1974 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        18         18 ---> string sub -l 20 -- $command
        47       1571 ---> prompt_pwd -d 1 -D 1
        64         64 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        39         39 ----> argparse -n prompt_pwd $options -- $argv
         7         12 ----> if set -q _flag_help...
         5          5 -----> set -q _flag_help
         4          4 ----> set -q argv[1]
        10         10 ----> set argv $PWD
         3          3 ----> set -ql _flag_d
        23         23 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         4          4 ----> set -q fish_prompt_pwd_dir_length
         5          5 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         7          7 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         4          4 ----> set -q fish_prompt_pwd_full_dirs
        21       1346 ----> for path in $argv...
       137        641 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       289        504 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       124        150 -------> set -l realhome (string escape --style=regex -- ~)
        26         26 --------> string escape --style=regex -- ~
        65         65 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        20        684 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        21         21 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         7          7 ------> set -l full
        16        294 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 -------> test $fish_prompt_pwd_full_dirs -gt 0
       118        251 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
        97        133 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        36         36 ---------> math $fish_prompt_pwd_full_dirs - 1
        12         12 -------> set tmp $all[1]
         7          7 -------> set full $all[2..]
       253        342 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        89         89 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        49        288 > __fish_winch_handler SIGWINCH
        28        239 -> if test "$fish_handle_reflow" = 1 2>/dev/null...
       129        129 --> test "$fish_handle_reflow" = 1 2>/dev/null
        82         82 --> commandline -f repaint >/dev/null 2>/dev/null
        44        121 > fish_mode_prompt
        15         77 -> fish_default_mode_prompt
        19         62 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        38         38 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         5          5 ---> return
       107     106252 > fish_prompt
        39         39 -> set -l last_pipestatus $pipestatus
        14         14 -> set -lx __fish_last_status $status
       227        248 -> set -l normal (set_color --reset)
        21         21 --> set_color --reset
        18         18 -> set -l color_cwd $fish_color_cwd
         8          8 -> set -l suffix '>'
         8        180 -> if functions -q fish_is_root_user...
        17         17 --> functions -q fish_is_root_user
        22        155 --> fish_is_root_user
         9         96 ---> if test "$EUID" = 0 2>/dev/null...
        87         87 ----> test "$EUID" = 0 2>/dev/null
         2         20 ---> if contains -- $USER root toor Administrator...
        18         18 ----> contains -- $USER root toor Administrator
        17         17 ---> return 1
        14         14 -> set -l bold_flag --bold
         6          6 -> set -q __fish_prompt_status_generation
         6         27 -> if test $__fish_prompt_status_generation = $status_generation...
        14         14 --> test $__fish_prompt_status_generation = $status_generation
         7          7 --> set bold_flag
        13         13 -> set __fish_prompt_status_generation $status_generation
       301        331 -> set -l status_color (set_color $fish_color_status)
        30         30 --> set_color $fish_color_status
       213        242 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        29         29 --> set_color $bold_flag $fish_color_status
       290        511 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        55        221 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        11         11 ---> set -l last_status
        15         73 ---> if set -q __fish_last_status...
        45         45 ----> set -q __fish_last_status
        13         13 ----> set last_status $__fish_last_status
        13         13 ---> set -l left_brace $argv[1]
         7          7 ---> set -l right_brace $argv[2]
         7          7 ---> set -l separator $argv[3]
         8          8 ---> set -l brace_sep_color $argv[4]
        10         10 ---> set -l status_color $argv[5]
         9          9 ---> set -e argv[1 2 3 4 5]
         4          9 ---> if not set -q argv[1]...
         5          5 ----> not set -q argv[1]
         7         19 ---> if not contains $last_status 0 141...
        12         12 ----> not contains $last_status 0 141
      2424     104494 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
       137       4114 --> prompt_login
        29         58 ---> if not set -q __fish_machine...
        29         29 ----> not set -q __fish_machine
        13         35 ---> if set -q __fish_machine[1]...
        22         22 ----> set -q __fish_machine[1]
       144        144 ---> set -l color_host $fish_color_host
        15         35 ---> if set -q SSH_TTY...
        20         20 ----> set -q SSH_TTY
      2953       3705 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        94         94 ----> set_color $fish_color_user
       102        102 ----> set_color --reset
       139        139 ----> set_color $color_host
       131        318 ----> prompt_hostname
       187        187 -----> string replace -r -- "\..*" "" $hostname
        99         99 ----> set_color --reset
       322        322 --> set_color $color_cwd
       178       5096 --> prompt_pwd
        78         78 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        93         93 ---> argparse -n prompt_pwd $options -- $argv
        23         49 ---> if set -q _flag_help...
        26         26 ----> set -q _flag_help
        18         18 ---> set -q argv[1]
        48         48 ---> set argv $PWD
        14         14 ---> set -ql _flag_d
        16         16 ---> set -q fish_prompt_pwd_dir_length
        24         24 ---> set -l fish_prompt_pwd_dir_length 1
        21         21 ---> set -l fulldirs 0
        13         13 ---> set -ql _flag_D
        14         14 ---> set -q fish_prompt_pwd_full_dirs
        23         23 ---> set -l fish_prompt_pwd_full_dirs 1
        74       4507 ---> for path in $argv...
       664       2400 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       803       1736 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       553        648 ------> set -l realhome (string escape --style=regex -- ~)
        95         95 -------> string escape --style=regex -- ~
       285        285 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        48       2033 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        81         81 -----> test "$fish_prompt_pwd_dir_length" -eq 0
        82         82 -----> set -l full
        43       1492 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
       120        120 ------> test $fish_prompt_pwd_full_dirs -gt 0
       639       1290 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       490        651 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
       161        161 --------> math $fish_prompt_pwd_full_dirs - 1
        30         30 ------> set tmp $all[1]
         9          9 ------> set full $all[2..]
       240        330 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        90         90 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        50      92538 --> fish_vcs_prompt
        47        219 ---> fish_jj_prompt $argv
        19        172 ----> if not command -sq jj...
       143        143 -----> not command -sq jj
        10         10 -----> return 1
       180      92269 ---> fish_git_prompt $argv
        11        150 ----> if not command -sq git...
       139        139 -----> not command -sq git
         5         30 ----> if functions -q __fish_git_prompt_ready...
        25         25 -----> functions -q __fish_git_prompt_ready
       855      37675 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     36562      36820 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        50        258 ------> __fish_winch_handler SIGWINCH
        19        208 -------> if test "$fish_handle_reflow" = 1 2>/dev/null...
       105        105 --------> test "$fish_handle_reflow" = 1 2>/dev/null
        84         84 --------> commandline -f repaint >/dev/null 2>/dev/null
        40         40 ----> test -n "$repo_info"
        24         24 ----> set -l git_dir $repo_info[1]
        11         11 ----> set -l git_common_dir $repo_info[2]
         8          8 ----> set -l inside_gitdir $repo_info[3]
         8          8 ----> set -l bare_repo $repo_info[4]
        13         13 ----> set -l inside_worktree $repo_info[5]
         5          5 ----> set -q repo_info[6]
        41         41 ----> set -l sha $repo_info[6]
       295      26454 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
       112      26159 -----> __fish_git_prompt_operation_branch_bare $repo_info
        25         25 ------> set -l git_dir $argv[1]
        15         15 ------> set -l inside_gitdir $argv[3]
        10         10 ------> set -l bare_repo $argv[4]
         5          5 ------> set -q argv[6]
         8          8 ------> set -l sha $argv[6]
       154        154 ------> set -l branch
        20         20 ------> set -l operation
         6          6 ------> set -l detached no
         5          5 ------> set -l bare
         4          4 ------> set -l step
         3          3 ------> set -l total
        25        153 ------> if test -d $git_dir/rebase-merge...
        46         46 -------> test -d $git_dir/rebase-merge
        22         82 -------> if test -d $git_dir/rebase-apply...
        17         17 --------> test -d $git_dir/rebase-apply
        13         13 --------> test -f $git_dir/MERGE_HEAD
        11         11 --------> test -f $git_dir/CHERRY_PICK_HEAD
         9          9 --------> test -f $git_dir/REVERT_HEAD
        10         10 --------> test -f $git_dir/BISECT_LOG
         5         23 ------> if test -n "$step" -a -n "$total"...
        18         18 -------> test -n "$step" -a -n "$total"
         9      25531 ------> if test -z "$branch"...
         6          6 -------> test -z "$branch"
        28      25516 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       463      25488 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     25025      25025 ---------> command git symbolic-ref HEAD 2>/dev/null
         6         36 ------> if test true = $inside_gitdir...
        30         30 -------> test true = $inside_gitdir
        29         29 ------> echo $operation
         9          9 ------> echo $branch
         7          7 ------> echo $detached
         4          4 ------> echo $bare
        21         21 ----> set -l operation $branch_state[1]
         8          8 ----> set -l branch $branch_state[2]
        10         10 ----> set -l detached $branch_state[3]
         6          6 ----> set -l dirtystate
        12         12 ----> set -l stagedstate
         4          4 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         5          5 ----> set -l untrackedfiles
         7          7 ----> set -l bare_prefix $branch_state[4]
         5          5 ----> set -l upstream
         5          5 ----> set -l informative_status
         7          7 ----> set -q __fish_git_prompt_status_order
         7         13 ----> if not set -q ___fish_git_prompt_init...
         6          6 -----> not set -q ___fish_git_prompt_init
        25         25 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         5          5 ----> set -l informative
         4          4 ----> set -l dirty
         4          4 ----> set -l untracked
      2115      22976 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     20861      20861 -----> read -lz key value
        23        110 ----> if not set -q dirty[1]...
        43         43 -----> not set -q dirty[1]
        44         44 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        35         35 ----> contains dirtystate $__fish_git_prompt_status_order
         6         25 ----> if not set -q untracked[1]...
         8          8 -----> not set -q untracked[1]
        11         11 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        10         10 ----> contains untrackedfiles $__fish_git_prompt_status_order
        19        142 ----> if test true = $inside_worktree...
        17         17 -----> test true = $inside_worktree
        11         86 -----> if test "$informative" = true...
         9          9 ------> test "$informative" = true
         7         17 ------> ...
        10         10 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        11         33 ------> if not test "$dirty" = true...
         8          8 -------> not test "$dirty" = true
         8          8 -------> test "$untracked" = true
         6          6 -------> test "$dirty" = true
         7         16 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         9          9 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         4         20 -----> if set -q __fish_git_prompt_showupstream...
         6          6 ------> set -q __fish_git_prompt_showupstream
        10         10 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        20         20 ----> set -l branch_color $___fish_git_prompt_color_branch
        17         17 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         6         14 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
         8          8 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         7          7 ----> set -l flags ""
        26         75 ----> for i in $__fish_git_prompt_status_order...
         6         15 -----> if test -n "$$i"...
         9          9 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
       284        320 ----> set branch (string replace refs/heads/ '' -- $branch)
        36         36 -----> string replace refs/heads/ '' -- $branch
       248        334 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        86         86 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       180        224 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        44         44 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        15         60 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        45         45 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         6         76 ----> if test -n "$branch"...
        15         15 -----> test -n "$branch"
        13         13 -----> set branch "$branch_color$branch$branch_done"
        28         42 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
         6          6 ------> test -n "$___fish_git_prompt_char_cleanstate"
         2         11 ----> if test -n "$bare_prefix"...
         9          9 -----> test -n "$bare_prefix"
         3          8 ----> if test -n "$operation"...
         5          5 -----> test -n "$operation"
         2          8 ----> if test -n "$upstream"...
         6          6 -----> test -n "$upstream"
         2          9 ----> if test -n "$flags$bare_prefix$upstream"...
         7          7 -----> test -n "$flags$bare_prefix$upstream"
        11         11 ----> set -l format $argv[1]
         4         16 ----> if test -z "$format"...
         5          5 -----> test -z "$format"
         7          7 -----> set format " (%s)"
      2977       2977 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        52       2745 > fish_title
        33         33 -> set -l ssh
         8          8 -> set -q SSH_TTY
        19       2652 -> if set -q argv[1]...
         6          6 --> set -q argv[1]
       231        243 --> set -l command (status current-command)
        12         12 ---> status current-command
        14         50 --> if test "$command" = fish...
        22         22 ---> test "$command" = fish
        14         14 ---> set command
       339       2334 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        32         32 ---> string sub -l 20 -- $command
        57       1963 ---> prompt_pwd -d 1 -D 1
        15         15 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        39         39 ----> argparse -n prompt_pwd $options -- $argv
         6         12 ----> if set -q _flag_help...
         6          6 -----> set -q _flag_help
         5          5 ----> set -q argv[1]
        22         22 ----> set argv $PWD
         4          4 ----> set -ql _flag_d
        15         15 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         4          4 ----> set -q fish_prompt_pwd_dir_length
         5          5 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         7          7 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        22       1772 ----> for path in $argv...
       214       1001 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       370        787 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       303        342 -------> set -l realhome (string escape --style=regex -- ~)
        39         39 --------> string escape --style=regex -- ~
        75         75 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        24        749 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        25         25 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         9          9 ------> set -l full
        19        450 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         9          9 -------> test $fish_prompt_pwd_full_dirs -gt 0
       192        399 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       168        207 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        39         39 ---------> math $fish_prompt_pwd_full_dirs - 1
        15         15 -------> set tmp $all[1]
         8          8 -------> set full $all[2..]
       168        241 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        73         73 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
       188       7031 > fish_title \#\ 1.\ Ensure\ the\ required\ Shizuku\ application\ identifier\ variable\ is\ present
        99         99 -> set -l ssh
        39         39 -> set -q SSH_TTY
        23       6705 -> if set -q argv[1]...
        25         25 --> set -q argv[1]
       822       6657 --> echo -- $ssh (string sub -l 20 -- $argv[1]) (prompt_pwd -d 1 -D 1)
       115        115 ---> string sub -l 20 -- $argv[1]
       286       5720 ---> prompt_pwd -d 1 -D 1
       102        102 ----> set -l options h/help d/dir-length= D/full-length-dirs=
       136        136 ----> argparse -n prompt_pwd $options -- $argv
        31         66 ----> if set -q _flag_help...
        35         35 -----> set -q _flag_help
        29         29 ----> set -q argv[1]
        59         59 ----> set argv $PWD
        17         17 ----> set -ql _flag_d
        54         54 ----> set -l fish_prompt_pwd_dir_length $_flag_d
        19         19 ----> set -q fish_prompt_pwd_dir_length
        29         29 ----> set -l fulldirs 0
        14         14 ----> set -ql _flag_D
        37         37 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
        14         14 ----> set -q fish_prompt_pwd_full_dirs
        64       4858 ----> for path in $argv...
       599       2367 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
      1182       1768 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       356        432 -------> set -l realhome (string escape --style=regex -- ~)
        76         76 --------> string escape --style=regex -- ~
       154        154 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        57       2427 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        85         85 ------> test "$fish_prompt_pwd_dir_length" -eq 0
        63         63 ------> set -l full
        39       1962 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
        65         65 -------> test $fish_prompt_pwd_full_dirs -gt 0
       422       1827 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
      1350       1405 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        55         55 ---------> math $fish_prompt_pwd_full_dirs - 1
        24         24 -------> set tmp $all[1]
         7          7 -------> set full $all[2..]
       194        260 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        66         66 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        77        558 > __fish_update_cwd_osc
        38         38 -> set -l host $hostname
         7         12 -> if set -q KONSOLE_VERSION...
         5          5 --> set -q KONSOLE_VERSION
         6         51 -> if [ -n "$MSYSTEM" ]...
        45         45 --> [ -n "$MSYSTEM" ]
        24         43 -> if [ "$TERM" = dumb ]...
        19         19 --> [ "$TERM" = dumb ]
       302        337 -> printf \e\]7\;file://%s%s\a (string escape --style=url -- $host $PWD)
        35         35 --> string escape --style=url -- $host $PWD
        27         81 > fish_mode_prompt
        16         54 -> fish_default_mode_prompt
         9         38 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        25         25 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         4          4 ---> return
        86      49088 > fish_prompt
        29         29 -> set -l last_pipestatus $pipestatus
        14         14 -> set -lx __fish_last_status $status
       160        182 -> set -l normal (set_color --reset)
        22         22 --> set_color --reset
        13         13 -> set -l color_cwd $fish_color_cwd
         6          6 -> set -l suffix '>'
         7        155 -> if functions -q fish_is_root_user...
        14         14 --> functions -q fish_is_root_user
        21        134 --> fish_is_root_user
        10         87 ---> if test "$EUID" = 0 2>/dev/null...
        77         77 ----> test "$EUID" = 0 2>/dev/null
         4         21 ---> if contains -- $USER root toor Administrator...
        17         17 ----> contains -- $USER root toor Administrator
         5          5 ---> return 1
        12         12 -> set -l bold_flag --bold
         7          7 -> set -q __fish_prompt_status_generation
         7         26 -> if test $__fish_prompt_status_generation = $status_generation...
        13         13 --> test $__fish_prompt_status_generation = $status_generation
         6          6 --> set bold_flag
        13         13 -> set __fish_prompt_status_generation $status_generation
       245        278 -> set -l status_color (set_color $fish_color_status)
        33         33 --> set_color $fish_color_status
       167        196 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        29         29 --> set_color $bold_flag $fish_color_status
       200        358 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        59        158 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        11         11 ---> set -l last_status
        10         23 ---> if set -q __fish_last_status...
         4          4 ----> set -q __fish_last_status
         9          9 ----> set last_status $__fish_last_status
        10         10 ---> set -l left_brace $argv[1]
         6          6 ---> set -l right_brace $argv[2]
         5          5 ---> set -l separator $argv[3]
         7          7 ---> set -l brace_sep_color $argv[4]
         6          6 ---> set -l status_color $argv[5]
         7          7 ---> set -e argv[1 2 3 4 5]
         4          9 ---> if not set -q argv[1]...
         5          5 ----> not set -q argv[1]
         4         15 ---> if not contains $last_status 0 141...
        11         11 ----> not contains $last_status 0 141
       612      47713 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        31        960 --> prompt_login
        11         23 ---> if not set -q __fish_machine...
        12         12 ----> not set -q __fish_machine
         3          8 ---> if set -q __fish_machine[1]...
         5          5 ----> set -q __fish_machine[1]
        16         16 ---> set -l color_host $fish_color_host
         3          7 ---> if set -q SSH_TTY...
         4          4 ----> set -q SSH_TTY
       712        875 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        25         25 ----> set_color $fish_color_user
        22         22 ----> set_color --reset
        26         26 ----> set_color $color_host
        24         72 ----> prompt_hostname
        48         48 -----> string replace -r -- "\..*" "" $hostname
        18         18 ----> set_color --reset
        26         26 --> set_color $color_cwd
        45       1198 --> prompt_pwd
        15         15 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        24         24 ---> argparse -n prompt_pwd $options -- $argv
         6         11 ---> if set -q _flag_help...
         5          5 ----> set -q _flag_help
         4          4 ---> set -q argv[1]
         9          9 ---> set argv $PWD
         3          3 ---> set -ql _flag_d
         4          4 ---> set -q fish_prompt_pwd_dir_length
         5          5 ---> set -l fish_prompt_pwd_dir_length 1
         4          4 ---> set -l fulldirs 0
         3          3 ---> set -ql _flag_D
         3          3 ---> set -q fish_prompt_pwd_full_dirs
        20         20 ---> set -l fish_prompt_pwd_full_dirs 1
        22       1048 ---> for path in $argv...
       126        505 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       170        379 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       111        155 ------> set -l realhome (string escape --style=regex -- ~)
        44         44 -------> string escape --style=regex -- ~
        54         54 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        20        521 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        20         20 -----> test "$fish_prompt_pwd_dir_length" -eq 0
         6          6 -----> set -l full
        12        311 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        10         10 ------> test $fish_prompt_pwd_full_dirs -gt 0
       118        269 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       119        151 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        32         32 --------> math $fish_prompt_pwd_full_dirs - 1
        13         13 ------> set tmp $all[1]
         7          7 ------> set full $all[2..]
       108        164 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        56         56 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        42      44917 --> fish_vcs_prompt
        20        104 ---> fish_jj_prompt $argv
        11         84 ----> if not command -sq jj...
        68         68 -----> not command -sq jj
         5          5 -----> return 1
       153      44771 ---> fish_git_prompt $argv
         9        111 ----> if not command -sq git...
       102        102 -----> not command -sq git
         4         19 ----> if functions -q __fish_git_prompt_ready...
        15         15 -----> functions -q __fish_git_prompt_ready
       285      14257 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     13972      13972 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        39         39 ----> test -n "$repo_info"
        19         19 ----> set -l git_dir $repo_info[1]
         8          8 ----> set -l git_common_dir $repo_info[2]
         6          6 ----> set -l inside_gitdir $repo_info[3]
         9          9 ----> set -l bare_repo $repo_info[4]
        10         10 ----> set -l inside_worktree $repo_info[5]
         4          4 ----> set -q repo_info[6]
         6          6 ----> set -l sha $repo_info[6]
       240      15777 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
        70      15537 -----> __fish_git_prompt_operation_branch_bare $repo_info
        15         15 ------> set -l git_dir $argv[1]
         7          7 ------> set -l inside_gitdir $argv[3]
         6          6 ------> set -l bare_repo $argv[4]
         3          3 ------> set -q argv[6]
         6          6 ------> set -l sha $argv[6]
         4          4 ------> set -l branch
         6          6 ------> set -l operation
         4          4 ------> set -l detached no
         3          3 ------> set -l bare
         3          3 ------> set -l step
         3          3 ------> set -l total
        14        105 ------> if test -d $git_dir/rebase-merge...
        31         31 -------> test -d $git_dir/rebase-merge
        19         60 -------> if test -d $git_dir/rebase-apply...
        11         11 --------> test -d $git_dir/rebase-apply
         9          9 --------> test -f $git_dir/MERGE_HEAD
         8          8 --------> test -f $git_dir/CHERRY_PICK_HEAD
         7          7 --------> test -f $git_dir/REVERT_HEAD
         6          6 --------> test -f $git_dir/BISECT_LOG
         4         17 ------> if test -n "$step" -a -n "$total"...
        13         13 -------> test -n "$step" -a -n "$total"
         6      15214 ------> if test -z "$branch"...
         5          5 -------> test -z "$branch"
        23      15203 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       312      15180 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     14868      14868 ---------> command git symbolic-ref HEAD 2>/dev/null
         5         31 ------> if test true = $inside_gitdir...
        26         26 -------> test true = $inside_gitdir
        24         24 ------> echo $operation
         7          7 ------> echo $branch
         5          5 ------> echo $detached
         4          4 ------> echo $bare
        19         19 ----> set -l operation $branch_state[1]
         9          9 ----> set -l branch $branch_state[2]
         7          7 ----> set -l detached $branch_state[3]
         8          8 ----> set -l dirtystate
        10         10 ----> set -l stagedstate
         4          4 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         4          4 ----> set -l untrackedfiles
         6          6 ----> set -l bare_prefix $branch_state[4]
         4          4 ----> set -l upstream
         4          4 ----> set -l informative_status
         7          7 ----> set -q __fish_git_prompt_status_order
         6         11 ----> if not set -q ___fish_git_prompt_init...
         5          5 -----> not set -q ___fish_git_prompt_init
        21         21 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         4          4 ----> set -l informative
         4          4 ----> set -l dirty
         3          3 ----> set -l untracked
      1264      12396 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     11132      11132 -----> read -lz key value
        25        163 ----> if not set -q dirty[1]...
        50         50 -----> not set -q dirty[1]
        88         88 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        34         34 ----> contains dirtystate $__fish_git_prompt_status_order
         5         23 ----> if not set -q untracked[1]...
         8          8 -----> not set -q untracked[1]
        10         10 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
         9          9 ----> contains untrackedfiles $__fish_git_prompt_status_order
        11        162 ----> if test true = $inside_worktree...
        17         17 -----> test true = $inside_worktree
        12        108 -----> if test "$informative" = true...
         7          7 ------> test "$informative" = true
         7         40 ------> ...
        33         33 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        12         31 ------> if not test "$dirty" = true...
         8          8 -------> not test "$dirty" = true
         6          6 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         8         18 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
        10         10 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         6         26 -----> if set -q __fish_git_prompt_showupstream...
         6          6 ------> set -q __fish_git_prompt_showupstream
        14         14 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        21         21 ----> set -l branch_color $___fish_git_prompt_color_branch
        20         20 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         5         15 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        10         10 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         7          7 ----> set -l flags ""
        25         83 ----> for i in $__fish_git_prompt_status_order...
         5         18 -----> if test -n "$$i"...
        13         13 ------> test -n "$$i"
         4         11 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
         4          9 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         4         11 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
         4          9 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
       253        282 ----> set branch (string replace refs/heads/ '' -- $branch)
        29         29 -----> string replace refs/heads/ '' -- $branch
       158        218 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        60         60 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       200        336 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
       136        136 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        16         78 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        62         62 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         9         62 ----> if test -n "$branch"...
        16         16 -----> test -n "$branch"
        13         13 -----> set branch "$branch_color$branch$branch_done"
         7         24 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
        10         10 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
         7          7 ------> test -n "$___fish_git_prompt_char_cleanstate"
         3          8 ----> if test -n "$bare_prefix"...
         5          5 -----> test -n "$bare_prefix"
         3          8 ----> if test -n "$operation"...
         5          5 -----> test -n "$operation"
         1          7 ----> if test -n "$upstream"...
         6          6 -----> test -n "$upstream"
         3          9 ----> if test -n "$flags$bare_prefix$upstream"...
         6          6 -----> test -n "$flags$bare_prefix$upstream"
        10         10 ----> set -l format $argv[1]
         5         17 ----> if test -z "$format"...
         5          5 -----> test -z "$format"
         7          7 -----> set format " (%s)"
       256        256 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        44       2461 > fish_title
        29         29 -> set -l ssh
         7          7 -> set -q SSH_TTY
        19       2381 -> if set -q argv[1]...
         6          6 --> set -q argv[1]
       216        234 --> set -l command (status current-command)
        18         18 ---> status current-command
        11         38 --> if test "$command" = fish...
        20         20 ---> test "$command" = fish
         7          7 ---> set command
       291       2084 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        17         17 ---> string sub -l 20 -- $command
        60       1776 ---> prompt_pwd -d 1 -D 1
        30         30 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        40         40 ----> argparse -n prompt_pwd $options -- $argv
         6         12 ----> if set -q _flag_help...
         6          6 -----> set -q _flag_help
         7          7 ----> set -q argv[1]
        10         10 ----> set argv $PWD
         4          4 ----> set -ql _flag_d
        19         19 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         6          6 ----> set -q fish_prompt_pwd_dir_length
         7          7 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
        10         10 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         6          6 ----> set -q fish_prompt_pwd_full_dirs
        27       1562 ----> for path in $argv...
       166        762 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       326        596 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       160        193 -------> set -l realhome (string escape --style=regex -- ~)
        33         33 --------> string escape --style=regex -- ~
        77         77 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        38        773 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        30         30 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         8          8 ------> set -l full
        22        448 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
        11         11 -------> test $fish_prompt_pwd_full_dirs -gt 0
       177        391 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       147        214 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        67         67 ---------> math $fish_prompt_pwd_full_dirs - 1
        16         16 -------> set tmp $all[1]
         8          8 -------> set full $all[2..]
       164        249 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        85         85 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        38        102 > fish_mode_prompt
        14         64 -> fish_default_mode_prompt
        14         50 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        32         32 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         4          4 ---> return
        67      59147 > fish_prompt
        35         35 -> set -l last_pipestatus $pipestatus
        12         12 -> set -lx __fish_last_status $status
       154        176 -> set -l normal (set_color --reset)
        22         22 --> set_color --reset
        14         14 -> set -l color_cwd $fish_color_cwd
         7          7 -> set -l suffix '>'
         7        145 -> if functions -q fish_is_root_user...
        13         13 --> functions -q fish_is_root_user
        28        125 --> fish_is_root_user
         8         75 ---> if test "$EUID" = 0 2>/dev/null...
        67         67 ----> test "$EUID" = 0 2>/dev/null
         3         18 ---> if contains -- $USER root toor Administrator...
        15         15 ----> contains -- $USER root toor Administrator
         4          4 ---> return 1
        10         10 -> set -l bold_flag --bold
         5          5 -> set -q __fish_prompt_status_generation
         5         21 -> if test $__fish_prompt_status_generation = $status_generation...
        10         10 --> test $__fish_prompt_status_generation = $status_generation
         6          6 --> set bold_flag
        13         13 -> set __fish_prompt_status_generation $status_generation
       133        159 -> set -l status_color (set_color $fish_color_status)
        26         26 --> set_color $fish_color_status
       125        149 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        24         24 --> set_color $bold_flag $fish_color_status
       118        258 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        43        140 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        10         10 ---> set -l last_status
         8         21 ---> if set -q __fish_last_status...
         4          4 ----> set -q __fish_last_status
         9          9 ----> set last_status $__fish_last_status
        10         10 ---> set -l left_brace $argv[1]
         6          6 ---> set -l right_brace $argv[2]
         5          5 ---> set -l separator $argv[3]
         7          7 ---> set -l brace_sep_color $argv[4]
         7          7 ---> set -l status_color $argv[5]
         8          8 ---> set -e argv[1 2 3 4 5]
         5         10 ---> if not set -q argv[1]...
         5          5 ----> not set -q argv[1]
         4         13 ---> if not contains $last_status 0 141...
         9          9 ----> not contains $last_status 0 141
       566      58076 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        30       1371 --> prompt_login
         8         16 ---> if not set -q __fish_machine...
         8          8 ----> not set -q __fish_machine
         2          7 ---> if set -q __fish_machine[1]...
         5          5 ----> set -q __fish_machine[1]
        12         12 ---> set -l color_host $fish_color_host
         2          6 ---> if set -q SSH_TTY...
         4          4 ----> set -q SSH_TTY
      1072       1300 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        23         23 ----> set_color $fish_color_user
        39         39 ----> set_color --reset
        38         38 ----> set_color $color_host
        37        101 ----> prompt_hostname
        64         64 -----> string replace -r -- "\..*" "" $hostname
        27         27 ----> set_color --reset
        31         31 --> set_color $color_cwd
        46       1430 --> prompt_pwd
        19         19 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        22         22 ---> argparse -n prompt_pwd $options -- $argv
         6         12 ---> if set -q _flag_help...
         6          6 ----> set -q _flag_help
         4          4 ---> set -q argv[1]
         9          9 ---> set argv $PWD
         3          3 ---> set -ql _flag_d
         4          4 ---> set -q fish_prompt_pwd_dir_length
         5          5 ---> set -l fish_prompt_pwd_dir_length 1
         4          4 ---> set -l fulldirs 0
         2          2 ---> set -ql _flag_D
         3          3 ---> set -q fish_prompt_pwd_full_dirs
         4          4 ---> set -l fish_prompt_pwd_full_dirs 1
        31       1293 ---> for path in $argv...
       140        674 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       296        534 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       132        175 ------> set -l realhome (string escape --style=regex -- ~)
        43         43 -------> string escape --style=regex -- ~
        63         63 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        21        588 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        21         21 -----> test "$fish_prompt_pwd_dir_length" -eq 0
         9          9 -----> set -l full
        14        327 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
         9          9 ------> test $fish_prompt_pwd_full_dirs -gt 0
       126        284 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       120        158 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        38         38 --------> math $fish_prompt_pwd_full_dirs - 1
        13         13 ------> set tmp $all[1]
         7          7 ------> set full $all[2..]
       124        210 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        86         86 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        37      54678 --> fish_vcs_prompt
        22        108 ---> fish_jj_prompt $argv
        12         86 ----> if not command -sq jj...
        68         68 -----> not command -sq jj
         6          6 -----> return 1
       154      54533 ---> fish_git_prompt $argv
         7         88 ----> if not command -sq git...
        81         81 -----> not command -sq git
        27        793 ----> if functions -q __fish_git_prompt_ready...
       766        766 -----> functions -q __fish_git_prompt_ready
       426      20541 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     20115      20115 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        32         32 ----> test -n "$repo_info"
        17         17 ----> set -l git_dir $repo_info[1]
         7          7 ----> set -l git_common_dir $repo_info[2]
         6          6 ----> set -l inside_gitdir $repo_info[3]
         7          7 ----> set -l bare_repo $repo_info[4]
        10         10 ----> set -l inside_worktree $repo_info[5]
         4          4 ----> set -q repo_info[6]
         6          6 ----> set -l sha $repo_info[6]
       222      14424 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
       104      14202 -----> __fish_git_prompt_operation_branch_bare $repo_info
        14         14 ------> set -l git_dir $argv[1]
        11         11 ------> set -l inside_gitdir $argv[3]
         6          6 ------> set -l bare_repo $argv[4]
         3          3 ------> set -q argv[6]
         7          7 ------> set -l sha $argv[6]
         5          5 ------> set -l branch
         6          6 ------> set -l operation
         4          4 ------> set -l detached no
         4          4 ------> set -l bare
         4          4 ------> set -l step
         3          3 ------> set -l total
        12         92 ------> if test -d $git_dir/rebase-merge...
        23         23 -------> test -d $git_dir/rebase-merge
        15         57 -------> if test -d $git_dir/rebase-apply...
        11         11 --------> test -d $git_dir/rebase-apply
         9          9 --------> test -f $git_dir/MERGE_HEAD
         8          8 --------> test -f $git_dir/CHERRY_PICK_HEAD
         7          7 --------> test -f $git_dir/REVERT_HEAD
         7          7 --------> test -f $git_dir/BISECT_LOG
         3         15 ------> if test -n "$step" -a -n "$total"...
        12         12 -------> test -n "$step" -a -n "$total"
         7      13846 ------> if test -z "$branch"...
         4          4 -------> test -z "$branch"
        24      13835 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       372      13811 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     13439      13439 ---------> command git symbolic-ref HEAD 2>/dev/null
         6         33 ------> if test true = $inside_gitdir...
        27         27 -------> test true = $inside_gitdir
        25         25 ------> echo $operation
         8          8 ------> echo $branch
         7          7 ------> echo $detached
         5          5 ------> echo $bare
        22         22 ----> set -l operation $branch_state[1]
        11         11 ----> set -l branch $branch_state[2]
        10         10 ----> set -l detached $branch_state[3]
         6          6 ----> set -l dirtystate
        11         11 ----> set -l stagedstate
         5          5 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         5          5 ----> set -l untrackedfiles
         7          7 ----> set -l bare_prefix $branch_state[4]
         5          5 ----> set -l upstream
         5          5 ----> set -l informative_status
         7          7 ----> set -q __fish_git_prompt_status_order
         8         14 ----> if not set -q ___fish_git_prompt_init...
         6          6 -----> not set -q ___fish_git_prompt_init
        24         24 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         6          6 ----> set -l informative
         4          4 ----> set -l dirty
         5          5 ----> set -l untracked
      1494      16311 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     14817      14817 -----> read -lz key value
        25        116 ----> if not set -q dirty[1]...
        48         48 -----> not set -q dirty[1]
        43         43 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        36         36 ----> contains dirtystate $__fish_git_prompt_status_order
         6         27 ----> if not set -q untracked[1]...
        10         10 -----> not set -q untracked[1]
        11         11 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        10         10 ----> contains untrackedfiles $__fish_git_prompt_status_order
        12        191 ----> if test true = $inside_worktree...
        17         17 -----> test true = $inside_worktree
        12         95 -----> if test "$informative" = true...
         8          8 ------> test "$informative" = true
         6         20 ------> ...
        14         14 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        13         33 ------> if not test "$dirty" = true...
         8          8 -------> not test "$dirty" = true
         6          6 -------> test "$untracked" = true
         6          6 -------> test "$dirty" = true
         7         22 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
        15         15 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
        51         67 -----> if set -q __fish_git_prompt_showupstream...
         6          6 ------> set -q __fish_git_prompt_showupstream
        10         10 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        25         25 ----> set -l branch_color $___fish_git_prompt_color_branch
        25         25 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         5         19 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        14         14 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         8          8 ----> set -l flags ""
        35        122 ----> for i in $__fish_git_prompt_status_order...
         5         20 -----> if test -n "$$i"...
        15         15 ------> test -n "$$i"
         3         13 -----> if test -n "$$i"...
        10         10 ------> test -n "$$i"
         3         10 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
         5         34 -----> if test -n "$$i"...
        29         29 ------> test -n "$$i"
         3         10 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
       527        563 ----> set branch (string replace refs/heads/ '' -- $branch)
        36         36 -----> string replace refs/heads/ '' -- $branch
       225        296 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        71         71 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       227        278 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        51         51 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        15         60 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        45         45 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         8         66 ----> if test -n "$branch"...
        16         16 -----> test -n "$branch"
        14         14 -----> set branch "$branch_color$branch$branch_done"
         9         28 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
        10         10 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
         9          9 ------> test -n "$___fish_git_prompt_char_cleanstate"
         3         10 ----> if test -n "$bare_prefix"...
         7          7 -----> test -n "$bare_prefix"
         4          9 ----> if test -n "$operation"...
         5          5 -----> test -n "$operation"
         2          9 ----> if test -n "$upstream"...
         7          7 -----> test -n "$upstream"
         2         11 ----> if test -n "$flags$bare_prefix$upstream"...
         9          9 -----> test -n "$flags$bare_prefix$upstream"
        13         13 ----> set -l format $argv[1]
         6         22 ----> if test -z "$format"...
         6          6 -----> test -z "$format"
        10         10 -----> set format " (%s)"
        66         66 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        33       1981 > fish_title
        19         19 -> set -l ssh
         6          6 -> set -q SSH_TTY
        19       1923 -> if set -q argv[1]...
         6          6 --> set -q argv[1]
       135        148 --> set -l command (status current-command)
        13         13 ---> status current-command
        12         40 --> if test "$command" = fish...
        19         19 ---> test "$command" = fish
         9          9 ---> set command
       214       1710 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        17         17 ---> string sub -l 20 -- $command
        52       1479 ---> prompt_pwd -d 1 -D 1
        15         15 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        40         40 ----> argparse -n prompt_pwd $options -- $argv
         6         12 ----> if set -q _flag_help...
         6          6 -----> set -q _flag_help
         5          5 ----> set -q argv[1]
        12         12 ----> set argv $PWD
         4          4 ----> set -ql _flag_d
        18         18 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         5          5 ----> set -q fish_prompt_pwd_dir_length
         6          6 ----> set -l fulldirs 0
         4          4 ----> set -ql _flag_D
         9          9 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         4          4 ----> set -q fish_prompt_pwd_full_dirs
        21       1293 ----> for path in $argv...
       188        717 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       293        529 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       143        170 -------> set -l realhome (string escape --style=regex -- ~)
        27         27 --------> string escape --style=regex -- ~
        66         66 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        20        555 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        20         20 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         8          8 ------> set -l full
        25        331 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
        11         11 -------> test $fish_prompt_pwd_full_dirs -gt 0
       127        274 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       112        147 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        35         35 ---------> math $fish_prompt_pwd_full_dirs - 1
        13         13 -------> set tmp $all[1]
         8          8 -------> set full $all[2..]
       118        176 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        58         58 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        34         92 > fish_mode_prompt
        12         58 -> fish_default_mode_prompt
        13         46 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        29         29 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         4          4 ---> return
        84      48778 > fish_prompt
        35         35 -> set -l last_pipestatus $pipestatus
        11         11 -> set -lx __fish_last_status $status
       156        177 -> set -l normal (set_color --reset)
        21         21 --> set_color --reset
        14         14 -> set -l color_cwd $fish_color_cwd
         6          6 -> set -l suffix '>'
         7        145 -> if functions -q fish_is_root_user...
        12         12 --> functions -q fish_is_root_user
        23        126 --> fish_is_root_user
         9         79 ---> if test "$EUID" = 0 2>/dev/null...
        70         70 ----> test "$EUID" = 0 2>/dev/null
         3         20 ---> if contains -- $USER root toor Administrator...
        17         17 ----> contains -- $USER root toor Administrator
         4          4 ---> return 1
        11         11 -> set -l bold_flag --bold
         4          4 -> set -q __fish_prompt_status_generation
         6         23 -> if test $__fish_prompt_status_generation = $status_generation...
        12         12 --> test $__fish_prompt_status_generation = $status_generation
         5          5 --> set bold_flag
        13         13 -> set __fish_prompt_status_generation $status_generation
       138        163 -> set -l status_color (set_color $fish_color_status)
        25         25 --> set_color $fish_color_status
       259        284 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        25         25 --> set_color $bold_flag $fish_color_status
       117        297 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        81        180 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        12         12 ---> set -l last_status
        10         23 ---> if set -q __fish_last_status...
         5          5 ----> set -q __fish_last_status
         8          8 ----> set last_status $__fish_last_status
        11         11 ---> set -l left_brace $argv[1]
         6          6 ---> set -l right_brace $argv[2]
         6          6 ---> set -l separator $argv[3]
         6          6 ---> set -l brace_sep_color $argv[4]
         6          6 ---> set -l status_color $argv[5]
         7          7 ---> set -e argv[1 2 3 4 5]
         3          8 ---> if not set -q argv[1]...
         5          5 ----> not set -q argv[1]
         5         14 ---> if not contains $last_status 0 141...
         9          9 ----> not contains $last_status 0 141
       531      47511 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        20        681 --> prompt_login
        40         49 ---> if not set -q __fish_machine...
         9          9 ----> not set -q __fish_machine
         3         10 ---> if set -q __fish_machine[1]...
         7          7 ----> set -q __fish_machine[1]
        12         12 ---> set -l color_host $fish_color_host
         4          7 ---> if set -q SSH_TTY...
         3          3 ----> set -q SSH_TTY
       451        583 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        26         26 ----> set_color $fish_color_user
        14         14 ----> set_color --reset
        15         15 ----> set_color $color_host
        20         64 ----> prompt_hostname
        44         44 -----> string replace -r -- "\..*" "" $hostname
        13         13 ----> set_color --reset
        18         18 --> set_color $color_cwd
        36       1221 --> prompt_pwd
        13         13 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        22         22 ---> argparse -n prompt_pwd $options -- $argv
         5         10 ---> if set -q _flag_help...
         5          5 ----> set -q _flag_help
         4          4 ---> set -q argv[1]
         8          8 ---> set argv $PWD
         4          4 ---> set -ql _flag_d
         4          4 ---> set -q fish_prompt_pwd_dir_length
        18         18 ---> set -l fish_prompt_pwd_dir_length 1
         6          6 ---> set -l fulldirs 0
         3          3 ---> set -ql _flag_D
         3          3 ---> set -q fish_prompt_pwd_full_dirs
         5          5 ---> set -l fish_prompt_pwd_full_dirs 1
        28       1085 ---> for path in $argv...
       126        524 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       213        398 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       105        126 ------> set -l realhome (string escape --style=regex -- ~)
        21         21 -------> string escape --style=regex -- ~
        59         59 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        18        533 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        21         21 -----> test "$fish_prompt_pwd_dir_length" -eq 0
         7          7 -----> set -l full
        14        308 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 ------> test $fish_prompt_pwd_full_dirs -gt 0
       120        266 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       115        146 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        31         31 --------> math $fish_prompt_pwd_full_dirs - 1
        13         13 ------> set tmp $all[1]
         7          7 ------> set full $all[2..]
       116        179 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        63         63 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        38      45060 --> fish_vcs_prompt
        17         99 ---> fish_jj_prompt $argv
        11         82 ----> if not command -sq jj...
        65         65 -----> not command -sq jj
         6          6 -----> return 1
       146      44923 ---> fish_git_prompt $argv
         8         81 ----> if not command -sq git...
        73         73 -----> not command -sq git
         4         17 ----> if functions -q __fish_git_prompt_ready...
        13         13 -----> functions -q __fish_git_prompt_ready
       325      14715 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     14390      14390 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        32         32 ----> test -n "$repo_info"
        16         16 ----> set -l git_dir $repo_info[1]
         7          7 ----> set -l git_common_dir $repo_info[2]
         8          8 ----> set -l inside_gitdir $repo_info[3]
         7          7 ----> set -l bare_repo $repo_info[4]
        12         12 ----> set -l inside_worktree $repo_info[5]
         4          4 ----> set -q repo_info[6]
         7          7 ----> set -l sha $repo_info[6]
       195      14623 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
        71      14428 -----> __fish_git_prompt_operation_branch_bare $repo_info
        13         13 ------> set -l git_dir $argv[1]
         8          8 ------> set -l inside_gitdir $argv[3]
         7          7 ------> set -l bare_repo $argv[4]
         3          3 ------> set -q argv[6]
         6          6 ------> set -l sha $argv[6]
         3          3 ------> set -l branch
         5          5 ------> set -l operation
         4          4 ------> set -l detached no
         4          4 ------> set -l bare
         4          4 ------> set -l step
         3          3 ------> set -l total
        10        100 ------> if test -d $git_dir/rebase-merge...
        21         21 -------> test -d $git_dir/rebase-merge
        16         69 -------> if test -d $git_dir/rebase-apply...
        10         10 --------> test -d $git_dir/rebase-apply
        21         21 --------> test -f $git_dir/MERGE_HEAD
         8          8 --------> test -f $git_dir/CHERRY_PICK_HEAD
         7          7 --------> test -f $git_dir/REVERT_HEAD
         7          7 --------> test -f $git_dir/BISECT_LOG
         3         17 ------> if test -n "$step" -a -n "$total"...
        14         14 -------> test -n "$step" -a -n "$total"
         8      14098 ------> if test -z "$branch"...
         4          4 -------> test -z "$branch"
        24      14086 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       375      14062 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     13687      13687 ---------> command git symbolic-ref HEAD 2>/dev/null
         7         38 ------> if test true = $inside_gitdir...
        31         31 -------> test true = $inside_gitdir
        27         27 ------> echo $operation
         7          7 ------> echo $branch
         5          5 ------> echo $detached
         5          5 ------> echo $bare
        20         20 ----> set -l operation $branch_state[1]
         7          7 ----> set -l branch $branch_state[2]
        10         10 ----> set -l detached $branch_state[3]
         6          6 ----> set -l dirtystate
         9          9 ----> set -l stagedstate
         5          5 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         3          3 ----> set -l untrackedfiles
         6          6 ----> set -l bare_prefix $branch_state[4]
         3          3 ----> set -l upstream
         4          4 ----> set -l informative_status
         6          6 ----> set -q __fish_git_prompt_status_order
         7         13 ----> if not set -q ___fish_git_prompt_init...
         6          6 -----> not set -q ___fish_git_prompt_init
        24         24 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         5          5 ----> set -l informative
         4          4 ----> set -l dirty
         3          3 ----> set -l untracked
      1353      13675 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     12322      12322 -----> read -lz key value
        20         96 ----> if not set -q dirty[1]...
        38         38 -----> not set -q dirty[1]
        38         38 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        47         47 ----> contains dirtystate $__fish_git_prompt_status_order
         6         23 ----> if not set -q untracked[1]...
         6          6 -----> not set -q untracked[1]
        11         11 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        10         10 ----> contains untrackedfiles $__fish_git_prompt_status_order
        12        121 ----> if test true = $inside_worktree...
        10         10 -----> test true = $inside_worktree
        11         83 -----> if test "$informative" = true...
        10         10 ------> test "$informative" = true
         5         17 ------> ...
        12         12 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        12         29 ------> if not test "$dirty" = true...
         6          6 -------> not test "$dirty" = true
         5          5 -------> test "$untracked" = true
         6          6 -------> test "$dirty" = true
         6         16 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
        10         10 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         3         16 -----> if set -q __fish_git_prompt_showupstream...
         5          5 ------> set -q __fish_git_prompt_showupstream
         8          8 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        18         18 ----> set -l branch_color $___fish_git_prompt_color_branch
        17         17 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         8         20 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        12         12 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         7          7 ----> set -l flags ""
        24         72 ----> for i in $__fish_git_prompt_status_order...
         4         13 -----> if test -n "$$i"...
         9          9 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         4          9 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
       205        237 ----> set branch (string replace refs/heads/ '' -- $branch)
        32         32 -----> string replace refs/heads/ '' -- $branch
       233        294 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        61         61 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       193        228 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        35         35 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        13         51 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        38         38 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         6         58 ----> if test -n "$branch"...
        13         13 -----> test -n "$branch"
        13         13 -----> set branch "$branch_color$branch$branch_done"
         7         26 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        11         11 ------> test -n "$___fish_git_prompt_char_cleanstate"
         3          8 ----> if test -n "$bare_prefix"...
         5          5 -----> test -n "$bare_prefix"
         2          6 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         4         34 ----> if test -n "$upstream"...
        30         30 -----> test -n "$upstream"
         2         11 ----> if test -n "$flags$bare_prefix$upstream"...
         9          9 -----> test -n "$flags$bare_prefix$upstream"
        10         10 ----> set -l format $argv[1]
         5         16 ----> if test -z "$format"...
         5          5 -----> test -z "$format"
         6          6 -----> set format " (%s)"
        57         57 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        26       2281 > fish_title
        17         17 -> set -l ssh
         7          7 -> set -q SSH_TTY
        15       2231 -> if set -q argv[1]...
         4          4 --> set -q argv[1]
        81         92 --> set -l command (status current-command)
        11         11 ---> status current-command
         8         26 --> if test "$command" = fish...
        12         12 ---> test "$command" = fish
         6          6 ---> set command
       364       2094 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        14         14 ---> string sub -l 20 -- $command
        58       1716 ---> prompt_pwd -d 1 -D 1
        17         17 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        38         38 ----> argparse -n prompt_pwd $options -- $argv
         6         11 ----> if set -q _flag_help...
         5          5 -----> set -q _flag_help
         4          4 ----> set -q argv[1]
         8          8 ----> set argv $PWD
         4          4 ----> set -ql _flag_d
        14         14 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         4          4 ----> set -q fish_prompt_pwd_dir_length
         5          5 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         7          7 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        21       1540 ----> for path in $argv...
       209        752 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       288        543 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       167        192 -------> set -l realhome (string escape --style=regex -- ~)
        25         25 --------> string escape --style=regex -- ~
        63         63 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        19        767 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        19         19 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         7          7 ------> set -l full
        16        492 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 -------> test $fish_prompt_pwd_full_dirs -gt 0
       177        448 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       235        271 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        36         36 ---------> math $fish_prompt_pwd_full_dirs - 1
        13         13 -------> set tmp $all[1]
         7          7 -------> set full $all[2..]
       180        230 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        50         50 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        31         87 > fish_mode_prompt
        12         56 -> fish_default_mode_prompt
        13         44 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        27         27 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         4          4 ---> return
        83      58464 > fish_prompt
        31         31 -> set -l last_pipestatus $pipestatus
        11         11 -> set -lx __fish_last_status $status
       295        315 -> set -l normal (set_color --reset)
        20         20 --> set_color --reset
        15         15 -> set -l color_cwd $fish_color_cwd
         8          8 -> set -l suffix '>'
         7        201 -> if functions -q fish_is_root_user...
        13         13 --> functions -q fish_is_root_user
        24        181 --> fish_is_root_user
         8        131 ---> if test "$EUID" = 0 2>/dev/null...
       123        123 ----> test "$EUID" = 0 2>/dev/null
         3         21 ---> if contains -- $USER root toor Administrator...
        18         18 ----> contains -- $USER root toor Administrator
         5          5 ---> return 1
        10         10 -> set -l bold_flag --bold
         5          5 -> set -q __fish_prompt_status_generation
         6         24 -> if test $__fish_prompt_status_generation = $status_generation...
        12         12 --> test $__fish_prompt_status_generation = $status_generation
         6          6 --> set bold_flag
        15         15 -> set __fish_prompt_status_generation $status_generation
       207        231 -> set -l status_color (set_color $fish_color_status)
        24         24 --> set_color $fish_color_status
       231        253 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        22         22 --> set_color $bold_flag $fish_color_status
       197        399 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        75        202 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        11         11 ---> set -l last_status
        10         23 ---> if set -q __fish_last_status...
         4          4 ----> set -q __fish_last_status
         9          9 ----> set last_status $__fish_last_status
        10         10 ---> set -l left_brace $argv[1]
         7          7 ---> set -l right_brace $argv[2]
        28         28 ---> set -l separator $argv[3]
        10         10 ---> set -l brace_sep_color $argv[4]
         8          8 ---> set -l status_color $argv[5]
         7          7 ---> set -e argv[1 2 3 4 5]
         3          8 ---> if not set -q argv[1]...
         5          5 ----> not set -q argv[1]
         5         15 ---> if not contains $last_status 0 141...
        10         10 ----> not contains $last_status 0 141
      1258      56863 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        35        964 --> prompt_login
         8         16 ---> if not set -q __fish_machine...
         8          8 ----> not set -q __fish_machine
         3          8 ---> if set -q __fish_machine[1]...
         5          5 ----> set -q __fish_machine[1]
        13         13 ---> set -l color_host $fish_color_host
         3          7 ---> if set -q SSH_TTY...
         4          4 ----> set -q SSH_TTY
       729        885 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        20         20 ----> set_color $fish_color_user
        12         12 ----> set_color --reset
        22         22 ----> set_color $color_host
        32         85 ----> prompt_hostname
        53         53 -----> string replace -r -- "\..*" "" $hostname
        17         17 ----> set_color --reset
        25         25 --> set_color $color_cwd
        53       2822 --> prompt_pwd
        20         20 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        29         29 ---> argparse -n prompt_pwd $options -- $argv
        56         62 ---> if set -q _flag_help...
         6          6 ----> set -q _flag_help
         9          9 ---> set -q argv[1]
        15         15 ---> set argv $PWD
         5          5 ---> set -ql _flag_d
         6          6 ---> set -q fish_prompt_pwd_dir_length
         8          8 ---> set -l fish_prompt_pwd_dir_length 1
         6          6 ---> set -l fulldirs 0
         4          4 ---> set -ql _flag_D
         5          5 ---> set -q fish_prompt_pwd_full_dirs
         7          7 ---> set -l fish_prompt_pwd_full_dirs 1
        31       2593 ---> for path in $argv...
       383       1442 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       452       1059 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       454        482 ------> set -l realhome (string escape --style=regex -- ~)
        28         28 -------> string escape --style=regex -- ~
       125        125 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        35       1120 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        32         32 -----> test "$fish_prompt_pwd_dir_length" -eq 0
        12         12 -----> set -l full
        24        672 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        12         12 ------> test $fish_prompt_pwd_full_dirs -gt 0
       264        604 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       274        340 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        66         66 --------> math $fish_prompt_pwd_full_dirs - 1
        22         22 ------> set tmp $all[1]
        10         10 ------> set full $all[2..]
       287        369 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        82         82 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        64      51794 --> fish_vcs_prompt
        34        143 ---> fish_jj_prompt $argv
        17        109 ----> if not command -sq jj...
        82         82 -----> not command -sq jj
        10         10 -----> return 1
       160      51587 ---> fish_git_prompt $argv
        10         92 ----> if not command -sq git...
        82         82 -----> not command -sq git
         5         23 ----> if functions -q __fish_git_prompt_ready...
        18         18 -----> functions -q __fish_git_prompt_ready
       536      14258 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     13722      13722 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        45         45 ----> test -n "$repo_info"
        21         21 ----> set -l git_dir $repo_info[1]
         9          9 ----> set -l git_common_dir $repo_info[2]
         8          8 ----> set -l inside_gitdir $repo_info[3]
        11         11 ----> set -l bare_repo $repo_info[4]
        12         12 ----> set -l inside_worktree $repo_info[5]
         4          4 ----> set -q repo_info[6]
        13         13 ----> set -l sha $repo_info[6]
       281      17947 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
        79      17666 -----> __fish_git_prompt_operation_branch_bare $repo_info
        18         18 ------> set -l git_dir $argv[1]
         8          8 ------> set -l inside_gitdir $argv[3]
         7          7 ------> set -l bare_repo $argv[4]
         4          4 ------> set -q argv[6]
         8          8 ------> set -l sha $argv[6]
         4          4 ------> set -l branch
        10         10 ------> set -l operation
         5          5 ------> set -l detached no
         5          5 ------> set -l bare
         4          4 ------> set -l step
         5          5 ------> set -l total
        16        115 ------> if test -d $git_dir/rebase-merge...
        31         31 -------> test -d $git_dir/rebase-merge
        18         68 -------> if test -d $git_dir/rebase-apply...
        13         13 --------> test -d $git_dir/rebase-apply
        11         11 --------> test -f $git_dir/MERGE_HEAD
        10         10 --------> test -f $git_dir/CHERRY_PICK_HEAD
         8          8 --------> test -f $git_dir/REVERT_HEAD
         8          8 --------> test -f $git_dir/BISECT_LOG
         3         18 ------> if test -n "$step" -a -n "$total"...
        15         15 -------> test -n "$step" -a -n "$total"
        16      17306 ------> if test -z "$branch"...
         6          6 -------> test -z "$branch"
        25      17284 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       464      17259 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     16795      16795 ---------> command git symbolic-ref HEAD 2>/dev/null
         5         29 ------> if test true = $inside_gitdir...
        24         24 -------> test true = $inside_gitdir
        25         25 ------> echo $operation
         7          7 ------> echo $branch
         5          5 ------> echo $detached
         4          4 ------> echo $bare
        16         16 ----> set -l operation $branch_state[1]
         8          8 ----> set -l branch $branch_state[2]
        11         11 ----> set -l detached $branch_state[3]
         5          5 ----> set -l dirtystate
         9          9 ----> set -l stagedstate
         4          4 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         4          4 ----> set -l untrackedfiles
         6          6 ----> set -l bare_prefix $branch_state[4]
         4          4 ----> set -l upstream
         4          4 ----> set -l informative_status
         7          7 ----> set -q __fish_git_prompt_status_order
         5         10 ----> if not set -q ___fish_git_prompt_init...
         5          5 -----> not set -q ___fish_git_prompt_init
        24         24 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         4          4 ----> set -l informative
         4          4 ----> set -l dirty
         4          4 ----> set -l untracked
      1359      16329 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     14970      14970 -----> read -lz key value
        24        118 ----> if not set -q dirty[1]...
        49         49 -----> not set -q dirty[1]
        45         45 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        33         33 ----> contains dirtystate $__fish_git_prompt_status_order
         5         20 ----> if not set -q untracked[1]...
         6          6 -----> not set -q untracked[1]
         9          9 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
         8          8 ----> contains untrackedfiles $__fish_git_prompt_status_order
        24        122 ----> if test true = $inside_worktree...
        12         12 -----> test true = $inside_worktree
         9         71 -----> if test "$informative" = true...
         8          8 ------> test "$informative" = true
         5         13 ------> ...
         8          8 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        10         26 ------> if not test "$dirty" = true...
         6          6 -------> not test "$dirty" = true
         5          5 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         8         15 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         7          7 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         3         15 -----> if set -q __fish_git_prompt_showupstream...
         5          5 ------> set -q __fish_git_prompt_showupstream
         7          7 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        20         20 ----> set -l branch_color $___fish_git_prompt_color_branch
        18         18 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         9         26 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        17         17 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         7          7 ----> set -l flags ""
        23         75 ----> for i in $__fish_git_prompt_status_order...
         5         18 -----> if test -n "$$i"...
        13         13 ------> test -n "$$i"
         3         10 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         4          8 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
       477        502 ----> set branch (string replace refs/heads/ '' -- $branch)
        25         25 -----> string replace refs/heads/ '' -- $branch
       597        682 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        85         85 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       416        492 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        76         76 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        23         94 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        71         71 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
        14        101 ----> if test -n "$branch"...
        23         23 -----> test -n "$branch"
        21         21 -----> set branch "$branch_color$branch$branch_done"
         9         43 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
        14         14 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        20         20 ------> test -n "$___fish_git_prompt_char_cleanstate"
         3         12 ----> if test -n "$bare_prefix"...
         9          9 -----> test -n "$bare_prefix"
        22         32 ----> if test -n "$operation"...
        10         10 -----> test -n "$operation"
         4         11 ----> if test -n "$upstream"...
         7          7 -----> test -n "$upstream"
         3         14 ----> if test -n "$flags$bare_prefix$upstream"...
        11         11 -----> test -n "$flags$bare_prefix$upstream"
        18         18 ----> set -l format $argv[1]
         9         27 ----> if test -z "$format"...
         7          7 -----> test -z "$format"
        11         11 -----> set format " (%s)"
        95         95 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        52       5150 > fish_title
        31         31 -> set -l ssh
         8          8 -> set -q SSH_TTY
        27       5059 -> if set -q argv[1]...
         7          7 --> set -q argv[1]
       617        635 --> set -l command (status current-command)
        18         18 ---> status current-command
        15         51 --> if test "$command" = fish...
        26         26 ---> test "$command" = fish
        10         10 ---> set command
       826       4339 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        28         28 ---> string sub -l 20 -- $command
        82       3485 ---> prompt_pwd -d 1 -D 1
        26         26 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        57         57 ----> argparse -n prompt_pwd $options -- $argv
         8         17 ----> if set -q _flag_help...
         9          9 -----> set -q _flag_help
         7          7 ----> set -q argv[1]
        66         66 ----> set argv $PWD
         8          8 ----> set -ql _flag_d
        25         25 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         6          6 ----> set -q fish_prompt_pwd_dir_length
         8          8 ----> set -l fulldirs 0
        10         10 ----> set -ql _flag_D
        12         12 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         5          5 ----> set -q fish_prompt_pwd_full_dirs
        31       3156 ----> for path in $argv...
       459       1810 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       570       1351 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       632        677 -------> set -l realhome (string escape --style=regex -- ~)
        45         45 --------> string escape --style=regex -- ~
       104        104 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        35       1315 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        37         37 ------> test "$fish_prompt_pwd_dir_length" -eq 0
        11         11 ------> set -l full
        23        838 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
        14         14 -------> test $fish_prompt_pwd_full_dirs -gt 0
       336        765 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       380        429 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        49         49 ---------> math $fish_prompt_pwd_full_dirs - 1
        24         24 -------> set tmp $all[1]
        12         12 -------> set full $all[2..]
       289        394 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
       105        105 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        46        131 > fish_mode_prompt
        20         85 -> fish_default_mode_prompt
        18         65 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        40         40 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         7          7 ---> return
       113      60460 > fish_prompt
        46         46 -> set -l last_pipestatus $pipestatus
        17         17 -> set -lx __fish_last_status $status
       293        320 -> set -l normal (set_color --reset)
        27         27 --> set_color --reset
        20         20 -> set -l color_cwd $fish_color_cwd
        10         10 -> set -l suffix '>'
        10        216 -> if functions -q fish_is_root_user...
        18         18 --> functions -q fish_is_root_user
        38        188 --> fish_is_root_user
        13        111 ---> if test "$EUID" = 0 2>/dev/null...
        98         98 ----> test "$EUID" = 0 2>/dev/null
         7         32 ---> if contains -- $USER root toor Administrator...
        25         25 ----> contains -- $USER root toor Administrator
         7          7 ---> return 1
        14         14 -> set -l bold_flag --bold
         7          7 -> set -q __fish_prompt_status_generation
         9         35 -> if test $__fish_prompt_status_generation = $status_generation...
        16         16 --> test $__fish_prompt_status_generation = $status_generation
        10         10 --> set bold_flag
        44         44 -> set __fish_prompt_status_generation $status_generation
       353        384 -> set -l status_color (set_color $fish_color_status)
        31         31 --> set_color $fish_color_status
       345        377 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        32         32 --> set_color $bold_flag $fish_color_status
       248        498 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        87        250 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        17         17 ---> set -l last_status
        12         39 ---> if set -q __fish_last_status...
         7          7 ----> set -q __fish_last_status
        20         20 ----> set last_status $__fish_last_status
        18         18 ---> set -l left_brace $argv[1]
        12         12 ---> set -l right_brace $argv[2]
        10         10 ---> set -l separator $argv[3]
        11         11 ---> set -l brace_sep_color $argv[4]
        12         12 ---> set -l status_color $argv[5]
        11         11 ---> set -e argv[1 2 3 4 5]
         5         12 ---> if not set -q argv[1]...
         7          7 ----> not set -q argv[1]
         7         21 ---> if not contains $last_status 0 141...
        14         14 ----> not contains $last_status 0 141
      1511      58359 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        35       1524 --> prompt_login
        12         25 ---> if not set -q __fish_machine...
        13         13 ----> not set -q __fish_machine
         5         35 ---> if set -q __fish_machine[1]...
        30         30 ----> set -q __fish_machine[1]
        20         20 ---> set -l color_host $fish_color_host
         4         11 ---> if set -q SSH_TTY...
         7          7 ----> set -q SSH_TTY
      1134       1398 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        38         38 ----> set_color $fish_color_user
        22         22 ----> set_color --reset
        23         23 ----> set_color $color_host
        34        156 ----> prompt_hostname
       122        122 -----> string replace -r -- "\..*" "" $hostname
        25         25 ----> set_color --reset
        32         32 --> set_color $color_cwd
        68       3044 --> prompt_pwd
        25         25 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        35         35 ---> argparse -n prompt_pwd $options -- $argv
        10         18 ---> if set -q _flag_help...
         8          8 ----> set -q _flag_help
         7          7 ---> set -q argv[1]
        14         14 ---> set argv $PWD
         6          6 ---> set -ql _flag_d
         6          6 ---> set -q fish_prompt_pwd_dir_length
         8          8 ---> set -l fish_prompt_pwd_dir_length 1
         7          7 ---> set -l fulldirs 0
         5          5 ---> set -ql _flag_D
         6          6 ---> set -q fish_prompt_pwd_full_dirs
         8          8 ---> set -l fish_prompt_pwd_full_dirs 1
        34       2831 ---> for path in $argv...
       338       1121 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       443        783 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       234        266 ------> set -l realhome (string escape --style=regex -- ~)
        32         32 -------> string escape --style=regex -- ~
        74         74 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        31       1676 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        34         34 -----> test "$fish_prompt_pwd_dir_length" -eq 0
        12         12 -----> set -l full
        24       1147 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        14         14 ------> test $fish_prompt_pwd_full_dirs -gt 0
       304       1075 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       703        771 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        68         68 --------> math $fish_prompt_pwd_full_dirs - 1
        24         24 ------> set tmp $all[1]
        10         10 ------> set full $all[2..]
       370        452 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        82         82 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        61      52248 --> fish_vcs_prompt
        72        184 ---> fish_jj_prompt $argv
        16        112 ----> if not command -sq jj...
        87         87 -----> not command -sq jj
         9          9 -----> return 1
       205      52003 ---> fish_git_prompt $argv
         9         96 ----> if not command -sq git...
        87         87 -----> not command -sq git
         7         26 ----> if functions -q __fish_git_prompt_ready...
        19         19 -----> functions -q __fish_git_prompt_ready
       349      17064 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     16715      16715 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        34         34 ----> test -n "$repo_info"
        20         20 ----> set -l git_dir $repo_info[1]
        11         11 ----> set -l git_common_dir $repo_info[2]
         8          8 ----> set -l inside_gitdir $repo_info[3]
         9          9 ----> set -l bare_repo $repo_info[4]
        14         14 ----> set -l inside_worktree $repo_info[5]
         5          5 ----> set -q repo_info[6]
         9          9 ----> set -l sha $repo_info[6]
       256      16613 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
        95      16357 -----> __fish_git_prompt_operation_branch_bare $repo_info
        20         20 ------> set -l git_dir $argv[1]
        11         11 ------> set -l inside_gitdir $argv[3]
         8          8 ------> set -l bare_repo $argv[4]
         4          4 ------> set -q argv[6]
        33         33 ------> set -l sha $argv[6]
         5          5 ------> set -l branch
        10         10 ------> set -l operation
         7          7 ------> set -l detached no
         5          5 ------> set -l bare
         4          4 ------> set -l step
         4          4 ------> set -l total
        14        117 ------> if test -d $git_dir/rebase-merge...
        33         33 -------> test -d $git_dir/rebase-merge
        20         70 -------> if test -d $git_dir/rebase-apply...
        14         14 --------> test -d $git_dir/rebase-apply
        10         10 --------> test -f $git_dir/MERGE_HEAD
        10         10 --------> test -f $git_dir/CHERRY_PICK_HEAD
         8          8 --------> test -f $git_dir/REVERT_HEAD
         8          8 --------> test -f $git_dir/BISECT_LOG
         4         19 ------> if test -n "$step" -a -n "$total"...
        15         15 -------> test -n "$step" -a -n "$total"
         7      15939 ------> if test -z "$branch"...
         6          6 -------> test -z "$branch"
        23      15926 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       334      15903 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     15569      15569 ---------> command git symbolic-ref HEAD 2>/dev/null
         6         34 ------> if test true = $inside_gitdir...
        28         28 -------> test true = $inside_gitdir
        24         24 ------> echo $operation
         8          8 ------> echo $branch
         5          5 ------> echo $detached
         5          5 ------> echo $bare
        18         18 ----> set -l operation $branch_state[1]
         8          8 ----> set -l branch $branch_state[2]
         6          6 ----> set -l detached $branch_state[3]
         6          6 ----> set -l dirtystate
        14         14 ----> set -l stagedstate
         4          4 ----> set -l invalidstate
         5          5 ----> set -l stashstate
         5          5 ----> set -l untrackedfiles
         8          8 ----> set -l bare_prefix $branch_state[4]
         5          5 ----> set -l upstream
         5          5 ----> set -l informative_status
         8          8 ----> set -q __fish_git_prompt_status_order
         6         12 ----> if not set -q ___fish_git_prompt_init...
         6          6 -----> not set -q ___fish_git_prompt_init
        25         25 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         4          4 ----> set -l informative
         4          4 ----> set -l dirty
         4          4 ----> set -l untracked
      1432      15927 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     14495      14495 -----> read -lz key value
        21        101 ----> if not set -q dirty[1]...
        38         38 -----> not set -q dirty[1]
        42         42 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        26         26 ----> contains dirtystate $__fish_git_prompt_status_order
         7         22 ----> if not set -q untracked[1]...
         6          6 -----> not set -q untracked[1]
         9          9 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        10         10 ----> contains untrackedfiles $__fish_git_prompt_status_order
        13        132 ----> if test true = $inside_worktree...
        11         11 -----> test true = $inside_worktree
        10         89 -----> if test "$informative" = true...
         7          7 ------> test "$informative" = true
         5         15 ------> ...
        10         10 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        12         30 ------> if not test "$dirty" = true...
         6          6 -------> not test "$dirty" = true
         7          7 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
        10         27 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
        17         17 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         5         19 -----> if set -q __fish_git_prompt_showupstream...
         5          5 ------> set -q __fish_git_prompt_showupstream
         9          9 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        22         22 ----> set -l branch_color $___fish_git_prompt_color_branch
        21         21 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         7         27 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        20         20 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         8          8 ----> set -l flags ""
        28         82 ----> for i in $__fish_git_prompt_status_order...
         6         15 -----> if test -n "$$i"...
         9          9 ------> test -n "$$i"
         4         10 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         4         11 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         4          9 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
       245        275 ----> set branch (string replace refs/heads/ '' -- $branch)
        30         30 -----> string replace refs/heads/ '' -- $branch
       222        288 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        66         66 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       390        447 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        57         57 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        18         88 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        70         70 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
        11         89 ----> if test -n "$branch"...
        20         20 -----> test -n "$branch"
        20         20 -----> set branch "$branch_color$branch$branch_done"
        10         38 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
        12         12 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        16         16 ------> test -n "$___fish_git_prompt_char_cleanstate"
         5         13 ----> if test -n "$bare_prefix"...
         8          8 -----> test -n "$bare_prefix"
         3         11 ----> if test -n "$operation"...
         8          8 -----> test -n "$operation"
         3         10 ----> if test -n "$upstream"...
         7          7 -----> test -n "$upstream"
         4         14 ----> if test -n "$flags$bare_prefix$upstream"...
        10         10 -----> test -n "$flags$bare_prefix$upstream"
        16         16 ----> set -l format $argv[1]
         7         24 ----> if test -z "$format"...
         7          7 -----> test -z "$format"
        10         10 -----> set format " (%s)"
        95         95 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        46       3873 > fish_title
        29         29 -> set -l ssh
         8          8 -> set -q SSH_TTY
        23       3790 -> if set -q argv[1]...
         7          7 --> set -q argv[1]
       139        154 --> set -l command (status current-command)
        15         15 ---> status current-command
        12         44 --> if test "$command" = fish...
        23         23 ---> test "$command" = fish
         9          9 ---> set command
       347       3562 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        22         22 ---> string sub -l 20 -- $command
        69       3193 ---> prompt_pwd -d 1 -D 1
        29         29 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        51         51 ----> argparse -n prompt_pwd $options -- $argv
         7         15 ----> if set -q _flag_help...
         8          8 -----> set -q _flag_help
         6          6 ----> set -q argv[1]
        13         13 ----> set argv $PWD
         5          5 ----> set -ql _flag_d
        24         24 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         5          5 ----> set -q fish_prompt_pwd_dir_length
         9          9 ----> set -l fulldirs 0
         4          4 ----> set -ql _flag_D
        12         12 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         5          5 ----> set -q fish_prompt_pwd_full_dirs
        30       2946 ----> for path in $argv...
       515       1761 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       838       1246 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       260        313 -------> set -l realhome (string escape --style=regex -- ~)
        53         53 --------> string escape --style=regex -- ~
        95         95 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        28       1155 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        30         30 ------> test "$fish_prompt_pwd_dir_length" -eq 0
        11         11 ------> set -l full
        23        738 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
        14         14 -------> test $fish_prompt_pwd_full_dirs -gt 0
       265        668 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       353        403 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        50         50 ---------> math $fish_prompt_pwd_full_dirs - 1
        21         21 -------> set tmp $all[1]
        12         12 -------> set full $all[2..]
       252        348 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        96         96 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        39        124 > fish_mode_prompt
        20         85 -> fish_default_mode_prompt
        16         65 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        38         38 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
        11         11 ---> return
        97      63373 > fish_prompt
        90         90 -> set -l last_pipestatus $pipestatus
        19         19 -> set -lx __fish_last_status $status
       382        409 -> set -l normal (set_color --reset)
        27         27 --> set_color --reset
        20         20 -> set -l color_cwd $fish_color_cwd
        12         12 -> set -l suffix '>'
        11        211 -> if functions -q fish_is_root_user...
        18         18 --> functions -q fish_is_root_user
        40        182 --> fish_is_root_user
        13        108 ---> if test "$EUID" = 0 2>/dev/null...
        95         95 ----> test "$EUID" = 0 2>/dev/null
         6         28 ---> if contains -- $USER root toor Administrator...
        22         22 ----> contains -- $USER root toor Administrator
         6          6 ---> return 1
        12         12 -> set -l bold_flag --bold
         8          8 -> set -q __fish_prompt_status_generation
         8         36 -> if test $__fish_prompt_status_generation = $status_generation...
        19         19 --> test $__fish_prompt_status_generation = $status_generation
         9          9 --> set bold_flag
        73         73 -> set __fish_prompt_status_generation $status_generation
       285        320 -> set -l status_color (set_color $fish_color_status)
        35         35 --> set_color $fish_color_status
       270        350 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        80         80 --> set_color $bold_flag $fish_color_status
       264        567 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        72        303 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        14         14 ---> set -l last_status
        13         33 ---> if set -q __fish_last_status...
         7          7 ----> set -q __fish_last_status
        13         13 ----> set last_status $__fish_last_status
        17         17 ---> set -l left_brace $argv[1]
        12         12 ---> set -l right_brace $argv[2]
        10         10 ---> set -l separator $argv[3]
        11         11 ---> set -l brace_sep_color $argv[4]
        13         13 ---> set -l status_color $argv[5]
        11         11 ---> set -e argv[1 2 3 4 5]
         8         85 ---> if not set -q argv[1]...
        77         77 ----> not set -q argv[1]
         9         25 ---> if not contains $last_status 0 141...
        16         16 ----> not contains $last_status 0 141
       868      61149 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        35       1125 --> prompt_login
        11         22 ---> if not set -q __fish_machine...
        11         11 ----> not set -q __fish_machine
         3         12 ---> if set -q __fish_machine[1]...
         9          9 ----> set -q __fish_machine[1]
        19         19 ---> set -l color_host $fish_color_host
         4         10 ---> if set -q SSH_TTY...
         6          6 ----> set -q SSH_TTY
       827       1027 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        29         29 ----> set_color $fish_color_user
        17         17 ----> set_color --reset
        25         25 ----> set_color $color_host
        31        109 ----> prompt_hostname
        78         78 -----> string replace -r -- "\..*" "" $hostname
        20         20 ----> set_color --reset
        30         30 --> set_color $color_cwd
        59       2877 --> prompt_pwd
        20         20 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        32         32 ---> argparse -n prompt_pwd $options -- $argv
         7         14 ---> if set -q _flag_help...
         7          7 ----> set -q _flag_help
         7          7 ---> set -q argv[1]
        13         13 ---> set argv $PWD
         6          6 ---> set -ql _flag_d
         7          7 ---> set -q fish_prompt_pwd_dir_length
         9          9 ---> set -l fish_prompt_pwd_dir_length 1
         7          7 ---> set -l fulldirs 0
         4          4 ---> set -ql _flag_D
         6          6 ---> set -q fish_prompt_pwd_full_dirs
         9          9 ---> set -l fish_prompt_pwd_full_dirs 1
        33       2684 ---> for path in $argv...
       296       1214 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       492        918 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       317        348 ------> set -l realhome (string escape --style=regex -- ~)
        31         31 -------> string escape --style=regex -- ~
        78         78 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        31       1437 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        34         34 -----> test "$fish_prompt_pwd_dir_length" -eq 0
        11         11 -----> set -l full
        26        871 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        13         13 ------> test $fish_prompt_pwd_full_dirs -gt 0
       294        796 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       446        502 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        56         56 --------> math $fish_prompt_pwd_full_dirs - 1
        24         24 ------> set tmp $all[1]
        12         12 ------> set full $all[2..]
       400        490 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        90         90 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        47      56249 --> fish_vcs_prompt
        33        157 ---> fish_jj_prompt $argv
        19        124 ----> if not command -sq jj...
        95         95 -----> not command -sq jj
        10         10 -----> return 1
       139      56045 ---> fish_git_prompt $argv
        11        107 ----> if not command -sq git...
        96         96 -----> not command -sq git
         8         28 ----> if functions -q __fish_git_prompt_ready...
        20         20 -----> functions -q __fish_git_prompt_ready
       371      19552 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     19181      19181 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        37         37 ----> test -n "$repo_info"
        20         20 ----> set -l git_dir $repo_info[1]
        10         10 ----> set -l git_common_dir $repo_info[2]
         6          6 ----> set -l inside_gitdir $repo_info[3]
         7          7 ----> set -l bare_repo $repo_info[4]
        10         10 ----> set -l inside_worktree $repo_info[5]
         4          4 ----> set -q repo_info[6]
         7          7 ----> set -l sha $repo_info[6]
       266      16571 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
       113      16305 -----> __fish_git_prompt_operation_branch_bare $repo_info
        19         19 ------> set -l git_dir $argv[1]
         8          8 ------> set -l inside_gitdir $argv[3]
         5          5 ------> set -l bare_repo $argv[4]
         3          3 ------> set -q argv[6]
         8          8 ------> set -l sha $argv[6]
         5          5 ------> set -l branch
         8          8 ------> set -l operation
         4          4 ------> set -l detached no
         4          4 ------> set -l bare
         4          4 ------> set -l step
         3          3 ------> set -l total
        10         95 ------> if test -d $git_dir/rebase-merge...
        25         25 -------> test -d $git_dir/rebase-merge
        17         60 -------> if test -d $git_dir/rebase-apply...
        12         12 --------> test -d $git_dir/rebase-apply
        10         10 --------> test -f $git_dir/MERGE_HEAD
         8          8 --------> test -f $git_dir/CHERRY_PICK_HEAD
         7          7 --------> test -f $git_dir/REVERT_HEAD
         6          6 --------> test -f $git_dir/BISECT_LOG
         4         17 ------> if test -n "$step" -a -n "$total"...
        13         13 -------> test -n "$step" -a -n "$total"
         7      15940 ------> if test -z "$branch"...
         5          5 -------> test -z "$branch"
        20      15928 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       366      15908 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     15542      15542 ---------> command git symbolic-ref HEAD 2>/dev/null
         5         30 ------> if test true = $inside_gitdir...
        25         25 -------> test true = $inside_gitdir
        23         23 ------> echo $operation
         7          7 ------> echo $branch
         5          5 ------> echo $detached
         4          4 ------> echo $bare
        18         18 ----> set -l operation $branch_state[1]
        10         10 ----> set -l branch $branch_state[2]
         6          6 ----> set -l detached $branch_state[3]
         5          5 ----> set -l dirtystate
        10         10 ----> set -l stagedstate
         5          5 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         4          4 ----> set -l untrackedfiles
         5          5 ----> set -l bare_prefix $branch_state[4]
         4          4 ----> set -l upstream
         4          4 ----> set -l informative_status
         7          7 ----> set -q __fish_git_prompt_status_order
         7         12 ----> if not set -q ___fish_git_prompt_init...
         5          5 -----> not set -q ___fish_git_prompt_init
        23         23 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         5          5 ----> set -l informative
         4          4 ----> set -l dirty
         4          4 ----> set -l untracked
      1350      17738 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     16388      16388 -----> read -lz key value
        21        109 ----> if not set -q dirty[1]...
        41         41 -----> not set -q dirty[1]
        47         47 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        32         32 ----> contains dirtystate $__fish_git_prompt_status_order
         8         35 ----> if not set -q untracked[1]...
         8          8 -----> not set -q untracked[1]
        19         19 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        12         12 ----> contains untrackedfiles $__fish_git_prompt_status_order
        24        140 ----> if test true = $inside_worktree...
        13         13 -----> test true = $inside_worktree
        11         86 -----> if test "$informative" = true...
        10         10 ------> test "$informative" = true
         6         20 ------> ...
        14         14 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        12         30 ------> if not test "$dirty" = true...
         7          7 -------> not test "$dirty" = true
         6          6 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         7         15 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         8          8 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         4         17 -----> if set -q __fish_git_prompt_showupstream...
         6          6 ------> set -q __fish_git_prompt_showupstream
         7          7 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        21         21 ----> set -l branch_color $___fish_git_prompt_color_branch
        20         20 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         6         15 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
         9          9 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         7          7 ----> set -l flags ""
        30         81 ----> for i in $__fish_git_prompt_status_order...
         4         18 -----> if test -n "$$i"...
        14         14 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         2          7 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
       294        328 ----> set branch (string replace refs/heads/ '' -- $branch)
        34         34 -----> string replace refs/heads/ '' -- $branch
       273        337 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        64         64 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       244        298 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        54         54 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        13         58 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        45         45 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         7         56 ----> if test -n "$branch"...
        13         13 -----> test -n "$branch"
        12         12 -----> set branch "$branch_color$branch$branch_done"
         6         24 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        10         10 ------> test -n "$___fish_git_prompt_char_cleanstate"
         3          8 ----> if test -n "$bare_prefix"...
         5          5 -----> test -n "$bare_prefix"
         2          7 ----> if test -n "$operation"...
         5          5 -----> test -n "$operation"
         2          8 ----> if test -n "$upstream"...
         6          6 -----> test -n "$upstream"
         3         22 ----> if test -n "$flags$bare_prefix$upstream"...
        19         19 -----> test -n "$flags$bare_prefix$upstream"
        10         10 ----> set -l format $argv[1]
         5         16 ----> if test -z "$format"...
         5          5 -----> test -z "$format"
         6          6 -----> set format " (%s)"
        59         59 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        32       3763 > fish_title
        13         13 -> set -l ssh
         5          5 -> set -q SSH_TTY
        27       3713 -> if set -q argv[1]...
         5          5 --> set -q argv[1]
       168        179 --> set -l command (status current-command)
        11         11 ---> status current-command
         8         29 --> if test "$command" = fish...
        15         15 ---> test "$command" = fish
         6          6 ---> set command
       480       3473 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        14         14 ---> string sub -l 20 -- $command
        56       2979 ---> prompt_pwd -d 1 -D 1
        13         13 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        66         66 ----> argparse -n prompt_pwd $options -- $argv
         5         11 ----> if set -q _flag_help...
         6          6 -----> set -q _flag_help
         4          4 ----> set -q argv[1]
         9          9 ----> set argv $PWD
         4          4 ----> set -ql _flag_d
        14         14 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         3          3 ----> set -q fish_prompt_pwd_dir_length
         4          4 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         7          7 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        30       2782 ----> for path in $argv...
       315       1320 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       687       1005 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       216        248 -------> set -l realhome (string escape --style=regex -- ~)
        32         32 --------> string escape --style=regex -- ~
        70         70 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        36       1432 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        43         43 ------> test "$fish_prompt_pwd_dir_length" -eq 0
        17         17 ------> set -l full
        33        867 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
        18         18 -------> test $fish_prompt_pwd_full_dirs -gt 0
       381        770 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       332        389 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        57         57 ---------> math $fish_prompt_pwd_full_dirs - 1
        30         30 -------> set tmp $all[1]
        16         16 -------> set full $all[2..]
       369        469 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
       100        100 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        47        143 > fish_mode_prompt
        26         96 -> fish_default_mode_prompt
        20         70 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        42         42 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         8          8 ---> return
       115      78937 > fish_prompt
        44         44 -> set -l last_pipestatus $pipestatus
        22         22 -> set -lx __fish_last_status $status
       715        749 -> set -l normal (set_color --reset)
        34         34 --> set_color --reset
        41         41 -> set -l color_cwd $fish_color_cwd
        17         17 -> set -l suffix '>'
        13        300 -> if functions -q fish_is_root_user...
        28         28 --> functions -q fish_is_root_user
        48        259 --> fish_is_root_user
        17        161 ---> if test "$EUID" = 0 2>/dev/null...
       144        144 ----> test "$EUID" = 0 2>/dev/null
         8         41 ---> if contains -- $USER root toor Administrator...
        33         33 ----> contains -- $USER root toor Administrator
         9          9 ---> return 1
        19         19 -> set -l bold_flag --bold
        10         10 -> set -q __fish_prompt_status_generation
        12         47 -> if test $__fish_prompt_status_generation = $status_generation...
        23         23 --> test $__fish_prompt_status_generation = $status_generation
        12         12 --> set bold_flag
        35         35 -> set __fish_prompt_status_generation $status_generation
      1062       1113 -> set -l status_color (set_color $fish_color_status)
        51         51 --> set_color $fish_color_status
       408        473 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        65         65 --> set_color $bold_flag $fish_color_status
       587       1016 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
       136        429 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        39         39 ---> set -l last_status
        20        103 ---> if set -q __fish_last_status...
        59         59 ----> set -q __fish_last_status
        24         24 ----> set last_status $__fish_last_status
        22         22 ---> set -l left_brace $argv[1]
        14         14 ---> set -l right_brace $argv[2]
        13         13 ---> set -l separator $argv[3]
        14         14 ---> set -l brace_sep_color $argv[4]
        23         23 ---> set -l status_color $argv[5]
        16         16 ---> set -e argv[1 2 3 4 5]
         8         17 ---> if not set -q argv[1]...
         9          9 ----> not set -q argv[1]
         9         32 ---> if not contains $last_status 0 141...
        23         23 ----> not contains $last_status 0 141
      1805      74936 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        51       2068 --> prompt_login
        17         36 ---> if not set -q __fish_machine...
        19         19 ----> not set -q __fish_machine
         6         16 ---> if set -q __fish_machine[1]...
        10         10 ----> set -q __fish_machine[1]
        30         30 ---> set -l color_host $fish_color_host
         6         15 ---> if set -q SSH_TTY...
         9          9 ----> set -q SSH_TTY
      1653       1920 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        49         49 ----> set_color $fish_color_user
        29         29 ----> set_color --reset
        36         36 ----> set_color $color_host
        43        125 ----> prompt_hostname
        82         82 -----> string replace -r -- "\..*" "" $hostname
        28         28 ----> set_color --reset
       113        113 --> set_color $color_cwd
       117       4470 --> prompt_pwd
        37         37 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        46         46 ---> argparse -n prompt_pwd $options -- $argv
        11         22 ---> if set -q _flag_help...
        11         11 ----> set -q _flag_help
         9          9 ---> set -q argv[1]
        17         17 ---> set argv $PWD
         6          6 ---> set -ql _flag_d
        10         10 ---> set -q fish_prompt_pwd_dir_length
        10         10 ---> set -l fish_prompt_pwd_dir_length 1
        11         11 ---> set -l fulldirs 0
         5          5 ---> set -ql _flag_D
         7          7 ---> set -q fish_prompt_pwd_full_dirs
         9          9 ---> set -l fish_prompt_pwd_full_dirs 1
       100       4164 ---> for path in $argv...
       503       2331 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       641       1828 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
      1032       1077 ------> set -l realhome (string escape --style=regex -- ~)
        45         45 -------> string escape --style=regex -- ~
       110        110 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        44       1733 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        40         40 -----> test "$fish_prompt_pwd_dir_length" -eq 0
        14         14 -----> set -l full
        32       1140 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        15         15 ------> test $fish_prompt_pwd_full_dirs -gt 0
       363       1052 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       635        689 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        54         54 --------> math $fish_prompt_pwd_full_dirs - 1
        27         27 ------> set tmp $all[1]
        14         14 ------> set full $all[2..]
       397        495 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        98         98 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        63      66480 --> fish_vcs_prompt
        41        197 ---> fish_jj_prompt $argv
        22        156 ----> if not command -sq jj...
       121        121 -----> not command -sq jj
        13         13 -----> return 1
       190      66220 ---> fish_git_prompt $argv
        13        124 ----> if not command -sq git...
       111        111 -----> not command -sq git
         9         35 ----> if functions -q __fish_git_prompt_ready...
        26         26 -----> functions -q __fish_git_prompt_ready
       556      19310 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     18754      18754 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        59         59 ----> test -n "$repo_info"
        36         36 ----> set -l git_dir $repo_info[1]
        15         15 ----> set -l git_common_dir $repo_info[2]
        13         13 ----> set -l inside_gitdir $repo_info[3]
        16         16 ----> set -l bare_repo $repo_info[4]
        22         22 ----> set -l inside_worktree $repo_info[5]
         8          8 ----> set -q repo_info[6]
        25         25 ----> set -l sha $repo_info[6]
       594      22509 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
       132      21915 -----> __fish_git_prompt_operation_branch_bare $repo_info
        33         33 ------> set -l git_dir $argv[1]
        15         15 ------> set -l inside_gitdir $argv[3]
        11         11 ------> set -l bare_repo $argv[4]
         7          7 ------> set -q argv[6]
        13         13 ------> set -l sha $argv[6]
         8          8 ------> set -l branch
        16         16 ------> set -l operation
         9          9 ------> set -l detached no
         8          8 ------> set -l bare
         8          8 ------> set -l step
         7          7 ------> set -l total
        22        184 ------> if test -d $git_dir/rebase-merge...
        45         45 -------> test -d $git_dir/rebase-merge
        26        117 -------> if test -d $git_dir/rebase-apply...
        26         26 --------> test -d $git_dir/rebase-apply
        19         19 --------> test -f $git_dir/MERGE_HEAD
        16         16 --------> test -f $git_dir/CHERRY_PICK_HEAD
        15         15 --------> test -f $git_dir/REVERT_HEAD
        15         15 --------> test -f $git_dir/BISECT_LOG
         8         33 ------> if test -n "$step" -a -n "$total"...
        25         25 -------> test -n "$step" -a -n "$total"
         9      21337 ------> if test -z "$branch"...
        11         11 -------> test -z "$branch"
        28      21317 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       898      21289 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     20391      20391 ---------> command git symbolic-ref HEAD 2>/dev/null
         7         41 ------> if test true = $inside_gitdir...
        34         34 -------> test true = $inside_gitdir
        30         30 ------> echo $operation
         9          9 ------> echo $branch
         7          7 ------> echo $detached
         7          7 ------> echo $bare
        25         25 ----> set -l operation $branch_state[1]
         7          7 ----> set -l branch $branch_state[2]
         8          8 ----> set -l detached $branch_state[3]
         5          5 ----> set -l dirtystate
        12         12 ----> set -l stagedstate
         5          5 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         7          7 ----> set -l untrackedfiles
         7          7 ----> set -l bare_prefix $branch_state[4]
         5          5 ----> set -l upstream
         6          6 ----> set -l informative_status
         7          7 ----> set -q __fish_git_prompt_status_order
         8         14 ----> if not set -q ___fish_git_prompt_init...
         6          6 -----> not set -q ___fish_git_prompt_init
        27         27 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         4          4 ----> set -l informative
         4          4 ----> set -l dirty
         4          4 ----> set -l untracked
      1501      22211 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     20710      20710 -----> read -lz key value
        27        112 ----> if not set -q dirty[1]...
        41         41 -----> not set -q dirty[1]
        44         44 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        26         26 ----> contains dirtystate $__fish_git_prompt_status_order
         7         24 ----> if not set -q untracked[1]...
         8          8 -----> not set -q untracked[1]
         9          9 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
         8          8 ----> contains untrackedfiles $__fish_git_prompt_status_order
         9        131 ----> if test true = $inside_worktree...
        13         13 -----> test true = $inside_worktree
        11         89 -----> if test "$informative" = true...
         7          7 ------> test "$informative" = true
         6         17 ------> ...
        11         11 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        12         28 ------> if not test "$dirty" = true...
         6          6 -------> not test "$dirty" = true
         5          5 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         8         26 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
        18         18 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         4         20 -----> if set -q __fish_git_prompt_showupstream...
         7          7 ------> set -q __fish_git_prompt_showupstream
         9          9 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        20         20 ----> set -l branch_color $___fish_git_prompt_color_branch
        22         22 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         5         14 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
         9          9 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         7          7 ----> set -l flags ""
        26         74 ----> for i in $__fish_git_prompt_status_order...
         4         14 -----> if test -n "$$i"...
        10         10 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         2          7 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3         10 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
       356        391 ----> set branch (string replace refs/heads/ '' -- $branch)
        35         35 -----> string replace refs/heads/ '' -- $branch
       190        250 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        60         60 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       162        205 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        43         43 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        11         51 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        40         40 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         6         52 ----> if test -n "$branch"...
        12         12 -----> test -n "$branch"
        12         12 -----> set branch "$branch_color$branch$branch_done"
         6         22 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
         8          8 ------> test -n "$___fish_git_prompt_char_cleanstate"
         2          7 ----> if test -n "$bare_prefix"...
         5          5 -----> test -n "$bare_prefix"
         2          6 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         3          7 ----> if test -n "$upstream"...
         4          4 -----> test -n "$upstream"
         2          8 ----> if test -n "$flags$bare_prefix$upstream"...
         6          6 -----> test -n "$flags$bare_prefix$upstream"
         9          9 ----> set -l format $argv[1]
         4         14 ----> if test -z "$format"...
         4          4 -----> test -z "$format"
         6          6 -----> set format " (%s)"
        58         58 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        32       3106 > fish_title
        16         16 -> set -l ssh
         4          4 -> set -q SSH_TTY
        39       3054 -> if set -q argv[1]...
         4          4 --> set -q argv[1]
       178        191 --> set -l command (status current-command)
        13         13 ---> status current-command
         9         29 --> if test "$command" = fish...
        14         14 ---> test "$command" = fish
         6          6 ---> set command
       446       2791 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        13         13 ---> string sub -l 20 -- $command
        57       2332 ---> prompt_pwd -d 1 -D 1
        13         13 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        34         34 ----> argparse -n prompt_pwd $options -- $argv
         5         10 ----> if set -q _flag_help...
         5          5 -----> set -q _flag_help
         4          4 ----> set -q argv[1]
        26         26 ----> set argv $PWD
         4          4 ----> set -ql _flag_d
        37         37 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         4          4 ----> set -q fish_prompt_pwd_dir_length
         5          5 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         6          6 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        34       2126 ----> for path in $argv...
       299       1092 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       549        793 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       163        186 -------> set -l realhome (string escape --style=regex -- ~)
        23         23 --------> string escape --style=regex -- ~
        58         58 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        35       1000 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        25         25 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         9          9 ------> set -l full
        28        511 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 -------> test $fish_prompt_pwd_full_dirs -gt 0
       232        426 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       160        194 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        34         34 ---------> math $fish_prompt_pwd_full_dirs - 1
        30         30 -------> set tmp $all[1]
        19         19 -------> set full $all[2..]
       315        420 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
       105        105 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        56        179 > fish_mode_prompt
        29        123 -> fish_default_mode_prompt
        28         94 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        55         55 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
        11         11 ---> return
       128      65909 > fish_prompt
        57         57 -> set -l last_pipestatus $pipestatus
        24         24 -> set -lx __fish_last_status $status
       336        377 -> set -l normal (set_color --reset)
        41         41 --> set_color --reset
        33         33 -> set -l color_cwd $fish_color_cwd
        16         16 -> set -l suffix '>'
        15        296 -> if functions -q fish_is_root_user...
        26         26 --> functions -q fish_is_root_user
        47        255 --> fish_is_root_user
        20        156 ---> if test "$EUID" = 0 2>/dev/null...
       136        136 ----> test "$EUID" = 0 2>/dev/null
         8         42 ---> if contains -- $USER root toor Administrator...
        34         34 ----> contains -- $USER root toor Administrator
        10         10 ---> return 1
        23         23 -> set -l bold_flag --bold
        12         12 -> set -q __fish_prompt_status_generation
        11         56 -> if test $__fish_prompt_status_generation = $status_generation...
        30         30 --> test $__fish_prompt_status_generation = $status_generation
        15         15 --> set bold_flag
        32         32 -> set __fish_prompt_status_generation $status_generation
       492        546 -> set -l status_color (set_color $fish_color_status)
        54         54 --> set_color $fish_color_status
       296        343 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        47         47 --> set_color $bold_flag $fish_color_status
       352        692 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
       107        340 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        23         23 ---> set -l last_status
        18         48 ---> if set -q __fish_last_status...
        10         10 ----> set -q __fish_last_status
        20         20 ----> set last_status $__fish_last_status
        23         23 ---> set -l left_brace $argv[1]
        21         21 ---> set -l right_brace $argv[2]
        16         16 ---> set -l separator $argv[3]
        16         16 ---> set -l brace_sep_color $argv[4]
        18         18 ---> set -l status_color $argv[5]
        17         17 ---> set -e argv[1 2 3 4 5]
         8         19 ---> if not set -q argv[1]...
        11         11 ----> not set -q argv[1]
        11         32 ---> if not contains $last_status 0 141...
        21         21 ----> not contains $last_status 0 141
       754      63274 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        75       1622 --> prompt_login
        18         38 ---> if not set -q __fish_machine...
        20         20 ----> not set -q __fish_machine
         5         18 ---> if set -q __fish_machine[1]...
        13         13 ----> set -q __fish_machine[1]
        27         27 ---> set -l color_host $fish_color_host
         7         16 ---> if set -q SSH_TTY...
         9          9 ----> set -q SSH_TTY
      1211       1448 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        41         41 ----> set_color $fish_color_user
        31         31 ----> set_color --reset
        37         37 ----> set_color $color_host
        27        110 ----> prompt_hostname
        83         83 -----> string replace -r -- "\..*" "" $hostname
        18         18 ----> set_color --reset
        25         25 --> set_color $color_cwd
        51       2707 --> prompt_pwd
        19         19 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        29         29 ---> argparse -n prompt_pwd $options -- $argv
         9         15 ---> if set -q _flag_help...
         6          6 ----> set -q _flag_help
         5          5 ---> set -q argv[1]
        11         11 ---> set argv $PWD
         4          4 ---> set -ql _flag_d
         4          4 ---> set -q fish_prompt_pwd_dir_length
         7          7 ---> set -l fish_prompt_pwd_dir_length 1
         5          5 ---> set -l fulldirs 0
         3          3 ---> set -ql _flag_D
         4          4 ---> set -q fish_prompt_pwd_full_dirs
         5          5 ---> set -l fish_prompt_pwd_full_dirs 1
        29       2545 ---> for path in $argv...
       250       1550 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       422       1300 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       760        788 ------> set -l realhome (string escape --style=regex -- ~)
        28         28 -------> string escape --style=regex -- ~
        90         90 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        31        966 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        34         34 -----> test "$fish_prompt_pwd_dir_length" -eq 0
        11         11 -----> set -l full
        22        545 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        10         10 ------> test $fish_prompt_pwd_full_dirs -gt 0
       226        487 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       211        261 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        50         50 --------> math $fish_prompt_pwd_full_dirs - 1
        17         17 ------> set tmp $all[1]
         9          9 ------> set full $all[2..]
       201        345 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
       144        144 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        57      58166 --> fish_vcs_prompt
        40        266 ---> fish_jj_prompt $argv
       120        226 ----> if not command -sq jj...
        98         98 -----> not command -sq jj
         8          8 -----> return 1
       154      57843 ---> fish_git_prompt $argv
        10        169 ----> if not command -sq git...
       159        159 -----> not command -sq git
         6         29 ----> if functions -q __fish_git_prompt_ready...
        23         23 -----> functions -q __fish_git_prompt_ready
       492      21818 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     21326      21326 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        45         45 ----> test -n "$repo_info"
        21         21 ----> set -l git_dir $repo_info[1]
        10         10 ----> set -l git_common_dir $repo_info[2]
         6          6 ----> set -l inside_gitdir $repo_info[3]
         7          7 ----> set -l bare_repo $repo_info[4]
        10         10 ----> set -l inside_worktree $repo_info[5]
         4          4 ----> set -q repo_info[6]
         9          9 ----> set -l sha $repo_info[6]
       255      13419 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
        93      13164 -----> __fish_git_prompt_operation_branch_bare $repo_info
        24         24 ------> set -l git_dir $argv[1]
         9          9 ------> set -l inside_gitdir $argv[3]
         6          6 ------> set -l bare_repo $argv[4]
         4          4 ------> set -q argv[6]
        40         40 ------> set -l sha $argv[6]
         6          6 ------> set -l branch
         7          7 ------> set -l operation
         5          5 ------> set -l detached no
         4          4 ------> set -l bare
         3          3 ------> set -l step
         4          4 ------> set -l total
        14        123 ------> if test -d $git_dir/rebase-merge...
        36         36 -------> test -d $git_dir/rebase-merge
        25         73 -------> if test -d $git_dir/rebase-apply...
        13         13 --------> test -d $git_dir/rebase-apply
        10         10 --------> test -f $git_dir/MERGE_HEAD
        10         10 --------> test -f $git_dir/CHERRY_PICK_HEAD
         8          8 --------> test -f $git_dir/REVERT_HEAD
         7          7 --------> test -f $git_dir/BISECT_LOG
         4         24 ------> if test -n "$step" -a -n "$total"...
        20         20 -------> test -n "$step" -a -n "$total"
         8      12747 ------> if test -z "$branch"...
         6          6 -------> test -z "$branch"
        21      12733 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       332      12712 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     12380      12380 ---------> command git symbolic-ref HEAD 2>/dev/null
         5         28 ------> if test true = $inside_gitdir...
        23         23 -------> test true = $inside_gitdir
        21         21 ------> echo $operation
         7          7 ------> echo $branch
         5          5 ------> echo $detached
         4          4 ------> echo $bare
        17         17 ----> set -l operation $branch_state[1]
         9          9 ----> set -l branch $branch_state[2]
         8          8 ----> set -l detached $branch_state[3]
         5          5 ----> set -l dirtystate
         8          8 ----> set -l stagedstate
         3          3 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         4          4 ----> set -l untrackedfiles
         6          6 ----> set -l bare_prefix $branch_state[4]
         4          4 ----> set -l upstream
         4          4 ----> set -l informative_status
         8          8 ----> set -q __fish_git_prompt_status_order
         3          9 ----> if not set -q ___fish_git_prompt_init...
         6          6 -----> not set -q ___fish_git_prompt_init
        19         19 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         5          5 ----> set -l informative
         4          4 ----> set -l dirty
         3          3 ----> set -l untracked
      1408      20558 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     19150      19150 -----> read -lz key value
        22        104 ----> if not set -q dirty[1]...
        40         40 -----> not set -q dirty[1]
        42         42 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        31         31 ----> contains dirtystate $__fish_git_prompt_status_order
         8         49 ----> if not set -q untracked[1]...
         7          7 -----> not set -q untracked[1]
        34         34 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        13         13 ----> contains untrackedfiles $__fish_git_prompt_status_order
        13        140 ----> if test true = $inside_worktree...
        19         19 -----> test true = $inside_worktree
        12         88 -----> if test "$informative" = true...
         9          9 ------> test "$informative" = true
         6         17 ------> ...
        11         11 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        14         34 ------> if not test "$dirty" = true...
         7          7 -------> not test "$dirty" = true
         7          7 -------> test "$untracked" = true
         6          6 -------> test "$dirty" = true
         7         16 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         9          9 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         6         20 -----> if set -q __fish_git_prompt_showupstream...
         5          5 ------> set -q __fish_git_prompt_showupstream
         9          9 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        22         22 ----> set -l branch_color $___fish_git_prompt_color_branch
        21         21 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         8         17 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
         9          9 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         8          8 ----> set -l flags ""
        28         87 ----> for i in $__fish_git_prompt_status_order...
         5         17 -----> if test -n "$$i"...
        12         12 ------> test -n "$$i"
         4         11 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
         4         11 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
         5         11 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
       282        317 ----> set branch (string replace refs/heads/ '' -- $branch)
        35         35 -----> string replace refs/heads/ '' -- $branch
       156        223 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        67         67 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       138        174 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        36         36 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        13         49 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        36         36 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
        15         71 ----> if test -n "$branch"...
        13         13 -----> test -n "$branch"
        14         14 -----> set branch "$branch_color$branch$branch_done"
         7         29 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
        12         12 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        10         10 ------> test -n "$___fish_git_prompt_char_cleanstate"
         3         10 ----> if test -n "$bare_prefix"...
         7          7 -----> test -n "$bare_prefix"
         2          8 ----> if test -n "$operation"...
         6          6 -----> test -n "$operation"
         3          9 ----> if test -n "$upstream"...
         6          6 -----> test -n "$upstream"
         2         11 ----> if test -n "$flags$bare_prefix$upstream"...
         9          9 -----> test -n "$flags$bare_prefix$upstream"
        12         12 ----> set -l format $argv[1]
         5         19 ----> if test -z "$format"...
         6          6 -----> test -z "$format"
         8          8 -----> set format " (%s)"
        69         69 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        31       3228 > fish_title
        17         17 -> set -l ssh
         6          6 -> set -q SSH_TTY
        25       3174 -> if set -q argv[1]...
         5          5 --> set -q argv[1]
       138        153 --> set -l command (status current-command)
        15         15 ---> status current-command
         8         30 --> if test "$command" = fish...
        14         14 ---> test "$command" = fish
         8          8 ---> set command
       351       2961 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        16         16 ---> string sub -l 20 -- $command
        60       2594 ---> prompt_pwd -d 1 -D 1
        13         13 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        39         39 ----> argparse -n prompt_pwd $options -- $argv
         4         11 ----> if set -q _flag_help...
         7          7 -----> set -q _flag_help
         5          5 ----> set -q argv[1]
        11         11 ----> set argv $PWD
         4          4 ----> set -ql _flag_d
        17         17 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         5          5 ----> set -q fish_prompt_pwd_dir_length
         6          6 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         9          9 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         4          4 ----> set -q fish_prompt_pwd_full_dirs
        31       2407 ----> for path in $argv...
       383       1065 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       398        682 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       151        215 -------> set -l realhome (string escape --style=regex -- ~)
        64         64 --------> string escape --style=regex -- ~
        69         69 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        39       1311 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        98         98 ------> test "$fish_prompt_pwd_dir_length" -eq 0
        20         20 ------> set -l full
        30        780 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
        18         18 -------> test $fish_prompt_pwd_full_dirs -gt 0
       312        691 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       325        379 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        54         54 ---------> math $fish_prompt_pwd_full_dirs - 1
        26         26 -------> set tmp $all[1]
        15         15 -------> set full $all[2..]
       285        374 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        89         89 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        49        147 > fish_mode_prompt
        21         98 -> fish_default_mode_prompt
        24         77 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        46         46 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         7          7 ---> return
        93      60568 > fish_prompt
        41         41 -> set -l last_pipestatus $pipestatus
        18         18 -> set -lx __fish_last_status $status
       319        346 -> set -l normal (set_color --reset)
        27         27 --> set_color --reset
        25         25 -> set -l color_cwd $fish_color_cwd
        13         13 -> set -l suffix '>'
        11        293 -> if functions -q fish_is_root_user...
        20         20 --> functions -q fish_is_root_user
        35        262 --> fish_is_root_user
        14        170 ---> if test "$EUID" = 0 2>/dev/null...
       156        156 ----> test "$EUID" = 0 2>/dev/null
         7         34 ---> if contains -- $USER root toor Administrator...
        27         27 ----> contains -- $USER root toor Administrator
        23         23 ---> return 1
        16         16 -> set -l bold_flag --bold
         9          9 -> set -q __fish_prompt_status_generation
        61         91 -> if test $__fish_prompt_status_generation = $status_generation...
        19         19 --> test $__fish_prompt_status_generation = $status_generation
        11         11 --> set bold_flag
        28         28 -> set __fish_prompt_status_generation $status_generation
       390        428 -> set -l status_color (set_color $fish_color_status)
        38         38 --> set_color $fish_color_status
       187        220 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        33         33 --> set_color $bold_flag $fish_color_status
       183        436 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        65        253 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        12         12 ---> set -l last_status
        13         30 ---> if set -q __fish_last_status...
         6          6 ----> set -q __fish_last_status
        11         11 ----> set last_status $__fish_last_status
        23         23 ---> set -l left_brace $argv[1]
        11         11 ---> set -l right_brace $argv[2]
        51         51 ---> set -l separator $argv[3]
        11         11 ---> set -l brace_sep_color $argv[4]
         9          9 ---> set -l status_color $argv[5]
        10         10 ---> set -e argv[1 2 3 4 5]
         5         12 ---> if not set -q argv[1]...
         7          7 ----> not set -q argv[1]
         7         19 ---> if not contains $last_status 0 141...
        12         12 ----> not contains $last_status 0 141
       695      58511 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        27        867 --> prompt_login
        11         27 ---> if not set -q __fish_machine...
        16         16 ----> not set -q __fish_machine
         4         12 ---> if set -q __fish_machine[1]...
         8          8 ----> set -q __fish_machine[1]
        15         15 ---> set -l color_host $fish_color_host
         4          9 ---> if set -q SSH_TTY...
         5          5 ----> set -q SSH_TTY
       620        777 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        26         26 ----> set_color $fish_color_user
        16         16 ----> set_color --reset
        20         20 ----> set_color $color_host
        25         80 ----> prompt_hostname
        55         55 -----> string replace -r -- "\..*" "" $hostname
        15         15 ----> set_color --reset
        24         24 --> set_color $color_cwd
        54       1623 --> prompt_pwd
        18         18 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        29         29 ---> argparse -n prompt_pwd $options -- $argv
         5         13 ---> if set -q _flag_help...
         8          8 ----> set -q _flag_help
         5          5 ---> set -q argv[1]
        11         11 ---> set argv $PWD
         4          4 ---> set -ql _flag_d
         5          5 ---> set -q fish_prompt_pwd_dir_length
         6          6 ---> set -l fish_prompt_pwd_dir_length 1
         7          7 ---> set -l fulldirs 0
         4          4 ---> set -ql _flag_D
         5          5 ---> set -q fish_prompt_pwd_full_dirs
         7          7 ---> set -l fish_prompt_pwd_full_dirs 1
        28       1455 ---> for path in $argv...
       195        725 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       246        530 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       170        211 ------> set -l realhome (string escape --style=regex -- ~)
        41         41 -------> string escape --style=regex -- ~
        73         73 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        23        702 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        27         27 -----> test "$fish_prompt_pwd_dir_length" -eq 0
         9          9 -----> set -l full
        23        411 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        10         10 ------> test $fish_prompt_pwd_full_dirs -gt 0
       173        351 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       138        178 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        40         40 --------> math $fish_prompt_pwd_full_dirs - 1
        17         17 ------> set tmp $all[1]
        10         10 ------> set full $all[2..]
       161        232 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        71         71 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        40      55302 --> fish_vcs_prompt
        25        130 ---> fish_jj_prompt $argv
        14        105 ----> if not command -sq jj...
        81         81 -----> not command -sq jj
        10         10 -----> return 1
       176      55132 ---> fish_git_prompt $argv
        13        204 ----> if not command -sq git...
       191        191 -----> not command -sq git
         9         33 ----> if functions -q __fish_git_prompt_ready...
        24         24 -----> functions -q __fish_git_prompt_ready
       487      13782 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     13295      13295 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        43         43 ----> test -n "$repo_info"
        25         25 ----> set -l git_dir $repo_info[1]
        10         10 ----> set -l git_common_dir $repo_info[2]
        10         10 ----> set -l inside_gitdir $repo_info[3]
        11         11 ----> set -l bare_repo $repo_info[4]
        16         16 ----> set -l inside_worktree $repo_info[5]
         5          5 ----> set -q repo_info[6]
        10         10 ----> set -l sha $repo_info[6]
      1253      17108 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
        88      15855 -----> __fish_git_prompt_operation_branch_bare $repo_info
        19         19 ------> set -l git_dir $argv[1]
        12         12 ------> set -l inside_gitdir $argv[3]
         8          8 ------> set -l bare_repo $argv[4]
         6          6 ------> set -q argv[6]
         9          9 ------> set -l sha $argv[6]
         5          5 ------> set -l branch
        10         10 ------> set -l operation
         7          7 ------> set -l detached no
         5          5 ------> set -l bare
         5          5 ------> set -l step
         6          6 ------> set -l total
        13        140 ------> if test -d $git_dir/rebase-merge...
        42         42 -------> test -d $git_dir/rebase-merge
        24         85 -------> if test -d $git_dir/rebase-apply...
        15         15 --------> test -d $git_dir/rebase-apply
        13         13 --------> test -f $git_dir/MERGE_HEAD
        12         12 --------> test -f $git_dir/CHERRY_PICK_HEAD
        11         11 --------> test -f $git_dir/REVERT_HEAD
        10         10 --------> test -f $git_dir/BISECT_LOG
         4         23 ------> if test -n "$step" -a -n "$total"...
        19         19 -------> test -n "$step" -a -n "$total"
         9      15431 ------> if test -z "$branch"...
         6          6 -------> test -z "$branch"
        26      15416 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
      1127      15390 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     14263      14263 ---------> command git symbolic-ref HEAD 2>/dev/null
         8         39 ------> if test true = $inside_gitdir...
        31         31 -------> test true = $inside_gitdir
        26         26 ------> echo $operation
         7          7 ------> echo $branch
         4          4 ------> echo $detached
         5          5 ------> echo $bare
        33         33 ----> set -l operation $branch_state[1]
         9          9 ----> set -l branch $branch_state[2]
        18         18 ----> set -l detached $branch_state[3]
        16         16 ----> set -l dirtystate
        22         22 ----> set -l stagedstate
         5          5 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         4          4 ----> set -l untrackedfiles
         8          8 ----> set -l bare_prefix $branch_state[4]
         5          5 ----> set -l upstream
         5          5 ----> set -l informative_status
         8          8 ----> set -q __fish_git_prompt_status_order
        11         18 ----> if not set -q ___fish_git_prompt_init...
         7          7 -----> not set -q ___fish_git_prompt_init
        73         73 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         8          8 ----> set -l informative
         5          5 ----> set -l dirty
         5          5 ----> set -l untracked
      9541      22171 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     12630      12630 -----> read -lz key value
        21         97 ----> if not set -q dirty[1]...
        36         36 -----> not set -q dirty[1]
        40         40 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        24         24 ----> contains dirtystate $__fish_git_prompt_status_order
         6         22 ----> if not set -q untracked[1]...
         7          7 -----> not set -q untracked[1]
         9          9 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
         9          9 ----> contains untrackedfiles $__fish_git_prompt_status_order
        10        121 ----> if test true = $inside_worktree...
        12         12 -----> test true = $inside_worktree
        10         83 -----> if test "$informative" = true...
         7          7 ------> test "$informative" = true
         6         16 ------> ...
        10         10 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        14         34 ------> if not test "$dirty" = true...
         6          6 -------> not test "$dirty" = true
         9          9 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         7         16 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         9          9 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         3         16 -----> if set -q __fish_git_prompt_showupstream...
         6          6 ------> set -q __fish_git_prompt_showupstream
         7          7 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        17         17 ----> set -l branch_color $___fish_git_prompt_color_branch
        16         16 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         7         15 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
         8          8 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         8          8 ----> set -l flags ""
        24         72 ----> for i in $__fish_git_prompt_status_order...
         5         16 -----> if test -n "$$i"...
        11         11 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         4          8 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
         2          8 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          7 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
       247        281 ----> set branch (string replace refs/heads/ '' -- $branch)
        34         34 -----> string replace refs/heads/ '' -- $branch
       159        218 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        59         59 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       139        178 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        39         39 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        12         48 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        36         36 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         7         53 ----> if test -n "$branch"...
        11         11 -----> test -n "$branch"
        12         12 -----> set branch "$branch_color$branch$branch_done"
         6         23 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
         9          9 ------> test -n "$___fish_git_prompt_char_cleanstate"
         2          7 ----> if test -n "$bare_prefix"...
         5          5 -----> test -n "$bare_prefix"
         2          6 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         1          6 ----> if test -n "$upstream"...
         5          5 -----> test -n "$upstream"
         2          8 ----> if test -n "$flags$bare_prefix$upstream"...
         6          6 -----> test -n "$flags$bare_prefix$upstream"
         8          8 ----> set -l format $argv[1]
         4         14 ----> if test -z "$format"...
         4          4 -----> test -z "$format"
         6          6 -----> set format " (%s)"
        54         54 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        31       2013 > fish_title
        15         15 -> set -l ssh
         6          6 -> set -q SSH_TTY
        16       1961 -> if set -q argv[1]...
         5          5 --> set -q argv[1]
       138        149 --> set -l command (status current-command)
        11         11 ---> status current-command
         8         30 --> if test "$command" = fish...
        16         16 ---> test "$command" = fish
         6          6 ---> set command
       228       1761 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        16         16 ---> string sub -l 20 -- $command
        48       1517 ---> prompt_pwd -d 1 -D 1
        15         15 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        37         37 ----> argparse -n prompt_pwd $options -- $argv
         7         59 ----> if set -q _flag_help...
        52         52 -----> set -q _flag_help
         6          6 ----> set -q argv[1]
        12         12 ----> set argv $PWD
         4          4 ----> set -ql _flag_d
        21         21 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         4          4 ----> set -q fish_prompt_pwd_dir_length
         6          6 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
        12         12 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         4          4 ----> set -q fish_prompt_pwd_full_dirs
        22       1286 ----> for path in $argv...
       178        675 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       271        497 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       131        159 -------> set -l realhome (string escape --style=regex -- ~)
        28         28 --------> string escape --style=regex -- ~
        67         67 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        20        589 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        21         21 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         7          7 ------> set -l full
        16        347 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         9          9 -------> test $fish_prompt_pwd_full_dirs -gt 0
       131        301 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       133        170 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        37         37 ---------> math $fish_prompt_pwd_full_dirs - 1
        13         13 -------> set tmp $all[1]
         8          8 -------> set full $all[2..]
       125        194 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        69         69 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        52        150 > fish_mode_prompt
        23         98 -> fish_default_mode_prompt
        21         75 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        48         48 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         6          6 ---> return
       582      75660 > fish_prompt
       105        105 -> set -l last_pipestatus $pipestatus
        42         42 -> set -lx __fish_last_status $status
       364        420 -> set -l normal (set_color --reset)
        56         56 --> set_color --reset
        44         44 -> set -l color_cwd $fish_color_cwd
        31         31 -> set -l suffix '>'
        25        532 -> if functions -q fish_is_root_user...
        38         38 --> functions -q fish_is_root_user
        62        469 --> fish_is_root_user
        28        333 ---> if test "$EUID" = 0 2>/dev/null...
       305        305 ----> test "$EUID" = 0 2>/dev/null
        14         58 ---> if contains -- $USER root toor Administrator...
        44         44 ----> contains -- $USER root toor Administrator
        16         16 ---> return 1
        33         33 -> set -l bold_flag --bold
        19         19 -> set -q __fish_prompt_status_generation
        38        124 -> if test $__fish_prompt_status_generation = $status_generation...
        39         39 --> test $__fish_prompt_status_generation = $status_generation
        47         47 --> set bold_flag
        79         79 -> set __fish_prompt_status_generation $status_generation
       367        439 -> set -l status_color (set_color $fish_color_status)
        72         72 --> set_color $fish_color_status
       312        371 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        59         59 --> set_color $bold_flag $fish_color_status
       301        915 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
       213        614 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        32         32 ---> set -l last_status
        29         81 ---> if set -q __fish_last_status...
        18         18 ----> set -q __fish_last_status
        34         34 ----> set last_status $__fish_last_status
        40         40 ---> set -l left_brace $argv[1]
        32         32 ---> set -l right_brace $argv[2]
        31         31 ---> set -l separator $argv[3]
        32         32 ---> set -l brace_sep_color $argv[4]
        35         35 ---> set -l status_color $argv[5]
        30         30 ---> set -e argv[1 2 3 4 5]
        15         34 ---> if not set -q argv[1]...
        19         19 ----> not set -q argv[1]
        20         54 ---> if not contains $last_status 0 141...
        34         34 ----> not contains $last_status 0 141
       996      71924 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        66       1858 --> prompt_login
        19         38 ---> if not set -q __fish_machine...
        19         19 ----> not set -q __fish_machine
         9         27 ---> if set -q __fish_machine[1]...
        18         18 ----> set -q __fish_machine[1]
        34         34 ---> set -l color_host $fish_color_host
         9         24 ---> if set -q SSH_TTY...
        15         15 ----> set -q SSH_TTY
      1254       1669 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        53         53 ----> set_color $fish_color_user
        44         44 ----> set_color --reset
        51         51 ----> set_color $color_host
        75        217 ----> prompt_hostname
       142        142 -----> string replace -r -- "\..*" "" $hostname
        50         50 ----> set_color --reset
        48         48 --> set_color $color_cwd
       122       2945 --> prompt_pwd
        37         37 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        55         55 ---> argparse -n prompt_pwd $options -- $argv
        19         36 ---> if set -q _flag_help...
        17         17 ----> set -q _flag_help
        16         16 ---> set -q argv[1]
        29         29 ---> set argv $PWD
        13         13 ---> set -ql _flag_d
        15         15 ---> set -q fish_prompt_pwd_dir_length
        19         19 ---> set -l fish_prompt_pwd_dir_length 1
        17         17 ---> set -l fulldirs 0
        75         75 ---> set -ql _flag_D
        27         27 ---> set -q fish_prompt_pwd_full_dirs
        22         22 ---> set -l fish_prompt_pwd_full_dirs 1
        57       2462 ---> for path in $argv...
       259       1152 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       405        893 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       287        337 ------> set -l realhome (string escape --style=regex -- ~)
        50         50 -------> string escape --style=regex -- ~
       151        151 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        46       1253 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        45         45 -----> test "$fish_prompt_pwd_dir_length" -eq 0
        22         22 -----> set -l full
        48        778 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        28         28 ------> test $fish_prompt_pwd_full_dirs -gt 0
       282        641 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       282        359 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        77         77 --------> math $fish_prompt_pwd_full_dirs - 1
        36         36 ------> set tmp $all[1]
        25         25 ------> set full $all[2..]
       240        362 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
       122        122 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        68      66077 --> fish_vcs_prompt
        47        294 ---> fish_jj_prompt $argv
        33        247 ----> if not command -sq jj...
       196        196 -----> not command -sq jj
        18         18 -----> return 1
       264      65715 ---> fish_git_prompt $argv
        19        167 ----> if not command -sq git...
       148        148 -----> not command -sq git
        14         48 ----> if functions -q __fish_git_prompt_ready...
        34         34 -----> functions -q __fish_git_prompt_ready
       551      28088 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     27537      27537 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
       117        117 ----> test -n "$repo_info"
        64         64 ----> set -l git_dir $repo_info[1]
        38         38 ----> set -l git_common_dir $repo_info[2]
        28         28 ----> set -l inside_gitdir $repo_info[3]
        59         59 ----> set -l bare_repo $repo_info[4]
        39         39 ----> set -l inside_worktree $repo_info[5]
        16         16 ----> set -q repo_info[6]
        30         30 ----> set -l sha $repo_info[6]
       354      18204 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
       211      17850 -----> __fish_git_prompt_operation_branch_bare $repo_info
        36         36 ------> set -l git_dir $argv[1]
        34         34 ------> set -l inside_gitdir $argv[3]
        28         28 ------> set -l bare_repo $argv[4]
        14         14 ------> set -q argv[6]
        29         29 ------> set -l sha $argv[6]
        18         18 ------> set -l branch
        26         26 ------> set -l operation
        19         19 ------> set -l detached no
        18         18 ------> set -l bare
        23         23 ------> set -l step
        17         17 ------> set -l total
        29        314 ------> if test -d $git_dir/rebase-merge...
        58         58 -------> test -d $git_dir/rebase-merge
        59        227 -------> if test -d $git_dir/rebase-apply...
        36         36 --------> test -d $git_dir/rebase-apply
        34         34 --------> test -f $git_dir/MERGE_HEAD
        35         35 --------> test -f $git_dir/CHERRY_PICK_HEAD
        31         31 --------> test -f $git_dir/REVERT_HEAD
        32         32 --------> test -f $git_dir/BISECT_LOG
        12         50 ------> if test -n "$step" -a -n "$total"...
        38         38 -------> test -n "$step" -a -n "$total"
        12      16935 ------> if test -z "$branch"...
        20         20 -------> test -z "$branch"
        25      16903 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       597      16878 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     16281      16281 ---------> command git symbolic-ref HEAD 2>/dev/null
         6         38 ------> if test true = $inside_gitdir...
        32         32 -------> test true = $inside_gitdir
        24         24 ------> echo $operation
         7          7 ------> echo $branch
         5          5 ------> echo $detached
         4          4 ------> echo $bare
        20         20 ----> set -l operation $branch_state[1]
        11         11 ----> set -l branch $branch_state[2]
         8          8 ----> set -l detached $branch_state[3]
         5          5 ----> set -l dirtystate
         9          9 ----> set -l stagedstate
         3          3 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         5          5 ----> set -l untrackedfiles
         6          6 ----> set -l bare_prefix $branch_state[4]
         3          3 ----> set -l upstream
         6          6 ----> set -l informative_status
         6          6 ----> set -q __fish_git_prompt_status_order
         6         12 ----> if not set -q ___fish_git_prompt_init...
         6          6 -----> not set -q ___fish_git_prompt_init
        24         24 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         6          6 ----> set -l informative
         4          4 ----> set -l dirty
         4          4 ----> set -l untracked
      1579      15536 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     13957      13957 -----> read -lz key value
        26        123 ----> if not set -q dirty[1]...
        48         48 -----> not set -q dirty[1]
        49         49 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        38         38 ----> contains dirtystate $__fish_git_prompt_status_order
         8         29 ----> if not set -q untracked[1]...
         9          9 -----> not set -q untracked[1]
        12         12 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
         9          9 ----> contains untrackedfiles $__fish_git_prompt_status_order
         8        120 ----> if test true = $inside_worktree...
        13         13 -----> test true = $inside_worktree
        10         79 -----> if test "$informative" = true...
         7          7 ------> test "$informative" = true
         7         17 ------> ...
        10         10 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        10         29 ------> if not test "$dirty" = true...
         8          8 -------> not test "$dirty" = true
         7          7 -------> test "$untracked" = true
         4          4 -------> test "$dirty" = true
         7         16 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         9          9 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         6         20 -----> if set -q __fish_git_prompt_showupstream...
         5          5 ------> set -q __fish_git_prompt_showupstream
         9          9 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        21         21 ----> set -l branch_color $___fish_git_prompt_color_branch
        21         21 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         7         21 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        14         14 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         7          7 ----> set -l flags ""
        28         78 ----> for i in $__fish_git_prompt_status_order...
         4         18 -----> if test -n "$$i"...
        14         14 ------> test -n "$$i"
         4         10 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         2          6 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
      1095       1134 ----> set branch (string replace refs/heads/ '' -- $branch)
        39         39 -----> string replace refs/heads/ '' -- $branch
       526        608 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        82         82 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       309        376 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        67         67 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        19         86 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        67         67 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         9         68 ----> if test -n "$branch"...
        17         17 -----> test -n "$branch"
        16         16 -----> set branch "$branch_color$branch$branch_done"
         6         26 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        12         12 ------> test -n "$___fish_git_prompt_char_cleanstate"
         3          7 ----> if test -n "$bare_prefix"...
         4          4 -----> test -n "$bare_prefix"
         5          9 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         3          7 ----> if test -n "$upstream"...
         4          4 -----> test -n "$upstream"
         2         10 ----> if test -n "$flags$bare_prefix$upstream"...
         8          8 -----> test -n "$flags$bare_prefix$upstream"
        13         13 ----> set -l format $argv[1]
         4         15 ----> if test -z "$format"...
         5          5 -----> test -z "$format"
         6          6 -----> set format " (%s)"
        81         81 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        38       2979 > fish_title
        24         24 -> set -l ssh
         5          5 -> set -q SSH_TTY
        22       2912 -> if set -q argv[1]...
         5          5 --> set -q argv[1]
       217        237 --> set -l command (status current-command)
        20         20 ---> status current-command
        13         41 --> if test "$command" = fish...
        21         21 ---> test "$command" = fish
         7          7 ---> set command
       494       2607 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        32         32 ---> string sub -l 20 -- $command
        67       2081 ---> prompt_pwd -d 1 -D 1
        21         21 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        99         99 ----> argparse -n prompt_pwd $options -- $argv
        10         19 ----> if set -q _flag_help...
         9          9 -----> set -q _flag_help
         6          6 ----> set -q argv[1]
        19         19 ----> set argv $PWD
         4          4 ----> set -ql _flag_d
        16         16 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         4          4 ----> set -q fish_prompt_pwd_dir_length
         6          6 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         7          7 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        26       1807 ----> for path in $argv...
       247        921 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       342        674 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       216        264 -------> set -l realhome (string escape --style=regex -- ~)
        48         48 --------> string escape --style=regex -- ~
        68         68 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        22        860 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        27         27 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         7          7 ------> set -l full
        17        543 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 -------> test $fish_prompt_pwd_full_dirs -gt 0
       222        496 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       235        274 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        39         39 ---------> math $fish_prompt_pwd_full_dirs - 1
        15         15 -------> set tmp $all[1]
         7          7 -------> set full $all[2..]
       193        261 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        68         68 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        28         76 > fish_mode_prompt
        10         48 -> fish_default_mode_prompt
        13         38 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        22         22 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         3          3 ---> return
        71      67470 > fish_prompt
        25         25 -> set -l last_pipestatus $pipestatus
        10         10 -> set -lx __fish_last_status $status
       470        489 -> set -l normal (set_color --reset)
        19         19 --> set_color --reset
        27         27 -> set -l color_cwd $fish_color_cwd
         6          6 -> set -l suffix '>'
         7        170 -> if functions -q fish_is_root_user...
        17         17 --> functions -q fish_is_root_user
        25        146 --> fish_is_root_user
        14         88 ---> if test "$EUID" = 0 2>/dev/null...
        74         74 ----> test "$EUID" = 0 2>/dev/null
         4         28 ---> if contains -- $USER root toor Administrator...
        24         24 ----> contains -- $USER root toor Administrator
         5          5 ---> return 1
        11         11 -> set -l bold_flag --bold
         4          4 -> set -q __fish_prompt_status_generation
         7         23 -> if test $__fish_prompt_status_generation = $status_generation...
        10         10 --> test $__fish_prompt_status_generation = $status_generation
         6          6 --> set bold_flag
        19         19 -> set __fish_prompt_status_generation $status_generation
       239        273 -> set -l status_color (set_color $fish_color_status)
        34         34 --> set_color $fish_color_status
       199        232 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        33         33 --> set_color $bold_flag $fish_color_status
       180        347 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        61        167 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        13         13 ---> set -l last_status
        11         24 ---> if set -q __fish_last_status...
         5          5 ----> set -q __fish_last_status
         8          8 ----> set last_status $__fish_last_status
        15         15 ---> set -l left_brace $argv[1]
         7          7 ---> set -l right_brace $argv[2]
         5          5 ---> set -l separator $argv[3]
         6          6 ---> set -l brace_sep_color $argv[4]
         6          6 ---> set -l status_color $argv[5]
         7          7 ---> set -e argv[1 2 3 4 5]
         4          9 ---> if not set -q argv[1]...
         5          5 ----> not set -q argv[1]
         5         14 ---> if not contains $last_status 0 141...
         9          9 ----> not contains $last_status 0 141
       825      65763 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        28        932 --> prompt_login
         9         18 ---> if not set -q __fish_machine...
         9          9 ----> not set -q __fish_machine
         2          7 ---> if set -q __fish_machine[1]...
         5          5 ----> set -q __fish_machine[1]
        12         12 ---> set -l color_host $fish_color_host
         2          6 ---> if set -q SSH_TTY...
         4          4 ----> set -q SSH_TTY
       706        861 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        25         25 ----> set_color $fish_color_user
        26         26 ----> set_color --reset
        16         16 ----> set_color $color_host
        24         70 ----> prompt_hostname
        46         46 -----> string replace -r -- "\..*" "" $hostname
        18         18 ----> set_color --reset
        37         37 --> set_color $color_cwd
        51       1982 --> prompt_pwd
        19         19 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        24         24 ---> argparse -n prompt_pwd $options -- $argv
         7         13 ---> if set -q _flag_help...
         6          6 ----> set -q _flag_help
         5          5 ---> set -q argv[1]
         8          8 ---> set argv $PWD
         3          3 ---> set -ql _flag_d
        17         17 ---> set -q fish_prompt_pwd_dir_length
        12         12 ---> set -l fish_prompt_pwd_dir_length 1
         5          5 ---> set -l fulldirs 0
         2          2 ---> set -ql _flag_D
         3          3 ---> set -q fish_prompt_pwd_full_dirs
         5          5 ---> set -l fish_prompt_pwd_full_dirs 1
        24       1815 ---> for path in $argv...
       249        820 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       338        571 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       156        179 ------> set -l realhome (string escape --style=regex -- ~)
        23         23 -------> string escape --style=regex -- ~
        54         54 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        36        971 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        26         26 -----> test "$fish_prompt_pwd_dir_length" -eq 0
         8          8 -----> set -l full
        27        600 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        13         13 ------> test $fish_prompt_pwd_full_dirs -gt 0
       230        439 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       171        209 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        38         38 --------> math $fish_prompt_pwd_full_dirs - 1
        95         95 ------> set tmp $all[1]
        26         26 ------> set full $all[2..]
       231        301 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        70         70 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        44      61987 --> fish_vcs_prompt
        24        112 ---> fish_jj_prompt $argv
        15         88 ----> if not command -sq jj...
        66         66 -----> not command -sq jj
         7          7 -----> return 1
       172      61831 ---> fish_git_prompt $argv
        19        186 ----> if not command -sq git...
       167        167 -----> not command -sq git
         6         29 ----> if functions -q __fish_git_prompt_ready...
        23         23 -----> functions -q __fish_git_prompt_ready
       394      18236 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     17842      17842 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        36         36 ----> test -n "$repo_info"
        21         21 ----> set -l git_dir $repo_info[1]
         8          8 ----> set -l git_common_dir $repo_info[2]
         6          6 ----> set -l inside_gitdir $repo_info[3]
        10         10 ----> set -l bare_repo $repo_info[4]
        11         11 ----> set -l inside_worktree $repo_info[5]
         4          4 ----> set -q repo_info[6]
         7          7 ----> set -l sha $repo_info[6]
       309      24504 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
       103      24195 -----> __fish_git_prompt_operation_branch_bare $repo_info
        21         21 ------> set -l git_dir $argv[1]
         8          8 ------> set -l inside_gitdir $argv[3]
         6          6 ------> set -l bare_repo $argv[4]
         5          5 ------> set -q argv[6]
         7          7 ------> set -l sha $argv[6]
         4          4 ------> set -l branch
         7          7 ------> set -l operation
         6          6 ------> set -l detached no
         3          3 ------> set -l bare
         4          4 ------> set -l step
         4          4 ------> set -l total
        11         99 ------> if test -d $git_dir/rebase-merge...
        25         25 -------> test -d $git_dir/rebase-merge
        20         63 -------> if test -d $git_dir/rebase-apply...
        12         12 --------> test -d $git_dir/rebase-apply
         9          9 --------> test -f $git_dir/MERGE_HEAD
         8          8 --------> test -f $git_dir/CHERRY_PICK_HEAD
         7          7 --------> test -f $git_dir/REVERT_HEAD
         7          7 --------> test -f $git_dir/BISECT_LOG
         3         18 ------> if test -n "$step" -a -n "$total"...
        15         15 -------> test -n "$step" -a -n "$total"
         6      23824 ------> if test -z "$branch"...
         5          5 -------> test -z "$branch"
        24      23813 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       563      23789 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     23226      23226 ---------> command git symbolic-ref HEAD 2>/dev/null
         7         35 ------> if test true = $inside_gitdir...
        28         28 -------> test true = $inside_gitdir
        23         23 ------> echo $operation
         7          7 ------> echo $branch
         6          6 ------> echo $detached
         5          5 ------> echo $bare
        23         23 ----> set -l operation $branch_state[1]
         7          7 ----> set -l branch $branch_state[2]
         6          6 ----> set -l detached $branch_state[3]
         5          5 ----> set -l dirtystate
        11         11 ----> set -l stagedstate
         5          5 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         3          3 ----> set -l untrackedfiles
         6          6 ----> set -l bare_prefix $branch_state[4]
         3          3 ----> set -l upstream
         4          4 ----> set -l informative_status
         7          7 ----> set -q __fish_git_prompt_status_order
         6         11 ----> if not set -q ___fish_git_prompt_init...
         5          5 -----> not set -q ___fish_git_prompt_init
        29         29 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         4          4 ----> set -l informative
         4          4 ----> set -l dirty
         3          3 ----> set -l untracked
      1539      17001 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     15462      15462 -----> read -lz key value
        26         99 ----> if not set -q dirty[1]...
        34         34 -----> not set -q dirty[1]
        39         39 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        39         39 ----> contains dirtystate $__fish_git_prompt_status_order
         5         23 ----> if not set -q untracked[1]...
         8          8 -----> not set -q untracked[1]
        10         10 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
         9          9 ----> contains untrackedfiles $__fish_git_prompt_status_order
         9        107 ----> if test true = $inside_worktree...
        13         13 -----> test true = $inside_worktree
        11         70 -----> if test "$informative" = true...
         7          7 ------> test "$informative" = true
         6         14 ------> ...
         8          8 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
         9         25 ------> if not test "$dirty" = true...
         6          6 -------> not test "$dirty" = true
         5          5 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         6         13 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         7          7 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         4         15 -----> if set -q __fish_git_prompt_showupstream...
         4          4 ------> set -q __fish_git_prompt_showupstream
         7          7 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        16         16 ----> set -l branch_color $___fish_git_prompt_color_branch
        17         17 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         5         13 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
         8          8 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         7          7 ----> set -l flags ""
        22         65 ----> for i in $__fish_git_prompt_status_order...
         4         13 -----> if test -n "$$i"...
         9          9 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3          7 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         2          7 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
       251        285 ----> set branch (string replace refs/heads/ '' -- $branch)
        34         34 -----> string replace refs/heads/ '' -- $branch
       223        278 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        55         55 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       206        258 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        52         52 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        14         56 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        42         42 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         7         57 ----> if test -n "$branch"...
        13         13 -----> test -n "$branch"
        12         12 -----> set branch "$branch_color$branch$branch_done"
         7         25 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        10         10 ------> test -n "$___fish_git_prompt_char_cleanstate"
         2          7 ----> if test -n "$bare_prefix"...
         5          5 -----> test -n "$bare_prefix"
         2          6 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         5         10 ----> if test -n "$upstream"...
         5          5 -----> test -n "$upstream"
         2          8 ----> if test -n "$flags$bare_prefix$upstream"...
         6          6 -----> test -n "$flags$bare_prefix$upstream"
        10         10 ----> set -l format $argv[1]
         4         14 ----> if test -z "$format"...
         4          4 -----> test -z "$format"
         6          6 -----> set format " (%s)"
        81         81 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        36       9821 > fish_title
        24         24 -> set -l ssh
         5          5 -> set -q SSH_TTY
        24       9756 -> if set -q argv[1]...
         5          5 --> set -q argv[1]
       102        113 --> set -l command (status current-command)
        11         11 ---> status current-command
         8         29 --> if test "$command" = fish...
        15         15 ---> test "$command" = fish
         6          6 ---> set command
      3900       9585 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        15         15 ---> string sub -l 20 -- $command
        95       5670 ---> prompt_pwd -d 1 -D 1
        34         34 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        43         43 ----> argparse -n prompt_pwd $options -- $argv
         8         14 ----> if set -q _flag_help...
         6          6 -----> set -q _flag_help
         5          5 ----> set -q argv[1]
        11         11 ----> set argv $PWD
         4          4 ----> set -ql _flag_d
        23         23 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         6          6 ----> set -q fish_prompt_pwd_dir_length
         6          6 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         8          8 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         4          4 ----> set -q fish_prompt_pwd_full_dirs
        29       5414 ----> for path in $argv...
       313       4423 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
      2706       4110 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
      1265       1297 -------> set -l realhome (string escape --style=regex -- ~)
        32         32 --------> string escape --style=regex -- ~
       107        107 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        29        962 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        33         33 ------> test "$fish_prompt_pwd_dir_length" -eq 0
        10         10 ------> set -l full
        22        589 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         9          9 -------> test $fish_prompt_pwd_full_dirs -gt 0
       264        532 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       220        268 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        48         48 ---------> math $fish_prompt_pwd_full_dirs - 1
        20         20 -------> set tmp $all[1]
         6          6 -------> set full $all[2..]
       235        301 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        66         66 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        42        118 > fish_mode_prompt
        17         76 -> fish_default_mode_prompt
        18         59 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        36         36 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         5          5 ---> return
        83      73654 > fish_prompt
        38         38 -> set -l last_pipestatus $pipestatus
        12         12 -> set -lx __fish_last_status $status
       261        287 -> set -l normal (set_color --reset)
        26         26 --> set_color --reset
        21         21 -> set -l color_cwd $fish_color_cwd
         8          8 -> set -l suffix '>'
         9        225 -> if functions -q fish_is_root_user...
        14         14 --> functions -q fish_is_root_user
        40        202 --> fish_is_root_user
        11         94 ---> if test "$EUID" = 0 2>/dev/null...
        83         83 ----> test "$EUID" = 0 2>/dev/null
         3         21 ---> if contains -- $USER root toor Administrator...
        18         18 ----> contains -- $USER root toor Administrator
        47         47 ---> return 1
        12         12 -> set -l bold_flag --bold
         5          5 -> set -q __fish_prompt_status_generation
         5         25 -> if test $__fish_prompt_status_generation = $status_generation...
        14         14 --> test $__fish_prompt_status_generation = $status_generation
         6          6 --> set bold_flag
        11         11 -> set __fish_prompt_status_generation $status_generation
       257        285 -> set -l status_color (set_color $fish_color_status)
        28         28 --> set_color $fish_color_status
       205        234 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        29         29 --> set_color $bold_flag $fish_color_status
       200        382 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        82        182 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        10         10 ---> set -l last_status
        12         26 ---> if set -q __fish_last_status...
         5          5 ----> set -q __fish_last_status
         9          9 ----> set last_status $__fish_last_status
        10         10 ---> set -l left_brace $argv[1]
         6          6 ---> set -l right_brace $argv[2]
         6          6 ---> set -l separator $argv[3]
         6          6 ---> set -l brace_sep_color $argv[4]
         6          6 ---> set -l status_color $argv[5]
         7          7 ---> set -e argv[1 2 3 4 5]
         4          8 ---> if not set -q argv[1]...
         4          4 ----> not set -q argv[1]
         5         15 ---> if not contains $last_status 0 141...
        10         10 ----> not contains $last_status 0 141
      1645      72026 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        44       5627 --> prompt_login
        10         18 ---> if not set -q __fish_machine...
         8          8 ----> not set -q __fish_machine
         2          6 ---> if set -q __fish_machine[1]...
         4          4 ----> set -q __fish_machine[1]
        12         12 ---> set -l color_host $fish_color_host
         2          6 ---> if set -q SSH_TTY...
         4          4 ----> set -q SSH_TTY
      5226       5541 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        25         25 ----> set_color $fish_color_user
        35         35 ----> set_color --reset
        64         64 ----> set_color $color_host
        65        142 ----> prompt_hostname
        77         77 -----> string replace -r -- "\..*" "" $hostname
        49         49 ----> set_color --reset
        56         56 --> set_color $color_cwd
        94       9959 --> prompt_pwd
        29         29 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        31         31 ---> argparse -n prompt_pwd $options -- $argv
         8         14 ---> if set -q _flag_help...
         6          6 ----> set -q _flag_help
         5          5 ---> set -q argv[1]
         9          9 ---> set argv $PWD
         4          4 ---> set -ql _flag_d
         3          3 ---> set -q fish_prompt_pwd_dir_length
         6          6 ---> set -l fish_prompt_pwd_dir_length 1
         4          4 ---> set -l fulldirs 0
         2          2 ---> set -ql _flag_D
         3          3 ---> set -q fish_prompt_pwd_full_dirs
         5          5 ---> set -l fish_prompt_pwd_full_dirs 1
        40       9750 ---> for path in $argv...
       248       3395 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       416       3147 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
      2604       2659 ------> set -l realhome (string escape --style=regex -- ~)
        55         55 -------> string escape --style=regex -- ~
        72         72 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        68       6315 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        30         30 -----> test "$fish_prompt_pwd_dir_length" -eq 0
         8          8 -----> set -l full
        77       5204 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
         9          9 ------> test $fish_prompt_pwd_full_dirs -gt 0
      4731       4998 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       226        267 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        41         41 --------> math $fish_prompt_pwd_full_dirs - 1
        88         88 ------> set tmp $all[1]
        32         32 ------> set full $all[2..]
       786       1005 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
       219        219 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
       113      54739 --> fish_vcs_prompt
        89        302 ---> fish_jj_prompt $argv
        62        213 ----> if not command -sq jj...
       113        113 -----> not command -sq jj
        38         38 -----> return 1
       223      54324 ---> fish_git_prompt $argv
        42        237 ----> if not command -sq git...
       195        195 -----> not command -sq git
        28         92 ----> if functions -q __fish_git_prompt_ready...
        64         64 -----> functions -q __fish_git_prompt_ready
       544      16164 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     15620      15620 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        36         36 ----> test -n "$repo_info"
        23         23 ----> set -l git_dir $repo_info[1]
         8          8 ----> set -l git_common_dir $repo_info[2]
         6          6 ----> set -l inside_gitdir $repo_info[3]
         8          8 ----> set -l bare_repo $repo_info[4]
        10         10 ----> set -l inside_worktree $repo_info[5]
         4          4 ----> set -q repo_info[6]
         6          6 ----> set -l sha $repo_info[6]
      2110      20425 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
        98      18315 -----> __fish_git_prompt_operation_branch_bare $repo_info
        22         22 ------> set -l git_dir $argv[1]
         9          9 ------> set -l inside_gitdir $argv[3]
         6          6 ------> set -l bare_repo $argv[4]
         4          4 ------> set -q argv[6]
         7          7 ------> set -l sha $argv[6]
         4          4 ------> set -l branch
         9          9 ------> set -l operation
         4          4 ------> set -l detached no
         3          3 ------> set -l bare
         4          4 ------> set -l step
         3          3 ------> set -l total
        11        107 ------> if test -d $git_dir/rebase-merge...
        33         33 -------> test -d $git_dir/rebase-merge
        17         63 -------> if test -d $git_dir/rebase-apply...
        15         15 --------> test -d $git_dir/rebase-apply
         9          9 --------> test -f $git_dir/MERGE_HEAD
         8          8 --------> test -f $git_dir/CHERRY_PICK_HEAD
         7          7 --------> test -f $git_dir/REVERT_HEAD
         7          7 --------> test -f $git_dir/BISECT_LOG
         5         19 ------> if test -n "$step" -a -n "$total"...
        14         14 -------> test -n "$step" -a -n "$total"
         7      17924 ------> if test -z "$branch"...
         4          4 -------> test -z "$branch"
        27      17913 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       664      17886 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     17222      17222 ---------> command git symbolic-ref HEAD 2>/dev/null
         7         42 ------> if test true = $inside_gitdir...
        35         35 -------> test true = $inside_gitdir
        28         28 ------> echo $operation
         8          8 ------> echo $branch
         6          6 ------> echo $detached
         8          8 ------> echo $bare
        38         38 ----> set -l operation $branch_state[1]
        12         12 ----> set -l branch $branch_state[2]
        10         10 ----> set -l detached $branch_state[3]
         5          5 ----> set -l dirtystate
        73         73 ----> set -l stagedstate
        20         20 ----> set -l invalidstate
         3          3 ----> set -l stashstate
         6          6 ----> set -l untrackedfiles
        17         17 ----> set -l bare_prefix $branch_state[4]
         5          5 ----> set -l upstream
         6          6 ----> set -l informative_status
        12         12 ----> set -q __fish_git_prompt_status_order
         7         13 ----> if not set -q ___fish_git_prompt_init...
         6          6 -----> not set -q ___fish_git_prompt_init
        25         25 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         5          5 ----> set -l informative
         3          3 ----> set -l dirty
         4          4 ----> set -l untracked
      1519      15155 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     13636      13636 -----> read -lz key value
        20        100 ----> if not set -q dirty[1]...
        39         39 -----> not set -q dirty[1]
        41         41 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        34         34 ----> contains dirtystate $__fish_git_prompt_status_order
         7         25 ----> if not set -q untracked[1]...
         8          8 -----> not set -q untracked[1]
        10         10 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        10         10 ----> contains untrackedfiles $__fish_git_prompt_status_order
        10        113 ----> if test true = $inside_worktree...
        12         12 -----> test true = $inside_worktree
         9         73 -----> if test "$informative" = true...
         7          7 ------> test "$informative" = true
         4         13 ------> ...
         9          9 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        11         27 ------> if not test "$dirty" = true...
         6          6 -------> not test "$dirty" = true
         5          5 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         9         17 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         8          8 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         3         18 -----> if set -q __fish_git_prompt_showupstream...
         6          6 ------> set -q __fish_git_prompt_showupstream
         9          9 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        22         22 ----> set -l branch_color $___fish_git_prompt_color_branch
        19         19 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         6         18 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        12         12 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         9          9 ----> set -l flags ""
        30        121 ----> for i in $__fish_git_prompt_status_order...
        30         44 -----> if test -n "$$i"...
        14         14 ------> test -n "$$i"
         4         17 -----> if test -n "$$i"...
        13         13 ------> test -n "$$i"
         5         13 -----> if test -n "$$i"...
         8          8 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
       196        292 ----> set branch (string replace refs/heads/ '' -- $branch)
        96         96 -----> string replace refs/heads/ '' -- $branch
       298        377 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        79         79 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       218        272 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        54         54 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        14         66 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        52         52 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         8         63 ----> if test -n "$branch"...
        14         14 -----> test -n "$branch"
        15         15 -----> set branch "$branch_color$branch$branch_done"
         8         26 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        10         10 ------> test -n "$___fish_git_prompt_char_cleanstate"
         2          7 ----> if test -n "$bare_prefix"...
         5          5 -----> test -n "$bare_prefix"
         2          7 ----> if test -n "$operation"...
         5          5 -----> test -n "$operation"
         3          8 ----> if test -n "$upstream"...
         5          5 -----> test -n "$upstream"
         4         13 ----> if test -n "$flags$bare_prefix$upstream"...
         9          9 -----> test -n "$flags$bare_prefix$upstream"
        12         12 ----> set -l format $argv[1]
        11         24 ----> if test -z "$format"...
         5          5 -----> test -z "$format"
         8          8 -----> set format " (%s)"
        58         58 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        42       2934 > fish_title
        27         27 -> set -l ssh
         4          4 -> set -q SSH_TTY
        29       2861 -> if set -q argv[1]...
         4          4 --> set -q argv[1]
       187        198 --> set -l command (status current-command)
        11         11 ---> status current-command
        11         33 --> if test "$command" = fish...
        15         15 ---> test "$command" = fish
         7          7 ---> set command
       593       2597 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        18         18 ---> string sub -l 20 -- $command
        60       1986 ---> prompt_pwd -d 1 -D 1
        16         16 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        36         36 ----> argparse -n prompt_pwd $options -- $argv
         6         11 ----> if set -q _flag_help...
         5          5 -----> set -q _flag_help
         4          4 ----> set -q argv[1]
        22         22 ----> set argv $PWD
         5          5 ----> set -ql _flag_d
        16         16 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         5          5 ----> set -q fish_prompt_pwd_dir_length
         5          5 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         7          7 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         2          2 ----> set -q fish_prompt_pwd_full_dirs
        21       1794 ----> for path in $argv...
       200        862 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       369        662 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       197        223 -------> set -l realhome (string escape --style=regex -- ~)
        26         26 --------> string escape --style=regex -- ~
        70         70 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        27        911 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        24         24 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         8          8 ------> set -l full
        19        515 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 -------> test $fish_prompt_pwd_full_dirs -gt 0
       222        466 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       195        244 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        49         49 ---------> math $fish_prompt_pwd_full_dirs - 1
        15         15 -------> set tmp $all[1]
         7          7 -------> set full $all[2..]
       255        337 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        82         82 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        49        136 > fish_mode_prompt
        19         87 -> fish_default_mode_prompt
        22         68 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        40         40 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         6          6 ---> return
       101      66256 > fish_prompt
        41         41 -> set -l last_pipestatus $pipestatus
        13         13 -> set -lx __fish_last_status $status
       245        277 -> set -l normal (set_color --reset)
        32         32 --> set_color --reset
        19         19 -> set -l color_cwd $fish_color_cwd
         7          7 -> set -l suffix '>'
         8        169 -> if functions -q fish_is_root_user...
        14         14 --> functions -q fish_is_root_user
        28        147 --> fish_is_root_user
        10         92 ---> if test "$EUID" = 0 2>/dev/null...
        82         82 ----> test "$EUID" = 0 2>/dev/null
         3         23 ---> if contains -- $USER root toor Administrator...
        20         20 ----> contains -- $USER root toor Administrator
         4          4 ---> return 1
        10         10 -> set -l bold_flag --bold
         5          5 -> set -q __fish_prompt_status_generation
         5         21 -> if test $__fish_prompt_status_generation = $status_generation...
        10         10 --> test $__fish_prompt_status_generation = $status_generation
         6          6 --> set bold_flag
        18         18 -> set __fish_prompt_status_generation $status_generation
       222        250 -> set -l status_color (set_color $fish_color_status)
        28         28 --> set_color $fish_color_status
       214        239 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        25         25 --> set_color $bold_flag $fish_color_status
       179        346 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        66        167 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        10         10 ---> set -l last_status
        10         22 ---> if set -q __fish_last_status...
         5          5 ----> set -q __fish_last_status
         7          7 ----> set last_status $__fish_last_status
        10         10 ---> set -l left_brace $argv[1]
         7          7 ---> set -l right_brace $argv[2]
         7          7 ---> set -l separator $argv[3]
         7          7 ---> set -l brace_sep_color $argv[4]
         7          7 ---> set -l status_color $argv[5]
         8          8 ---> set -e argv[1 2 3 4 5]
         4          8 ---> if not set -q argv[1]...
         4          4 ----> not set -q argv[1]
         5         15 ---> if not contains $last_status 0 141...
        10         10 ----> not contains $last_status 0 141
       917      64740 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        25       1025 --> prompt_login
         8         16 ---> if not set -q __fish_machine...
         8          8 ----> not set -q __fish_machine
         2          7 ---> if set -q __fish_machine[1]...
         5          5 ----> set -q __fish_machine[1]
        13         13 ---> set -l color_host $fish_color_host
         3          6 ---> if set -q SSH_TTY...
         3          3 ----> set -q SSH_TTY
       791        958 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        30         30 ----> set_color $fish_color_user
        14         14 ----> set_color --reset
        27         27 ----> set_color $color_host
        27         79 ----> prompt_hostname
        52         52 -----> string replace -r -- "\..*" "" $hostname
        17         17 ----> set_color --reset
        27         27 --> set_color $color_cwd
        50       1753 --> prompt_pwd
        18         18 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        22         22 ---> argparse -n prompt_pwd $options -- $argv
         7         13 ---> if set -q _flag_help...
         6          6 ----> set -q _flag_help
        37         37 ---> set -q argv[1]
        11         11 ---> set argv $PWD
         4          4 ---> set -ql _flag_d
         4          4 ---> set -q fish_prompt_pwd_dir_length
         5          5 ---> set -l fish_prompt_pwd_dir_length 1
         4          4 ---> set -l fulldirs 0
         3          3 ---> set -ql _flag_D
         4          4 ---> set -q fish_prompt_pwd_full_dirs
         5          5 ---> set -l fish_prompt_pwd_full_dirs 1
        23       1573 ---> for path in $argv...
       184        773 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       317        589 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       176        212 ------> set -l realhome (string escape --style=regex -- ~)
        36         36 -------> string escape --style=regex -- ~
        60         60 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        23        777 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        23         23 -----> test "$fish_prompt_pwd_dir_length" -eq 0
         7          7 -----> set -l full
        18        483 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 ------> test $fish_prompt_pwd_full_dirs -gt 0
       195        436 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       201        241 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        40         40 --------> math $fish_prompt_pwd_full_dirs - 1
        14         14 ------> set tmp $all[1]
         7          7 ------> set full $all[2..]
       178        241 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        63         63 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        42      61018 --> fish_vcs_prompt
        22        108 ---> fish_jj_prompt $argv
        12         86 ----> if not command -sq jj...
        67         67 -----> not command -sq jj
         7          7 -----> return 1
       153      60868 ---> fish_git_prompt $argv
         7         69 ----> if not command -sq git...
        62         62 -----> not command -sq git
         4         19 ----> if functions -q __fish_git_prompt_ready...
        15         15 -----> functions -q __fish_git_prompt_ready
       394      16599 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     16205      16205 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        44         44 ----> test -n "$repo_info"
        28         28 ----> set -l git_dir $repo_info[1]
        10         10 ----> set -l git_common_dir $repo_info[2]
         6          6 ----> set -l inside_gitdir $repo_info[3]
         8          8 ----> set -l bare_repo $repo_info[4]
        12         12 ----> set -l inside_worktree $repo_info[5]
         5          5 ----> set -q repo_info[6]
         7          7 ----> set -l sha $repo_info[6]
       310      23279 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
       107      22969 -----> __fish_git_prompt_operation_branch_bare $repo_info
       123        123 ------> set -l git_dir $argv[1]
        30         30 ------> set -l inside_gitdir $argv[3]
         7          7 ------> set -l bare_repo $argv[4]
         4          4 ------> set -q argv[6]
         9          9 ------> set -l sha $argv[6]
         4          4 ------> set -l branch
         9          9 ------> set -l operation
         6          6 ------> set -l detached no
         5          5 ------> set -l bare
         4          4 ------> set -l step
         4          4 ------> set -l total
        16        125 ------> if test -d $git_dir/rebase-merge...
        40         40 -------> test -d $git_dir/rebase-merge
        19         69 -------> if test -d $git_dir/rebase-apply...
        16         16 --------> test -d $git_dir/rebase-apply
        10         10 --------> test -f $git_dir/MERGE_HEAD
         9          9 --------> test -f $git_dir/CHERRY_PICK_HEAD
         7          7 --------> test -f $git_dir/REVERT_HEAD
         8          8 --------> test -f $git_dir/BISECT_LOG
         5         26 ------> if test -n "$step" -a -n "$total"...
        21         21 -------> test -n "$step" -a -n "$total"
         7      22433 ------> if test -z "$branch"...
         8          8 -------> test -z "$branch"
        24      22418 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       407      22394 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     21987      21987 ---------> command git symbolic-ref HEAD 2>/dev/null
         6         31 ------> if test true = $inside_gitdir...
        25         25 -------> test true = $inside_gitdir
        24         24 ------> echo $operation
         8          8 ------> echo $branch
         5          5 ------> echo $detached
         5          5 ------> echo $bare
        19         19 ----> set -l operation $branch_state[1]
         7          7 ----> set -l branch $branch_state[2]
        10         10 ----> set -l detached $branch_state[3]
         5          5 ----> set -l dirtystate
         9          9 ----> set -l stagedstate
         4          4 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         4          4 ----> set -l untrackedfiles
         7          7 ----> set -l bare_prefix $branch_state[4]
         4          4 ----> set -l upstream
         6          6 ----> set -l informative_status
         6          6 ----> set -q __fish_git_prompt_status_order
         7         13 ----> if not set -q ___fish_git_prompt_init...
         6          6 -----> not set -q ___fish_git_prompt_init
        25         25 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         5          5 ----> set -l informative
         3          3 ----> set -l dirty
         4          4 ----> set -l untracked
      1432      18814 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     17382      17382 -----> read -lz key value
        24        119 ----> if not set -q dirty[1]...
        47         47 -----> not set -q dirty[1]
        48         48 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        29         29 ----> contains dirtystate $__fish_git_prompt_status_order
         6         23 ----> if not set -q untracked[1]...
         8          8 -----> not set -q untracked[1]
         9          9 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        10         10 ----> contains untrackedfiles $__fish_git_prompt_status_order
         9        116 ----> if test true = $inside_worktree...
        13         13 -----> test true = $inside_worktree
        10         76 -----> if test "$informative" = true...
         7          7 ------> test "$informative" = true
         4         13 ------> ...
         9          9 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        10         31 ------> if not test "$dirty" = true...
         7          7 -------> not test "$dirty" = true
         6          6 -------> test "$untracked" = true
         8          8 -------> test "$dirty" = true
         6         15 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         9          9 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         3         18 -----> if set -q __fish_git_prompt_showupstream...
         5          5 ------> set -q __fish_git_prompt_showupstream
        10         10 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        21         21 ----> set -l branch_color $___fish_git_prompt_color_branch
        20         20 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         5         14 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
         9          9 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         6          6 ----> set -l flags ""
        26         71 ----> for i in $__fish_git_prompt_status_order...
         4         13 -----> if test -n "$$i"...
         9          9 ------> test -n "$$i"
         4          9 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3          7 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          7 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
       426        463 ----> set branch (string replace refs/heads/ '' -- $branch)
        37         37 -----> string replace refs/heads/ '' -- $branch
       239        316 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        77         77 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       182        230 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        48         48 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        15         65 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        50         50 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         7         58 ----> if test -n "$branch"...
        13         13 -----> test -n "$branch"
        13         13 -----> set branch "$branch_color$branch$branch_done"
         7         25 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        10         10 ------> test -n "$___fish_git_prompt_char_cleanstate"
         2          8 ----> if test -n "$bare_prefix"...
         6          6 -----> test -n "$bare_prefix"
         3          7 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         4          8 ----> if test -n "$upstream"...
         4          4 -----> test -n "$upstream"
         2          8 ----> if test -n "$flags$bare_prefix$upstream"...
         6          6 -----> test -n "$flags$bare_prefix$upstream"
        10         10 ----> set -l format $argv[1]
         3         15 ----> if test -z "$format"...
         5          5 -----> test -z "$format"
         7          7 -----> set format " (%s)"
        63         63 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        44       2765 > fish_title
        24         24 -> set -l ssh
         5          5 -> set -q SSH_TTY
        26       2692 -> if set -q argv[1]...
         5          5 --> set -q argv[1]
       377        397 --> set -l command (status current-command)
        20         20 ---> status current-command
        18         67 --> if test "$command" = fish...
        35         35 ---> test "$command" = fish
        14         14 ---> set command
       394       2197 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        21         21 ---> string sub -l 20 -- $command
        83       1782 ---> prompt_pwd -d 1 -D 1
        20         20 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        35         35 ----> argparse -n prompt_pwd $options -- $argv
         8         13 ----> if set -q _flag_help...
         5          5 -----> set -q _flag_help
         5          5 ----> set -q argv[1]
         8          8 ----> set argv $PWD
         3          3 ----> set -ql _flag_d
        16         16 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         4          4 ----> set -q fish_prompt_pwd_dir_length
         6          6 ----> set -l fulldirs 0
         2          2 ----> set -ql _flag_D
         6          6 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        22       1578 ----> for path in $argv...
       194        855 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       341        661 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       197        246 -------> set -l realhome (string escape --style=regex -- ~)
        49         49 --------> string escape --style=regex -- ~
        74         74 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        20        701 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        21         21 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         7          7 ------> set -l full
        15        425 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 -------> test $fish_prompt_pwd_full_dirs -gt 0
       188        381 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       151        193 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        42         42 ---------> math $fish_prompt_pwd_full_dirs - 1
        13         13 -------> set tmp $all[1]
         8          8 -------> set full $all[2..]
       175        228 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        53         53 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        39        171 > fish_mode_prompt
        16        132 -> fish_default_mode_prompt
        19        116 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        89         89 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         8          8 ---> return
        72      52395 > fish_prompt
        36         36 -> set -l last_pipestatus $pipestatus
        11         11 -> set -lx __fish_last_status $status
       193        211 -> set -l normal (set_color --reset)
        18         18 --> set_color --reset
        16         16 -> set -l color_cwd $fish_color_cwd
         7          7 -> set -l suffix '>'
         7        165 -> if functions -q fish_is_root_user...
        12         12 --> functions -q fish_is_root_user
        31        146 --> fish_is_root_user
         8         92 ---> if test "$EUID" = 0 2>/dev/null...
        84         84 ----> test "$EUID" = 0 2>/dev/null
         4         19 ---> if contains -- $USER root toor Administrator...
        15         15 ----> contains -- $USER root toor Administrator
         4          4 ---> return 1
        10         10 -> set -l bold_flag --bold
         4          4 -> set -q __fish_prompt_status_generation
         6         37 -> if test $__fish_prompt_status_generation = $status_generation...
        23         23 --> test $__fish_prompt_status_generation = $status_generation
         8          8 --> set bold_flag
        10         10 -> set __fish_prompt_status_generation $status_generation
       203        228 -> set -l status_color (set_color $fish_color_status)
        25         25 --> set_color $fish_color_status
       206        233 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        27         27 --> set_color $bold_flag $fish_color_status
       163        326 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        68        163 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        10         10 ---> set -l last_status
        11         23 ---> if set -q __fish_last_status...
         5          5 ----> set -q __fish_last_status
         7          7 ----> set last_status $__fish_last_status
        10         10 ---> set -l left_brace $argv[1]
         6          6 ---> set -l right_brace $argv[2]
         5          5 ---> set -l separator $argv[3]
         6          6 ---> set -l brace_sep_color $argv[4]
         7          7 ---> set -l status_color $argv[5]
         6          6 ---> set -e argv[1 2 3 4 5]
         3          7 ---> if not set -q argv[1]...
         4          4 ----> not set -q argv[1]
         5         15 ---> if not contains $last_status 0 141...
        10         10 ----> not contains $last_status 0 141
       692      51029 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        26        937 --> prompt_login
         8         15 ---> if not set -q __fish_machine...
         7          7 ----> not set -q __fish_machine
         2          8 ---> if set -q __fish_machine[1]...
         6          6 ----> set -q __fish_machine[1]
        11         11 ---> set -l color_host $fish_color_host
         3          6 ---> if set -q SSH_TTY...
         3          3 ----> set -q SSH_TTY
       724        871 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        22         22 ----> set_color $fish_color_user
        12         12 ----> set_color --reset
        20         20 ----> set_color $color_host
        23         75 ----> prompt_hostname
        52         52 -----> string replace -r -- "\..*" "" $hostname
        18         18 ----> set_color --reset
        29         29 --> set_color $color_cwd
        74       1942 --> prompt_pwd
        20         20 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        33         33 ---> argparse -n prompt_pwd $options -- $argv
         8         13 ---> if set -q _flag_help...
         5          5 ----> set -q _flag_help
         4          4 ---> set -q argv[1]
         9          9 ---> set argv $PWD
         3          3 ---> set -ql _flag_d
         3          3 ---> set -q fish_prompt_pwd_dir_length
         5          5 ---> set -l fish_prompt_pwd_dir_length 1
         4          4 ---> set -l fulldirs 0
         2          2 ---> set -ql _flag_D
         3          3 ---> set -q fish_prompt_pwd_full_dirs
        12         12 ---> set -l fish_prompt_pwd_full_dirs 1
        23       1757 ---> for path in $argv...
       203        800 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       344        597 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       160        188 ------> set -l realhome (string escape --style=regex -- ~)
        28         28 -------> string escape --style=regex -- ~
        65         65 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        25        934 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        25         25 -----> test "$fish_prompt_pwd_dir_length" -eq 0
        56         56 -----> set -l full
        55        589 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        18         18 ------> test $fish_prompt_pwd_full_dirs -gt 0
       191        491 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       252        300 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        48         48 --------> math $fish_prompt_pwd_full_dirs - 1
        17         17 ------> set tmp $all[1]
         8          8 ------> set full $all[2..]
       178        239 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        61         61 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        42      47429 --> fish_vcs_prompt
        22        158 ---> fish_jj_prompt $argv
        62        136 ----> if not command -sq jj...
        65         65 -----> not command -sq jj
         9          9 -----> return 1
       134      47229 ---> fish_git_prompt $argv
        16         89 ----> if not command -sq git...
        73         73 -----> not command -sq git
         5         21 ----> if functions -q __fish_git_prompt_ready...
        16         16 -----> functions -q __fish_git_prompt_ready
       367      15107 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     14740      14740 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        33         33 ----> test -n "$repo_info"
        18         18 ----> set -l git_dir $repo_info[1]
         8          8 ----> set -l git_common_dir $repo_info[2]
         6          6 ----> set -l inside_gitdir $repo_info[3]
         7          7 ----> set -l bare_repo $repo_info[4]
        10         10 ----> set -l inside_worktree $repo_info[5]
         3          3 ----> set -q repo_info[6]
         8          8 ----> set -l sha $repo_info[6]
       294      16200 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
        74      15906 -----> __fish_git_prompt_operation_branch_bare $repo_info
        15         15 ------> set -l git_dir $argv[1]
         8          8 ------> set -l inside_gitdir $argv[3]
         6          6 ------> set -l bare_repo $argv[4]
         3          3 ------> set -q argv[6]
         7          7 ------> set -l sha $argv[6]
         4          4 ------> set -l branch
         7          7 ------> set -l operation
         4          4 ------> set -l detached no
         4          4 ------> set -l bare
         4          4 ------> set -l step
         4          4 ------> set -l total
        14        107 ------> if test -d $git_dir/rebase-merge...
        27         27 -------> test -d $git_dir/rebase-merge
        18         66 -------> if test -d $git_dir/rebase-apply...
        12         12 --------> test -d $git_dir/rebase-apply
        13         13 --------> test -f $git_dir/MERGE_HEAD
         8          8 --------> test -f $git_dir/CHERRY_PICK_HEAD
         8          8 --------> test -f $git_dir/REVERT_HEAD
         7          7 --------> test -f $git_dir/BISECT_LOG
         4         17 ------> if test -n "$step" -a -n "$total"...
        13         13 -------> test -n "$step" -a -n "$total"
         8      15557 ------> if test -z "$branch"...
         5          5 -------> test -z "$branch"
        26      15544 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       367      15518 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     15151      15151 ---------> command git symbolic-ref HEAD 2>/dev/null
         6         34 ------> if test true = $inside_gitdir...
        28         28 -------> test true = $inside_gitdir
        26         26 ------> echo $operation
        11         11 ------> echo $branch
         8          8 ------> echo $detached
         6          6 ------> echo $bare
        20         20 ----> set -l operation $branch_state[1]
        10         10 ----> set -l branch $branch_state[2]
        10         10 ----> set -l detached $branch_state[3]
         5          5 ----> set -l dirtystate
        10         10 ----> set -l stagedstate
         4          4 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         5          5 ----> set -l untrackedfiles
         6          6 ----> set -l bare_prefix $branch_state[4]
         4          4 ----> set -l upstream
         5          5 ----> set -l informative_status
         6          6 ----> set -q __fish_git_prompt_status_order
         7         12 ----> if not set -q ___fish_git_prompt_init...
         5          5 -----> not set -q ___fish_git_prompt_init
        27         27 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         4          4 ----> set -l informative
         5          5 ----> set -l dirty
         4          4 ----> set -l untracked
      1492      14022 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     12530      12530 -----> read -lz key value
        19         99 ----> if not set -q dirty[1]...
        43         43 -----> not set -q dirty[1]
        37         37 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        31         31 ----> contains dirtystate $__fish_git_prompt_status_order
         6         22 ----> if not set -q untracked[1]...
         7          7 -----> not set -q untracked[1]
         9          9 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
         8          8 ----> contains untrackedfiles $__fish_git_prompt_status_order
         8        113 ----> if test true = $inside_worktree...
        12         12 -----> test true = $inside_worktree
        13         78 -----> if test "$informative" = true...
         7          7 ------> test "$informative" = true
         5         15 ------> ...
        10         10 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        10         26 ------> if not test "$dirty" = true...
         6          6 -------> not test "$dirty" = true
         5          5 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         8         17 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         9          9 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         3         15 -----> if set -q __fish_git_prompt_showupstream...
         5          5 ------> set -q __fish_git_prompt_showupstream
         7          7 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        17         17 ----> set -l branch_color $___fish_git_prompt_color_branch
        17         17 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         5         13 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
         8          8 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         6          6 ----> set -l flags ""
        22         69 ----> for i in $__fish_git_prompt_status_order...
         4         16 -----> if test -n "$$i"...
        12         12 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3          7 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
         3          7 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
       254        276 ----> set branch (string replace refs/heads/ '' -- $branch)
        22         22 -----> string replace refs/heads/ '' -- $branch
       204        262 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        58         58 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       216        259 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        43         43 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        17         59 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        42         42 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         9         57 ----> if test -n "$branch"...
        12         12 -----> test -n "$branch"
        11         11 -----> set branch "$branch_color$branch$branch_done"
         7         25 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        10         10 ------> test -n "$___fish_git_prompt_char_cleanstate"
         3          7 ----> if test -n "$bare_prefix"...
         4          4 -----> test -n "$bare_prefix"
         3          6 ----> if test -n "$operation"...
         3          3 -----> test -n "$operation"
         1          5 ----> if test -n "$upstream"...
         4          4 -----> test -n "$upstream"
         3         18 ----> if test -n "$flags$bare_prefix$upstream"...
        15         15 -----> test -n "$flags$bare_prefix$upstream"
        10         10 ----> set -l format $argv[1]
         5         15 ----> if test -z "$format"...
         4          4 -----> test -z "$format"
         6          6 -----> set format " (%s)"
        53         53 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        27       2346 > fish_title
        15         15 -> set -l ssh
         4          4 -> set -q SSH_TTY
        16       2300 -> if set -q argv[1]...
         5          5 --> set -q argv[1]
       160        170 --> set -l command (status current-command)
        10         10 ---> status current-command
        10         31 --> if test "$command" = fish...
        15         15 ---> test "$command" = fish
         6          6 ---> set command
       303       2078 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        13         13 ---> string sub -l 20 -- $command
        44       1762 ---> prompt_pwd -d 1 -D 1
        14         14 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        33         33 ----> argparse -n prompt_pwd $options -- $argv
         5          9 ----> if set -q _flag_help...
         4          4 -----> set -q _flag_help
         3          3 ----> set -q argv[1]
         9          9 ----> set argv $PWD
         3          3 ----> set -ql _flag_d
        16         16 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         4          4 ----> set -q fish_prompt_pwd_dir_length
         4          4 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         6          6 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        43       1611 ----> for path in $argv...
       188        813 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       342        625 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       192        219 -------> set -l realhome (string escape --style=regex -- ~)
        27         27 --------> string escape --style=regex -- ~
        64         64 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        24        755 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        22         22 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         7          7 ------> set -l full
        17        457 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 -------> test $fish_prompt_pwd_full_dirs -gt 0
       185        405 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       184        220 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        36         36 ---------> math $fish_prompt_pwd_full_dirs - 1
        19         19 -------> set tmp $all[1]
         8          8 -------> set full $all[2..]
       182        245 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        63         63 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        38        101 > fish_mode_prompt
        12         63 -> fish_default_mode_prompt
        14         51 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        32         32 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         5          5 ---> return
        73      60689 > fish_prompt
        32         32 -> set -l last_pipestatus $pipestatus
        14         14 -> set -lx __fish_last_status $status
       180        202 -> set -l normal (set_color --reset)
        22         22 --> set_color --reset
        16         16 -> set -l color_cwd $fish_color_cwd
        50         50 -> set -l suffix '>'
         6        168 -> if functions -q fish_is_root_user...
        14         14 --> functions -q fish_is_root_user
        21        148 --> fish_is_root_user
        11        101 ---> if test "$EUID" = 0 2>/dev/null...
        90         90 ----> test "$EUID" = 0 2>/dev/null
         4         22 ---> if contains -- $USER root toor Administrator...
        18         18 ----> contains -- $USER root toor Administrator
         4          4 ---> return 1
        10         10 -> set -l bold_flag --bold
         4          4 -> set -q __fish_prompt_status_generation
         5         22 -> if test $__fish_prompt_status_generation = $status_generation...
        12         12 --> test $__fish_prompt_status_generation = $status_generation
         5          5 --> set bold_flag
        14         14 -> set __fish_prompt_status_generation $status_generation
       255        281 -> set -l status_color (set_color $fish_color_status)
        26         26 --> set_color $fish_color_status
       206        273 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        67         67 --> set_color $bold_flag $fish_color_status
       201        345 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        48        144 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        12         12 ---> set -l last_status
         9         22 ---> if set -q __fish_last_status...
         5          5 ----> set -q __fish_last_status
         8          8 ----> set last_status $__fish_last_status
        10         10 ---> set -l left_brace $argv[1]
         6          6 ---> set -l right_brace $argv[2]
         6          6 ---> set -l separator $argv[3]
         6          6 ---> set -l brace_sep_color $argv[4]
         6          6 ---> set -l status_color $argv[5]
         6          6 ---> set -e argv[1 2 3 4 5]
         4          8 ---> if not set -q argv[1]...
         4          4 ----> not set -q argv[1]
         4         14 ---> if not contains $last_status 0 141...
        10         10 ----> not contains $last_status 0 141
       791      59185 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        29       1137 --> prompt_login
        10         20 ---> if not set -q __fish_machine...
        10         10 ----> not set -q __fish_machine
         2          7 ---> if set -q __fish_machine[1]...
         5          5 ----> set -q __fish_machine[1]
        14         14 ---> set -l color_host $fish_color_host
         3          6 ---> if set -q SSH_TTY...
         3          3 ----> set -q SSH_TTY
       887       1061 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        24         24 ----> set_color $fish_color_user
        20         20 ----> set_color --reset
        30         30 ----> set_color $color_host
        27         80 ----> prompt_hostname
        53         53 -----> string replace -r -- "\..*" "" $hostname
        20         20 ----> set_color --reset
        29         29 --> set_color $color_cwd
        45       2156 --> prompt_pwd
        19         19 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        23         23 ---> argparse -n prompt_pwd $options -- $argv
         7         12 ---> if set -q _flag_help...
         5          5 ----> set -q _flag_help
         4          4 ---> set -q argv[1]
         8          8 ---> set argv $PWD
         3          3 ---> set -ql _flag_d
         3          3 ---> set -q fish_prompt_pwd_dir_length
         5          5 ---> set -l fish_prompt_pwd_dir_length 1
         4          4 ---> set -l fulldirs 0
         3          3 ---> set -ql _flag_D
        10         10 ---> set -q fish_prompt_pwd_full_dirs
         6          6 ---> set -l fish_prompt_pwd_full_dirs 1
        23       2011 ---> for path in $argv...
       230        861 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       392        631 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       161        183 ------> set -l realhome (string escape --style=regex -- ~)
        22         22 -------> string escape --style=regex -- ~
        56         56 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        29       1127 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        25         25 -----> test "$fish_prompt_pwd_dir_length" -eq 0
         9          9 -----> set -l full
        18        778 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
         7          7 ------> test $fish_prompt_pwd_full_dirs -gt 0
       303        724 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       370        421 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        51         51 --------> math $fish_prompt_pwd_full_dirs - 1
        21         21 ------> set tmp $all[1]
         8          8 ------> set full $all[2..]
       217        286 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        69         69 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        44      55072 --> fish_vcs_prompt
        27        127 ---> fish_jj_prompt $argv
        17        100 ----> if not command -sq jj...
        75         75 -----> not command -sq jj
         8          8 -----> return 1
       152      54901 ---> fish_git_prompt $argv
        12         92 ----> if not command -sq git...
        80         80 -----> not command -sq git
         6         38 ----> if functions -q __fish_git_prompt_ready...
        32         32 -----> functions -q __fish_git_prompt_ready
       390      14531 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     14141      14141 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        39         39 ----> test -n "$repo_info"
        18         18 ----> set -l git_dir $repo_info[1]
         9          9 ----> set -l git_common_dir $repo_info[2]
         6          6 ----> set -l inside_gitdir $repo_info[3]
         8          8 ----> set -l bare_repo $repo_info[4]
        11         11 ----> set -l inside_worktree $repo_info[5]
         4          4 ----> set -q repo_info[6]
         8          8 ----> set -l sha $repo_info[6]
       554      24434 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
        68      23880 -----> __fish_git_prompt_operation_branch_bare $repo_info
        16         16 ------> set -l git_dir $argv[1]
         7          7 ------> set -l inside_gitdir $argv[3]
         8          8 ------> set -l bare_repo $argv[4]
         4          4 ------> set -q argv[6]
         6          6 ------> set -l sha $argv[6]
         4          4 ------> set -l branch
         7          7 ------> set -l operation
         4          4 ------> set -l detached no
         4          4 ------> set -l bare
         4          4 ------> set -l step
         4          4 ------> set -l total
        15         99 ------> if test -d $git_dir/rebase-merge...
        26         26 -------> test -d $git_dir/rebase-merge
        18         58 -------> if test -d $git_dir/rebase-apply...
        10         10 --------> test -d $git_dir/rebase-apply
         9          9 --------> test -f $git_dir/MERGE_HEAD
         7          7 --------> test -f $git_dir/CHERRY_PICK_HEAD
         7          7 --------> test -f $git_dir/REVERT_HEAD
         7          7 --------> test -f $git_dir/BISECT_LOG
         4         18 ------> if test -n "$step" -a -n "$total"...
        14         14 -------> test -n "$step" -a -n "$total"
         6      23560 ------> if test -z "$branch"...
         6          6 -------> test -z "$branch"
        24      23548 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
      1445      23524 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     22079      22079 ---------> command git symbolic-ref HEAD 2>/dev/null
         5         29 ------> if test true = $inside_gitdir...
        24         24 -------> test true = $inside_gitdir
        21         21 ------> echo $operation
         7          7 ------> echo $branch
         5          5 ------> echo $detached
         5          5 ------> echo $bare
        26         26 ----> set -l operation $branch_state[1]
         8          8 ----> set -l branch $branch_state[2]
         6          6 ----> set -l detached $branch_state[3]
         5          5 ----> set -l dirtystate
        11         11 ----> set -l stagedstate
         4          4 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         4          4 ----> set -l untrackedfiles
         6          6 ----> set -l bare_prefix $branch_state[4]
         4          4 ----> set -l upstream
         5          5 ----> set -l informative_status
         7          7 ----> set -q __fish_git_prompt_status_order
         8         14 ----> if not set -q ___fish_git_prompt_init...
         6          6 -----> not set -q ___fish_git_prompt_init
        28         28 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         5          5 ----> set -l informative
         4          4 ----> set -l dirty
         3          3 ----> set -l untracked
      1361      13702 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     12341      12341 -----> read -lz key value
        22        107 ----> if not set -q dirty[1]...
        41         41 -----> not set -q dirty[1]
        44         44 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        32         32 ----> contains dirtystate $__fish_git_prompt_status_order
         6         23 ----> if not set -q untracked[1]...
         8          8 -----> not set -q untracked[1]
         9          9 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
         9          9 ----> contains untrackedfiles $__fish_git_prompt_status_order
        10        110 ----> if test true = $inside_worktree...
        13         13 -----> test true = $inside_worktree
        11         71 -----> if test "$informative" = true...
         6          6 ------> test "$informative" = true
         6         14 ------> ...
         8          8 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        11         26 ------> if not test "$dirty" = true...
         6          6 -------> not test "$dirty" = true
         5          5 -------> test "$untracked" = true
         4          4 -------> test "$dirty" = true
         7         14 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         7          7 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         3         16 -----> if set -q __fish_git_prompt_showupstream...
         5          5 ------> set -q __fish_git_prompt_showupstream
         8          8 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        19         19 ----> set -l branch_color $___fish_git_prompt_color_branch
        20         20 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         6         18 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        12         12 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         6          6 ----> set -l flags ""
        22         69 ----> for i in $__fish_git_prompt_status_order...
         6         14 -----> if test -n "$$i"...
         8          8 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         4          8 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
         4          9 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3          7 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
       365        398 ----> set branch (string replace refs/heads/ '' -- $branch)
        33         33 -----> string replace refs/heads/ '' -- $branch
       287        352 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        65         65 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       214        272 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        58         58 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        13         59 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        46         46 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         9         97 ----> if test -n "$branch"...
        14         14 -----> test -n "$branch"
        13         13 -----> set branch "$branch_color$branch$branch_done"
         9         61 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
        42         42 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        10         10 ------> test -n "$___fish_git_prompt_char_cleanstate"
         2          7 ----> if test -n "$bare_prefix"...
         5          5 -----> test -n "$bare_prefix"
         1          5 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         2          6 ----> if test -n "$upstream"...
         4          4 -----> test -n "$upstream"
         1          8 ----> if test -n "$flags$bare_prefix$upstream"...
         7          7 -----> test -n "$flags$bare_prefix$upstream"
        11         11 ----> set -l format $argv[1]
         5         14 ----> if test -z "$format"...
         4          4 -----> test -z "$format"
         5          5 -----> set format " (%s)"
        63         63 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        27       2427 > fish_title
        15         15 -> set -l ssh
         4          4 -> set -q SSH_TTY
        19       2381 -> if set -q argv[1]...
         4          4 --> set -q argv[1]
       226        235 --> set -l command (status current-command)
         9          9 ---> status current-command
         7         28 --> if test "$command" = fish...
        15         15 ---> test "$command" = fish
         6          6 ---> set command
       323       2095 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        14         14 ---> string sub -l 20 -- $command
        56       1758 ---> prompt_pwd -d 1 -D 1
        15         15 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        30         30 ----> argparse -n prompt_pwd $options -- $argv
         5         10 ----> if set -q _flag_help...
         5          5 -----> set -q _flag_help
         3          3 ----> set -q argv[1]
         7          7 ----> set argv $PWD
         3          3 ----> set -ql _flag_d
        13         13 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         3          3 ----> set -q fish_prompt_pwd_dir_length
         4          4 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         9          9 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        20       1599 ----> for path in $argv...
       188        852 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       334        664 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       242        272 -------> set -l realhome (string escape --style=regex -- ~)
        30         30 --------> string escape --style=regex -- ~
        58         58 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        22        727 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        20         20 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         6          6 ------> set -l full
        15        432 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 -------> test $fish_prompt_pwd_full_dirs -gt 0
       194        389 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       164        195 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        31         31 ---------> math $fish_prompt_pwd_full_dirs - 1
        13         13 -------> set tmp $all[1]
         7          7 -------> set full $all[2..]
       186        247 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        61         61 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        32         91 > fish_mode_prompt
        12         59 -> fish_default_mode_prompt
        14         47 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        29         29 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         4          4 ---> return
        98      72574 > fish_prompt
        40         40 -> set -l last_pipestatus $pipestatus
        13         13 -> set -lx __fish_last_status $status
       289        322 -> set -l normal (set_color --reset)
        33         33 --> set_color --reset
        22         22 -> set -l color_cwd $fish_color_cwd
         9          9 -> set -l suffix '>'
         7        168 -> if functions -q fish_is_root_user...
        16         16 --> functions -q fish_is_root_user
        25        145 --> fish_is_root_user
        10         96 ---> if test "$EUID" = 0 2>/dev/null...
        86         86 ----> test "$EUID" = 0 2>/dev/null
         3         19 ---> if contains -- $USER root toor Administrator...
        16         16 ----> contains -- $USER root toor Administrator
         5          5 ---> return 1
         9          9 -> set -l bold_flag --bold
         5          5 -> set -q __fish_prompt_status_generation
         6         30 -> if test $__fish_prompt_status_generation = $status_generation...
        17         17 --> test $__fish_prompt_status_generation = $status_generation
         7          7 --> set bold_flag
        11         11 -> set __fish_prompt_status_generation $status_generation
       229        254 -> set -l status_color (set_color $fish_color_status)
        25         25 --> set_color $fish_color_status
       330        352 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        22         22 --> set_color $bold_flag $fish_color_status
       179        332 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        49        153 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
         9          9 ---> set -l last_status
         9         31 ---> if set -q __fish_last_status...
         5          5 ----> set -q __fish_last_status
        17         17 ----> set last_status $__fish_last_status
        10         10 ---> set -l left_brace $argv[1]
         8          8 ---> set -l right_brace $argv[2]
         5          5 ---> set -l separator $argv[3]
         6          6 ---> set -l brace_sep_color $argv[4]
         7          7 ---> set -l status_color $argv[5]
         7          7 ---> set -e argv[1 2 3 4 5]
         3          7 ---> if not set -q argv[1]...
         4          4 ----> not set -q argv[1]
         4         14 ---> if not contains $last_status 0 141...
        10         10 ----> not contains $last_status 0 141
      1163      70909 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        33       1241 --> prompt_login
         9         16 ---> if not set -q __fish_machine...
         7          7 ----> not set -q __fish_machine
         3          7 ---> if set -q __fish_machine[1]...
         4          4 ----> set -q __fish_machine[1]
        35         35 ---> set -l color_host $fish_color_host
         2          7 ---> if set -q SSH_TTY...
         5          5 ----> set -q SSH_TTY
      1008       1143 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        21         21 ----> set_color $fish_color_user
        15         15 ----> set_color --reset
        18         18 ----> set_color $color_host
        23         66 ----> prompt_hostname
        43         43 -----> string replace -r -- "\..*" "" $hostname
        15         15 ----> set_color --reset
        34         34 --> set_color $color_cwd
        60       2717 --> prompt_pwd
        21         21 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        23         23 ---> argparse -n prompt_pwd $options -- $argv
         7         11 ---> if set -q _flag_help...
         4          4 ----> set -q _flag_help
         4          4 ---> set -q argv[1]
         8          8 ---> set argv $PWD
         3          3 ---> set -ql _flag_d
         4          4 ---> set -q fish_prompt_pwd_dir_length
         5          5 ---> set -l fish_prompt_pwd_dir_length 1
         4          4 ---> set -l fulldirs 0
         2          2 ---> set -ql _flag_D
         3          3 ---> set -q fish_prompt_pwd_full_dirs
         5          5 ---> set -l fish_prompt_pwd_full_dirs 1
        22       2564 ---> for path in $argv...
       245        937 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       368        692 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       245        267 ------> set -l realhome (string escape --style=regex -- ~)
        22         22 -------> string escape --style=regex -- ~
        57         57 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        34       1605 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        25         25 -----> test "$fish_prompt_pwd_dir_length" -eq 0
         7          7 -----> set -l full
        25       1148 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 ------> test $fish_prompt_pwd_full_dirs -gt 0
       310       1078 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       731        768 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        37         37 --------> math $fish_prompt_pwd_full_dirs - 1
        29         29 ------> set tmp $all[1]
         8          8 ------> set full $all[2..]
       302        391 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        89         89 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        50      65754 --> fish_vcs_prompt
        30        142 ---> fish_jj_prompt $argv
        24        112 ----> if not command -sq jj...
        75         75 -----> not command -sq jj
        13         13 -----> return 1
       288      65562 ---> fish_git_prompt $argv
        15         82 ----> if not command -sq git...
        67         67 -----> not command -sq git
         5         26 ----> if functions -q __fish_git_prompt_ready...
        21         21 -----> functions -q __fish_git_prompt_ready
       438      18130 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     17692      17692 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
       103        103 ----> test -n "$repo_info"
        27         27 ----> set -l git_dir $repo_info[1]
        10         10 ----> set -l git_common_dir $repo_info[2]
         7          7 ----> set -l inside_gitdir $repo_info[3]
         7          7 ----> set -l bare_repo $repo_info[4]
        11         11 ----> set -l inside_worktree $repo_info[5]
         4          4 ----> set -q repo_info[6]
         7          7 ----> set -l sha $repo_info[6]
       877      19377 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
       170      18500 -----> __fish_git_prompt_operation_branch_bare $repo_info
        24         24 ------> set -l git_dir $argv[1]
         9          9 ------> set -l inside_gitdir $argv[3]
         5          5 ------> set -l bare_repo $argv[4]
         4          4 ------> set -q argv[6]
        26         26 ------> set -l sha $argv[6]
         7          7 ------> set -l branch
         8          8 ------> set -l operation
         4          4 ------> set -l detached no
         4          4 ------> set -l bare
         4          4 ------> set -l step
         3          3 ------> set -l total
        15        115 ------> if test -d $git_dir/rebase-merge...
        36         36 -------> test -d $git_dir/rebase-merge
        20         64 -------> if test -d $git_dir/rebase-apply...
        11         11 --------> test -d $git_dir/rebase-apply
        11         11 --------> test -f $git_dir/MERGE_HEAD
         8          8 --------> test -f $git_dir/CHERRY_PICK_HEAD
         7          7 --------> test -f $git_dir/REVERT_HEAD
         7          7 --------> test -f $git_dir/BISECT_LOG
         4         26 ------> if test -n "$step" -a -n "$total"...
        22         22 -------> test -n "$step" -a -n "$total"
        19      17736 ------> if test -z "$branch"...
         6          6 -------> test -z "$branch"
        71      17711 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
      1216      17640 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     16424      16424 ---------> command git symbolic-ref HEAD 2>/dev/null
        38        139 ------> if test true = $inside_gitdir...
       101        101 -------> test true = $inside_gitdir
       101        101 ------> echo $operation
        50         50 ------> echo $branch
        37         37 ------> echo $detached
        28         28 ------> echo $bare
        85         85 ----> set -l operation $branch_state[1]
        68         68 ----> set -l branch $branch_state[2]
        49         49 ----> set -l detached $branch_state[3]
        29         29 ----> set -l dirtystate
        44         44 ----> set -l stagedstate
        25         25 ----> set -l invalidstate
        21         21 ----> set -l stashstate
        20         20 ----> set -l untrackedfiles
       262        262 ----> set -l bare_prefix $branch_state[4]
        38         38 ----> set -l upstream
        22         22 ----> set -l informative_status
        38         38 ----> set -q __fish_git_prompt_status_order
        25         43 ----> if not set -q ___fish_git_prompt_init...
        18         18 -----> not set -q ___fish_git_prompt_init
        77         77 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
        23         23 ----> set -l informative
        21         21 ----> set -l dirty
        17         17 ----> set -l untracked
      2985      24992 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     22007      22007 -----> read -lz key value
        21        102 ----> if not set -q dirty[1]...
        42         42 -----> not set -q dirty[1]
        39         39 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        29         29 ----> contains dirtystate $__fish_git_prompt_status_order
         6         23 ----> if not set -q untracked[1]...
         8          8 -----> not set -q untracked[1]
         9          9 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
         9          9 ----> contains untrackedfiles $__fish_git_prompt_status_order
        12        121 ----> if test true = $inside_worktree...
        12         12 -----> test true = $inside_worktree
         9         80 -----> if test "$informative" = true...
         8          8 ------> test "$informative" = true
         6         15 ------> ...
         9          9 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        10         31 ------> if not test "$dirty" = true...
         7          7 -------> not test "$dirty" = true
         9          9 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         6         17 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
        11         11 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         3         17 -----> if set -q __fish_git_prompt_showupstream...
         6          6 ------> set -q __fish_git_prompt_showupstream
         8          8 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        18         18 ----> set -l branch_color $___fish_git_prompt_color_branch
        19         19 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         7         15 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
         8          8 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         7          7 ----> set -l flags ""
        27         73 ----> for i in $__fish_git_prompt_status_order...
         4         16 -----> if test -n "$$i"...
        12         12 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3          7 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
         2          6 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
       287        321 ----> set branch (string replace refs/heads/ '' -- $branch)
        34         34 -----> string replace refs/heads/ '' -- $branch
       252        338 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        86         86 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       229        281 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        52         52 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        13         73 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        60         60 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
        10         60 ----> if test -n "$branch"...
        14         14 -----> test -n "$branch"
        13         13 -----> set branch "$branch_color$branch$branch_done"
         6         23 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
         9          9 ------> test -n "$___fish_git_prompt_char_cleanstate"
         2          7 ----> if test -n "$bare_prefix"...
         5          5 -----> test -n "$bare_prefix"
         2          6 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         7         12 ----> if test -n "$upstream"...
         5          5 -----> test -n "$upstream"
         2          8 ----> if test -n "$flags$bare_prefix$upstream"...
         6          6 -----> test -n "$flags$bare_prefix$upstream"
        10         10 ----> set -l format $argv[1]
         5         15 ----> if test -z "$format"...
         4          4 -----> test -z "$format"
         6          6 -----> set format " (%s)"
        62         62 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        31       3324 > fish_title
        17         17 -> set -l ssh
         5          5 -> set -q SSH_TTY
        25       3271 -> if set -q argv[1]...
         5          5 --> set -q argv[1]
       251        263 --> set -l command (status current-command)
        12         12 ---> status current-command
        11         39 --> if test "$command" = fish...
        20         20 ---> test "$command" = fish
         8          8 ---> set command
       456       2939 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        20         20 ---> string sub -l 20 -- $command
        80       2463 ---> prompt_pwd -d 1 -D 1
        17         17 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        33         33 ----> argparse -n prompt_pwd $options -- $argv
         6         11 ----> if set -q _flag_help...
         5          5 -----> set -q _flag_help
         4          4 ----> set -q argv[1]
        10         10 ----> set argv $PWD
         3          3 ----> set -ql _flag_d
        16         16 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         4          4 ----> set -q fish_prompt_pwd_dir_length
         4          4 ----> set -l fulldirs 0
         2          2 ----> set -ql _flag_D
        14         14 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        22       2262 ----> for path in $argv...
       261       1341 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       430       1080 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       531        572 -------> set -l realhome (string escape --style=regex -- ~)
        41         41 --------> string escape --style=regex -- ~
        78         78 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        27        899 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        30         30 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         9          9 ------> set -l full
        16        546 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         9          9 -------> test $fish_prompt_pwd_full_dirs -gt 0
       246        497 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       205        251 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        46         46 ---------> math $fish_prompt_pwd_full_dirs - 1
        17         17 -------> set tmp $all[1]
         7          7 -------> set full $all[2..]
       218        287 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        69         69 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
       121        820 > __fish_winch_handler SIGWINCH
       102        699 -> if test "$fish_handle_reflow" = 1 2>/dev/null...
       303        303 --> test "$fish_handle_reflow" = 1 2>/dev/null
       294        294 --> commandline -f repaint >/dev/null 2>/dev/null
        53        135 > fish_mode_prompt
        16         82 -> fish_default_mode_prompt
        22         66 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        38         38 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         6          6 ---> return
        84     118706 > fish_prompt
        43         43 -> set -l last_pipestatus $pipestatus
        11         11 -> set -lx __fish_last_status $status
       186        210 -> set -l normal (set_color --reset)
        24         24 --> set_color --reset
        16         16 -> set -l color_cwd $fish_color_cwd
         7          7 -> set -l suffix '>'
         7        159 -> if functions -q fish_is_root_user...
        14         14 --> functions -q fish_is_root_user
        26        138 --> fish_is_root_user
         9         87 ---> if test "$EUID" = 0 2>/dev/null...
        78         78 ----> test "$EUID" = 0 2>/dev/null
         3         20 ---> if contains -- $USER root toor Administrator...
        17         17 ----> contains -- $USER root toor Administrator
         5          5 ---> return 1
        10         10 -> set -l bold_flag --bold
         5          5 -> set -q __fish_prompt_status_generation
         6         23 -> if test $__fish_prompt_status_generation = $status_generation...
        11         11 --> test $__fish_prompt_status_generation = $status_generation
         6          6 --> set bold_flag
        12         12 -> set __fish_prompt_status_generation $status_generation
       173        199 -> set -l status_color (set_color $fish_color_status)
        26         26 --> set_color $fish_color_status
       150        176 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        26         26 --> set_color $bold_flag $fish_color_status
       242        399 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        52        157 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        11         11 ---> set -l last_status
        10         23 ---> if set -q __fish_last_status...
         5          5 ----> set -q __fish_last_status
         8          8 ----> set last_status $__fish_last_status
        10         10 ---> set -l left_brace $argv[1]
         6          6 ---> set -l right_brace $argv[2]
         5          5 ---> set -l separator $argv[3]
         7          7 ---> set -l brace_sep_color $argv[4]
        12         12 ---> set -l status_color $argv[5]
         7          7 ---> set -e argv[1 2 3 4 5]
         4          9 ---> if not set -q argv[1]...
         5          5 ----> not set -q argv[1]
         4         15 ---> if not contains $last_status 0 141...
        11         11 ----> not contains $last_status 0 141
       693     117352 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        37       3630 --> prompt_login
        11         46 ---> if not set -q __fish_machine...
        35         35 ----> not set -q __fish_machine
         3          8 ---> if set -q __fish_machine[1]...
         5          5 ----> set -q __fish_machine[1]
        16         16 ---> set -l color_host $fish_color_host
         3          7 ---> if set -q SSH_TTY...
         4          4 ----> set -q SSH_TTY
      3200       3516 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        27         27 ----> set_color $fish_color_user
        58         58 ----> set_color --reset
        58         58 ----> set_color $color_host
        54        127 ----> prompt_hostname
        73         73 -----> string replace -r -- "\..*" "" $hostname
        46         46 ----> set_color --reset
        49         49 --> set_color $color_cwd
        61       3624 --> prompt_pwd
        26         26 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        30         30 ---> argparse -n prompt_pwd $options -- $argv
        10         16 ---> if set -q _flag_help...
         6          6 ----> set -q _flag_help
         5          5 ---> set -q argv[1]
         9          9 ---> set argv $PWD
         3          3 ---> set -ql _flag_d
         4          4 ---> set -q fish_prompt_pwd_dir_length
         5          5 ---> set -l fish_prompt_pwd_dir_length 1
         4          4 ---> set -l fulldirs 0
         2          2 ---> set -ql _flag_D
         6          6 ---> set -q fish_prompt_pwd_full_dirs
         5          5 ---> set -l fish_prompt_pwd_full_dirs 1
        36       3448 ---> for path in $argv...
       316       2329 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
      1150       2013 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       722        758 ------> set -l realhome (string escape --style=regex -- ~)
        36         36 -------> string escape --style=regex -- ~
       105        105 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        34       1083 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        46         46 -----> test "$fish_prompt_pwd_dir_length" -eq 0
        10         10 -----> set -l full
        23        636 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        13         13 ------> test $fish_prompt_pwd_full_dirs -gt 0
       230        571 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       277        341 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        64         64 --------> math $fish_prompt_pwd_full_dirs - 1
        22         22 ------> set tmp $all[1]
         7          7 ------> set full $all[2..]
       242        357 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
       115        115 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        56     109356 --> fish_vcs_prompt
        29        161 ---> fish_jj_prompt $argv
        19        132 ----> if not command -sq jj...
       103        103 -----> not command -sq jj
        10         10 -----> return 1
       233     109139 ---> fish_git_prompt $argv
        16        196 ----> if not command -sq git...
       180        180 -----> not command -sq git
         5         30 ----> if functions -q __fish_git_prompt_ready...
        25         25 -----> functions -q __fish_git_prompt_ready
       350      28358 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     28008      28008 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        40         40 ----> test -n "$repo_info"
        24         24 ----> set -l git_dir $repo_info[1]
         8          8 ----> set -l git_common_dir $repo_info[2]
         6          6 ----> set -l inside_gitdir $repo_info[3]
         6          6 ----> set -l bare_repo $repo_info[4]
        14         14 ----> set -l inside_worktree $repo_info[5]
         3          3 ----> set -q repo_info[6]
        10         10 ----> set -l sha $repo_info[6]
      5698      52065 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
       240      46367 -----> __fish_git_prompt_operation_branch_bare $repo_info
       155        155 ------> set -l git_dir $argv[1]
        63         63 ------> set -l inside_gitdir $argv[3]
        11         11 ------> set -l bare_repo $argv[4]
         5          5 ------> set -q argv[6]
        13         13 ------> set -l sha $argv[6]
         5          5 ------> set -l branch
        17         17 ------> set -l operation
         5          5 ------> set -l detached no
         4          4 ------> set -l bare
         5          5 ------> set -l step
         3          3 ------> set -l total
        30        147 ------> if test -d $git_dir/rebase-merge...
        46         46 -------> test -d $git_dir/rebase-merge
        20         71 -------> if test -d $git_dir/rebase-apply...
        15         15 --------> test -d $git_dir/rebase-apply
        10         10 --------> test -f $git_dir/MERGE_HEAD
        10         10 --------> test -f $git_dir/CHERRY_PICK_HEAD
         9          9 --------> test -f $git_dir/REVERT_HEAD
         7          7 --------> test -f $git_dir/BISECT_LOG
         5         23 ------> if test -n "$step" -a -n "$total"...
        18         18 -------> test -n "$step" -a -n "$total"
         6      45604 ------> if test -z "$branch"...
         6          6 -------> test -z "$branch"
        23      45592 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       760      45569 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     44516      44809 ---------> command git symbolic-ref HEAD 2>/dev/null
        62        293 ----------> __fish_winch_handler SIGWINCH
        18        231 -----------> if test "$fish_handle_reflow" = 1 2>/dev/null...
       117        117 ------------> test "$fish_handle_reflow" = 1 2>/dev/null
        96         96 ------------> commandline -f repaint >/dev/null 2>/dev/null
         5         30 ------> if test true = $inside_gitdir...
        25         25 -------> test true = $inside_gitdir
        21         21 ------> echo $operation
         7          7 ------> echo $branch
         5          5 ------> echo $detached
         4          4 ------> echo $bare
        48         48 ----> set -l operation $branch_state[1]
        10         10 ----> set -l branch $branch_state[2]
        10         10 ----> set -l detached $branch_state[3]
         6          6 ----> set -l dirtystate
        11         11 ----> set -l stagedstate
         4          4 ----> set -l invalidstate
         4          4 ----> set -l stashstate
         5          5 ----> set -l untrackedfiles
         7          7 ----> set -l bare_prefix $branch_state[4]
         3          3 ----> set -l upstream
         5          5 ----> set -l informative_status
         8          8 ----> set -q __fish_git_prompt_status_order
        14         21 ----> if not set -q ___fish_git_prompt_init...
         7          7 -----> not set -q ___fish_git_prompt_init
       107        107 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         6          6 ----> set -l informative
         4          4 ----> set -l dirty
         4          4 ----> set -l untracked
      3199      26469 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     23270      23270 -----> read -lz key value
        18         90 ----> if not set -q dirty[1]...
        35         35 -----> not set -q dirty[1]
        37         37 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        27         27 ----> contains dirtystate $__fish_git_prompt_status_order
         5         21 ----> if not set -q untracked[1]...
         7          7 -----> not set -q untracked[1]
         9          9 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        31         31 ----> contains untrackedfiles $__fish_git_prompt_status_order
         8        118 ----> if test true = $inside_worktree...
        13         13 -----> test true = $inside_worktree
         8         80 -----> if test "$informative" = true...
         7          7 ------> test "$informative" = true
         6         18 ------> ...
        12         12 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        12         31 ------> if not test "$dirty" = true...
         7          7 -------> not test "$dirty" = true
         5          5 -------> test "$untracked" = true
         7          7 -------> test "$dirty" = true
         8         16 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         8          8 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         4         17 -----> if set -q __fish_git_prompt_showupstream...
         6          6 ------> set -q __fish_git_prompt_showupstream
         7          7 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        18         18 ----> set -l branch_color $___fish_git_prompt_color_branch
        65         65 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         7         18 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        11         11 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         7          7 ----> set -l flags ""
        26         74 ----> for i in $__fish_git_prompt_status_order...
         4         17 -----> if test -n "$$i"...
        13         13 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3          7 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
         2          9 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
         3          7 -----> if test -n "$$i"...
         4          4 ------> test -n "$$i"
       213        245 ----> set branch (string replace refs/heads/ '' -- $branch)
        32         32 -----> string replace refs/heads/ '' -- $branch
       205        271 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        66         66 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       147        195 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        48         48 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        17         62 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        45         45 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         7         61 ----> if test -n "$branch"...
        14         14 -----> test -n "$branch"
        13         13 -----> set branch "$branch_color$branch$branch_done"
         7         27 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        12         12 ------> test -n "$___fish_git_prompt_char_cleanstate"
         2          7 ----> if test -n "$bare_prefix"...
         5          5 -----> test -n "$bare_prefix"
         2          6 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         3          7 ----> if test -n "$upstream"...
         4          4 -----> test -n "$upstream"
         2          9 ----> if test -n "$flags$bare_prefix$upstream"...
         7          7 -----> test -n "$flags$bare_prefix$upstream"
        10         10 ----> set -l format $argv[1]
         5         15 ----> if test -z "$format"...
         5          5 -----> test -z "$format"
         5          5 -----> set format " (%s)"
        57         57 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        38       6090 > fish_title
        20         20 -> set -l ssh
         5          5 -> set -q SSH_TTY
       167       6027 -> if set -q argv[1]...
         5          5 --> set -q argv[1]
       176        202 --> set -l command (status current-command)
        26         26 ---> status current-command
        12         34 --> if test "$command" = fish...
        16         16 ---> test "$command" = fish
         6          6 ---> set command
       269       5619 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        19         19 ---> string sub -l 20 -- $command
        55       5331 ---> prompt_pwd -d 1 -D 1
        20         20 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        47         47 ----> argparse -n prompt_pwd $options -- $argv
         8         14 ----> if set -q _flag_help...
         6          6 -----> set -q _flag_help
         4          4 ----> set -q argv[1]
         9          9 ----> set argv $PWD
         4          4 ----> set -ql _flag_d
        38         38 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         5          5 ----> set -q fish_prompt_pwd_dir_length
         4          4 ----> set -l fulldirs 0
         2          2 ----> set -ql _flag_D
         9          9 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        25       5117 ----> for path in $argv...
       219       4348 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
      3864       4129 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       157        190 -------> set -l realhome (string escape --style=regex -- ~)
        33         33 --------> string escape --style=regex -- ~
        75         75 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        23        744 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        32         32 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         8          8 ------> set -l full
        19        455 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         9          9 -------> test $fish_prompt_pwd_full_dirs -gt 0
       192        403 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       161        211 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        50         50 ---------> math $fish_prompt_pwd_full_dirs - 1
        17         17 -------> set tmp $all[1]
         7          7 -------> set full $all[2..]
       161        226 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        65         65 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        48        358 > __fish_winch_handler SIGWINCH
        37        310 -> if test "$fish_handle_reflow" = 1 2>/dev/null...
       198        198 --> test "$fish_handle_reflow" = 1 2>/dev/null
        75         75 --> commandline -f repaint >/dev/null 2>/dev/null
        86        274 > fish_mode_prompt
        21        188 -> fish_default_mode_prompt
        92        167 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        62         62 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
        13         13 ---> return
       139      96180 > fish_prompt
        48         48 -> set -l last_pipestatus $pipestatus
        14         14 -> set -lx __fish_last_status $status
       390        420 -> set -l normal (set_color --reset)
        30         30 --> set_color --reset
        25         25 -> set -l color_cwd $fish_color_cwd
         8          8 -> set -l suffix '>'
        10        199 -> if functions -q fish_is_root_user...
        20         20 --> functions -q fish_is_root_user
        34        169 --> fish_is_root_user
        13        100 ---> if test "$EUID" = 0 2>/dev/null...
        87         87 ----> test "$EUID" = 0 2>/dev/null
         4         29 ---> if contains -- $USER root toor Administrator...
        25         25 ----> contains -- $USER root toor Administrator
         6          6 ---> return 1
        14         14 -> set -l bold_flag --bold
        18         18 -> set -q __fish_prompt_status_generation
         7         31 -> if test $__fish_prompt_status_generation = $status_generation...
        15         15 --> test $__fish_prompt_status_generation = $status_generation
         9          9 --> set bold_flag
       367        367 -> set __fish_prompt_status_generation $status_generation
       435        496 -> set -l status_color (set_color $fish_color_status)
        61         61 --> set_color $fish_color_status
       583        718 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
       135        135 --> set_color $bold_flag $fish_color_status
       510       1397 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
       314        887 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        69         69 ---> set -l last_status
        51        160 ---> if set -q __fish_last_status...
        50         50 ----> set -q __fish_last_status
        59         59 ----> set last_status $__fish_last_status
        57         57 ---> set -l left_brace $argv[1]
        34         34 ---> set -l right_brace $argv[2]
        33         33 ---> set -l separator $argv[3]
        32         32 ---> set -l brace_sep_color $argv[4]
        34         34 ---> set -l status_color $argv[5]
        31         31 ---> set -e argv[1 2 3 4 5]
        26         46 ---> if not set -q argv[1]...
        20         20 ----> not set -q argv[1]
        22         77 ---> if not contains $last_status 0 141...
        55         55 ----> not contains $last_status 0 141
       682      92286 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        98       8457 --> prompt_login
        52         82 ---> if not set -q __fish_machine...
        30         30 ----> not set -q __fish_machine
        16         45 ---> if set -q __fish_machine[1]...
        29         29 ----> set -q __fish_machine[1]
       429        429 ---> set -l color_host $fish_color_host
        27         79 ---> if set -q SSH_TTY...
        52         52 ----> set -q SSH_TTY
      6696       7724 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
       174        174 ----> set_color $fish_color_user
       123        123 ----> set_color --reset
       214        214 ----> set_color $color_host
       187        469 ----> prompt_hostname
       282        282 -----> string replace -r -- "\..*" "" $hostname
        48         48 ----> set_color --reset
        37         37 --> set_color $color_cwd
        57       6979 --> prompt_pwd
        21         21 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        30         30 ---> argparse -n prompt_pwd $options -- $argv
        18        112 ---> if set -q _flag_help...
        94         94 ----> set -q _flag_help
        12         12 ---> set -q argv[1]
        19         19 ---> set argv $PWD
         4          4 ---> set -ql _flag_d
         5          5 ---> set -q fish_prompt_pwd_dir_length
         6          6 ---> set -l fish_prompt_pwd_dir_length 1
         5          5 ---> set -l fulldirs 0
         3          3 ---> set -ql _flag_D
         4          4 ---> set -q fish_prompt_pwd_full_dirs
         5          5 ---> set -l fish_prompt_pwd_full_dirs 1
        59       6696 ---> for path in $argv...
       390       5623 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
      1758       5233 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
      3289       3352 ------> set -l realhome (string escape --style=regex -- ~)
        63         63 -------> string escape --style=regex -- ~
       123        123 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        40       1014 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        54         54 -----> test "$fish_prompt_pwd_dir_length" -eq 0
        14         14 -----> set -l full
        30        603 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        13         13 ------> test $fish_prompt_pwd_full_dirs -gt 0
       234        530 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       211        296 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        85         85 --------> math $fish_prompt_pwd_full_dirs - 1
        21         21 ------> set tmp $all[1]
         9          9 ------> set full $all[2..]
       197        303 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
       106        106 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        47      76131 --> fish_vcs_prompt
        26        146 ---> fish_jj_prompt $argv
        16        120 ----> if not command -sq jj...
        96         96 -----> not command -sq jj
         8          8 -----> return 1
       154      75938 ---> fish_git_prompt $argv
        11        137 ----> if not command -sq git...
       126        126 -----> not command -sq git
         6         26 ----> if functions -q __fish_git_prompt_ready...
        20         20 -----> functions -q __fish_git_prompt_ready
      1989      27345 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     24977      25356 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
       127        379 ------> __fish_winch_handler SIGWINCH
        17        252 -------> if test "$fish_handle_reflow" = 1 2>/dev/null...
       123        123 --------> test "$fish_handle_reflow" = 1 2>/dev/null
       112        112 --------> commandline -f repaint >/dev/null 2>/dev/null
        48         48 ----> test -n "$repo_info"
        27         27 ----> set -l git_dir $repo_info[1]
         9          9 ----> set -l git_common_dir $repo_info[2]
         7          7 ----> set -l inside_gitdir $repo_info[3]
         8          8 ----> set -l bare_repo $repo_info[4]
        19         19 ----> set -l inside_worktree $repo_info[5]
         5          5 ----> set -q repo_info[6]
        11         11 ----> set -l sha $repo_info[6]
       266      30153 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
       100      29887 -----> __fish_git_prompt_operation_branch_bare $repo_info
        30         30 ------> set -l git_dir $argv[1]
        10         10 ------> set -l inside_gitdir $argv[3]
         7          7 ------> set -l bare_repo $argv[4]
         6          6 ------> set -q argv[6]
         9          9 ------> set -l sha $argv[6]
         4          4 ------> set -l branch
        13         13 ------> set -l operation
         6          6 ------> set -l detached no
         5          5 ------> set -l bare
         4          4 ------> set -l step
         4          4 ------> set -l total
        23        149 ------> if test -d $git_dir/rebase-merge...
        46         46 -------> test -d $git_dir/rebase-merge
        21         80 -------> if test -d $git_dir/rebase-apply...
        19         19 --------> test -d $git_dir/rebase-apply
        11         11 --------> test -f $git_dir/MERGE_HEAD
        11         11 --------> test -f $git_dir/CHERRY_PICK_HEAD
        10         10 --------> test -f $git_dir/REVERT_HEAD
         8          8 --------> test -f $git_dir/BISECT_LOG
         5         25 ------> if test -n "$step" -a -n "$total"...
        20         20 -------> test -n "$step" -a -n "$total"
         9      29436 ------> if test -z "$branch"...
         6          6 -------> test -z "$branch"
        27      29421 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       438      29394 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     28956      28956 ---------> command git symbolic-ref HEAD 2>/dev/null
         5         34 ------> if test true = $inside_gitdir...
        29         29 -------> test true = $inside_gitdir
        26         26 ------> echo $operation
         8          8 ------> echo $branch
         6          6 ------> echo $detached
         5          5 ------> echo $bare
        26         26 ----> set -l operation $branch_state[1]
        10         10 ----> set -l branch $branch_state[2]
         7          7 ----> set -l detached $branch_state[3]
         5          5 ----> set -l dirtystate
        11         11 ----> set -l stagedstate
         4          4 ----> set -l invalidstate
         5          5 ----> set -l stashstate
         5          5 ----> set -l untrackedfiles
         8          8 ----> set -l bare_prefix $branch_state[4]
         5          5 ----> set -l upstream
         6          6 ----> set -l informative_status
         7          7 ----> set -q __fish_git_prompt_status_order
         5         12 ----> if not set -q ___fish_git_prompt_init...
         7          7 -----> not set -q ___fish_git_prompt_init
        28         28 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         5          5 ----> set -l informative
         6          6 ----> set -l dirty
         5          5 ----> set -l untracked
      1584      16564 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     14980      14980 -----> read -lz key value
        20         97 ----> if not set -q dirty[1]...
        38         38 -----> not set -q dirty[1]
        39         39 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        28         28 ----> contains dirtystate $__fish_git_prompt_status_order
         7         25 ----> if not set -q untracked[1]...
         6          6 -----> not set -q untracked[1]
        12         12 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        55         55 ----> contains untrackedfiles $__fish_git_prompt_status_order
        10        131 ----> if test true = $inside_worktree...
        15         15 -----> test true = $inside_worktree
         9         87 -----> if test "$informative" = true...
        10         10 ------> test "$informative" = true
         6         20 ------> ...
        14         14 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        12         33 ------> if not test "$dirty" = true...
         8          8 -------> not test "$dirty" = true
         8          8 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         7         15 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         8          8 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         4         19 -----> if set -q __fish_git_prompt_showupstream...
         5          5 ------> set -q __fish_git_prompt_showupstream
        10         10 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        19         19 ----> set -l branch_color $___fish_git_prompt_color_branch
        16         16 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         6         25 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        19         19 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         9          9 ----> set -l flags ""
        24         77 ----> for i in $__fish_git_prompt_status_order...
         6         17 -----> if test -n "$$i"...
        11         11 ------> test -n "$$i"
         4         10 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         4          9 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
       215        236 ----> set branch (string replace refs/heads/ '' -- $branch)
        21         21 -----> string replace refs/heads/ '' -- $branch
       125        189 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        64         64 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       105        136 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        31         31 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        10         54 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        44         44 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         8         57 ----> if test -n "$branch"...
        13         13 -----> test -n "$branch"
        11         11 -----> set branch "$branch_color$branch$branch_done"
         7         25 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        10         10 ------> test -n "$___fish_git_prompt_char_cleanstate"
         3          8 ----> if test -n "$bare_prefix"...
         5          5 -----> test -n "$bare_prefix"
         4          8 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         3          7 ----> if test -n "$upstream"...
         4          4 -----> test -n "$upstream"
         2          9 ----> if test -n "$flags$bare_prefix$upstream"...
         7          7 -----> test -n "$flags$bare_prefix$upstream"
         9          9 ----> set -l format $argv[1]
         4         17 ----> if test -z "$format"...
         5          5 -----> test -z "$format"
         8          8 -----> set format " (%s)"
        58         58 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        27       2021 > fish_title
        17         17 -> set -l ssh
         6          6 -> set -q SSH_TTY
        18       1971 -> if set -q argv[1]...
         5          5 --> set -q argv[1]
       218        231 --> set -l command (status current-command)
        13         13 ---> status current-command
        11         41 --> if test "$command" = fish...
        21         21 ---> test "$command" = fish
         9          9 ---> set command
       271       1676 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        16         16 ---> string sub -l 20 -- $command
        59       1389 ---> prompt_pwd -d 1 -D 1
        13         13 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        46         46 ----> argparse -n prompt_pwd $options -- $argv
         6         13 ----> if set -q _flag_help...
         7          7 -----> set -q _flag_help
         5          5 ----> set -q argv[1]
        10         10 ----> set argv $PWD
         3          3 ----> set -ql _flag_d
        13         13 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         4          4 ----> set -q fish_prompt_pwd_dir_length
         5          5 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         9          9 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        20       1203 ----> for path in $argv...
       150        635 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       252        485 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       141        168 -------> set -l realhome (string escape --style=regex -- ~)
        27         27 --------> string escape --style=regex -- ~
        65         65 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        20        548 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        22         22 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         8          8 ------> set -l full
        18        330 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         9          9 -------> test $fish_prompt_pwd_full_dirs -gt 0
       124        282 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       123        158 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        35         35 ---------> math $fish_prompt_pwd_full_dirs - 1
        14         14 -------> set tmp $all[1]
         7          7 -------> set full $all[2..]
       115        168 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        53         53 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        67        188 > fish_mode_prompt
        20        121 -> fish_default_mode_prompt
        21        101 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        71         71 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         9          9 ---> return
        87      53080 > fish_prompt
        50         50 -> set -l last_pipestatus $pipestatus
        11         11 -> set -lx __fish_last_status $status
       160        181 -> set -l normal (set_color --reset)
        21         21 --> set_color --reset
        15         15 -> set -l color_cwd $fish_color_cwd
         7          7 -> set -l suffix '>'
         8        210 -> if functions -q fish_is_root_user...
        15         15 --> functions -q fish_is_root_user
        58        187 --> fish_is_root_user
        12        101 ---> if test "$EUID" = 0 2>/dev/null...
        89         89 ----> test "$EUID" = 0 2>/dev/null
         5         22 ---> if contains -- $USER root toor Administrator...
        17         17 ----> contains -- $USER root toor Administrator
         6          6 ---> return 1
        10         10 -> set -l bold_flag --bold
         6          6 -> set -q __fish_prompt_status_generation
         6         25 -> if test $__fish_prompt_status_generation = $status_generation...
        12         12 --> test $__fish_prompt_status_generation = $status_generation
         7          7 --> set bold_flag
        14         14 -> set __fish_prompt_status_generation $status_generation
       169        193 -> set -l status_color (set_color $fish_color_status)
        24         24 --> set_color $fish_color_status
       161        192 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        31         31 --> set_color $bold_flag $fish_color_status
       166        336 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        50        170 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        11         11 ---> set -l last_status
        12         35 ---> if set -q __fish_last_status...
         4          4 ----> set -q __fish_last_status
        19         19 ----> set last_status $__fish_last_status
        11         11 ---> set -l left_brace $argv[1]
         7          7 ---> set -l right_brace $argv[2]
         7          7 ---> set -l separator $argv[3]
         7          7 ---> set -l brace_sep_color $argv[4]
         8          8 ---> set -l status_color $argv[5]
         8          8 ---> set -e argv[1 2 3 4 5]
         4         10 ---> if not set -q argv[1]...
         6          6 ----> not set -q argv[1]
         5         16 ---> if not contains $last_status 0 141...
        11         11 ----> not contains $last_status 0 141
       463      51743 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        25        720 --> prompt_login
         8         17 ---> if not set -q __fish_machine...
         9          9 ----> not set -q __fish_machine
         2          8 ---> if set -q __fish_machine[1]...
         6          6 ----> set -q __fish_machine[1]
        13         13 ---> set -l color_host $fish_color_host
         3          7 ---> if set -q SSH_TTY...
         4          4 ----> set -q SSH_TTY
       512        650 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        21         21 ----> set_color $fish_color_user
        13         13 ----> set_color --reset
        17         17 ----> set_color $color_host
        24         75 ----> prompt_hostname
        51         51 -----> string replace -r -- "\..*" "" $hostname
        12         12 ----> set_color --reset
        19         19 --> set_color $color_cwd
        65       1559 --> prompt_pwd
        14         14 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        23         23 ---> argparse -n prompt_pwd $options -- $argv
         4         10 ---> if set -q _flag_help...
         6          6 ----> set -q _flag_help
         4          4 ---> set -q argv[1]
         9          9 ---> set argv $PWD
         4          4 ---> set -ql _flag_d
         4          4 ---> set -q fish_prompt_pwd_dir_length
         7          7 ---> set -l fish_prompt_pwd_dir_length 1
         5          5 ---> set -l fulldirs 0
         3          3 ---> set -ql _flag_D
         4          4 ---> set -q fish_prompt_pwd_full_dirs
         6          6 ---> set -l fish_prompt_pwd_full_dirs 1
        24       1401 ---> for path in $argv...
       152        773 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       412        621 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       111        148 ------> set -l realhome (string escape --style=regex -- ~)
        37         37 -------> string escape --style=regex -- ~
        61         61 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        19        604 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        27         27 -----> test "$fish_prompt_pwd_dir_length" -eq 0
         8          8 -----> set -l full
        18        338 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
        10         10 ------> test $fish_prompt_pwd_full_dirs -gt 0
       135        288 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       118        153 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        35         35 --------> math $fish_prompt_pwd_full_dirs - 1
        15         15 ------> set tmp $all[1]
         7          7 ------> set full $all[2..]
       154        212 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        58         58 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        37      48982 --> fish_vcs_prompt
        21        125 ---> fish_jj_prompt $argv
        17        104 ----> if not command -sq jj...
        80         80 -----> not command -sq jj
         7          7 -----> return 1
       137      48820 ---> fish_git_prompt $argv
         6         79 ----> if not command -sq git...
        73         73 -----> not command -sq git
         4         19 ----> if functions -q __fish_git_prompt_ready...
        15         15 -----> functions -q __fish_git_prompt_ready
       373      15727 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     15354      15354 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        41         41 ----> test -n "$repo_info"
        22         22 ----> set -l git_dir $repo_info[1]
         9          9 ----> set -l git_common_dir $repo_info[2]
        11         11 ----> set -l inside_gitdir $repo_info[3]
         8          8 ----> set -l bare_repo $repo_info[4]
        13         13 ----> set -l inside_worktree $repo_info[5]
         5          5 ----> set -q repo_info[6]
         8          8 ----> set -l sha $repo_info[6]
       237      16139 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
       110      15902 -----> __fish_git_prompt_operation_branch_bare $repo_info
        18         18 ------> set -l git_dir $argv[1]
         8          8 ------> set -l inside_gitdir $argv[3]
         6          6 ------> set -l bare_repo $argv[4]
         5          5 ------> set -q argv[6]
         7          7 ------> set -l sha $argv[6]
         5          5 ------> set -l branch
        19         19 ------> set -l operation
         5          5 ------> set -l detached no
         4          4 ------> set -l bare
         5          5 ------> set -l step
         6          6 ------> set -l total
        15        114 ------> if test -d $git_dir/rebase-merge...
        28         28 -------> test -d $git_dir/rebase-merge
        20         71 -------> if test -d $git_dir/rebase-apply...
        13         13 --------> test -d $git_dir/rebase-apply
        11         11 --------> test -f $git_dir/MERGE_HEAD
         9          9 --------> test -f $git_dir/CHERRY_PICK_HEAD
        10         10 --------> test -f $git_dir/REVERT_HEAD
         8          8 --------> test -f $git_dir/BISECT_LOG
         4         20 ------> if test -n "$step" -a -n "$total"...
        16         16 -------> test -n "$step" -a -n "$total"
         8      15490 ------> if test -z "$branch"...
         5          5 -------> test -z "$branch"
        28      15477 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       363      15449 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     15086      15086 ---------> command git symbolic-ref HEAD 2>/dev/null
         7         35 ------> if test true = $inside_gitdir...
        28         28 -------> test true = $inside_gitdir
        27         27 ------> echo $operation
         8          8 ------> echo $branch
         5          5 ------> echo $detached
         5          5 ------> echo $bare
        17         17 ----> set -l operation $branch_state[1]
         9          9 ----> set -l branch $branch_state[2]
         7          7 ----> set -l detached $branch_state[3]
         5          5 ----> set -l dirtystate
        12         12 ----> set -l stagedstate
         5          5 ----> set -l invalidstate
         3          3 ----> set -l stashstate
         4          4 ----> set -l untrackedfiles
         8          8 ----> set -l bare_prefix $branch_state[4]
         4          4 ----> set -l upstream
         5          5 ----> set -l informative_status
         7          7 ----> set -q __fish_git_prompt_status_order
         5         11 ----> if not set -q ___fish_git_prompt_init...
         6          6 -----> not set -q ___fish_git_prompt_init
        21         21 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         5          5 ----> set -l informative
         5          5 ----> set -l dirty
         4          4 ----> set -l untracked
      1539      15178 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     13639      13639 -----> read -lz key value
        21         98 ----> if not set -q dirty[1]...
        36         36 -----> not set -q dirty[1]
        41         41 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        42         42 ----> contains dirtystate $__fish_git_prompt_status_order
         7         25 ----> if not set -q untracked[1]...
         7          7 -----> not set -q untracked[1]
        11         11 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        10         10 ----> contains untrackedfiles $__fish_git_prompt_status_order
         9        122 ----> if test true = $inside_worktree...
        15         15 -----> test true = $inside_worktree
        11         80 -----> if test "$informative" = true...
         8          8 ------> test "$informative" = true
         6         15 ------> ...
         9          9 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        13         30 ------> if not test "$dirty" = true...
         6          6 -------> not test "$dirty" = true
         6          6 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         8         16 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         8          8 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         5         18 -----> if set -q __fish_git_prompt_showupstream...
         5          5 ------> set -q __fish_git_prompt_showupstream
         8          8 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        19         19 ----> set -l branch_color $___fish_git_prompt_color_branch
        20         20 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         7         27 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
        20         20 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         8          8 ----> set -l flags ""
        26         82 ----> for i in $__fish_git_prompt_status_order...
         5         14 -----> if test -n "$$i"...
         9          9 ------> test -n "$$i"
         3         10 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
         3         11 -----> if test -n "$$i"...
         8          8 ------> test -n "$$i"
         7         13 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
       226        253 ----> set branch (string replace refs/heads/ '' -- $branch)
        27         27 -----> string replace refs/heads/ '' -- $branch
       151        208 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        57         57 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       122        152 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        30         30 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        13         48 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        35         35 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         8         56 ----> if test -n "$branch"...
        11         11 -----> test -n "$branch"
        12         12 -----> set branch "$branch_color$branch$branch_done"
         7         25 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         8          8 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        10         10 ------> test -n "$___fish_git_prompt_char_cleanstate"
         2         10 ----> if test -n "$bare_prefix"...
         8          8 -----> test -n "$bare_prefix"
         3          7 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         6         12 ----> if test -n "$upstream"...
         6          6 -----> test -n "$upstream"
         2         12 ----> if test -n "$flags$bare_prefix$upstream"...
        10         10 -----> test -n "$flags$bare_prefix$upstream"
         9          9 ----> set -l format $argv[1]
         4         16 ----> if test -z "$format"...
         5          5 -----> test -z "$format"
         7          7 -----> set format " (%s)"
        56         56 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        26       2059 > fish_title
        16         16 -> set -l ssh
         6          6 -> set -q SSH_TTY
        17       2011 -> if set -q argv[1]...
         4          4 --> set -q argv[1]
       120        130 --> set -l command (status current-command)
        10         10 ---> status current-command
         9         31 --> if test "$command" = fish...
        16         16 ---> test "$command" = fish
         6          6 ---> set command
       219       1829 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        14         14 ---> string sub -l 20 -- $command
        52       1596 ---> prompt_pwd -d 1 -D 1
        13         13 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        35         35 ----> argparse -n prompt_pwd $options -- $argv
         4          9 ----> if set -q _flag_help...
         5          5 -----> set -q _flag_help
         4          4 ----> set -q argv[1]
        19         19 ----> set argv $PWD
         5          5 ----> set -ql _flag_d
        15         15 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         3          3 ----> set -q fish_prompt_pwd_dir_length
         5          5 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         8          8 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        23       1422 ----> for path in $argv...
       241        714 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       263        473 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       119        145 -------> set -l realhome (string escape --style=regex -- ~)
        26         26 --------> string escape --style=regex -- ~
        65         65 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        20        685 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        27         27 ------> test "$fish_prompt_pwd_dir_length" -eq 0
        10         10 ------> set -l full
        18        427 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         9          9 -------> test $fish_prompt_pwd_full_dirs -gt 0
       161        376 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       162        215 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        53         53 ---------> math $fish_prompt_pwd_full_dirs - 1
        17         17 -------> set tmp $all[1]
         7          7 -------> set full $all[2..]
       133        201 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        68         68 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        55        149 > fish_mode_prompt
        17         94 -> fish_default_mode_prompt
        24         77 --> if not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings...
        48         48 ---> not contains -- "$fish_key_bindings" fish_vi_key_bindings fish_hybrid_key_bindings
         5          5 ---> return
       112      58493 > fish_prompt
        50         50 -> set -l last_pipestatus $pipestatus
        11         11 -> set -lx __fish_last_status $status
       182        208 -> set -l normal (set_color --reset)
        26         26 --> set_color --reset
        17         17 -> set -l color_cwd $fish_color_cwd
        86         86 -> set -l suffix '>'
        15        211 -> if functions -q fish_is_root_user...
        23         23 --> functions -q fish_is_root_user
        30        173 --> fish_is_root_user
        11        113 ---> if test "$EUID" = 0 2>/dev/null...
       102        102 ----> test "$EUID" = 0 2>/dev/null
         3         23 ---> if contains -- $USER root toor Administrator...
        20         20 ----> contains -- $USER root toor Administrator
         7          7 ---> return 1
        10         10 -> set -l bold_flag --bold
         6          6 -> set -q __fish_prompt_status_generation
         6         28 -> if test $__fish_prompt_status_generation = $status_generation...
        14         14 --> test $__fish_prompt_status_generation = $status_generation
         8          8 --> set bold_flag
        16         16 -> set __fish_prompt_status_generation $status_generation
      1196       1225 -> set -l status_color (set_color $fish_color_status)
        29         29 --> set_color $fish_color_status
       184        224 -> set -l statusb_color (set_color $bold_flag $fish_color_status)
        40         40 --> set_color $bold_flag $fish_color_status
       174        362 -> set -l prompt_status (__fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus)
        73        188 --> __fish_print_pipestatus "[" "]" "|" "$status_color" "$statusb_color" $last_pipestatus
        12         12 ---> set -l last_status
        12         28 ---> if set -q __fish_last_status...
         6          6 ----> set -q __fish_last_status
        10         10 ----> set last_status $__fish_last_status
        12         12 ---> set -l left_brace $argv[1]
         7          7 ---> set -l right_brace $argv[2]
         7          7 ---> set -l separator $argv[3]
         8          8 ---> set -l brace_sep_color $argv[4]
         8          8 ---> set -l status_color $argv[5]
         8          8 ---> set -e argv[1 2 3 4 5]
         4          9 ---> if not set -q argv[1]...
         5          5 ----> not set -q argv[1]
         5         16 ---> if not contains $last_status 0 141...
        11         11 ----> not contains $last_status 0 141
       464      55927 -> echo -n -s (prompt_login)' ' (set_color $color_cwd) (prompt_pwd) $normal (fish_vcs_prompt) $normal " "$prompt_status $suffix " "
        27        891 --> prompt_login
         9         18 ---> if not set -q __fish_machine...
         9          9 ----> not set -q __fish_machine
         2          8 ---> if set -q __fish_machine[1]...
         6          6 ----> set -q __fish_machine[1]
        12         12 ---> set -l color_host $fish_color_host
         2          7 ---> if set -q SSH_TTY...
         5          5 ----> set -q SSH_TTY
       642        819 ---> echo -n -s (set_color $fish_color_user) "$USER" (set_color --reset) @ (set_color $color_host) (prompt_hostname) (set_color --reset)
        22         22 ----> set_color $fish_color_user
        22         22 ----> set_color --reset
        19         19 ----> set_color $color_host
        28        100 ----> prompt_hostname
        72         72 -----> string replace -r -- "\..*" "" $hostname
        14         14 ----> set_color --reset
        22         22 --> set_color $color_cwd
        47       1336 --> prompt_pwd
        18         18 ---> set -l options h/help d/dir-length= D/full-length-dirs=
        26         26 ---> argparse -n prompt_pwd $options -- $argv
         7         13 ---> if set -q _flag_help...
         6          6 ----> set -q _flag_help
         5          5 ---> set -q argv[1]
         9          9 ---> set argv $PWD
         4          4 ---> set -ql _flag_d
         5          5 ---> set -q fish_prompt_pwd_dir_length
        20         20 ---> set -l fish_prompt_pwd_dir_length 1
         6          6 ---> set -l fulldirs 0
         3          3 ---> set -ql _flag_D
         4          4 ---> set -q fish_prompt_pwd_full_dirs
         5          5 ---> set -l fish_prompt_pwd_full_dirs 1
        26       1171 ---> for path in $argv...
       181        579 ----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       195        398 -----> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       116        137 ------> set -l realhome (string escape --style=regex -- ~)
        21         21 -------> string escape --style=regex -- ~
        66         66 ------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        21        566 ----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        24         24 -----> test "$fish_prompt_pwd_dir_length" -eq 0
         8          8 -----> set -l full
        16        328 -----> if test $fish_prompt_pwd_full_dirs -gt 0...
         8          8 ------> test $fish_prompt_pwd_full_dirs -gt 0
       128        281 ------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       119        153 -------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        34         34 --------> math $fish_prompt_pwd_full_dirs - 1
        15         15 ------> set tmp $all[1]
         8          8 ------> set full $all[2..]
       120        185 -----> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        65         65 ------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
        38      53214 --> fish_vcs_prompt
        22        107 ---> fish_jj_prompt $argv
         9         85 ----> if not command -sq jj...
        69         69 -----> not command -sq jj
         7          7 -----> return 1
       151      53069 ---> fish_git_prompt $argv
         7         75 ----> if not command -sq git...
        68         68 -----> not command -sq git
         5         20 ----> if functions -q __fish_git_prompt_ready...
        15         15 -----> functions -q __fish_git_prompt_ready
       702      16163 ----> set -l repo_info (command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null)
     15461      15461 -----> command git rev-parse --git-dir --git-common-dir --is-inside-git-dir --is-bare-repository --is-inside-work-tree HEAD 2>/dev/null
        42         42 ----> test -n "$repo_info"
        23         23 ----> set -l git_dir $repo_info[1]
        12         12 ----> set -l git_common_dir $repo_info[2]
        10         10 ----> set -l inside_gitdir $repo_info[3]
        11         11 ----> set -l bare_repo $repo_info[4]
        14         14 ----> set -l inside_worktree $repo_info[5]
         5          5 ----> set -q repo_info[6]
         8          8 ----> set -l sha $repo_info[6]
       262      17504 ----> set -l branch_state (__fish_git_prompt_operation_branch_bare $repo_info)
        94      17242 -----> __fish_git_prompt_operation_branch_bare $repo_info
        18         18 ------> set -l git_dir $argv[1]
        12         12 ------> set -l inside_gitdir $argv[3]
        11         11 ------> set -l bare_repo $argv[4]
         5          5 ------> set -q argv[6]
        10         10 ------> set -l sha $argv[6]
         6          6 ------> set -l branch
         9          9 ------> set -l operation
         6          6 ------> set -l detached no
         5          5 ------> set -l bare
         5          5 ------> set -l step
         4          4 ------> set -l total
        22        142 ------> if test -d $git_dir/rebase-merge...
        39         39 -------> test -d $git_dir/rebase-merge
        23         81 -------> if test -d $git_dir/rebase-apply...
        16         16 --------> test -d $git_dir/rebase-apply
        12         12 --------> test -f $git_dir/MERGE_HEAD
        11         11 --------> test -f $git_dir/CHERRY_PICK_HEAD
        10         10 --------> test -f $git_dir/REVERT_HEAD
         9          9 --------> test -f $git_dir/BISECT_LOG
         4         20 ------> if test -n "$step" -a -n "$total"...
        16         16 -------> test -n "$step" -a -n "$total"
         9      16801 ------> if test -z "$branch"...
         6          6 -------> test -z "$branch"
        27      16786 -------> if not set branch (command git symbolic-ref HEAD 2>/dev/null)...
       403      16759 --------> not set branch (command git symbolic-ref HEAD 2>/dev/null)
     16356      16356 ---------> command git symbolic-ref HEAD 2>/dev/null
         8         41 ------> if test true = $inside_gitdir...
        33         33 -------> test true = $inside_gitdir
        32         32 ------> echo $operation
        10         10 ------> echo $branch
         6          6 ------> echo $detached
         5          5 ------> echo $bare
        22         22 ----> set -l operation $branch_state[1]
         8          8 ----> set -l branch $branch_state[2]
        14         14 ----> set -l detached $branch_state[3]
         7          7 ----> set -l dirtystate
        13         13 ----> set -l stagedstate
         5          5 ----> set -l invalidstate
         5          5 ----> set -l stashstate
         5          5 ----> set -l untrackedfiles
         8          8 ----> set -l bare_prefix $branch_state[4]
         5          5 ----> set -l upstream
         4          4 ----> set -l informative_status
         7          7 ----> set -q __fish_git_prompt_status_order
         6         13 ----> if not set -q ___fish_git_prompt_init...
         7          7 -----> not set -q ___fish_git_prompt_init
        31         31 ----> set -l space "$___fish_git_prompt_color$___fish_git_prompt_char_stateseparator$___fish_git_prompt_color_done"
         5          5 ----> set -l informative
         5          5 ----> set -l dirty
         4          4 ----> set -l untracked
      1672      17418 ----> command git config -z --get-regexp 'bash\.(showInformativeStatus|showDirtyState|showUntrackedFiles)' 2>/dev/null | while read -lz key value
                                    switch $key
                                        case bash.showinformativestatus
                                            set informative $value
                                        case bash.showdirtystate
                                            set dirty $value
                                        case bash.showuntrackedfiles
                                            set untracked $value
                                    end
                                end
     15746      15746 -----> read -lz key value
        22        103 ----> if not set -q dirty[1]...
        36         36 -----> not set -q dirty[1]
        45         45 -----> contains -- "$__fish_git_prompt_showdirtystate" yes true 1
        31         31 ----> contains dirtystate $__fish_git_prompt_status_order
         7         33 ----> if not set -q untracked[1]...
         6          6 -----> not set -q untracked[1]
        20         20 -----> contains -- "$__fish_git_prompt_showuntrackedfiles" yes true 1
        11         11 ----> contains untrackedfiles $__fish_git_prompt_status_order
        13        126 ----> if test true = $inside_worktree...
        15         15 -----> test true = $inside_worktree
         8         81 -----> if test "$informative" = true...
         8          8 ------> test "$informative" = true
         6         16 ------> ...
        10         10 -------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        14         33 ------> if not test "$dirty" = true...
         9          9 -------> not test "$dirty" = true
         5          5 -------> test "$untracked" = true
         5          5 -------> test "$dirty" = true
         7         16 ------> if contains -- "$__fish_git_prompt_showstashstate" yes true 1...
         9          9 -------> contains -- "$__fish_git_prompt_showstashstate" yes true 1
         5         17 -----> if set -q __fish_git_prompt_showupstream...
         5          5 ------> set -q __fish_git_prompt_showupstream
         7          7 ------> contains -- "$__fish_git_prompt_show_informative_status" yes true 1
        21         21 ----> set -l branch_color $___fish_git_prompt_color_branch
        19         19 ----> set -l branch_done $___fish_git_prompt_color_branch_done
         9         17 ----> if contains -- "$__fish_git_prompt_showcolorhints" yes true 1...
         8          8 -----> contains -- "$__fish_git_prompt_showcolorhints" yes true 1
         8          8 ----> set -l flags ""
        30         82 ----> for i in $__fish_git_prompt_status_order...
         5         14 -----> if test -n "$$i"...
         9          9 ------> test -n "$$i"
         4         10 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         3          9 -----> if test -n "$$i"...
         6          6 ------> test -n "$$i"
         4         11 -----> if test -n "$$i"...
         7          7 ------> test -n "$$i"
         3          8 -----> if test -n "$$i"...
         5          5 ------> test -n "$$i"
       268        297 ----> set branch (string replace refs/heads/ '' -- $branch)
        29         29 -----> string replace refs/heads/ '' -- $branch
       192        256 ----> set branch (string replace -ra '[[:cntrl:]]' '' -- $branch)
        64         64 -----> string replace -ra '[[:cntrl:]]' '' -- $branch
       142        194 ----> set operation (string replace -ra '[[:cntrl:]]' '' -- $operation)
        52         52 -----> string replace -ra '[[:cntrl:]]' '' -- $operation
        12         56 ----> if string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"...
        44         44 -----> string match -qr '^\d+$' "$__fish_git_prompt_shorten_branch_len"
         8         61 ----> if test -n "$branch"...
        14         14 -----> test -n "$branch"
        13         13 -----> set branch "$branch_color$branch$branch_done"
         6         26 -----> if test -z "$dirtystate$untrackedfiles$stagedstate"...
         9          9 ------> test -z "$dirtystate$untrackedfiles$stagedstate"
        11         11 ------> test -n "$___fish_git_prompt_char_cleanstate"
         3          9 ----> if test -n "$bare_prefix"...
         6          6 -----> test -n "$bare_prefix"
         2          6 ----> if test -n "$operation"...
         4          4 -----> test -n "$operation"
         1          6 ----> if test -n "$upstream"...
         5          5 -----> test -n "$upstream"
         2          9 ----> if test -n "$flags$bare_prefix$upstream"...
         7          7 -----> test -n "$flags$bare_prefix$upstream"
        10         10 ----> set -l format $argv[1]
         5         17 ----> if test -z "$format"...
         5          5 -----> test -z "$format"
         7          7 -----> set format " (%s)"
        80         80 ----> printf "%s$format%s" "$___fish_git_prompt_color_prefix" "$___fish_git_prompt_color_prefix_done$bare_prefix$branch$flags$operation$upstream$informative_status$___fish_git_prompt_color_suffix" "$___fish_git_prompt_color_suffix_done"
        37       2035 > fish_title
        13         13 -> set -l ssh
         4          4 -> set -q SSH_TTY
        25       1981 -> if set -q argv[1]...
         6          6 --> set -q argv[1]
       125        136 --> set -l command (status current-command)
        11         11 ---> status current-command
         9         31 --> if test "$command" = fish...
        15         15 ---> test "$command" = fish
         7          7 ---> set command
       279       1783 --> echo -- $ssh (string sub -l 20 -- $command) (prompt_pwd -d 1 -D 1)
        15         15 ---> string sub -l 20 -- $command
        48       1489 ---> prompt_pwd -d 1 -D 1
        14         14 ----> set -l options h/help d/dir-length= D/full-length-dirs=
        43         43 ----> argparse -n prompt_pwd $options -- $argv
         5         11 ----> if set -q _flag_help...
         6          6 -----> set -q _flag_help
         5          5 ----> set -q argv[1]
         9          9 ----> set argv $PWD
         4          4 ----> set -ql _flag_d
        14         14 ----> set -l fish_prompt_pwd_dir_length $_flag_d
         4          4 ----> set -q fish_prompt_pwd_dir_length
         6          6 ----> set -l fulldirs 0
         3          3 ----> set -ql _flag_D
         7          7 ----> set -l fish_prompt_pwd_full_dirs $_flag_D
         3          3 ----> set -q fish_prompt_pwd_full_dirs
        21       1318 ----> for path in $argv...
       146        617 -----> set -l tmp (__fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' '')
       249        471 ------> __fish_unexpand_tilde $path | string replace -ra '[[:cntrl:]]' ''
       135        161 -------> set -l realhome (string escape --style=regex -- ~)
        26         26 --------> string escape --style=regex -- ~
        61         61 -------> string replace -r -- "^$realhome(\$|/)" '~$1' $argv
        21        680 -----> if test "$fish_prompt_pwd_dir_length" -eq 0...
        22         22 ------> test "$fish_prompt_pwd_dir_length" -eq 0
         8          8 ------> set -l full
        15        322 ------> if test $fish_prompt_pwd_full_dirs -gt 0...
         9          9 -------> test $fish_prompt_pwd_full_dirs -gt 0
       121        274 -------> set -l all (string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp)
       119        153 --------> string split -m (math $fish_prompt_pwd_full_dirs - 1) -r / $tmp
        34         34 ---------> math $fish_prompt_pwd_full_dirs - 1
        16         16 -------> set tmp $all[1]
         8          8 -------> set full $all[2..]
       252        307 ------> string join / -- (string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp) $full
        55         55 -------> string replace -ar -- '(\.?[^/]{'"$fish_prompt_pwd_dir_length"'})[^/]*/' '$1/' $tmp
       451      28176 > fish_clipboard_copy
        28         28 -> function fish_clipboard_copy...
        26         26 -> set -l cmdline
        36       3537 -> if isatty stdin...
       262        428 --> isatty stdin
        26         26 ---> function isatty -d "Tests if a file descriptor is a tty"...
        19         19 ---> set -l options h/help
        29         29 ---> argparse -n isatty $options -- $argv
         5         10 ---> if set -q _flag_help...
         5          5 ----> set -q _flag_help
         3          8 ---> if set -q argv[2]...
         5          5 ----> set -q argv[2]
         8          8 ---> set -l fd
        12         17 ---> switch "$argv"...
         5          5 ----> set fd 0
        49         49 ---> test -t "$fd"
       400       2023 --> set cmdline (commandline --current-selection | fish_indent --only-indent | string collect)
      1623       1623 ---> commandline --current-selection | fish_indent --only-indent | string collect
        29         29 --> test -n "$cmdline"
       180       1021 --> set cmdline (commandline | fish_indent --only-indent | string collect)
       841        841 ---> commandline | fish_indent --only-indent | string collect
        29        654 -> if type -q pbcopy...
       495        495 --> type -q pbcopy
        19         19 --> set -q WAYLAND_DISPLAY
         4          4 --> set -q DISPLAY
         3          3 --> set -q DISPLAY
       104        104 --> type -q clip.exe
        40      23480 -> if type -q base64...
       450        450 --> type -q base64
        36         36 --> [ "$TERM" != dumb ]
         4        131 --> if not isatty stdout...
        32        127 ---> not isatty stdout
        12         12 ----> set -l options h/help
        20         20 ----> argparse -n isatty $options -- $argv
         5          9 ----> if set -q _flag_help...
         4          4 -----> set -q _flag_help
         4          8 ----> if set -q argv[2]...
         4          4 -----> set -q argv[2]
         4          4 ----> set -l fd
        14         18 ----> switch "$argv"...
         4          4 -----> set fd 1
        24         24 ----> test -t "$fd"
       274      22733 --> set -l encoded (printf %s $cmdline | base64 | string join '')
     22459      22459 ---> printf %s $cmdline | base64 | string join ''
        71         71 --> printf '\e]52;c;%s\a' "$encoded"
        11         19 --> if set -q TMUX...
         8          8 ---> set -q TMUX
