

```bash
pip install py-solc-x
solcx.install_solc('0.6.0')
```

- Installing the compiler

```bash
python
from brownie.project.compiler import install_solc
install_solc("0.5.10")
```

### Solving import issue in .sol file
- to define dependencies and remapping in brownie-config.yml
- to define remapping in .vscode/settings.json

### Adding custom network

```bash
brownie networks add Ethereum ganache-gui host=http://127.0.0.1:7545 chainid=1337
```