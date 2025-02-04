import argparse

def add_arg(parser, name, help_text, default=None, type=str):
    """Fügt ein Argument mit optionalen Werten hinzu."""
    parser.add_argument(name, help=help_text, default=default, type=type)

def parse_args(parser):
    parser.add_argument("--debug", action="store_true", help="Debug-Modus aktivieren")

    return parser.parse_args()
