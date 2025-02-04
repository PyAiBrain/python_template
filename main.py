from lib.cli.arguments import parse_args, add_arg, argparse
from lib.core.logger import LOG
from lib.core.parser import parse_custom_time

def init_arg_parser() -> dict:
    global standard_parser
    
    # Beispiel: Argumente dynamisch hinzufügen
    standard_parser = argparse.ArgumentParser(description="Standard Parser")
    
    add_arg(standard_parser, "t_parse", "Parses the given Time", type=str)
    parser = parse_args(standard_parser)

    if parser.debug:
        LOG.setLevel("DEBUG")
        LOG.debug("Debug-Modus aktiviert!")
    else:
        LOG.setLevel("INFO")


    
    return parser



def main():
    args = init_arg_parser()
    
    if args.t_parse:
        print(parse_custom_time(args.t_parse.replace('t_parse=', '')))



if __name__ == "__main__":
    main()