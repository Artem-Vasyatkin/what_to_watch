# opinions_app/cli_commands.py

import csv

import click

from . import app, db
from .models import Opinion


@app.cli.command('load_opinions')
def load_opinions_command():
    """Функция загрузки мнений в базу данных."""
    with open('opinions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        skipped = 0
        for i, row in enumerate(reader, start=2):
            # Пропускаем строки с лишними/недостающими полями
            if None in row:
                click.echo(f'Пропущена строка {i}: некорректное число полей')
                skipped += 1
                continue

            # Проверяем, нет ли уже такого текста в базе
            existing = Opinion.query.filter_by(text=row['text']).first()
            if existing:
                click.echo(f'Строка {i}: запись уже есть, пропускаем')
                skipped += 1
                continue

            try:
                opinion = Opinion(**row)
                db.session.add(opinion)
                db.session.commit()
                counter += 1
            except Exception as e:
                db.session.rollback()
                click.echo(f'Ошибка в строке {i}: {e}')
                skipped += 1

    click.echo(f'Загружено мнений: {counter}, пропущено: {skipped}')
