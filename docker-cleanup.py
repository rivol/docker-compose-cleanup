#!/usr/bin/env python3

from collections import defaultdict
import docker


client = docker.from_env()

imgs_by_project = defaultdict(list)
tags_by_project = defaultdict(list)
imgs_without_tags = []

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


if imgs_without_tags:
    print("Images without tags:")
    print("docker image rm %s" % ' '.join(img.short_id for img in imgs_without_tags))
print("Project images:")
for project, tags in sorted(tags_by_project.items()):
    print(project)
    print("docker image rm %s" % ' '.join(sorted(tags)))
