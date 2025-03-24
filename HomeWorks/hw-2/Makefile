PIP := venv/bin/pip
PYTHON3 := venv/bin/python3
TESTS := venv/bin/pytest -v ./test_controllers.py

clear: ## удалить виртуальное окружение
	rm -rf venv

venv: ## создать виртуальное окружение
	python3 -m venv venv

install_requirements: ## установить зависимости из requirements.txt
	${PIP} install --upgrade pip
	${PIP} install -r requirements.txt

run: ## запустить сервер
	${PYTHON3} server.py

add_dependency: ## добавить зависимость в requirements.txt
	@echo "Какой пакет вы хотите установить? (Введите название) "
	@read package; ${PIP} install $$package && ${PIP} freeze > requirements.txt

test: ## запуск тестов
	${TESTS}

help: ## вывести список доступных команд
	@echo "Доступные команды:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'