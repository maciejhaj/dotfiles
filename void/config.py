#
#               _       _                                     
#    __ _ _   _| |_ ___| |__  _ __ _____      _____  ___ _ __ 
#   / _` | | | | __/ _ \ '_ \| '__/ _ \ \ /\ / / __|/ _ \ '__|
#  | (_| | |_| | ||  __/ |_) | | | (_) \ V  V /\__ \  __/ |   
#   \__, |\__,_|\__\___|_.__/|_|  \___/ \_/\_/ |___/\___|_|   
#      |_|   
#

c.auto_save.session=True
# Uncomment this to still load settings configured via autoconfig.yml
#config.load_autoconfig()

# Set custom User Agent
#config.set('content.headers.user_agent', 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0')

# Enable Javascript
# config.set('content.javascript.enabled', True, 'file://*')
# config.set('content.javascript.enabled', True, 'chrome://*/*')
# config.set('content.javascript.enabled', True, 'qute://*/*')

# Custom Adblock list file
#c.content.host_blocking.lists.append( str(config.configdir) + "/blockedHosts")
config.set('url.start_pages', 'https://start.duckduckgo.com/?kae=d&k5=2&kp=-2&kaj=m&kao=-1&kav=1&kaq=-1&kam=osm&kap=-1&kak=-1&kax=-1&kay=b&kw=n&ks=n&ko=1&kx=5f819d&kaa=aaaaaa&kj=1d1f30&k8=5f819d&kt=p&k9=aaaaaa&k7=1d1f30')
config.set('url.default_page', 'https://start.duckduckgo.com/?kae=d&k5=2&kp=-2&kaj=m&kao=-1&kav=1&kaq=-1&kam=osm&kap=-1&kak=-1&kax=-1&kay=b&kw=n&ks=n&ko=1&kx=5f819d&kaa=aaaaaa&kj=1d1f30&k8=5f819d&kt=p&k9=aaaaaa&k7=1d1f30')
config.set('url.searchengines', {"DEFAULT": 'https://start.duckduckgo.com/?q={}&kae=d&k5=2&kp=-2&kaj=m&kao=-1&kav=1&kaq=-1&kam=osm&kap=-1&kak=-1&kax=-1&kay=b&kw=n&ks=n&ko=1&kx=5f819d&kaa=aaaaaa&kj=1d1f30&k8=5f819d&kt=p&k9=aaaaaa&k7=1d1f30'})

# Custom CSS
# c.content.user_stylesheets = [ 'css/main.css' ]
config.set('url.searchengines',
    {"DEFAULT":"https://duckduckgo.com/?q={}",
    "yt":"https://www.youtube.com/results?search_query={}",
    "g":"https://www.google.com/search?hl=pl&q={}",
    "ap":"https://www.diki.pl/slownik-angielskiego?q={}",
    "ud":"https://www.urbandictionary.com/define.php?term={}",
    "jp":"https://sjp.pl/{}",
    "pb":"https://thepiratebay.org/search/{}/0/99/0",
    "kat":"https://kickasstorrents.to/usearch/{}/",
    "yts":"https://yts.am/browse-movies/{}/all/all/0/latest",
    "fw":"https://www.filmweb.pl/search?q={}",
    "imdb":"https://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=all",
    "d":"https://www.discogs.com/search/?q={}&type=all",
    "j":"https://www.juno.co.uk/search/?q[all][0]={}&hide_forthcoming=0&show_out_of_stock=1&media_type=vinyl&solrorder=date_down",
    "cpp":"http://www.cplusplus.com/search.do?q={}",
    "cppr":"https://en.cppreference.com/mwiki/index.php?title=Special%3ASearch&search={}&button=",
    "sl":"http://slant.co/search?query={}",
    "alter":"https://alternativeto.net/browse/search?q={}" })

# Disable case sensitivity for searching
config.set('search.ignore_case', 'always')

# Confirm exit when downloading files
c.confirm_quit = ['downloads']
# Change start/default pages + search engine

#
# Tab settings
config.set('tabs.padding', {"top": 1, "bottom": 2, "left": 5, "right": 5})
config.set('tabs.indicator.width', 0)
config.set('tabs.favicons.scale', 1.2)

#c.content.host_blocking.enabled=True
#c.content.host_blocking.lists = [
#    "https://easylist-downloads.adblockplus.org/antiadblockfilters.txt",
#    "https://alleblock.pl/alleblock/alleblock.txt",
#    "https://easylist-downloads.adblockplus.org/easyprivacy.txt",
#    "https://easylist-downloads.adblockplus.org/fanboy-social.txt",
#    "https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt",
#    "https://easylist-downloads.adblockplus.org/easylistpolish+easylist.txt",
#    "https://raw.githubusercontent.com/azet12/KAD/master/KAD.txt",
#    "https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt",
#    "https://raw.githubusercontent.com/MajkiIT/polish-ads-filter/master/polish-adblock-filters/adblock.txt"]
    #"https://raw.githubusercontent.com/olegwukr/polish-privacy-filters/master/adblock.txt"]
    #"https://raw.githubusercontent.com/MajkiIT/polish-ads-filter/master/adblock_social_filters/adblock_social_list.txt"]
#"https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"

# Fonts
c.fonts.monospace = '"DejaVu Sans Mono"'
c.fonts.completion.category = '10pt DejaVu Sans Mono'
c.fonts.completion.entry = '10pt DejaVu Sans Mono'
c.fonts.tabs = '10pt DejaVu Sans Mono'
c.fonts.statusbar = '10pt DejaVu Sans Mono'
c.fonts.downloads = '11pt DejaVu Sans Mono'
c.fonts.hints = 'bold 10pt DejaVu Sans Mono'
c.fonts.debug_console = '10pt DejaVu Sans Mono'

# Color Scheme
black =         "#1d1f30"
white =         "#aaaaaa"
red =           "#b54848"
green =         "#7c933f"
yellow =        "#af774f"
blue =          "#5f819d"
magenta =       "#915b8d"
cyan =          "#5e8d87"

background =    "#1d1f30"
backgroundAlt = "#2a3145"
accent =        "#5f819d"

# 
#     # Set colors from color scheme
#     c.colors.completion.category.bg = background
#     c.colors.completion.category.border.bottom = background
#     c.colors.completion.category.border.top = background
#     c.colors.completion.category.fg = accent
#     c.colors.completion.fg = white
#     c.colors.completion.item.selected.bg = backgroundAlt
#     c.colors.completion.item.selected.border.bottom = backgroundAlt
#     c.colors.completion.item.selected.border.top = backgroundAlt
#     c.colors.completion.item.selected.fg = accent
#     c.colors.completion.match.fg = white
#     c.colors.completion.odd.bg = background 
#     c.colors.completion.even.bg = background
#     c.colors.completion.scrollbar.bg = background
#     c.colors.completion.scrollbar.fg = accent
#     c.colors.downloads.bar.bg = background
#     c.colors.downloads.error.fg = red
#     c.colors.downloads.start.bg = background
#     c.colors.downloads.start.fg = white
#     c.colors.downloads.stop.bg = background
#     c.colors.downloads.stop.fg = accent
#     c.colors.hints.bg = yellow
#     c.colors.hints.fg = background
#     c.colors.hints.match.fg = yellow
#     c.colors.keyhint.bg = background
#     c.colors.keyhint.fg = accent
#     c.colors.keyhint.suffix.fg = accent
#     c.colors.messages.error.fg = accent
#     c.colors.messages.error.bg = background
#     c.colors.messages.error.border = background
#     c.colors.messages.info.bg = background
#     c.colors.messages.info.border = background
#     c.colors.messages.info.fg = accent
#     c.colors.messages.warning.bg = red
#     c.colors.messages.warning.border = red
#     c.colors.messages.warning.fg = background
#     c.colors.prompts.bg = background
#     c.colors.prompts.border = background
#     c.colors.prompts.fg = white
#     c.colors.prompts.selected.bg = accent
#     c.colors.statusbar.caret.bg = accent
#     c.colors.statusbar.caret.fg = background
#     c.colors.statusbar.caret.selection.bg = accent
#     c.colors.statusbar.caret.selection.fg = background
#     c.colors.statusbar.command.bg = backgroundAlt
#     c.colors.statusbar.command.fg = accent
#     c.colors.statusbar.command.private.bg = backgroundAlt
#     c.colors.statusbar.command.private.fg = accent
#     c.colors.statusbar.insert.bg = backgroundAlt
#     c.colors.statusbar.insert.fg = accent
#     c.colors.statusbar.normal.bg = background
#     c.colors.statusbar.normal.fg = accent
#     c.colors.statusbar.passthrough.bg = accent
#     c.colors.statusbar.passthrough.fg = background
#     c.colors.statusbar.private.bg = background
#     c.colors.statusbar.private.fg = accent
#     c.colors.statusbar.progress.bg = accent
#     c.colors.statusbar.url.error.fg = red
#     c.colors.statusbar.url.fg = background
#     c.colors.statusbar.url.hover.fg = accent
#     c.colors.statusbar.url.success.http.fg = accent
#     c.colors.statusbar.url.success.https.fg = accent
#     c.colors.statusbar.url.warn.fg = red
#     c.colors.tabs.bar.bg = background
#     c.colors.tabs.even.bg = background
#     c.colors.tabs.even.fg = accent
#     c.colors.tabs.indicator.error = background
#     c.colors.tabs.indicator.start = accent
#     c.colors.tabs.indicator.stop = background
#     c.colors.tabs.odd.bg = background
#     c.colors.tabs.odd.fg = accent
#     c.colors.tabs.selected.even.bg = backgroundAlt
#     c.colors.tabs.selected.even.fg = accent
#     c.colors.tabs.selected.odd.bg = backgroundAlt
#     c.colors.tabs.selected.odd.fg = accent
#     #c.colors.webpage.bg = background
