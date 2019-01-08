from todoist.api import TodoistAPI

api = TodoistAPI('8d430dda9a8ec73bb41359f4606f91c5ed47a957')


def list_projects():
    api.sync()
    return api.state['projects']


def find_project_by_id(project_id):
    api.sync()
    projects = list_projects()
    for project in projects:
        if project.data.get('id') == project_id:
            return project


def find_project_by_name(name):
    api.sync()
    projects = []
    for project in list_projects():
        if project.data.get('name') == name:
            projects.append(project)
    return projects


def add_project(name):
    project = api.projects.add(name)
    api.commit()
    return project


def add_task(content, project_id):
    task = api.items.add(content, project_id)
    api.commit()
    return task.data


def delete_project(name):
    projects = []
    for project in find_project_by_name(name):
        projects.append(project.data.get('id'))

    api.projects.delete(projects)
    api.commit()


def delete_task(name):
    tasks = []
    for task in find_task(name):
        tasks.append(task.data.get('id'))

    api.items.delete(tasks)
    api.commit()


def get_task_by_id(task_id):
    api.sync()
    return api.items.get_by_id(task_id)


def find_task(content):
    api.sync()
    filtered_tasks = []
    for task in api.state['items']:
        if task.data.get('content') == content:
            filtered_tasks.append(task)
    return filtered_tasks


def reopen_task(content):
    for task in find_task(content):
        if task.data.get('content') == content:
            api.items.get_by_id(task.data.get('id')).uncomplete()
    api.commit()


def reopen_task_by_id(task_id):
    api.sync()
    api.items.get_by_id(task_id).uncomplete()
    api.commit()
