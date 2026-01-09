# 3PDD Dataset Builder

A tool for building the **3 Perspective Driver Dataset (3PDD)** from the Driver Monitoring Dataset (DMD).

## About

The **3 Perspective Driver Dataset (3PDD)** is built using one of the most comprehensive datasets in the literature: the **Driver Monitoring Dataset (DMD)**. We extend our sincere gratitude to [Vicomtech](https://www.vicomtech.org/) for their invaluable contribution to the driver monitoring research community.

The DMD is a multi-modal dataset specifically designed for Driver Monitoring Systems (DMS), featuring synchronized recordings from multiple cameras (body, face, hands) and multiple streams (RGB, Depth, IR) in real car and driving simulator scenarios.

### Learn More About DMD

- **GitHub Repository**: [Vicomtech/DMD-Driver-Monitoring-Dataset](https://github.com/Vicomtech/DMD-Driver-Monitoring-Dataset)
- **Official Website**: [dmd.vicomtech.org](https://dmd.vicomtech.org/)

---

## Prerequisites

Before using this tool, you need to extract frames from DMD videos.

### Step 1: Extract Frames from DMD Videos

Use the official DMD **Dataset Explorer Tool (DEx)** to extract frames:

1. Visit: [exploreMaterial-tool](https://github.com/Vicomtech/DMD-Driver-Monitoring-Dataset/tree/master/exploreMaterial-tool)
2. Follow the instructions to export frames from the video sequences
3. Organize the extracted frames in a source directory

### Step 2: Build 3PDD Dataset

Once you have extracted the frames, use this tool to organize them into the 3PDD structure.

---

## Installation

### Requirements

- Python 3.7+
- Required packages:

```bash
pip install -r requirements.txt
```

---

## Usage

### Quick Start

Run the main script:

```bash
python build_3pdd_dataset.py
```

The tool will guide you through an interactive process:

1. **Source Directory**: Path to your extracted DMD frames
2. **Perspective Selection**: Choose which camera perspectives to include
3. **Structure Type**: Select the output directory structure

### Interactive Options

#### 1. Perspective Selection

Choose one or more camera perspectives:

- `body` - Full body camera view
- `face` - Face-focused camera view  
- `hands` - Hands and steering wheel view
- `All` - Include all three perspectives

**Example:**
```
Select perspectives:
  1. body
  2. face
  3. hands
  0. All
Choices (comma-separated): 1,2
```

#### 2. Structure Type

Choose how to organize the output dataset:

- **`split`** - Organized by perspective/split/class structure
  ```
  3pdd/
  ├── body/
  │   ├── train/
  │   │   ├── class_0/
  │   │   └── class_1/
  │   ├── val/
  │   └── test/
  ├── face/
  └── hands/
  ```

- **`flat`** - Organized by perspective/class structure (all splits merged)
  ```
  3pdd/
  ├── body/
  │   ├── class_0/
  │   └── class_1/
  ├── face/
  └── hands/
  ```

**Example:**
```
Structure type:
  1. split
  2. flat
Choice: 1
```

---

## Features

### ⚡ High Performance

- **Parallel Processing**: Utilizes multi-core CPUs for fast indexing
- **Smart Indexing**: Handles millions of files efficiently
- **Real-time Progress**: Live updates during processing
- **Optimized for Large Datasets**: Designed to handle 50M+ files

### 🔍 Flexible Matching

- **Exact filename matching**: Fast lookup for identical filenames
- **Normalized matching**: Handles variations in filenames (special characters, separators)

### 📊 Progress Tracking

```
Indexing: E:\DMD\DMD_Main_Dataset
Scanning directories for images...
Using 7 parallel workers

  Discovering: 1,234 dirs found (156 dirs/s) - 2,345,678 images indexed
  Finalizing: 1,234/1,234 (0 remaining) - 52,456,789 images

✓ Indexed: 52,456,789 images from 1,234 directories in 342.5s

Building split structure...

BODY:
  train: copied=15234, not_found=12
  val: copied=3456, not_found=2
  test: copied=3789, not_found=1

Complete! Output: C:\Users\...\3pdd
```

---

## Directory Structure

### Input Requirements

Your source directory should contain the extracted frames from DMD:

```
source_directory/
├── frame_0001.jpg
├── frame_0002.jpg
├── ...
└── frame_NNNN.jpg
```

### Output Structure

The tool reads perspective-specific image lists from the `image_lists/` directory:

```
image_lists/
├── body_train_images.txt
├── body_val_images.txt
├── body_test_images.txt
├── face_train_images.txt
├── face_val_images.txt
├── face_test_images.txt
├── hands_train_images.txt
├── hands_val_images.txt
└── hands_test_images.txt
```

---

## Class Mapping

The tool uses `class_to_idx.json` to map class indices to human-readable names. This ensures consistent class organization across all perspectives and splits.

---

## Performance Tips

### For Large Datasets (50M+ files)

1. **Use SSD Storage**: Significantly faster than HDD
2. **Adjust Workers**: Modify worker count if needed
   ```python
   indexer.index_directory(source_dir, max_workers=8)
   ```
3. **Monitor Progress**: The tool provides real-time updates every 1-2 seconds
4. **Check Disk Space**: Ensure sufficient space for the output dataset

### Expected Processing Times

| Files | Workers | Estimated Time |
|-------|---------|----------------|
| 1M    | 4       | ~2-3 minutes   |
| 10M   | 8       | ~15-20 minutes |
| 50M   | 8       | ~60-90 minutes |

*Times vary based on CPU, disk speed, and directory structure*

---

## Project Structure

```
dmd-to-3pdd-builder/
├── build_3pdd_dataset.py    # Main entry point
├── builders.py               # Dataset structure builders
├── copier.py                 # Image copying operations
├── file_utils.py             # File handling utilities
├── indexer.py                # Fast image indexing with parallel processing
├── models.py                 # Data models
├── parser.py                 # Text file parser
├── ui.py                     # User interface
├── class_to_idx.json         # Class mapping configuration
├── image_lists/              # Perspective-specific image lists
│   ├── body_train_images.txt
│   ├── body_val_images.txt
│   └── ...
└── README.md                 # This file
```

---

## Troubleshooting

### Issue: "Directory not found"
- Ensure the source directory path is correct
- Use absolute paths if relative paths don't work

### Issue: "Many images not found"
- Verify frames were extracted correctly using DEx tool
- Check that filenames in `.txt` files match extracted frames
- The tool will report how many images were not found

### Issue: "Process is slow"
- Check if you're using HDD instead of SSD
- Reduce `max_workers` if system is overloaded
- Close other resource-intensive applications

---

### Related Works

If using 3PDD for driver distraction detection, consider citing:

```bibtex
@inproceedings{ortega2020dmd,
  title={DMD: A Large-Scale Multi-modal Driver Monitoring Dataset for Attention and Alertness Analysis},
  author={Ortega, Juan Diego and Kose, Neslihan and Ca{\~n}as, Paola and Chao, Min-An and Unnervik, Alexander and Nieto, Marcos and Otaegui, Oihana and Salgado, Luis},
  booktitle={Computer Vision--ECCV 2020 Workshops},
  pages={387--405},
  year={2020},
  publisher={Springer},
  doi={10.1007/978-3-030-66823-5_23}
}
```

```bibtex
@article{meld3_2024,
  title={MELD3: Integrating Multi-Task Ensemble Learning for Driver Distraction Detection},
  author={[Authors]},
  journal={IEEE Access},
  year={2024},
  doi={10.1109/ACCESS.2024.3509033}
}
```

---

## Related Publications

1. **MELD3: Integrating Multi-Task Ensemble Learning for Driver Distraction Detection**  
   IEEE Access, 2024  
   DOI: [10.1109/ACCESS.2024.3509033](https://doi.org/10.1109/ACCESS.2024.3509033)

2. **DMD: A Large-Scale Multi-modal Driver Monitoring Dataset for Attention and Alertness Analysis**  
   ECCV 2020 Workshops  
   DOI: [10.1007/978-3-030-66823-5_23](https://doi.org/10.1007/978-3-030-66823-5_23)

---

## License

This tool is provided for research purposes. Please refer to the [DMD License](https://dmd.vicomtech.org/) for dataset usage terms.

---

## Acknowledgments

Special thanks to:

- **Vicomtech** for creating and maintaining the DMD dataset
- All contributors to the DMD project

---

## Support

For issues related to:
- **This tool**: Open an issue in this repository
- **DMD dataset**: Visit [DMD GitHub](https://github.com/Vicomtech/DMD-Driver-Monitoring-Dataset)
- **Frame extraction**: Check [exploreMaterial-tool documentation](https://github.com/Vicomtech/DMD-Driver-Monitoring-Dataset/tree/master/exploreMaterial-tool)

---

**Developed with ❤️ for the driver monitoring research community**
