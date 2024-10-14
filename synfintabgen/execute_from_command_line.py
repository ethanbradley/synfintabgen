import argparse

from synfintabgen.generator_dataset import DatasetGenerator
from synfintabgen.configuration_dataset_generator import DatasetGeneratorConfig


def execute_from_command_line() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--dataset-size", type=int, required=True)
    parser.add_argument("-p", "--dataset-path", type=str)
    parser.add_argument("-n", "--dataset-name", type=str)
    parser.add_argument("-w", "--document-width", type=int)
    parser.add_argument("-x", "--document-height", type=int)

    args = parser.parse_args()
    dataset_size = args.dataset_size
    dataset_path = args.dataset_path
    dataset_name = args.dataset_name
    document_width = args.document_width
    document_height = args.document_height

    config = DatasetGeneratorConfig(
        dataset_path=dataset_path,
        dataset_name=dataset_name,
        document_width=document_width,
        document_height=document_height
    )
    generator = DatasetGenerator(config)
    generator(dataset_size)
