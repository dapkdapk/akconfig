import click

from ak.config import AKConfig

VAR_TEST_A = "Hello"


@click.command()
@click.option("-b", "--test-b", envvar="VAR_TEST_B", default="you")
@click.option("-c", "--test-c", envvar="VAR_TEST_C", default=True, type=click.BOOL)
def main(test_b, test_c):
    cfg = AKConfig()
    result = cfg.get_arg_envvar("test_a", "test_b")
    print(cfg.VAR_TEST_A, cfg.VAR_TEST_B, cfg.VAR_TEST_C, result)

    cfg.print_config()


if __name__ == "__main__":
    main()
