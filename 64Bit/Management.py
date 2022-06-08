try:
    from dataclasses import dataclass
    from tkinter.font import (BOLD , NORMAL)
    from tkinter.constants import (CENTER , BOTH , HORIZONTAL , VERTICAL , SINGLE , END , W)
    
except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Import Requirements') from None

finally:
    ...
            
            
            


@dataclass
class Materials:
    @dataclass
    class Fonts:
        bold: str = BOLD
        normal: str = NORMAL
    
    @dataclass
    class Colors:
        green: str = '#2ECC71'
        dark: str = '#1C1C1C'
        white: str = '#ffffff'
        
    @dataclass
    class Alignments:
        w: str = W
        both: str = BOTH
        center: str = CENTER
        single: str = SINGLE
        vertical: str = VERTICAL
        horizantal: str = HORIZONTAL
        
    @dataclass
    class Cursors:
        hand: str = 'hand2'
        
    @dataclass
    class Constants:
        end: str = END