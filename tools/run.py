
from datetime import datetime as dt
from pathlib import Path

import click
from loguru import logger

from pipelines import data_etl

from omegaconf import OmegaConf

def main(
    run_etl: bool = False,
    etl_config_filename: bool = False
    )  -> None:
    
    assert (run_etl or etl_config_filename), "At least one paramater must be provided"
    pipeline_args = {}
    root_dir = Path(__file__).resolve().parent.parent    
    logger.info(f"Root directory: {root_dir}")
    config_path = root_dir / "configs" / etl_config_filename
    assert config_path.exists(), f"Config file not found: {config_path}"
    config = OmegaConf.load(config_path)
    logger.info(f"Config loaded: {config}")
    data_etl(config['parameters']['user_full_name'], config['parameters']['links'])


if __name__ == "__main__":
    main(run_etl=True, etl_config_filename="data_etl_author1_1.yaml")
    # main(run_etl=True, etl_config_filename="data_etl_author2_2.yaml")