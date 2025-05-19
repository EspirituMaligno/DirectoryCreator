import os

path = "C:/Users/user/Desktop"


def create_dir(project_name: str, is_have_redis: bool = False):
    if not os.path.exists(f"{path}/{project_name}"):
        os.mkdir(f"{path}/{project_name}")
    else:
        print(f"Directory {project_name} already exists")

    os.mkdir(f"{path}/{project_name}/src")
    os.mkdir(f"{path}/{project_name}/src/core")
    os.mkdir(f"{path}/{project_name}/src/core/entities")
    os.mkdir(f"{path}/{project_name}/src/core/use_cases")

    os.mkdir(f"{path}/{project_name}/src/infrastructure")
    os.mkdir(f"{path}/{project_name}/src/infrastructure/database")
    os.mkdir(f"{path}/{project_name}/src/infrastructure/database/repositories")
    os.mkdir(f"{path}/{project_name}/src/infrastructure/database/modles")
    os.mkdir(f"{path}/{project_name}/src/infrastructure/database")
    os.mkdir(f"{path}/{project_name}/src/infrastructure/redis")
