"""
python submission.py --data-dir /path/to/data-dir --predictions-file-path /path/to/submission.csv
"""

from typing import Optional

import numpy as np
import pandas as pd
import click
from pathlib import Path


HERE = Path(__file__).absolute().resolve().parent


@click.command()
@click.option(
    "--data-dir",
    type=Path,
    help="path to data directory, which consists of folders of Dicom files, each one corresponding to a Dicom series.",
)
@click.option("--predictions-file-path", type=Path)
def main(data_dir: Path, predictions_file_path: Path):
    series_instance_uid_list = [i.name for i in data_dir.iterdir() if i.is_dir()]

    predictions_df = pd.DataFrame(
        {
            "SeriesInstanceUID": series_instance_uid_list,
            "prediction": np.random.random(len(series_instance_uid_list)),
        }
    )
    predictions_df.to_csv(predictions_file_path, index=False)


if __name__ == "__main__":
    main()
