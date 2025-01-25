import click

from ak.config import AKConfig
LALA="PLOPP"
@click.command()
@click.option("-t","--test",help="something",envvar="VAR_TEST", default="hello")
def main(test):
    cfg = AKConfig(globals(),None,None)
    print(cfg.test)
    print(click.argument().__dict__)
    """
    if "click" in globals():
        print(globals()["click"].get_current_context().params)
    print(click.get_current_context().params,test)
    """

if __name__ == "__main__":
    main()