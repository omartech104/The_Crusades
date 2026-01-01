# mechs/ascii_art.py

from rich.console import Console

console = Console()


def welcome_screen():
    art = r'''
          o 
       o^/|\^o
    o_^|\/*\/|^_o
   o\*`'.\|/.'`*/o
    \\\\\\|//////
     {><><@><><}
     `"""""""""`
    '''
    menu = [
        "[bold green]1. NEW GAME[/bold green]",
        "[bold cyan]2. LOAD GAME[/bold cyan]",
        "[bold yellow]3. RULES[/bold yellow]",
        "[bold red]4. QUIT GAME[/bold red]",
    ]

    # Print ASCII art (plain)
    console.print(art)

    # Print colored menu (plain alignment)
    for item in menu:
        console.print(item)


# weapons

longsword = """    /
O===[====================-
    \\"""

battle_axe = r"""  ,  /\  .  
 //`-||-'\\ 
(| -=||=- |)
 \\,-||-.// 
  `  ||  '  
||     
     ||     
     ||     
     ||     
     ||     
     ()
"""

longbow = r"""   (
    \
     )
##-------->        
     )
    /
   ("""

warhammer = r"""             +-+
=============| |
            `:_;'"""

dagger = r""")xxxxx[;;;;;;;;;>"""

rapier = r"""       |
       /~\
Oxxxxx|  (|=========================-
 \____/\_/
       |"""

halberd = r"""  ,  /\
 //`-|| 
(| -=||
 \\,-|| 
  `  ||  
     ||     
     ||     
     ||     
     ||     
     ||     
     ()"""

crossbow = r"""                .-.
               /  \\
          .---/-+--||
          |  K=====++->
          '---\-+--||
               \  //
                `-'  """

mace = r"""               <<()>>
                )__(
                )__(
                )__(
                )__(
                )__(
                )__(
                )__(
                )__(
                )__(
               _)__(_
             .'      `.
             | <   >  |>
            <|   <   >|
              `.____.'
                V  V"""

dirk = r"""0)xxxxx[=======------------"""

spear = r"""
 /\
/__\
 ||
 ||
 ||
 ||
 ||
 ||
 ||
 ||
 ||
 ||
 ()"""

composite_bow = r"""
|. .
|    .
|     .
|      . 
|      .
|     .
|    .
|..."""

zweilhander = r"""          />
         /<
O[\\\\\\(O):::<=======================-
         \<
          \>"""

shamshir = r'''   _,---,_
 /'_______`\
(/'       `\|___________----------"""""""------,
 \#########||______                          /'
  ^^^^^^^^^||      """"""-----_____        /'
            \                      """--_/'''

waraxe = r"""  ,:\      /:.
 //  \_()_/  \\
||   |    |   ||
||   |    |   ||
||   |____|   ||
 \\  / || \  //
  `:/  ||  \;'
       ||
       ||
       XX
       XX
       XX
       XX
       OO
       """

throwing_knife = r"""
       ________ ___,,,,,,,
      [________>__________\
"""
