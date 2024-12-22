# Echopype Test Resources

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/oftfrfbf/echopype-test-data)

![GitHub repo file or directory count](https://img.shields.io/github/directory-file-count/oftfrfbf/echopype-test-data)

![GitHub repo size](https://img.shields.io/github/repo-size/oftfrfbf/echopype-test-data)

Testing saving the echopype cormorack/http:latest data from the docker images as tagged release assets.

The assets don't contribute to the projects code size and the limit is 2 GB for each assest.

> conda install pooch

# Zenodo DOI
Goto my account, Github, flip the switch, 
https://zenodo.org/account/settings/github/repository/oftfrfbf/echopype-test-data

[![DOI](https://zenodo.org/badge/906437365.svg)](https://doi.org/10.5281/zenodo.14542544)

Unfortunately this only archives the actual code in the repo, not the assets.

# To create registry for pooch, do
$ find *.zip -type f -exec sha256sum {} \;
8c0e45451eca31b478e7ba9d265fc1bb5257045d30dc50fc5299d2df2abe8430  ad2cp.zip
6b2067e18e71e7752b768cb84284fef3e0d82b5b775ea2499d52df8202936415  azfp.zip
b13ad0cb026d42bd0112d2999e5f63ba28226e4c79ffe335d650fe3f28db760d  azfp6.zip
75cca9c320cd62be613874674cfbcbb8931f236c12ff4e08e4e5de0cc119864f  dump.zip
10bcd57c9d382e680e26a0f78b3e1c8bda8c68799d69334ab63031c10650d114  ea640.zip
e873754f40ec7142c5ece9706a9c63e6f49666b534c79aeac54952ece8267439  ecs.zip
2334ba26f00720c1d29241d35f32c9cddce3fdd1d3dd2b1a99d8962f04e977ee  ek60.zip
82a9f89c848f6925f779ef6b8d47e6fb1c59e720a303830010f73e45e82c6609  ek60_missing_channel_power.zip
e46dea3ba4531d2576bbae2cd17a33ead48cb594244dd611fddd98e53901aa39  ek80.zip
4eac7b0f40bdd8405aac38e114b47cc1901f7614002e7a5ea9a642bbcb884f93  ek80_bb_complex_multiplex.zip
362613ecce383136be16e0a7d7c74a33ef11866d5a0b6bf1581172b27186790a  ek80_bb_with_calibration.zip
f2affc25c0972c23ef2f9e1e78a7627bffe6105d39e5b4e9c68b3e8bb81e08b5  ek80_duplicate_ping_times.zip
dbaf35f2af1526e4d5a9e6b65b22e090d4db0e0355d8be8e5c2255fe03b65475  ek80_ext.zip
12f8bc32aecaf3c1c8a506491be2346382aed76f6c6dd8d60847f6915b597c50  ek80_invalid_env_datagrams.zip
56fd98974cf1dd1cd400358045cfbcf82c52e431e4acf822146458dbdf11a59e  ek80_missing_sound_velocity_profile.zip
644ef2c2d89e52b63635eaf523eb0b0385580b1bacd189aa39c62db69943abb6  ek80_new.zip
7abf0635a7d1365d075d9b4ce32abef86efe2ea1fda84be4f07187f384709ff5  es60.zip
e7d58335b0049b3709e08663913925d75a76250f787f84019dc5f3fadfc0983a  es70.zip
9547583dbd6ac77375384e614cd559ff61639d36f082f1ce80855f9b57a52213  es80.zip


## CICD
Moving the 
.ci_helpers/docker/setup-services.py
file 

# Replacing
```
{'cmd': None, 'msg': 'Starting test services deployment ...'}
{'cmd': ['docker-compose', '-f', WindowsPath('C:/Users/rudy/Documents/github/echopype/.ci_helpers/docker/docker-compose.yaml'), 'pull'], 'msg': 'Pulling latest images ...'}
{'cmd': ['docker-compose', '-f', WindowsPath('C:/Users/rudy/Documents/github/echopype/.ci_helpers/docker/docker-compose.yaml'), 'up', '-d', '--remove-orphans', '--force-recreate'], 'msg': 'Bringing up services ...'}
{'cmd': ['docker', 'cp', '-L', 'docker-httpserver-1:/usr/local/apache2/htdocs/data', WindowsPath('C:/Users/rudy/Documents/github/echopype/.ci_helpers/docker/echopype/test_data')], 'msg': 'Copying new test folder from http service ...'}
{'cmd': <function load_s3 at 0x0000020C590B3820>, 'msg': 'Setting up minio s3 bucket ...'}
{'cmd': ['docker', 'ps', '--last', '2'], 'msg': 'Done.'}
```

# In testing.py
> echopype/testing.py

replace the 
```
HERE = Path(__file__).parent.absolute()
TEST_DATA_FOLDER = HERE / "test_data"
```
with 

