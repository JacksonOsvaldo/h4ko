import os
import shutil
import click
from .database import init_db

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates', 'project_template')

@click.group()
def main():
    pass

@main.command()
@click.argument('name')
def startproject(name):
    if name == '.':
        shutil.copytree(TEMPLATE_DIR, os.path.join(name), dirs_exist_ok=True)
        click.echo(f'Projeto {name} criado com sucesso.')
    else:
        os.makedirs(name, exist_ok=True)
        shutil.copytree(TEMPLATE_DIR, os.path.join(name), dirs_exist_ok=True)
        click.echo(f'Projeto {name} criado com sucesso.')
   

@main.command()
def initdb():
    init_db()
    click.echo('Banco de dados inicializado com sucesso.')

if __name__ == '__main__':
    main()
