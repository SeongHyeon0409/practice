def print_ansi_demo():
    # ANSI escape code for styles
    styles = {
        'reset': '\033[0m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'reverse': '\033[7m'
    }
    
    # ANSI escape code for text colors
    text_colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m'
    }
    
    # ANSI escape code for background colors
    bg_colors = {
        'black': '\033[40m',
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'magenta': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m'
    }
    
    print(f"{styles['bold']}{text_colors['red']}This is bold red text{styles['reset']}")
    print(f"{styles['underline']}{text_colors['green']}This is underlined green text{styles['reset']}")
    print(f"{styles['reverse']}{text_colors['yellow']}This is reversed yellow text{styles['reset']}")
    print(f"{text_colors['blue']}This is blue text{styles['reset']}")
    print(f"{text_colors['magenta']}{bg_colors['cyan']}This is magenta text with cyan background{styles['reset']}")
    print(f"{text_colors['white']}{bg_colors['black']}This is white text with black background{styles['reset']}")
    
if __name__ == "__main__":
    print_ansi_demo()
