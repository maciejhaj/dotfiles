###################################################################################
# COOL COMMANDS 
###################################################################################

eval eg.
    c="ls -s | sort -n"
    $c <- this wont work, as bash wouldnt process pipe symbol
    eval $c <- it has to be executed that way

    opts="a b \$1 \$2 "
    set -- "$opts"       <- this will not work
    eval set -- $opts    <- this will work
    echo options are: $@


${variable//?/\#}
    fills variable with #, good thing for decorator

mkdir -p ~/Temp/site2/{site2/{html,logs,images},site{3..6},site7}

dirs -v

alias -s {yml,yaml}=vim
    if you type any file name ending with yml/yaml in the command line, zsh opens that file using
    vim:
    $ playbook.yml

ls -d .*/

Quotation
    echo text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER
	text /home/me/ls-output.txt a b foo 4 me
    echo "text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER"
	text ~/*.txt {a,b} foo 4 me
    echo 'text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER'
	text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER

glances # htop alternative

transfer # transfer huge files though internet

# inserting between two expressions
https://stackoverflow.com/questions/42597384/extract-lines-between-two-expressions-of-a-file-inside-bash-script-using-regexp
sed "/^INSTALL SESSION .* started .* $server ##/,/^INSTALL SESSION .* ended .* $server ##/!d" file
sed -r '/^<noscript>.*/,/.*<\/noscript>$/!d'

# paste services
https://unix.stackexchange.com/questions/108493/easy-way-to-paste-command-line-output-to-paste-bin-services

# Check progress of an ongoing dd operation (Run this command from another shell):
kill -USR1 $(pgrep dd)

${2:-${1}}
${var:-default} evaluates to the value of $var, unless $var isn't set in which case it evaluates to the text "default". $1, $2, et al are the command-line arguments to your program (or function). Putting the two together it means to return $2 if there were two arguments passed, otherwise return $1.
${var+something} expands to "something" unless $var is unset. It is clearly documented in all shells but hard to find in the bash documentation as you need to pay attention to this sentence:
    When not performing substring expansion, using the forms documented below, bash tests for a parameter that is unset or null. Omitting the colon results in a test only for a parameter that is unset.
###################################################################################
# Hackery stuff
###################################################################################
https://www.cyberciti.biz/faq/ping-test-a-specific-port-of-machine-ip-address-using-linux-unix/
https://en.wikipedia.org/wiki/Ntop
https://github.com/aanarchyy/bully
https://github.com/v1s1t0r1sh3r3/airgeddon/wiki/Optional%20Tools
https://www.dipol.com.pl/poradnik_instalatora_wlan_bib86.htm
http://www.cdr.pl/k259,karty-radiowe-mpci-usb-karty-2-4-ghz-karty-usb.html
https://www.amazon.co.uk/gp/product/B008200LHW/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1
https://www.amazon.co.uk/Network-AWUS036NHA-802-11b-wireless-adapter/dp/B004Y6MIXS/ref=sr_1_1?ie=UTF8&qid=1470582655&sr=8-1&keywords=alfa+wifi
https://scotthelme.co.uk/wifi-wardriving/
https://resources.infosecinstitute.com/antenna-theory-wardriving-penetration-testing/
https://yagi.pl/anteny-wewnetrzne
https://askubuntu.com/questions/55868/installing-broadcom-wireless-drivers
https://github.com/aircrack-ng/aircrack-ng
https://www.youtube.com/watch?v=v7L-NXpYQ3M&list=PLBf0hzazHTGNEv_hKWNYgB6Bw05xmhGLy

###################################################################################
# Crypto currency
###################################################################################
https://kryptopan.pl/jak-zabezpieczyc-kryptowaluty-bitcoin/
