import pooch


# file_path = pooch.retrieve(
#     # URL to one of Pooch's test files
#     url="https://github.com/fatiando/pooch/raw/v1.0.0/data/tiny-data.txt",
#     known_hash="md5:70e2afd3fd7e336ae478b1e740a5f08e",
# )

# ad2cp = pooch.retrieve(
#     # URL to one of Pooch's test files
#     url="https://github.com/oftfrfbf/echopype-test-data/releases/download/2024.12.21/ad2cp.zip",
#     known_hash="sha256:8c0e45451eca31b478e7ba9d265fc1bb5257045d30dc50fc5299d2df2abe8430",
# )
# print(ad2cp)


echopype_test_resources = pooch.create(
    # Use the default cache folder for the operating system
    path=pooch.os_cache("echopype"),
    base_url="https://github.com/oftfrfbf/echopype-test-data/releases/download/2024.12.21/",
    # The registry specifies the files that can be fetched
    registry={
        "ad2cp.zip": "sha256:8c0e45451eca31b478e7ba9d265fc1bb5257045d30dc50fc5299d2df2abe8430",

    },
)

print(echopype_test_resources)