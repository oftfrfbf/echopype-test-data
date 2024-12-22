import pooch
import xarray as xr

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
    },
)
print(ECHOPYPE_RESOURCES)

def fetch_ad2cp():
    """
        Load the C-137 sample data as a pandas.DataFrame.
        """
    # The file will be downloaded automatically the first time this is run
    # returns the file path to the downloaded file. Afterwards, Pooch finds
    # it in the local cache and doesn't repeat the download.
    fname = ECHOPYPE_RESOURCES.fetch("ad2cp.zip")
    # The "fetch" method returns the full path to the downloaded data file.
    # All we need to do now is load it with our standard Python tools.
    #data = pandas.read_csv(fname)
    return fname

#file_path = echopype_test_resources.fetch("ad2cp.zip")
# Standard use of xarray to load a netCDF file (.nc)
#print(file_path)
# data = xr.open_dataset(file_path)
# print(data)

data = fetch_ad2cp()