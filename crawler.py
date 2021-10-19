import gitlab
from gitlab.exceptions import GitlabParsingError


TAG = "inner-source"
# private token or personal token authentication
gl = gitlab.Gitlab.from_config('gitlab')

# list all the projects
# manual iterations over the generator as to capture the GitlabParsingError exception
items = gl.projects.list(as_list=False, owned=True)
while True:
    try:
        repo = items.next()
        attributes = repo.attributes
        if TAG in attributes["tag_list"]:
            print(attributes)
    except GitlabParsingError:
        continue
    except StopIteration:
        break

# for item in items:
#     try:
#         attributes = item.attributes
#         if TAG in attributes["tag_list"]:
#             print(attributes)
#     except gitlab.exceptions.GitlabParsingErro:
#         continue
#
#
