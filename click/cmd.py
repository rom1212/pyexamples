import click

@click.command()
@click.option('--count', '-c', default=0, help='count')
def main(count):
   print 'count:', count

if __name__ == "__main__":
    main()
