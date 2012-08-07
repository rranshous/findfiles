
import os
import glob
import os.path

version_info = (0, 0, 6)
__version__ = '.'.join(map(str, version_info))
version = __version__

def find_dirs_iter(path,exclude=None):
    """
    yield back dir (abs) paths meeting extension/exclude criteria

    path can be a glob-able path (contains a *) in which case all
    paths resulting from the glob will be considered source paths

    exclude should be a string which should not be part of
    a matching file's name
    """

    # expand our source path so that home paths (~) are
    # correctly interpreted
    path = os.path.expanduser(path)

    # go through all the paths resulting from interpreting
    # the path as a glob
    for source_path in glob.iglob(path):

        # go through all the files / dirs off the source path
        for dir_path, dir_names, file_names in os.walk(source_path):

            # remove paths which include the exclude string
            # this will keep them from being traversed
            bad_dirs = [x for x in dir_names if exclude in dir_names]
            map(dir_names.remove,bad_dirs)

            # see if any of the current files meet our
            # extension and exclude criteria
            for name in dir_names:

                # does this dir name include our excluded string?
                if exclude and exclude in name:
                    continue

                # yield back the absolute path
                yield os.path.abspath(os.path.join(dir_path,name))

def find_files_iter(path,extension=None,exclude=None,file_name=None):
    """
    yield back (abs) file paths meeting extension/exclude criteria

    path can be a glob-able path (contains a *) in which case all
    paths resulting from the glob will be considered source paths

    extension should start with a '.' if appropriate

    exclude should be a string which should not be part of
    a matching file's name
    """

    # expand our source path so that home paths (~) are
    # correctly interpreted
    path = os.path.expanduser(path)

    # go through all the paths resulting from interpreting
    # the path as a glob
    for source_path in glob.iglob(path):

        # go through all the files / dirs off the source path
        for dir_path, dir_names, file_names in os.walk(source_path):

            # remove paths which include the exclude string
            # this will keep them from being traversed
            bad_dirs = [x for x in dir_names if exclude in dir_names]
            map(dir_names.remove,bad_dirs)

            # see if any of the current files meet our
            # extension and exclude criteria
            for name in file_names:

                # if we specified a file name than we need to
                # check for that match first
                if file_name is not None and file_name != name:
                    continue

                # if there is a required extension specified
                # make sure the file meets the criteria
                if extension and not name.endswith(extension):
                    continue

                # if there is an excluded string, make sure the
                # file name does not include it
                if exclude and exclude in name:
                    continue

                # yield up our resulting file as an absolute path
                yield os.path.abspath(os.path.join(dir_path, name))

def find_files(path,extension=None,exclude=None,file_name=None):
    r = [f for f in find_files_iter(path,extension,exclude,file_name)]
    return r

def find_dirs(path,exclude=None):
    r = [f for f in find_dirs_iter(path,exclude)]
    return r

