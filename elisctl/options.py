import click

organization_option = click.option(
    "-o",
    "--organization-id",
    type=int,
    help="Organization ID (only useful for superadmin).",
    hidden=True,
)

name_option = click.option("-n", "--name", type=str)
