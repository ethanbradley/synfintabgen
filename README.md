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
@inproceedings{bradley2026synfintabs,
    title        = {Syn{F}in{T}abs: A Dataset of Synthetic Financial Tables for Information and Table Extraction},
    author       = {Bradley, Ethan and Roman, Muhammad and Rafferty, Karen and Devereux, Barry},
    year         = 2026,
    month        = jan,
    booktitle    = {Document Analysis and Recognition -- ICDAR 2025 Workshops},
    publisher    = {Springer Nature Switzerland},
    address      = {Cham},
    pages        = {85--100},
    doi          = {10.1007/978-3-032-09371-4_6},
    isbn         = {978-3-032-09371-4},
    editor       = {Jin, Lianwen and Zanibbi, Richard and Eglin, Veronique},
    abstract     = {Table extraction from document images is a challenging AI problem, and labelled data for many content domains is difficult to come by. Existing table extraction datasets often focus on scientific tables due to the vast amount of academic articles that are readily available, along with their source code. However, there are significant layout and typographical differences between tables found across scientific, financial, and other domains. Current datasets often lack the words, and their positions, contained within the tables, instead relying on unreliable OCR to extract these features for training modern machine learning models on natural language processing tasks. Therefore, there is a need for a more general method of obtaining labelled data. We present SynFinTabs, a large-scale, labelled dataset of synthetic financial tables. Our hope is that our method of generating these synthetic tables is transferable to other domains. To demonstrate the effectiveness of our dataset in training models to extract information from table images, we create FinTabQA, a layout large language model trained on an extractive question-answering task. We test our model using real-world financial tables and compare it to a state-of-the-art generative model and discuss the results. We make the dataset, model, and dataset generation code publicly available (https://ethanbradley.co.uk/research/synfintabs).}
}
```
