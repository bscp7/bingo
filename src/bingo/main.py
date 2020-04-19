import time
import click
from .bingo import roll

@click.command()
@click.option("--count", default=90, help="Bingo limit (Default: 90)")
@click.option("--interval", default=0.0, help="Auto-generate numbers at given interval (Default: Manual)")
def main(count, interval):
    rolls = roll(count)
    for x in rolls:
        print(x)
        if interval >0:
            time.sleep(interval)
        else:
            input()

if __name__ == "__main__":
    main()
