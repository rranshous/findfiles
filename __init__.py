import os


def find_files_iter(path,extension=None,exclude=None,file_name=None):
    """ yield back file paths meeting extension/exclude criteria """

    # absolute paths
    found = []


    for dir_path, dir_names, file_names in os.walk(path):
        # remove paths which include the exclude string
        # this will keep them from being traversed
        bad_dirs = [x for x in dir_names if exclude in dir_names]
        map(dir_names.remove,bad_dirs)

        # see if any of the current files meet our
        # extension and exclude criteria
        for name in file_names:
            # if we specified a file name than we need to
            # check for that match first
            if file_name is not None:
                if file_name != name:
                    continue

            if (not extension or name.endswith(extension)) \
               and (not exclude or exclude not in x):
                yield os.path.abspath(os.path.join(dir_path,name))

def find_files(path,extension=None,exclude=None,file_name=None):
    r = [f for f in find_files_iter(path,extension,exclude,file_name)]
    return r

