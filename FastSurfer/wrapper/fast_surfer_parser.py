import argparse
import os
from dataclasses import dataclass
from typing import Union


@dataclass
class Configurations:
    """
    Defines global configuration for the pipeline reading information from ENV variables.
    """

    t1: str = os.getenv("T1", os.path.join(os.getcwd(), "data", "sub-001.nii.gz"))
    sd: str = os.getenv("SD", os.path.join(os.getcwd(), "output"))
    sid: str = os.getenv("SID", "sub-001")
    fs_license: str = os.getenv(
        "FS_LICENSE", os.path.join(os.getcwd(), "freesurfer_license", "license.txt")
    )
    vox_size: Union[int, float] = os.getenv("VOX_SIZE", 1)
    threads: int = os.getenv("THREADS", 1)
    device: str = os.getenv("DEVICE", "cpu")
    viewagg_device: str = os.getenv("VIEWAGG_DEVICE", "cpu")
    batch: int = os.getenv("BATCH", 1)
    py: str = os.getenv("PY", "python3.8")

    # TODO add the following parameters
    # seg_only: str = os.getenv("SEG_ONLY", "seg_only")
    # no_biasfield: str = os.getenv("NO_BIASFIELD", "no_biasfield")
    # norm_name: str = os.getenv("NORM_NAME", "")
    # no_asegdkt: str = os.getenv("NO_ASEGDKT", "no_asegdkt")
    # asegdkt_segfile: str = os.getenv("ASEGDKT_SEGFILE", "")
    # no_cereb: str = os.getenv("NO_CEREB", "no_cereb")
    # cereb_segfile: str = os.getenv("CEREB_SEGFILE", "")
    # surf_only: str = os.getenv("SURF_ONLY", "surf_only")
    # parallel: str = os.getenv("PARALLEL", "parallel")


def parse_fast_surfer_arguments(config=None):
    if config is None:
        config = Configurations()

    parser = argparse.ArgumentParser(description="Arguments for running FastSurfer.")

    # make argument mandatory

    parser.add_argument(
        "--t1",
        type=str,
        default=config.t1,
        help="Path to the T1-weighted image.",
    )

    parser.add_argument(
        "--sd",
        type=str,
        default=config.sd,
        help="Path to the subject directory.",
    )

    parser.add_argument(
        "--sid",
        type=str,
        default=config.sid,
        help="Subject ID.",
    )

    parser.add_argument(
        "--fs_license",
        type=str,
        default=config.fs_license,
        help="Path to the Freesurfer license.",
    )
    parser.add_argument(
        "--vox_size",
        type=int,
        default=config.vox_size,
        help="Voxel size.",
    )

    parser.add_argument(
        "--threads",
        type=int,
        default=config.threads,
        help="",
    )

    parser.add_argument(
        "--device",
        type=str,
        default=config.device,
        help="",
    )

    parser.add_argument(
        "--viewagg_device",
        type=str,
        default=config.viewagg_device,
        help="",
    )

    parser.add_argument(
        "--batch",
        type=int,
        default=config.batch,
        help="",
    )

    parser.add_argument(
        "--py",
        type=str,
        default=config.py,
        help="",
    )

    # parser.add_argument(
    #     "--seg_only",
    #     type=str,
    #     default=config.seg_only,
    #     help="Segmentation only.",
    # )

    # parser.add_argument(
    #     "--no_biasfield",
    #     type=str,
    #     default=config.no_biasfield,
    #     help="No biasfield correction.",
    # )

    # parser.add_argument(
    #     "--norm_name",
    #     type=str,
    #     default=config.norm_name,
    #     help="Normalization name.",
    # )

    # parser.add_argument(
    #     "--no_asegdkt",
    #     type=str,
    #     default=config.no_asegdkt,
    #     help="No asegdkt.",
    # )

    # parser.add_argument(
    #     "--asegdkt_segfile",
    #     type=str,
    #     default=config.asegdkt_segfile,
    #     help="",
    # )

    # parser.add_argument(
    #     "--no_cereb",
    #     type=str,
    #     default=config.no_cereb,
    #     help="No cereb.",
    # )

    # parser.add_argument(
    #     "--cereb_segfile",
    #     type=str,
    #     default=config.cereb_segfile,
    #     help="",
    # )

    # parser.add_argument(
    #     "--surf_only",
    #     type=str,
    #     default=config.surf_only,
    #     help="",
    # )

    # parser.add_argument(
    #     "--parallel",
    #     type=str,
    #     default=config.parallel,
    #     help="",
    # )

    args = parser.parse_args()
    return args
