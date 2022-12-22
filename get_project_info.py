import io
import sys

import ftrack_api


from get_credentials import get_credentials
from mytimer import Timer


project_keys = [
    "created_at",
    "managers",
    "calendar_events",
    "color",
    "disk_id",
    "full_name",
    "disk",
    "children",
    "timelogs",
    "end_date",
    "parent_id",
    "created_by",
    "id",
    "user_security_role_projects",
    "start_date",
    "project_id",
    "project_schema",
    "metadata",
    "status",
    "scopes",
    "project_schema_id",
    "parent",
    "descendants",
    "thumbnail_id",
    "review_sessions",
    "appointments",
    "link",
    "review_session_folders",
    "is_private",
    "assets",
    "is_global",
    "name",
    "notes",
    "thumbnail",
    "assignments",
    "thumbnail_url",
    "allocations",
    "custom_attributes",
    "created_by_id",
    "_link",
    "root",
    "context_type",
]


def print_all_project_info(stdout=False):
    cred = get_credentials("talha.ahmed")
    outfile = sys.stdout if stdout else io.StringIO()

    t = Timer("Project Query")
    session = ftrack_api.Session(**cred)
    t.print_elapsed("After session create")

    project_query = "select {} from Project".format(",".join(project_keys))
    # project_query = 'Project'
    projects = session.query(project_query).all()
    t.print_elapsed("After project query")

    for project in projects:
        print(project["full_name"] + ":", file=outfile)
        for key in project_keys:
            print("\t%s = %s" % (key, project[key]), file=outfile)
        print(file=outfile)
    t.print_elapsed("After printing all info")

    session.close()


if __name__ == "__main__":
    print_all_project_info()
