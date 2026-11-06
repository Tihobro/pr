# Contributing

## Стиль коммитов (Conventional Commits)

Формат: `<type>: <description>`

### Типы
- `feat` — новая функциональность
- `fix` — исправление ошибки
- `docs` — изменения в документации
- `style` — форматирование, без изменения логики
- `refactor` — рефакторинг
- `test` — добавление тестов
- `ci` — настройка CI/CD

### Примеры
- `feat: add divide() function`
- `fix: correct Python version in workflow`
- `docs: update installation steps`

## Процесс разработки
1. Создайте Issue с описанием задачи
2. Заведите ветку `feature/<issue-number>-short-name`
3. Сделайте коммиты в соответствии с Conventional Commits
4. Создайте Pull Request с описанием `Closes #<N>`
5. Пройдите code review
6. После merge удалите локальную ветку
