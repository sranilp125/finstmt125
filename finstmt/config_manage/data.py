from dataclasses import dataclass
from typing import Dict, List

from sympy import symbols, IndexedBase, Idx

from finstmt.config_manage.base import ConfigManagerBase
from finstmt.items.config import ItemConfig


@dataclass
class DataConfigManager(ConfigManagerBase):
    """
    Used to manage the config for an individual time period of an individual statement
    """
    configs: List[ItemConfig]

    def __post_init__(self):
        self.configs = list(self.configs)

    def __getitem__(self, item):
        return self.configs[item]

    def __iter__(self):
        yield from self.configs

    def get(self, item_key: str) -> ItemConfig:
        """
        Get entire configuration for item by key
        """
        return self.config_dict[item_key]

    def set(self, item_key: str, config: ItemConfig):
        """
        Set entire configuration for item by key
        """
        orig_config = self.get(item_key)
        config_idx = self.configs.index(orig_config)
        self.configs[config_idx] = config

    # TODO: Avoid unnecessary calculations in DataConfigManager
    #
    #  Make config_dict and sympy_namespace not properties, but recalculate any time config changes
    @property
    def config_dict(self) -> Dict[str, ItemConfig]:
        return {config.key: config for config in self.configs}

    @property
    def sympy_namespace(self) -> Dict[str, IndexedBase]:
        t = symbols('t', cls=Idx)
        ns_dict = {'t': t}
        for config in self.configs:
            expr = IndexedBase(config.key)
            ns_dict.update({config.key: expr})
        return ns_dict

