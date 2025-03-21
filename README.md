# SynFinTabGen: Synthetic Financial Table Generator

A package for generating synthetic financial tables.

## Quick Start

To generate a dataset of synthetic financial tables, create a generator and pass how many tables you would like.

```python3
from synfintabgen import DatasetGenerator

generator = DatasetGenerator()

generator(10)
```

The output directory defaults to `dataset` in the current working directory.

## Configuration

You can configure the generator using the `DatasetGeneratorConfig` class.

```python3
from synfintabgen import DatasetGeneratorConfig

config = DatasetGeneratorConfig(
    dataset_path="my-datasets-dir",
    dataset_name="my-dataset-name",
    document_width=745,
    document_height=1503
)

generator = DatasetGenerator(config)
```

## Note

Before the first use of this package, you'll need to make sure you have `nltk` words corpus downloaded. You can do this like so:

```python3
import nltk

nltk.download('words')
```

## Citation

If you use this software, please cite both the article using the citation below and the software itself.

```bib
@misc{bradley2024synfintabs,
      title         = {Syn{F}in{T}abs: A Dataset of Synthetic Financial Tables for Information and Table Extraction},
      author        = {Bradley, Ethan and Roman, Muhammad and Rafferty, Karen and Devereux, Barry},
      year          = {2024},
      eprint        = {2412.04262},
      archivePrefix = {arXiv},
      primaryClass  = {cs.LG},
      url           = {https://arxiv.org/abs/2412.04262}
}
```
