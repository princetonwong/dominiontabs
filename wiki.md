usage: dominion_dividers [-h] [--outfile OUTFILE] [--papersize PAPERSIZE]
                         [--language {fr,en_us,es,nl_nl,it,cs,de}]
                         [--font-dir FONT_DIR]
                         [--orientation {horizontal,vertical}] [--size SIZE]
                         [--sleeved] [--order {expansion,global,colour,cost}]
                         [--front {card,rules,blank}]
                         [--back {card,rules,blank,none}] [--count] [--types]
                         [--tab-side {left,right,left-alternate,right-alternate,left-flip,right-flip,centre,full}]
                         [--tab-number TAB_NUMBER] [--tab-serpentine]
                         [--tab-name-align {left,right,centre,edge,center}]
                         [--tabwidth TABWIDTH] [--cost {tab,body-top,hide}]
                         [--set-icon {tab,body-top,hide}] [--no-tab-artwork]
                         [--tab-artwork-opacity TAB_ARTWORK_OPACITY]
                         [--tab-artwork-resolution TAB_ARTWORK_RESOLUTION]
                         [--use-text-set-icon] [--use-set-icon]
                         [--expansion-reset-tabs] [--expansion-dividers]
                         [--centre-expansion-dividers]
                         [--full-expansion-dividers]
                         [--expansion-dividers-long-name]
                         [--expansions [EXPANSIONS ...]] [--fan [FAN ...]]
                         [--exclude-expansions [EXCLUDED ...]]
                         [--edition {1,2,latest,upgrade,removed,all}]
                         [--upgrade-with-expansion]
                         [--base-cards-with-expansion] [--group-special]
                         [--group-kingdom] [--group-global [GROUP_GLOBAL ...]]
                         [--no-trash] [--curse10] [--start-decks]
                         [--include-blanks INCLUDE_BLANKS] [--exclude-events]
                         [--exclude-landmarks] [--exclude-projects]
                         [--exclude-ways] [--exclude-traits]
                         [--only-type-any [ONLY_TYPE_ANY ...]]
                         [--only-type-all [ONLY_TYPE_ALL ...]] [--wrapper]
                         [--pull-tab] [--tent] [--head {tab,strap,cover,none}]
                         [--tail {tab,strap,cover,folder,none}]
                         [--head-facing {front,back}]
                         [--tail-facing {front,back}]
                         [--head-text {card,rules,blank,front,back}]
                         [--tail-text {card,rules,blank,front,back}]
                         [--head-height HEAD_HEIGHT]
                         [--tail-height TAIL_HEIGHT]
                         [--spine {name,types,tab,blank}]
                         [--thickness THICKNESS] [--sleeved-thick]
                         [--sleeved-thin] [--notch]
                         [--notch-length NOTCH_LENGTH]
                         [--notch-height NOTCH_HEIGHT] [--minmargin MINMARGIN]
                         [--cropmarks] [--linewidth LINEWIDTH]
                         [--front-offset FRONT_OFFSET]
                         [--front-offset-height FRONT_OFFSET_HEIGHT]
                         [--back-offset BACK_OFFSET]
                         [--back-offset-height BACK_OFFSET_HEIGHT]
                         [--vertical-gap VERTICAL_GAP]
                         [--horizontal-gap HORIZONTAL_GAP] [--no-page-footer]
                         [--num-pages NUM_PAGES] [--tabs-only] [--black-tabs]
                         [--linetype {line,dot,cropmarks,line-cropmarks,dot-cropmarks}]
                         [--cropmarkLength CROPMARKLENGTH]
                         [--cropmarkSpacing CROPMARKSPACING]
                         [--rotate {0,90,180,270}]
                         [--label {8867,5167,5267,5667,5967,8167,8667,8927,15267,15667,18167,18667,28667,48267,48467,48867,95667,L4732,L7632,L4736,L6113,94211,H4201}]
                         [--info] [--info-all] [--preview]
                         [--preview-resolution PREVIEW_RESOLUTION]
                         [--cardlist CARDLIST] [-c C] [-w W]
                         [--log-level {TRACE,DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Generate Dominion Dividers

optional arguments:
  -h, --help            show this help message and exit

Basic Divider Options:
  Basic choices for the dividers.

  --outfile OUTFILE, -o OUTFILE
                        The output file name. (default: dominion_dividers.pdf)
  --papersize PAPERSIZE
                        The size of paper to use; '<%f>x<%f>' (size in cm), or
                        'A4', or 'LETTER'. If not specified, it will default
                        to system defaults, and if the system defaults are not
                        found, then to 'LETTER'. (default: None)
  --language {fr,en_us,es,nl_nl,it,cs,de}, -l {fr,en_us,es,nl_nl,it,cs,de}
                        Language of divider text. (default: en_us)
  --font-dir FONT_DIR   A directory path to scan for font files, preferring
                        them over fonts in the domdiv package (default: None)
  --orientation {horizontal,vertical}
                        Either horizontal or vertical divider orientation.
                        (default: horizontal)
  --size SIZE           Dimensions of the cards to use with the dividers
                        '<%f>x<%f>' (size in cm), or 'normal' = '9.1x5.9', or
                        'sleeved' = '9.4x6.15'. (default: normal)
  --sleeved             Same as --size=sleeved. (default: False)
  --order {expansion,global,colour,cost}
                        Sort order for the dividers: 'global' will sort by
                        card name; 'expansion' will sort by expansion, then
                        card name; 'colour' will sort by card type, then card
                        name; 'cost' will sort by expansion, then card cost,
                        then name. (default: expansion)

Divider Body:
  Changes what is displayed on the body of the dividers.

  --front {card,rules,blank}
                        Text to print on the front of the divider; 'card' will
                        print the text from the game card; 'rules' will print
                        additional rules for the game card; 'blank' will not
                        print text on the divider. (default: card)
  --back {card,rules,blank,none}
                        Text to print on the back of the divider; 'card' will
                        print the text from the game card; 'rules' will print
                        additional rules for the game card; 'blank' will not
                        print text on the divider; 'none' will prevent the
                        back pages from printing. (default: rules)
  --count               Display the card count on the body of card dividers
                        and the randomizer count on the body of expansion
                        dividers. (default: False)
  --types               Display card type on the body of the divider.
                        (default: False)

Divider Tab:
  Changes what is displayed on on the Divider Tab.

  --tab-side {left,right,left-alternate,right-alternate,left-flip,right-flip,centre,full}
                        Alignment of tab; 'left'/'right'/'centre' sets the
                        starting side of the tabs; 'full' will force all label
                        tabs to be full width of the divider; sets
                        --tab_number 1 'left-alternate' will start on the left
                        and then toggle between left and right for the tabs,
                        sets --tab_number 2; 'right-alternate' will start on
                        the right and then toggle between right and left for
                        the tabs, sets --tab_number 2; 'left-flip' like left-
                        alternate, but the right will be flipped front/back
                        with tab on left, sets --tab_number 2; 'right-flip'
                        like right-alternate, but the left will be flipped
                        front/back with tab on right, sets --tab_number 2;
                        (default: right-alternate)
  --tab-number TAB_NUMBER
                        The number of tabs. When set to 1, all tabs are on the
                        same side (specified by --tab_side). When set to 2,
                        tabs will alternate between left and right. (starting
                        side specified by --tab_side). When set > 2, the first
                        tab will be on left/right side specified by
                        --tab_side, then the rest of the tabs will be evenly
                        spaced until ending on the opposite side. Then the
                        cycle repeats. May be overriden by some options of
                        --tab_side. (default: 2)
  --tab-serpentine      Affects the order of tabs. When not selected, tabs
                        will progress from the starting side (left/right) to
                        the opposite side (right/left), and then repeat (e.g.,
                        left to right, left to right, etc.). When selected,
                        the order is changed to smoothly alternate between the
                        two sides (e.g., left to right, to left, to right,
                        etc.) Only valid if --tab_number > 2. (default: False)
  --tab-name-align {left,right,centre,edge,center}
                        Alignment of text on the tab; The 'edge' option will
                        align the card name to the outside edge of the tab, so
                        that when using tabs on alternating sides, the name is
                        less likely to be hidden by the tab in front (edge
                        will revert to left when tab_side is full since there
                        is no edge in that case). (default: left)
  --tabwidth TABWIDTH   Width in cm of stick-up tab (ignored if --tab_side is
                        'full' or --tabs_only is used). (default: 4.0)
  --cost {tab,body-top,hide}
                        Where to display the card cost; may be set to 'hide'
                        to indicate it should not be displayed, or given
                        multiple times to show it in multiple places. (If not
                        given, will default to 'tab'.) (default: None)
  --set-icon {tab,body-top,hide}
                        Where to display the set icon; may be set to 'hide' to
                        indicate it should not be displayed, or given multiple
                        times to show it in multiple places. (If not given,
                        will default to 'tab'.) (default: None)
  --no-tab-artwork      Don't show background artwork on tabs. (default:
                        False)
  --tab-artwork-opacity TAB_ARTWORK_OPACITY
                        Multiply opacity of tab background art by this value;
                        can be used to make text show up clearer on dark
                        backrounds, particularly on printers that output
                        darker than average (default: 1.0)
  --tab-artwork-resolution TAB_ARTWORK_RESOLUTION
                        Limit the DPI resolution of tab background art. If
                        nonzero, any higher-resolution images will be resized
                        to reduce output file size. (default: 0)
  --use-text-set-icon   Use text/letters to represent a card's set instead of
                        the set icon. (default: False)
  --use-set-icon        Use set icon instead of a card icon. Applies to Promo
                        cards. (default: False)
  --expansion-reset-tabs
                        When set, the tabs are restarted (left/right) at the
                        beginning of each expansion. If not set, the tab
                        pattern will continue from one expansion to the next.
                        (default: False)

Expansion Dividers:
  Adding separator dividers for each expansion.

  --expansion-dividers  Add dividers describing each expansion set. A list of
                        cards in the expansion will be shown on the front of
                        the divider. (default: False)
  --centre-expansion-dividers
                        Centre the tabs on expansion dividers (same width as
                        dividers.) (default: False)
  --full-expansion-dividers
                        Full width expansion dividers. (default: False)
  --expansion-dividers-long-name
                        Use the long name with edition information on the
                        expansion divider tab. Without this, the shorter
                        expansion name is used on the expansion divider tab.
                        (default: False)

Divider Selection:
  What expansions are used, and grouping of dividers.

  --expansions [EXPANSIONS ...], --expansion [EXPANSIONS ...]
                        Limit dividers to only the specified expansions. If no
                        limits are set, then the latest expansions are
                        included. Expansion names can also be given in the
                        language specified by the --language parameter. Any
                        expansion with a space in the name must be enclosed in
                        double quotes. This may be called multiple times.
                        Values are not case sensitive. Wildcards may be used:
                        '*' any number of characters, '?' matches any single
                        character, '[seq]' matches any character in seq, and
                        '[!seq]' matches any character not in seq. For
                        example, 'dominion*' will match all expansions that
                        start with 'dominion'. Choices available in all
                        languages include: adventures, alchemy, allies, base,
                        cornucopia1stEdition, cornucopia1stEditionRemoved,
                        cornucopia2ndEditionUpgrade,
                        cornucopiaAndGuilds2ndEdition, dark ages,
                        dominion1stEdition, dominion1stEditionRemoved,
                        dominion2ndEdition, dominion2ndEditionUpgrade,
                        empires, extras, guilds-bigbox2-de, guilds1stEdition,
                        guilds1stEditionRemoved, guilds2ndEditionUpgrade,
                        hinterlands1stEdition, hinterlands1stEditionRemoved,
                        hinterlands2ndEdition, hinterlands2ndEditionUpgrade,
                        intrigue1stEdition, intrigue1stEditionRemoved,
                        intrigue2ndEdition, intrigue2ndEditionUpgrade,
                        menagerie, nocturne, plunder, promo, promo-bigbox2-de,
                        prosperity1stEdition, prosperity1stEditionRemoved,
                        prosperity2ndEdition, prosperity2ndEditionUpgrade,
                        renaissance, risingSun, seaside1stEdition,
                        seaside1stEditionRemoved, seaside2ndEdition,
                        seaside2ndEditionUpgrade (default: None)
  --fan [FAN ...]       Add dividers from the specified fan made expansions.
                        If this option is not used, no fan expansions will be
                        included. Fan made expansion names can also be given
                        in the language specified by the --language parameter.
                        Any fan expansion with a space in the name must be
                        enclosed in double quotes. This may be called multiple
                        times. Values are not case sensitive. Wildcards may be
                        used: '*' any number of characters, '?' matches any
                        single character, '[seq]' matches any character in
                        seq, and '[!seq]' matches any character not in seq.
                        Choices available in all languages include: animals
                        (default: None)
  --exclude-expansions [EXCLUDED ...], --exclude-expansion [EXCLUDED ...]
                        Limit dividers to not include the specified
                        expansions. Useful if you want all the expansions,
                        except for one or two. If an expansion is explicitly
                        specified with both '--expansion' and '--exclude-
                        expansion', then '--exclude-expansion' wins, and the
                        expansion is NOT included. Expansion names can also be
                        given in the language specified by the --language
                        parameter. Any expansion with a space in the name must
                        be enclosed in double quotes. This may be called
                        multiple times. Values are not case sensitive.
                        Wildcards may be used. See the help for '--expansion'
                        for details on wildcards. May be the name of an
                        official expansion or fan expansion - see the help for
                        --expansion and --fan for a list of possible names.
                        (default: None)
  --edition {1,2,latest,upgrade,removed,all}
                        Editions to include: '1' is for all 1st Editions; '2'
                        is for all 2nd Editions; 'upgrade' is for all upgrade
                        cards for each expansion; 'removed' is for all removed
                        cards for each expansion; 'latest' is for the latest
                        edition for each expansion; 'all' is for all editions
                        of expansions, upgrade cards, and removed cards; This
                        can be combined with other options to refine the
                        expansions to include in the output. (default: all)
                        (default: None)
  --upgrade-with-expansion
                        Include any new edition upgrade cards with the
                        expansion being upgraded. (default: False)
  --base-cards-with-expansion
                        Print the base cards as part of the expansion (i.e., a
                        divider for 'Silver' will be printed as both a
                        'Dominion' card and as an 'Intrigue 1st Edition'
                        card). If this option is not given, all base cards are
                        placed in their own 'Base' expansion. (default: False)
  --group-special, --special-card-groups
                        Group cards that generally are used together (e.g.,
                        Shelters, Tournament and Prizes, Urchin/Mercenary,
                        etc.). (default: False)
  --group-kingdom       Group cards that have randomizers into the expansion,
                        and those that don't have randomizers into the
                        expansion's 'Extra' section. (default: False)
  --group-global [GROUP_GLOBAL ...]
                        Group all cards of the specified types across all
                        expansions into one 'Extras' divider. This may be
                        called multiple times. Values are not case sensitive.
                        Choices available include: allies, ally, boon, boons,
                        event, events, hex, hexes, landmark, landmarks,
                        project, projects, prophecies, prophecy, state,
                        states, trait, traits, way, ways (default: None)
  --no-trash            Exclude Trash from cards. (default: False)
  --curse10             Package Curse cards into groups of ten cards.
                        (default: False)
  --start-decks         Include four start decks with the Base cards.
                        (default: False)
  --include-blanks INCLUDE_BLANKS
                        Number of blank dividers to include. (default: 0)
  --exclude-events      Group all 'Event' cards across all expansions into one
                        divider.Same as '--group-global Events' (default:
                        False)
  --exclude-landmarks   Group all 'Landmark' cards across all expansions into
                        one divider.Same as '--group-global landmarks'
                        (default: False)
  --exclude-projects    Group all 'Project' cards across all expansions into
                        one divider.Same as '--group-global projects'
                        (default: False)
  --exclude-ways        Group all 'Way' cards across all expansions into one
                        divider.Same as '--group-global ways' (default: False)
  --exclude-traits      Group all 'Trait' cards across all expansions into one
                        divider.Same as '--group-global traits' (default:
                        False)
  --only-type-any [ONLY_TYPE_ANY ...], --only-type [ONLY_TYPE_ANY ...], --type-any [ONLY_TYPE_ANY ...]
                        Limit dividers to only those with the specified types.
                        A divider is kept if ANY of the provided types are
                        associated with the divider. Default is all types are
                        included. Any type with a space in the name must be
                        enclosed in double quotes. Values are not case
                        sensitive. Choices available in all languages include:
                        action, allies, ally, artifact, attack, augur, blank,
                        boon, boons, castle, clash, command, curse, doom,
                        duration, event, events, expansion, fate, fort,
                        gathering, heirloom, hex, hexes, landmark, landmarks,
                        liaison, loot, looter, night, odyssey, omen, prize,
                        prizes, project, projects, prophecies, prophecy,
                        reaction, reserve, reward, rewards, ruins, shadow,
                        shelter, shelters, spirit, start deck, state, states,
                        townsfolk, trait, traits, trash, traveller, treasure,
                        victory, way, ways, wizard, zombie (default: None)
  --only-type-all [ONLY_TYPE_ALL ...], --type-all [ONLY_TYPE_ALL ...]
                        Limit dividers to only those with the specified types.
                        A divider is kept if ALL of the provided types are
                        associated with the divider. Any type with a space in
                        the name must be enclosed in double quotes. Values are
                        not case sensitive. Choices available in all languages
                        include: action, allies, ally, artifact, attack,
                        augur, blank, boon, boons, castle, clash, command,
                        curse, doom, duration, event, events, expansion, fate,
                        fort, gathering, heirloom, hex, hexes, landmark,
                        landmarks, liaison, loot, looter, night, odyssey,
                        omen, prize, prizes, project, projects, prophecies,
                        prophecy, reaction, reserve, reward, rewards, ruins,
                        shadow, shelter, shelters, spirit, start deck, state,
                        states, townsfolk, trait, traits, trash, traveller,
                        treasure, victory, way, ways, wizard, zombie (default:
                        None)

Card Sleeves/Wrappers:
  Generating dividers that are card sleeves/wrappers.

  --wrapper             Draw sleeves (wrappers) instead of dividers for the
                        cards. Same as --head=strap --tail=folder (default:
                        False)
  --pull-tab            Draw folding pull tabs instead of dividers for the
                        cards. Same as --head=tab --tail=cover (default:
                        False)
  --tent                Draw folding tent covers instead of dividers for the
                        cards. Same as --head=cover --head-facing=back --head-
                        text=back --tail=tab --tail-facing=front (default:
                        False)
  --head {tab,strap,cover,none}
                        Top tab or wrapper type: 'tab' for divider tabs,
                        'strap' for longer folding tabs, 'cover' for
                        matchbook-style folding covers, or 'none' to leave the
                        top edge plain. The folding options create a top spine
                        that you can customize with --spine. (default: tab)
  --tail {tab,strap,cover,folder,none}
                        Bottom tab or wrapper type: 'tab' for a bottom tab
                        banner, 'strap' for a pull tab under the cards,
                        'cover' for a simple back cover, 'folder' to create
                        tab folders, or 'none' to leave the bottom edge plain.
                        (default: none)
  --head-facing {front,back}
                        Text orientation for top tabs and wrappers: 'front'
                        shows the text upright when flat, 'back' shows it
                        upright when folded over. (default: front)
  --tail-facing {front,back}
                        Text orientation for tail wrappers: 'front' shows the
                        text upright when flat, 'back' shows it upright when
                        folded under. (default: back)
  --head-text {card,rules,blank,front,back}
                        Text to print on top cover panels: 'card' shows the
                        text from the game card, 'rules' shows additional
                        rules for the game card, 'blank' leaves the panel
                        blank; 'front' uses the same setting as --front;
                        'back' uses the same setting as --back. (default:
                        blank)
  --tail-text {card,rules,blank,front,back}
                        Text to print on bottom folder panels: 'card' shows
                        the text from the game card, 'rules' shows additional
                        rules for the game card, 'blank' leaves the panel
                        blank; 'front' uses the same setting as --front;
                        'back' uses the same setting as --back. (default:
                        back)
  --head-height HEAD_HEIGHT
                        Height of the top panel in centimeters (a value of 0
                        uses tab height or card height as appropriate).
                        (default: 0.0)
  --tail-height TAIL_HEIGHT
                        Height of the bottom panel in centimeters (a value of
                        0 uses tab height or card height as appropriate).
                        (default: 0.0)
  --spine {name,types,tab,blank}
                        Text to print on the spine of top covers: 'name'
                        prints the card name; 'type' prints the card type;
                        'tab' prints tab text and graphics; 'blank' leaves the
                        spine blank. This is only valid with folding --head
                        options. (default: name)
  --thickness THICKNESS
                        Thickness of a stack of 60 cards (Copper) in
                        centimeters. Typically unsleeved cards are 2.0, thin
                        sleeved cards are 2.4, and thick sleeved cards are
                        3.2. This is only valid with --wrapper or other
                        folding options. (default: 2.0)
  --sleeved-thick       Same as --size=sleeved --thickness 3.2. (default:
                        False)
  --sleeved-thin        Same as --size=sleeved --thickness 2.4. (default:
                        False)
  --notch               Creates thumb notches opposite to the divider tabs,
                        which can make it easier to remove cards from wrappers
                        or stacks. Equivalent to --notch-length=1.5 --notch-
                        height=0.25 (default: False)
  --notch-length NOTCH_LENGTH
                        Sets the length of thumb notches in centimeters.
                        (default: 0.0)
  --notch-height NOTCH_HEIGHT
                        Sets the height of thumb notches in centimeters.
                        (default: 0.0)

Printing:
  Changes how the Dividers are printed.

  --minmargin MINMARGIN
                        Page margin in cm in the form '<%f>x<%f>', left/right
                        x top/bottom). (default: 1x1)
  --cropmarks           Print crop marks on both sides, rather than tab
                        outlines on the front side. (default: False)
  --linewidth LINEWIDTH
                        Width of lines for card outlines and crop marks.
                        (default: 0.1)
  --front-offset FRONT_OFFSET
                        Front page horizontal offset points to shift to the
                        right. Only needed for some printers. (default: 0)
  --front-offset-height FRONT_OFFSET_HEIGHT
                        Front page vertical offset points to shift upward.
                        Only needed for some printers. (default: 0)
  --back-offset BACK_OFFSET
                        Back page horizontal offset points to shift to the
                        right. Only needed for some printers. (default: 0)
  --back-offset-height BACK_OFFSET_HEIGHT
                        Back page vertical offset points to shift upward. Only
                        needed for some printers. (default: 0)
  --vertical-gap VERTICAL_GAP
                        Vertical gap between dividers in centimeters.
                        (default: 0.0)
  --horizontal-gap HORIZONTAL_GAP
                        Horizontal gap between dividers in centimeters.
                        (default: 0.0)
  --no-page-footer      Do not print the expansion name at the bottom of the
                        page. (default: False)
  --num-pages NUM_PAGES
                        Stop generating dividers after this many pages, -1 for
                        all. (default: -1)
  --tabs-only           Draw only the divider tabs and no divider outlines.
                        Used to print the divider tabs on labels. (default:
                        False)
  --black-tabs          In tabs-only mode, draw tabs on black background
                        (default: False)
  --linetype {line,dot,cropmarks,line-cropmarks,dot-cropmarks}
                        The divider outline type. 'line' will print a solid
                        line outlining the divider; 'dot' will print a dot at
                        each corner of the divider; 'cropmarks' will print
                        cropmarks for the divider; 'line-cropmarks' will
                        combine 'line' and 'cropmarks'; 'dot-cropmarks' will
                        combine 'dot' and 'cropmarks' (default: line)
  --cropmarkLength CROPMARKLENGTH
                        Length of actual drawn cropmark in centimeters.
                        (default: 0.2)
  --cropmarkSpacing CROPMARKSPACING
                        Spacing between card and the start of the cropmark in
                        centimeters. (default: 0.1)
  --rotate {0,90,180,270}
                        Divider degrees of rotation relative to the page edge.
                        No optimization will be done on the number of dividers
                        per page. (default: 0)
  --label {8867,5167,5267,5667,5967,8167,8667,8927,15267,15667,18167,18667,28667,48267,48467,48867,95667,L4732,L7632,L4736,L6113,94211,H4201}
                        Use preset label dimentions. Specify a label name.
                        This will override settings that conflict with the
                        preset label settings. (default: None)
  --info                Add a page that has all the options used for the file.
                        (default: False)
  --info-all            Same as --info, but includes pages with all the
                        possible options that can be used. (default: False)
  --preview             Only generate a preview png image of the first page
                        (default: False)
  --preview-resolution PREVIEW_RESOLUTION
                        resolution in DPI to render preview at, for --preview
                        option (default: 150)

Miscellaneous:
  These options are generally not used.

  --cardlist CARDLIST   Path to file that enumerates each card on its own line
                        to be included or excluded. To include a card, add its
                        card name on a line. The name can optionally be
                        preceeded by '+'. To exclude a card, add its card name
                        on a line preseeded by a '-' If any card is included
                        by this method, only cards specified in this file will
                        be printed. (default: None)
  -c C                  Use the specified configuration file to provide
                        options. Command line options override options from
                        this file. (default: None)
  -w W                  Write out the given options to the specified
                        configuration file. (default: None)
  --log-level {TRACE,DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level. (default: WARNING)

Source can be found at 'https://github.com/sumpfork/dominiontabs'. An online
version can be found at 'http://domdiv.bgtools.net/'.

Args that start with '--' can also be set in a config file (specified via -c).
Config file syntax allows: key=value, flag=true, stuff=[a,b,c] (for details,
see syntax at https://goo.gl/R74nmi). In general, command-line values override
config file values which override defaults.