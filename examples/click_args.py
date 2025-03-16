import click

from ak.config import AKConfig

VAR_TEST_A = "Hello"


@click.command()
@click.option("-b", "--test-b", envvar="VAR_TEST_B", default="you")
@click.option("-c", "--test-c", envvar="VAR_TEST_C", default=True, type=click.BOOL)
def main(test_b, test_c):
    cfg = AKConfig()
    result = cfg.get_arg_envvar("VAR_TEST_A", "test_b", "test_c")
    result2 = cfg.get_arg_envvar_deep(2, VAR_TEST_A, test_b, test_c)

    print("1:", cfg.VAR_TEST_A, cfg.VAR_TEST_B, cfg.VAR_TEST_C)
    print("2:", result)
    print("3:", result2)

    cfg.print_config()


if __name__ == "__main__":
    main()
