# IAAA MRI Contest Image

You can use dependencies in `pyproject.toml` file. Dependencies are installed in google colab plus some DICOM related dependencies like `pydicom` and `SimpleITK`.


## Prepare Environment

> Make sure you have **Python v3.10** installed!

- Method 1 ([poetry](https://python-poetry.org/docs/#installation))

```bash
poetry install
```

- method 2 (pip)

```bash
python -m venv venv
source venv/bin/activate
pip install -e .
```

## `submission.py`

We create a sample `submission.py` file, you script should follow these arguments to execute properly.

### File

```python
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
```

### Execution

```bash
python submission.py --data-dir /path/to/data-dir --predictions-file-path /path/to/submission.csv
```