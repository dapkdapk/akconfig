import click

from ak.config import AKConfig

"""
These are global variables
"""
VAR_A = "HELLO WORLD"
VAR_B = 100
VAR_C = 3.14
VAR_D = True
VAR_E = {"a": "b", "c": "d"}
VAR_F = ["a", "b", "c", "d"]
VAR_G = ("a", "b", "c", "d")
VAR_H = "SECRET"
VAR_I = r"^\sTest.*"
VAR_J = "Some text SECRET should be masked"
VARS_MASK = ["VAR_H"]

@click.command()
@click.option(
    "-c",
    "--config",
    multiple=True,
    type=(str, str),
    help="Config parameters are: {}".format(", ".join(AKConfig.GetGlobals(globals()))),
)
@click.option(
    "-f",
    "--force-env-vars",
    is_flag=True,
    help="Set argument if you want force environment variables",
)
@click.option(
    "-u",
    "--uncolored-print",
    is_flag=True,
    help="Set argument and output is not colored",
)
def main(config, force_env_vars, uncolored_print):
    cfg = AKConfig(
        global_vars=globals(),
        config_args=config,
        mask_keys=VARS_MASK,
        force_env_vars=force_env_vars,
        uncolored=uncolored_print,
    )

    cfg.print_config()

    cfg.VAR_D = False

    example_a = """
Example A
=========
description: use env var and force with arg -f
try: export VAR_B=200;poetry run basic -f
    """

    example_b = """
Example B
=========
description: use arg -c (multiple) to overwrite global variables
try: poetry run basic -c VAR_A "I'm here"
    """

    example_c = """
Example C
=========
description: use arg -c (multiple) to overwrite global variables
try: poetry run basic -c VAR_E '{"key_name":"val_anything"}'
    """

    if force_env_vars is False:
        print(example_a)
    if cfg.VAR_A == VAR_A:
        print(example_b)
    if cfg.VAR_E == VAR_E:
        print(example_c)


if __name__ == "__main__":
    main()
