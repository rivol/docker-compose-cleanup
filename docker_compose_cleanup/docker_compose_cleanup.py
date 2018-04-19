from collections import defaultdict

import colorama
import docker
import requests


Style_Heading = colorama.Style.BRIGHT
Style_Normal = colorama.Style.NORMAL
Style_Error = colorama.Fore.RED


def clean():
    colorama.init()
    client = docker.from_env()

    imgs_by_project = defaultdict(list)
    tags_by_project = defaultdict(list)
    imgs_without_tags = []

    try:
        client.ping()
    except (requests.ConnectionError, docker.errors.APIError):
        print(Style_Error + "Couldn't connect to Docker!")
        return

    # Go through all the images and group them by project (and additionally by tag, though we don't use that)
    for img in client.images.list():
        if not img.tags:
            imgs_without_tags.append(img)
            continue

        for tag in img.tags:
            if '_' not in tag:
                continue

            project = tag.split('_')[0]
            imgs_by_project[project].append(img)
            tags_by_project[project].append(tag)

    # Print out images that don't have any tags. Those are the dangling ones that 'docker image prune' cleans up.
    if imgs_without_tags:
        print(Style_Heading + "Images without tags:" + Style_Normal)
        print("docker image rm %s" % ' '.join(img.short_id for img in imgs_without_tags))
    # Now the projects
    print(Style_Heading + "Project images:" + Style_Normal)
    for project, tags in sorted(tags_by_project.items()):
        print(Style_Heading + project + Style_Normal)
        print("docker image rm %s" % ' '.join(sorted(tags)))


# Make this also usable as standalone script. Because why not.
if __name__ == '__main__':
    clean()
