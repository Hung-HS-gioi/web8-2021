import dvc.api

with dvc.api.open(
    'data/S.xml',
    repo='https://github.com/Hung-HS-gioi/web8-2021'
) as fd:
    # fd is a file descriptor which can be processed normally