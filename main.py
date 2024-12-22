import os

import pooch
#import pkg_resources
from zipfile import ZipFile
from pooch import Unzip


# ad2cp = pooch.retrieve(
#     # URL to one of Pooch's test files
#     url="https://github.com/oftfrfbf/echopype-test-data/releases/download/2024.12.21/ad2cp.zip",
#     known_hash="sha256:8c0e45451eca31b478e7ba9d265fc1bb5257045d30dc50fc5299d2df2abe8430",
# )
# print(ad2cp)

VERSION = '2024.12.21'
ECHOPYPE_RESOURCES = pooch.create(
    # Use the default cache folder for the operating system
    path=pooch.os_cache("echopype"),
    base_url="https://github.com/oftfrfbf/echopype-test-data/releases/download/{version}/",
    version=VERSION,
    retry_if_failed=1,
    registry={
        "ad2cp.zip": "sha256:8c0e45451eca31b478e7ba9d265fc1bb5257045d30dc50fc5299d2df2abe8430",
        "azfp.zip": "6b2067e18e71e7752b768cb84284fef3e0d82b5b775ea2499d52df8202936415",
        "azfp6.zip": "b13ad0cb026d42bd0112d2999e5f63ba28226e4c79ffe335d650fe3f28db760d",
    },
)
#registry_file = pkg_resources.resource_stream("plumbus", "registry.txt")
#print(ECHOPYPE_RESOURCES)

#def fetch_ad2cp():
#    """
#        Load the C-137 sample data as a pandas.DataFrame.
#        """
#    # The file will be downloaded automatically the first time this is run
#    # returns the file path to the downloaded file. Afterwards, Pooch finds
#    # it in the local cache and doesn't repeat the download.
#    fname = ECHOPYPE_RESOURCES.fetch("ad2cp.zip")
#    # The "fetch" method returns the full path to the downloaded data file.
#    # All we need to do now is load it with our standard Python tools.
#    #data = pandas.read_csv(fname)
#    return fname


def unpack(fname, action, pup):
    """
    Post-processing hook to unzip a file and return the unzipped file name.

    Parameters
    ----------
    fname : str
       Full path of the zipped file in local storage
    action : str
       One of "download" (file doesn't exist and will download),
       "update" (file is outdated and will download), and
       "fetch" (file exists and is updated so no download).
    pup : Pooch
       The instance of Pooch that called the processor function.

    Returns
    -------
    fname : str
       The full path to the unzipped file. (Return the same fname is your
       processor doesn't modify the file).

    """
    # Create a new name for the unzipped file. Appending something to the
    # name is a relatively safe way of making sure there are no clashes
    # with other files in the registry.
    unzipped = fname.split('.zip')[0] # + ".unzipped"
    # Don't unzip if file already exists and is not being downloaded
    if action in ("update", "download") or not os.path.exists(unzipped):
        with ZipFile(fname, "r") as zip_file:
            zip_file.extractall(path=unzipped)
    return unzipped

def fetch_zipped_file(filename):
    """
    Load a large zipped sample data as a pandas.DataFrame.
    """
    fname = ECHOPYPE_RESOURCES.fetch(
        fname=filename,
        processor=unpack,
        progressbar=True,
    )
    return fname


#file_path = echopype_test_resources.fetch("ad2cp.zip")
# Standard use of xarray to load a netCDF file (.nc)
#print(file_path)
# data = xr.open_dataset(file_path)
# print(data)

ad2cp = fetch_zipped_file("ad2cp.zip")
print(ad2cp)
azfp = fetch_zipped_file("azfp.zip")
print(azfp)
azfp6 = fetch_zipped_file("azfp6.zip")
print(azfp6)