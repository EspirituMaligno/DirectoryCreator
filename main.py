import os


def create_dir(
    project_name: str,
    path: str,
    is_have_redis: bool = False,
    is_have_docker: bool = False,
):
    project_root = f"{path}/{project_name}"
    if not os.path.exists(project_root):
        os.mkdir(project_root)
    else:
        print(f"Directory {project_name} already exists")

    if is_have_docker:
        os.mkdir(f"{project_root}/.deployment")
        open(os.path.join(project_root, ".deployment", "Dockerfile"), "w").close()
        open(
            os.path.join(project_root, ".deployment", "docker-compose.yml"), "w"
        ).close()

    os.mkdir(f"{project_root}/src")
    # Создание файлов
    open(os.path.join(project_root, "main.py"), "w").close()
    open(os.path.join(project_root, ".env"), "w").close()
    open(os.path.join(project_root, ".env.example"), "w").close()
    os.mkdir(f"{project_root}/src/core")
    os.mkdir(f"{project_root}/src/core/entities")
    os.mkdir(f"{project_root}/src/core/use_cases")
    os.mkdir(f"{project_root}/src/core/interfaces")
    open(
        os.path.join(project_root, "src", "core", "interfaces", "repositories.py"), "w"
    ).close()
    os.mkdir(f"{project_root}/src/core/services")
    open(os.path.join(project_root, "src", "core", "config.py"), "w").close()

    os.mkdir(f"{project_root}/src/infrastructure")
    os.mkdir(f"{project_root}/src/infrastructure/database")
    os.mkdir(f"{project_root}/src/infrastructure/database/repositories")
    open(
        os.path.join(project_root, "src", "infrastructure", "database", "base.py"), "w"
    ).close()
    os.mkdir(f"{project_root}/src/infrastructure/database/modles")
    open(
        os.path.join(project_root, "src", "infrastructure", "database", "session.py"),
        "w",
    ).close()
    open(
        os.path.join(project_root, "src", "infrastructure", "database", "setup.py"), "w"
    ).close()
    os.mkdir(f"{project_root}/src/infrastructure/external")

    if is_have_redis:
        os.mkdir(f"{project_root}/src/infrastructure/redis")

    os.mkdir(f"{project_root}/src/api")
    os.mkdir(f"{project_root}/src/api/endpoints")
    os.mkdir(f"{project_root}/src/api/schemas")
    open(os.path.join(project_root, "src", "api", "dependencies.py"), "w").close()
