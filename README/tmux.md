# https://github.com/tmux-plugins/tpm
Add new plugin to ~/.tmux.conf with set -g @plugin '...'
Press prefix + I (capital I, as in Install) to fetch the plugin.
You're good to go! The plugin was cloned to ~/.tmux/plugins/ dir and sourced.

# https://github.com/tmux-plugins/tmux-yank
Add plugin to the list of TPM plugins in .tmux.conf:
set -g @plugin 'tmux-plugins/tmux-yank'

Use prefix–I install tmux-yank. You should now be able to tmux-yank immediately.
When you want to update tmux-yank use prefix–U.


https://jamesoff.net/2017/08/26/tmux-configuration.html

git clone https://github.com/tmux-plugins/tpm /home/$USER/.tmux/plugins/tpm

# This one is obsolete
# curl -fLo /home/fm/.tmux/plugins/tpm --create-dirs http://github.com/tmux-plugins/tpm
