"""
fem_mesh.py

Generic functions for all meshing functions

Copyright 2014 Mark L. Palmeri (mlp6@duke.edu)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

__author__ = "Mark Palmeri"
__email__ = "mlp6@duke.edu"
__license__ = "Apache v2.0"

def check_version():
    """
    Check that at least python2.7 is being used for argparse compatibility
    """
    import sys

    if sys.version_info[:2] < (2, 7):
        sys.exit("ERROR: Requires Python >= 2.7")


def strip_comments(nodefile):
    import os
    nodefile_nocmt = '%s.tmp' % nodefile
    os.system("egrep -v '(^\*|^\$)' %s > %s" % (nodefile, nodefile_nocmt))
    return nodefile_nocmt


def rm_tmp_file(nodefile_nocmt):
    import os
    try:
        os.remove(nodefile_nocmt)
    except OSError as e:
        print('ERROR: %s - %s.' % (e.argsfilename, e.argsstrerror))
